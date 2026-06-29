from functools import wraps
from flask import abort
from flask_login import current_user
from app.models import OrganizationMembership, Role


def user_role_for_org(user_id: int, organization_id: int):
    membership = OrganizationMembership.query.filter_by(user_id=user_id, organization_id=organization_id).first()
    return membership.role if membership else None


def require_org_role(*roles: Role):
    def decorator(func):
        @wraps(func)
        def wrapper(organization_id, *args, **kwargs):
            role = user_role_for_org(current_user.id, organization_id)
            if current_user.is_admin or role in roles:
                return func(organization_id, *args, **kwargs)
            abort(403)
        return wrapper
    return decorator

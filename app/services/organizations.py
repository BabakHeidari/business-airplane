from app.extensions import db
from app.models import BusinessProfile, Organization, OrganizationMembership, Role, User


def create_organization(owner: User, **data) -> Organization:
    profile_fields = {key: data.pop(key) for key in list(data.keys()) if hasattr(BusinessProfile, key)}
    organization = Organization(name=data["name"])
    organization.memberships.append(OrganizationMembership(user=owner, role=Role.OWNER))
    organization.business_profile = BusinessProfile(**profile_fields)
    db.session.add(organization)
    db.session.commit()
    return organization

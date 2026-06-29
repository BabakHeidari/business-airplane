from app.extensions import db
from app.models import Organization, OrganizationMembership, Role, User
from app.utils.authorization import user_role_for_org


def test_password_hashing_and_check(app):
    user = User(email="owner@example.com", name="Owner")
    user.set_password("secure-password-123")
    assert user.password_hash != "secure-password-123"
    assert user.check_password("secure-password-123")


def test_user_role_for_org_is_isolated(app):
    user = User(email="owner@example.com", name="Owner")
    user.set_password("secure-password-123")
    org = Organization(name="Northstar Coffee")
    other = Organization(name="Other Co")
    db.session.add_all([user, org, other])
    db.session.flush()
    db.session.add(OrganizationMembership(user=user, organization=org, role=Role.OWNER))
    db.session.commit()
    assert user_role_for_org(user.id, org.id) == Role.OWNER
    assert user_role_for_org(user.id, other.id) is None


def test_dashboard_requires_login(client):
    response = client.get("/dashboard")
    assert response.status_code == 302
    assert "/auth/login" in response.location

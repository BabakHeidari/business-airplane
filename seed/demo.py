from app import create_app
from app.extensions import db
from app.models import BusinessProfile, Organization, OrganizationMembership, Role, User

OWNER_EMAIL = "owner@northstar.example"
CONSULTANT_EMAIL = "consultant@northstar.example"
DEMO_PASSWORD = "NorthstarDemo123!"

def run():
    app = create_app()
    with app.app_context():
        db.create_all()
        owner = User.query.filter_by(email=OWNER_EMAIL).first() or User(email=OWNER_EMAIL, name="Avery North")
        owner.set_password(DEMO_PASSWORD)
        consultant = User.query.filter_by(email=CONSULTANT_EMAIL).first() or User(email=CONSULTANT_EMAIL, name="Jordan Vale")
        consultant.set_password(DEMO_PASSWORD)
        org = Organization.query.filter_by(name="Northstar Coffee").first() or Organization(name="Northstar Coffee")
        org.business_profile = org.business_profile or BusinessProfile(industry="café / local food service", business_model="Retail café", country="United States", currency="USD", team_size=12, monthly_revenue_range="$50k-$100k", monthly_fixed_cost_range="$25k-$50k", average_gross_margin_range="55%-65%", current_cash_balance=28000, primary_growth_goal="Increase repeat visits", main_business_challenge="Unpredictable weekday demand", fiscal_year_start_month=1)
        db.session.add_all([owner, consultant, org])
        db.session.flush()
        for user, role in [(owner, Role.OWNER), (consultant, Role.CONSULTANT)]:
            if not OrganizationMembership.query.filter_by(user=user, organization=org).first():
                db.session.add(OrganizationMembership(user=user, organization=org, role=role))
        db.session.commit()
        print(f"Seeded demo users: {OWNER_EMAIL}, {CONSULTANT_EMAIL} / {DEMO_PASSWORD}")

if __name__ == "__main__":
    run()

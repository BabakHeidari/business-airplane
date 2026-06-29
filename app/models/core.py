import enum
import uuid
from datetime import datetime, timezone
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from app.extensions import db

class Role(enum.StrEnum):
    OWNER = "owner"
    TEAM_MEMBER = "team_member"
    CONSULTANT = "consultant"
    ADMIN = "admin"

class TimestampMixin:
    created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

class User(UserMixin, TimestampMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    name = db.Column(db.String(120), nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    memberships = db.relationship("OrganizationMembership", back_populates="user", cascade="all, delete-orphan")

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

class Organization(TimestampMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    name = db.Column(db.String(160), nullable=False)
    memberships = db.relationship("OrganizationMembership", back_populates="organization", cascade="all, delete-orphan")
    business_profile = db.relationship("BusinessProfile", back_populates="organization", uselist=False, cascade="all, delete-orphan")

class OrganizationMembership(TimestampMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    organization_id = db.Column(db.Integer, db.ForeignKey("organization.id"), nullable=False)
    role = db.Column(db.Enum(Role, values_callable=lambda enum: [item.value for item in enum]), nullable=False)
    user = db.relationship("User", back_populates="memberships")
    organization = db.relationship("Organization", back_populates="memberships")
    __table_args__ = (db.UniqueConstraint("user_id", "organization_id", name="uq_user_organization"),)

class BusinessProfile(TimestampMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    organization_id = db.Column(db.Integer, db.ForeignKey("organization.id"), unique=True, nullable=False)
    industry = db.Column(db.String(120), nullable=False)
    business_model = db.Column(db.String(120), nullable=True)
    country = db.Column(db.String(80), nullable=True)
    currency = db.Column(db.String(3), default="USD", nullable=False)
    team_size = db.Column(db.Integer, nullable=True)
    monthly_revenue_range = db.Column(db.String(80), nullable=True)
    monthly_fixed_cost_range = db.Column(db.String(80), nullable=True)
    average_gross_margin_range = db.Column(db.String(80), nullable=True)
    current_cash_balance = db.Column(db.Numeric(12, 2), nullable=True)
    primary_growth_goal = db.Column(db.Text, nullable=True)
    main_business_challenge = db.Column(db.Text, nullable=True)
    fiscal_year_start_month = db.Column(db.Integer, default=1, nullable=False)
    organization = db.relationship("Organization", back_populates="business_profile")

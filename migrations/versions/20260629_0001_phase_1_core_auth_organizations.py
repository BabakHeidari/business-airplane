"""phase 1 core auth organizations

Revision ID: 20260629_0001
Revises:
Create Date: 2026-06-29
"""
from alembic import op
import sqlalchemy as sa

revision = "20260629_0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("user",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("public_id", sa.String(length=36), nullable=False, unique=True),
        sa.Column("email", sa.String(length=255), nullable=False, unique=True),
        sa.Column("name", sa.String(length=120), nullable=False),
        sa.Column("password_hash", sa.String(length=255), nullable=False),
        sa.Column("is_admin", sa.Boolean(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index(op.f("ix_user_email"), "user", ["email"])
    op.create_table("organization",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("public_id", sa.String(length=36), nullable=False, unique=True),
        sa.Column("name", sa.String(length=160), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_table("business_profile",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("organization_id", sa.Integer(), sa.ForeignKey("organization.id"), nullable=False, unique=True),
        sa.Column("industry", sa.String(length=120), nullable=False),
        sa.Column("business_model", sa.String(length=120)),
        sa.Column("country", sa.String(length=80)),
        sa.Column("currency", sa.String(length=3), nullable=False),
        sa.Column("team_size", sa.Integer()),
        sa.Column("monthly_revenue_range", sa.String(length=80)),
        sa.Column("monthly_fixed_cost_range", sa.String(length=80)),
        sa.Column("average_gross_margin_range", sa.String(length=80)),
        sa.Column("current_cash_balance", sa.Numeric(12, 2)),
        sa.Column("primary_growth_goal", sa.Text()),
        sa.Column("main_business_challenge", sa.Text()),
        sa.Column("fiscal_year_start_month", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_table("organization_membership",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("user.id"), nullable=False),
        sa.Column("organization_id", sa.Integer(), sa.ForeignKey("organization.id"), nullable=False),
        sa.Column("role", sa.Enum("owner", "team_member", "consultant", "admin", name="role"), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.UniqueConstraint("user_id", "organization_id", name="uq_user_organization"),
    )


def downgrade():
    op.drop_table("organization_membership")
    op.drop_table("business_profile")
    op.drop_table("organization")
    op.drop_index(op.f("ix_user_email"), table_name="user")
    op.drop_table("user")
    op.execute("DROP TYPE IF EXISTS role")

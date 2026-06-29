from flask_wtf import FlaskForm
from wtforms import DecimalField, IntegerField, SelectField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange, Optional

class OrganizationForm(FlaskForm):
    name = StringField("Business name", validators=[DataRequired(), Length(max=160)])
    industry = StringField("Industry", validators=[DataRequired(), Length(max=120)])
    business_model = StringField("Business model", validators=[Optional(), Length(max=120)])
    country = StringField("Country", validators=[Optional(), Length(max=80)])
    currency = SelectField("Currency", choices=[("USD", "USD"), ("CAD", "CAD"), ("GBP", "GBP"), ("EUR", "EUR")])
    team_size = IntegerField("Team size", validators=[Optional(), NumberRange(min=1)])
    monthly_revenue_range = StringField("Monthly revenue range", validators=[Optional(), Length(max=80)])
    monthly_fixed_cost_range = StringField("Monthly fixed-cost range", validators=[Optional(), Length(max=80)])
    average_gross_margin_range = StringField("Average gross margin range", validators=[Optional(), Length(max=80)])
    current_cash_balance = DecimalField("Current cash balance", validators=[Optional()], places=2)
    primary_growth_goal = TextAreaField("Primary growth goal", validators=[Optional(), Length(max=1000)])
    main_business_challenge = TextAreaField("Main business challenge", validators=[Optional(), Length(max=1000)])
    fiscal_year_start_month = IntegerField("Fiscal year start month", default=1, validators=[DataRequired(), NumberRange(min=1, max=12)])
    submit = SubmitField("Create workspace")

from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from app.forms.organizations import OrganizationForm
from app.services.organizations import create_organization

bp = Blueprint("organizations", __name__, url_prefix="/organizations")

@bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    form = OrganizationForm()
    if form.validate_on_submit():
        org = create_organization(current_user, **form.data)
        return redirect(url_for("dashboard.index", organization=org.public_id))
    return render_template("organizations/create.html", form=form)

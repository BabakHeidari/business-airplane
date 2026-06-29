from flask import Blueprint, render_template
from flask_login import current_user, login_required

bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")

@bp.route("")
@login_required
def index():
    memberships = current_user.memberships
    return render_template("dashboard/index.html", memberships=memberships)

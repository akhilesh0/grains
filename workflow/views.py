from flask import Blueprint, render_template, request, redirect, session, url_for

from user.decorators import login_required

workflow_app = Blueprint('workflow_app', __name__)

@workflow_app.route('/workflow', methods=('GET', 'POST'))
@login_required
def workflow():
	return render_template('workflow/design.html')
from functools import wraps
from flask import session, request, url_for, redirect

def login_required(f):
	@wraps(f)
	def decorated_fuction(*args, **kwargs):
		if session.get('username') is None:
			return redirect(url_for('user_app.login', next=request.url))
		return f(*args, **kwargs)
	return decorated_fuction
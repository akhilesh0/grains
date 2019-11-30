from application import create_app as create_app_base
from mongoengine.connection import _get_db
from flask import session
import unittest

from user.models import User 

class UserTest(unittest.TestCase):
	def create_app(self):
		self.db_name = 'grains_test'
		return create_app_base(
			MONGODB_SETTINGS={'DB': self.db_name},
			TESTING=True,
			WTF_CSRF_ENABLED=False,
			SECRET_KEY='test-secret',
			)

	def setUp(self):
		self.app_factory = self.create_app()
		self.app = self.app_factory.test_client()

	def tearDown(self):
		db = _get_db()
		db.client.drop_database(db)

	def user_dict(self):
		return dict(
			first_name="Test",
			last_name="Test",
			username="test",
			email="test@example.com",
			password="test1234",
			confirm="test1234"
			)

	def test_register_user(self):
		#Testing registration module
		rv = self.app.post('/register', data=self.user_dict(), follow_redirects=True)
		assert User.objects.filter(username="test").count() == 1

	def test_login_user(self):
		# create user
		self.app.post('/register', data=self.user_dict())
		# login user
		rv = self.app.post('/login', data=dict(
			username=self.user_dict()['username'],
			password=self.user_dict()['password']
			))
		# check session
		with self.app as context:
			rv = context.get('/')
			assert session.get('username') == self.user_dict()['username']

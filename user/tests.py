from application import create_app as create_app_base
from mongoengine.connection import _get_db
import unittest

from user.models import User 

class UserTest(unittest.TestCase):
	def create_app(self):
		self.db_name = 'grains_test'
		return create_app_base(
			MONGODB_SETTINGS={'DB': self.db_name},
			TESTING=True,
			WTF_CSRF_ENABLED=False
			)

	def setUp(self):
		self.app_factory = self.create_app()
		self.app = self.app_factory.test_client()

	def tearDown(self):
		db = _get_db()
		db.client.drop_database(db)

	def test_register_user(self):
		#Testing registration module
		rv = self.app.post('/register', data=dict(
			first_name="Test",
			last_name="Test",
			username="test",
			email="test@example.com",
			password="test1234",
			confirm="test1234"
			), follow_redirects=True)
		assert User.objects.filter(username="test").count() == 1

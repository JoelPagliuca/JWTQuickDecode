from unittest import TestCase

from jwt_quick import decode_claims

class JWTTests(TestCase):
	
	def setUp(self):
		self.jwt1 = "eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9"
		self.jwt2 = "eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOmZhbHNlLCJub25zZW5zZSI6dHJ1ZX0"
	
	def test_jwt1(self):
		claims = decode_claims(self.jwt1)
		self.assertTrue(claims['admin'])
	
	def test_jwt2(self):
		claims = decode_claims(self.jwt2)
		self.assertTrue(claims['nonsense'])
		self.assertFalse(claims['admin'])
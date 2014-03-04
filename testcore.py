import unittest
import core

class TestCore(unittest.TestCase):
	
	def test_validate_true(self):
		val = core.validate('MyJaz1tvfjHby4ga7DkR6WbquDVy1aV5Xc');
		self.assertTrue(val)
	
	def test_validate_false(self):
		val = core.validate('42');
		self.assertFalse(val);
		
	def test_validate_none(self):
		val = core.validate(None);
		self.assertFalse(val);
	
if __name__ == '__main__':
    unittest.main()
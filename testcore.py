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
		
	def test_getinfo(self):
		val = core.getinfo()
		self.assertEqual(type(val), dict);
		self.assertEqual(len(val), 16);
	
	def test_getblockcount(self):
		control = core.getinfo()
		val = core.getblockcount();
		self.assertEqual(type(val), int);
		self.assertEqual(control['blocks'], val);
	
	def test_getdifficulty(self):
		control = core.getinfo()
		val = core.getdifficulty();
		self.assertEqual(type(val), float);
		self.assertEqual(control['difficulty'], val);
	
	def test_gethashespersec(self):
		control = core.getinfo()
		val = core.gethashespersec();
		self.assertEqual(type(val), int);
		self.assertEqual(control['hashespersec'], val);
	
	def test_getconnectioncount(self):
		control = core.getinfo()
		val = core.getconnectioncount();
		self.assertEqual(type(val), int);
		self.assertEqual(control['connections'], val);
		
	
	def test_name_show_exists(self):
		name = 'd/domain'
		val = core.name_show(name)
		self.assertEqual(type(val), dict);
		self.assertEqual(val['name'], name);
		
	def test_name_show_not_existing(self):
		name = 'dadajjunonexisting'
		val = core.name_show(name)
		self.assertEquals(val, None);
		
	def test_name_show_None(self):
		name = None
		val = core.name_show(name)
		self.assertEquals(val, None);
	
	# TODO
	# name_history
	# name_scan
	# name_filter
	# gettransaction
	
if __name__ == '__main__':
    unittest.main()
import unittest
from .. import info;

# namecoind.exe server needs to running.
class TestCore(unittest.TestCase):
	
	def test_validate_true(self):
		val = info.validate('MyJaz1tvfjHby4ga7DkR6WbquDVy1aV5Xc');
		self.assertTrue(val)
	
	def test_validate_false(self):
		val = info.validate('42');
		self.assertFalse(val);
		
	def test_validate_none(self):
		val = info.validate(None);
		self.assertFalse(val);
		
	def test_getinfo(self):
		val = info.getinfo()
		self.assertEqual(type(val), dict);
		self.assertEqual(len(val), 16);
	
	def test_getblockcount(self):
		control = info.getinfo()
		val = info.getblockcount();
		self.assertEqual(type(val), int);
		self.assertEqual(control['blocks'], val);
	
	def test_getdifficulty(self):
		control = info.getinfo()
		val = info.getdifficulty();
		self.assertEqual(type(val), float);
		self.assertEqual(control['difficulty'], val);
	
	def test_gethashespersec(self):
		control = info.getinfo()
		val = info.gethashespersec();
		self.assertEqual(type(val), int);
		self.assertEqual(control['hashespersec'], val);
	
	def test_getconnectioncount(self):
		control = info.getinfo()
		val = info.getconnectioncount();
		self.assertEqual(type(val), int);
		self.assertEqual(control['connections'], val);
		
	
	def test_name_show_exists(self):
		name = 'd/domain'
		val = info.name_show(name)
		self.assertEqual(type(val), dict);
		self.assertEqual(val['name'], name);
		
	def test_name_show_not_existing(self):
		name = 'dadajjunonexisting'
		val = info.name_show(name)
		self.assertEquals(val, None);
		
	def test_name_show_None(self):
		name = None
		val = info.name_show(name)
		self.assertEquals(val, None); # raise exception?
	
	def test_name_history_exists(self):
		name = 'd/domain';
		val = info.name_history(name);
		self.assertEqual(type(val), list);
		self.assertEqual(type(val[0]), dict);
		
	def test_name_history_not_existing(self):
		name = 'dadajjunonexisting'
		val = info.name_show(name)
		self.assertEquals(val, None);
		
	def test_name_history_none(self):
		name = None;
		val = info.name_history(name);
		self.assertEquals(val, None);
	
	def test_name_scan_exists(self):
		start_name = 'd/domain';
		count = 10;
		val = info.name_scan(start_name, count);
		self.assertEqual(type(val), list);
		self.assertEqual(len(val), count);
		self.assertEqual(type(val[0]), dict);
	
	def test_name_scan_not_existing(self):
		# Should this return results?
		start_name = 'saksjfsduiaehuh';
		count = 10;
		val = info.name_scan(start_name, count);
		self.assertEqual(type(val), list);
		self.assertEqual(len(val), count);
		self.assertEqual(type(val[0]), dict);
	
	def test_name_scan_none(self):
		with self.assertRaises(Exception):
			start_name = None;
			count = 10;
			val = info.name_scan(start_name, count);
		
	def test_name_scan_invaid_count(self):
		with self.assertRaises(Exception):
			start_name = 'd/domain'
			count = 0 
			val = info.name_scan(start_name, count);
	
	def test_name_filter(self):
		regex = 'test'
		val = info.name_filter(regex, count=10);
		self.assertEquals(type(val), list);
		self.assertEqual(type(val[0]), dict);
		
	def test_name_filter_invalid_regex(self):
		with self.assertRaises(Exception):
			regex = '\p**\\\\#\@'
			val = info.name_filter(regex, count=10);
	
	def test_name_filter_invalid_count(self):
		with self.assertRaises(Exception):
			regex = 'test'
			val = info.name_filter(regex, count=-1);
		
	def test_name_filter_invalid_maxage(self):
		with self.assertRaises(Exception):
			regex = 'test'
			val = info.name_filter(regex, maxage=-1, minage=-10);
	
	def test_name_filter_invalid_minage(self):
		with self.assertRaises(Exception):
			regex = 'test'
			val = info.name_filter(regex, minage=-1);
	
	def test_name_filter_conflicting_ages(self):
		with self.assertRaises(Exception):
			regex = 'test'
			val = info.name_filter(regex, maxage=100, minage=500);
	
	def test_name_filter_same_age(self):
		regex = 'test'
		val = info.name_filter(regex, maxage=10, minage=10);
		self.assertEquals(val, []);
	
	'''
	def test_gettransaction(self):
		val = info.gettransaction('6cce69f22841439b40bd576d15c46ec6d60ad44e1d604b51049ecebd011b53d4');
		self.assertEquals(val, None); 
	'''
	
	def test_gettransaction_nonexisting(self):
		with self.assertRaises(Exception):
			txid = '42';
			val = info.gettransaction(txid);
			self.assertEquals(val, None); 
	
	def test_gettransaction_none(self):
		with self.assertRaises(Exception):
			txid = None;
			val = info.gettransaction(txid);
			
if __name__ == '__main__':
    unittest.main()
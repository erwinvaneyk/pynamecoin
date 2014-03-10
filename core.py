import subprocess, json, logging
'''
Settings
'''
CLIENT  = 'namecoin/namecoind.exe'
LOG 	= 'pynamecoin.log'
SAFE_MODE = True

'''
Logger
'''
FORMAT = '%(asctime)-15s %(levelname)-8s: %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO, filename=LOG)
LOGGER = logging.getLogger('pynmc')


'''
ServerException is issued when server returns errors
'''
class ServerException(Exception):
	def __init__(self, value, code=0):
		LOGGER.error(value);
		self.value = value;
		self.code = code
	
	def __str__(self):
		return repr(self.value) + "(" + str(self.code) + ')';

'''
Pair dataclass
'''
class Pair:
	def __init__(self, name, value, owner_address, txid, expires_in):
		self.name = name;
		self.value = value;
		self.owner_address = owner_address;
		self.txid = txid;
		self.expires_in = expires_in;
		
	def expired():
		return expires_in < 0;
	
	def __str__():
		return str(self.name) + ": " + repr(self.value);

'''
Retrieve the transaction with id txid.

def gettransaction(txid):
	value = nmc_call('gettransaction', [str(txid)]);
	return value
'''	

'''
Return general information about the state of the network. Contains:
{version, balance, blocks, timeoffset, connections, proxy, 
	generate, genproclimit, difficulty, hashespersec, testnet,keypoololdest,
	keypoolsize,paytxfee,mininput,errors}
'''
def getinfo():
	return nmc_call('getinfo');


'''
Get the current block number
'''
def getblockcount():
	return nmc_call('getblockcount');

'''
Get the current mining difficulty
'''
def getdifficulty():
	return nmc_call('getdifficulty');

'''
Get the current hashrate of the network
'''	
def gethashespersec():
	return nmc_call('gethashespersec');

'''
Get connection count of the node
'''
def getconnectioncount():
	return nmc_call('getconnectioncount');
	
'''
Validate NMC address
'''
def validate(address):
	if type(address) is str:
		value = nmc_call('validateaddress', [address]);
		return value['isvalid'] == True;
	else:
		return False;
'''
Scans n number of names alphabetically, starting at start_name
'''
def name_scan(start_name, count):
	assert count > 0
	return nmc_call('name_scan', [(start_name), str(count)]);

'''
Retrieve names matching the regex (and additional parameters
'''
def name_filter(regex, maxage=36000, minage=0, count=0, stat = False):
	assert minage <= maxage;
	assert minage >= 0;
	assert maxage >= 0;
	assert count >= 0;
	stat = 'stat' if stat else None;
	value = nmc_call('name_filter', [(regex), str(maxage), str(minage), str(count)]);
	return value
	
'''
Return the associated value of the <name>, otherwise return None.
'''
def name_show(name):
	try:
		value = nmc_call('name_show',[(name)]);
	except:
		value = None;
	return value;

'''
Return the history (value updates) of the <name>.
'''
def name_history(name):
	try:
		value = nmc_call('name_history',[(name)]);
	except:
		value = None;
	return value;

'''
Calls the client with the method and additional args.
'''
def nmc_call(method, args = []):
	rargs = [CLIENT,method] + args;
	p = subprocess.Popen(rargs,stdout=subprocess.PIPE,stderr=subprocess.PIPE);
	out, err = p.communicate();
	LOGGER.info('input: ' + ' '.join(rargs));
	if err:
		raise ServerException(str(err['message']), str(err['code']));
	try:
		ret =  json.loads(out.replace('\r','').replace('\n',''));
	except Exception as e:
		raise ServerException(str(e) + ": " + repr(out));	
	return ret
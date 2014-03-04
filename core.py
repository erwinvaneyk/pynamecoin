import subprocess, json, logging

'''
Settings
'''
CLIENT = 'namecoin/namecoind.exe'
SAFE_MODE = True

'''
Logger
'''
FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT)

'''
ServerException is issued when server returns errors
'''
class ServerException(Exception):
	def __init__(self, value, code=0):
		logger = logging.getLogger('pynmc')
		logger.error(value);
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
Advanced functionality:
--
name_new(name) --
name_firstupdate(name,rand,value)
name_update(name,value,to)
--
\----> seperate module: namecoin.account
pynmc
pynmc.core				-> no wallet
pynmc.ServerException
pynmc.account
pynmc.account.Account
pynmc.core.Name ?-
'''

'''
Validate NMC address
'''
def validate(address):
	value = nmc_call('validateaddress', [address]);
	return value['isvalid'] == True;
	
'''
Scans n number of names alphabetically, starting at start_name
'''
def name_scan(start_name, count):
	return nmc_call('name_scan', [start_name, str(count)]);

'''
Retrieve names matching the regex (and additional parameters
'''
def name_filter(regex, maxage=36000, fromage=0, number=0, stat = False):
	stat = 'stat' if stat else None;
	value = nmc_call('name_filter', [regex, str(maxage), str(fromage), str(number)]);
	return value
	
'''
Return the associated value of the <name>, otherwise return None.
'''
def name_show(name):
	try:
		value = nmc_call('name_show',[name]);
	except:
		value = None;
	return value;

'''
Return the history (value updates) of the <name>.
'''
def name_history(name):
	value = nmc_call('name_history',[name]);
	return value;
	
'''
Return general information about the state of the network. Contains:
{version, balance, blocks, timeoffset, connections, proxy, 
	generate, genproclimit, difficulty, hashespersec, testnet,keypoololdest,
	keypoolsize,paytxfee,mininput,errors}
'''
def getinfo():
	return nmc_call('getinfo');

'''
Calls the client with the method and additional args.
'''
def nmc_call(method, args = []):
	rargs = [CLIENT,method] + args;
	p = subprocess.Popen(rargs,stdout=subprocess.PIPE,stderr=subprocess.PIPE);
	out, err = p.communicate();
	logger = logging.getLogger('pynmc')
	logger.info('input: ' + ' '.join(rargs));
	logger.info('output: ' + str(out));
	try:
		ret =  json.loads(out.replace('\r','').replace('\n',''));
	except Exception as e:
		raise ServerException(str(e));	
	if hasattr(ret, 'error'):
		raise ServerException(ret.error.msg, ret.error.code);
	return ret
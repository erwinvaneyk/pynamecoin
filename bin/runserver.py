import subprocess, logging, time, threading, json, os

# Setup
CLIENT = 'namecoin\\namecoind.exe';
LOGGER 	= logging.getLogger('namecoind');
FORMAT 	= '%(asctime)-15s %(levelname)-5s: %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO);

'''
Namecoind.exe-daemon
'''
class Namecoind(threading.Thread):
    def run(self):
		try:
			subprocess.Popen(CLIENT, shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
		except Exception as e:
			print e;

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
Checks for availability server
'''		
def checkServer():
	try:
		nmc_call('getinfo');
	except:
		return False;
	return True;

'''
Calls the client with the method and additional args.
'''
def nmc_call(method, args = []):
	rargs = [CLIENT,method] + args;
	p = subprocess.Popen(rargs,stdout=subprocess.PIPE,stderr=subprocess.PIPE);
	out, err = p.communicate();
	if err:
		err = err[7:];
		jerr =  json.loads(err.replace('\r','').replace('\n',''));
		raise ServerException(str(jerr['message']), str(jerr['code']));
	try:
		ret =  json.loads(out.replace('\r','').replace('\n',''));
	except Exception as e:
		ret = out
	return ret

if __name__ == "__main__":
	# Launch server
	LOGGER.info('Launching server...');
	thread = Namecoind()
	thread.daemon = True
	thread.start()
	LOGGER.info('Server synchronizing...');
	
	# Check heartbeat
	while not checkServer():
		LOGGER.info('...');
		time.sleep(20)
	LOGGER.info('Server is ready for requests.');
	
	# CLI
	while True:
		# Process input
		val = raw_input('> ')
		arr = val.split(' ')
		
		# special keywords
		if arr[0] == 'exit' or arr[0] == 'quit' or arr[0] == 'stop':
			print nmc_call('stop');
			exit();
		elif arr[0] == 'status' or arr[0] == 'info':
			# Status
			try:
				print 'status: online';
				info = nmc_call('getinfo');
				for item in info:
					print str(item) + ': ' + str(info[item]);
			except:
				print 'status: offline';
		else:
			# Or query namecoind.exe
			try:
				out = nmc_call(arr[0],arr[1:]);
				print repr(out);
			except Exception as e:
				print str(e);
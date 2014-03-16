# Simple example
import pynamecoin.info;

# Get general info about current state of network and server
inf = info.getinfo()
print inf
print 'Current difficulty: ' + str(inf['difficulty']) + '\r\n'

# Show the value of the name d/domain
print info.name_show('d/domain') + '\r\n';

# Show the history (value changes) of the name
print info.name_history('d/domain') + '\r\n';

# Scan 10 domains starting at d/domain
print info.name_scan('d/domain',10) + '\r\n';

# Filter all names by the string 'domain'
print info.name_filter('domain') + '\r\n';

# Validate address
print info.validate('MyJaz1tvfjHby4ga7DkR6WbquDVy1aV5Xc') + '\r\n';
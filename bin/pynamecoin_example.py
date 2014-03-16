# Examples
from .. import pynamcoin.info;

inf = info.getinfo()
print inf
print 'Current difficulty: ' + str(inf['difficulty'])
print ' '
print info.name_show('d/domain');
print ' '
print info.name_history('d/domain');
print ' '
print info.name_scan('d/domain',10);
print ' '
print info.name_filter('erwin');
print ' '
print info.validate('MyJaz1tvfjHby4ga7DkR6WbquDVy1aV5Xc');
print ' '
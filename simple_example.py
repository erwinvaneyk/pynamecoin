# Examples
import core;

info = core.getinfo()
print info
print 'Current difficulty: ' + str(info['difficulty'])
print ' '
print core.name_show('d/domain');
print ' '
print core.name_history('d/domain');
print ' '
print core.name_scan('d/domain',10);
print ' '
print core.name_filter('erwin');
print ' '
print core.validate('MyJaz1tvfjHby4ga7DkR6WbquDVy1aV5Xc');
print ' '
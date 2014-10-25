import os

print 'Starting MITM proxy on localhost on port 8080'
print 'Set your Tinder device to use this PC as a proxy'
print 'Install the cert on Tinder device from mitm.it once connected to proxy'
print '----------------'
print 'Waiting for Tinder device to fetch photos ++++'
os.system("mitmdump -s filter.py -q")

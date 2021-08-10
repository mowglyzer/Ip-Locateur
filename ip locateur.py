import pygeoip # pip install pygeoip

gip = pygeoip.GeoIP("GeoLiteCity.dat")
res = gip.record_by_addr('217.128.250.189')
for key, val in res.items():
    print('%s : %s' % (key, val))


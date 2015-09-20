from InfraUnit import infra
import time 
import httplib
import json

infraPath="infrastructures/sample_http_service"

def test_we_must_get_hostname(infra):
	conn = httplib.HTTPConnection(infra.server('service1').ip+":8001")
	conn.request("GET", "/")
	r = conn.getresponse()
	data = json.loads(r.read())
	assert r.status == 200
	assert data['hostname'] == 'service1'

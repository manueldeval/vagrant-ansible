from InfraUnit import infra
import httplib
import base64
import string
import json
import time


def getStatsHtml(infra,login,password):
	conn = httplib.HTTPConnection(infra.server('lb').ip+":80")
	auth = base64.encodestring(login+':'+password).replace('\n', '')
	headers = { 'Authorization' : 'Basic %s' %  auth }
	conn.request("GET", "/stats",headers=headers)
	r = conn.getresponse()
	return r

def test_we_must_have_access_on_ha_proxy_stats(infra):
	response = getStatsHtml(infra,"admin","password")
	html = response.read()
	assert response.status == 200
	assert "General process information" in html

def test_stats_url_must_be_protected(infra):
	response = getStatsHtml(infra,"badadmin","password")
	html = response.read()
	assert response.status == 401

def test_request_on_rest1_should_only_hit_ser1_because_ser2_is_the_backup(infra):
	for iteration in range(0,10):
		conn = httplib.HTTPConnection("192.168.33.201:80")
		conn.request("GET", "/rest1")
		r = conn.getresponse()
		data = json.loads(r.read())
		assert r.status == 200
		assert data['hostname'] == 'ser1'	

def test_ser2_should_be_used_if_we_stop_rest1_on_ser1(infra):
	stopHaOnLb1 = infra.server('ser1').ssh('service rest1 stop')
	time.sleep(5)
	conn = httplib.HTTPConnection("192.168.33.201:80")
	conn.request("GET", "/rest1")
	r = conn.getresponse()
	data = json.loads(r.read())
	assert r.status == 200
	assert data['hostname'] == 'ser2'
	time.sleep(5)
	stopHaOnLb1 = infra.server('ser1').ssh('service rest1 start')
	


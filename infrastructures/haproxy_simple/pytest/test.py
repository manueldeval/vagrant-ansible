from InfraUnit import infra
import time 

def test_vip_is_on_lb1(infra):
	vipOnLb1 = infra.server('lb1').ssh('ip addr show').stdoutContains("192.168.33.201")
	assert  vipOnLb1 == True

def test_if_haproxy_is_stopped_on_lb1_it_will_be_affected_on_lb2(infra):
	stopHaOnLb1 = infra.server('lb1').ssh('service haproxy stop')
	time.sleep(5)
	vipOnLb2 = infra.server('lb2').ssh('ip addr show').stdoutContains("192.168.33.201")
	assert  vipOnLb2 == True

def test_if_haproxy_is_restarted_on_lb1_it_will_be_affected_on_lb1(infra):
	stopHaOnLb1 = infra.server('lb1').ssh('service  haproxy start')
	time.sleep(5)
	vipOnLb1 = infra.server('lb1').ssh('ip addr show').stdoutContains("192.168.33.201")
	assert  vipOnLb1 == True

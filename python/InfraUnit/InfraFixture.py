import pytest
from Infrastructure import Infrastructure

INFRA = None

@pytest.fixture
def infra():
	global INFRA
	if INFRA == None:
		INFRA = Infrastructure("./infrastructures/haproxy_simple","./")
		INFRA.init()
	return INFRA


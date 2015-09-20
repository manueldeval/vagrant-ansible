import pytest
import os
from Infrastructure import Infrastructure

INFRA = None

@pytest.fixture(scope="module")
def infra(request):
	global INFRA
	if INFRA == None:
		infraPath = getInfraPathOfRequest(request)
		INFRA = Infrastructure(infraPath,"./")
		INFRA.init()
	return INFRA

def getInfraPathOfRequest(request):
	return os.path.dirname(os.path.dirname(request.fspath.__str__()))

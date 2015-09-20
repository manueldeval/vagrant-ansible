import pytest
from Infrastructure import Infrastructure

INFRA = None

@pytest.fixture(scope="module")
def infra(request):
	global INFRA
	if INFRA == None:
		infraPath = getattr(request.module, "infraPath")
		INFRA = Infrastructure(infraPath,"./")
		INFRA.init()
	return INFRA



import pytest
from fixture.application import Application

@pytest.fixture(scope='session')
def app(request):
    fix=Application()
    request.addfinalizer(fix.destroy)
    return fix

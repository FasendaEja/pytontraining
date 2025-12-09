
import pytest
from fixture.application import Application

@pytest.fixture(scope='session')
def app(request):
    fix=Application()
    fix.open_home_page()
    fix.session.login("admin", "secret")
    def fin():
        fix.session.logout()
        fix.destroy()
    request.addfinalizer(fin)
    return fix

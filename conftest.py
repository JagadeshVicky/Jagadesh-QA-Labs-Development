import pytest

@pytest.fixture(scope="session")
def user_credetials(request):
    return request.param
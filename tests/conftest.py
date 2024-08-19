import pytest
from selene import browser


@pytest.fixture(scope="function", params=[(1280, 720), (1920, 1080), (2560, 1600)],
                ids=['WEB_1280', 'WEB_1920', 'WEB_2560'])
def browser_management_desktop(request):
    browser.config.base_url = 'https://github.com'
    width, height = request.param
    browser.config.window_height = height
    browser.config.window_width = width

    yield

    browser.quit()


@pytest.fixture(scope='function', params=[(412, 915), (430, 932), (375, 667)],
                ids=['Pixel 7', 'iPhone 14 Pro Max', 'iPhone SE'])
def browser_management_mobile(request):
    browser.config.base_url = 'https://github.com'
    width, height = request.param
    browser.config.window_height = height
    browser.config.window_width = width

    yield

    browser.quit()


@pytest.fixture(scope='function', params=[(1280, 720), (1920, 1080), (412, 915)],
                ids=['WEB_1280', 'WEB_1920', 'Pixel 7'])
def browser_management(request):
    browser.config.base_url = 'https://github.com'
    width, height = request.param
    browser.config.window_height = height
    browser.config.window_width = width

    if width >= 800:
        yield 'desktop'
    else:
        yield 'mobile'

    browser.quit()

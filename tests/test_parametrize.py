"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""

import pytest
from selene import browser, be

desktop = pytest.mark.parametrize("browser_management",
                                  [(2560, 1600)], indirect=True,
                                  ids=['WEB_2560'])
mobile = pytest.mark.parametrize("browser_management",
                                 [(412, 915)], indirect=True,
                                 ids=['Pixel 7'])


@desktop
def test_github_desktop_indirect(browser_management):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email').should(be.visible)
    browser.element('[data-continue-to=password-container]').should(be.visible)


@mobile
def test_github_mobile_indirect(browser_management):
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email').should(be.visible)
    browser.element('[data-continue-to=password-container]').should(be.visible)

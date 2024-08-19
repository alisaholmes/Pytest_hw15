"""
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""

import pytest
from selene import browser, be


def test_github_desktop(browser_management):
    if browser_management == 'mobile':
        pytest.skip(reason='Размеры предназначены для мобильной версии')

    browser.open('/')
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email').should(be.visible)
    browser.element('[data-continue-to=password-container]').should(be.visible)


def test_github_mobile(browser_management):
    if browser_management == 'desktop':
        pytest.skip(reason='Размеры предназначены для настольной версии')

    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email').should(be.visible)
    browser.element('[data-continue-to=password-container]').should(be.visible)
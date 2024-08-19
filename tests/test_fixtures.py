"""
Cделайте разные фикстуры для каждого теста, c целью определения размеров окна браузера
"""
from selene import browser, be


def test_github_desktop(browser_management_desktop):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email').should(be.visible)
    browser.element('[data-continue-to=password-container]').should(be.visible)


def test_github_mobile(browser_management_mobile):
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email').should(be.visible)
    browser.element('[data-continue-to=password-container]').should(be.visible)

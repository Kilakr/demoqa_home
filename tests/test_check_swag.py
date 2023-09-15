from pages.swag_labs import SwagLabs
from conftest import browser


def test_site_visit(browser):
    swag = SwagLabs(browser)
    swag.visit()
    assert swag.exist_icon()
def test_site_visit_name(browser):
    swag = SwagLabs(browser)
    swag.visit()
    assert swag.exist_name()
def test_site_visit_password(browser):
    swag = SwagLabs(browser)
    swag.visit()
    assert swag.exist_password()


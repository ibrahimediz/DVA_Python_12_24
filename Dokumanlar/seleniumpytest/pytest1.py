import pytest

@pytest.fixture
def browser():
    driver = setup_driver()
    yield driver
    driver.quit()

def test_login(browser):
    """Login testi örneği"""
    browser.get("https://example.com/login")

    username = browser.find_element(By.ID, "username")
    password = browser.find_element(By.ID, "password")

    username.send_keys("test_user")
    password.send_keys("test_pass")

    submit = browser.find_element(By.ID, "submit")
    submit.click()

    # Assertion
    assert "Welcome" in browser.page_source
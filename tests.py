import time

import pytest
from selenium import webdriver

from pom.pages import RegisterPage, SuccessSubmitPage

@pytest.yield_fixture()
def driver():
    driver = webdriver.Chrome(
        executable_path='chromedriver2.43'
    )
    driver.set_window_size(1024, 800)
    driver.implicitly_wait(10)
    driver.set_page_load_timeout(10)
    yield driver
    driver.quit()

def test_uc_1_required_fields(driver):
    register_page = RegisterPage(driver)
    register_page.open_page()
    register_page.scroll_down()
    register_page.submit = True
    assert register_page.error_message == 'This field is required.'
    assert 'There are errors on the form' in register_page.error_button_message
    assert driver.current_url == 'https://form.jotformeu.com/92251830338354'

def test_uc_2_saved_values(driver):
    register_page = RegisterPage(driver)
    register_page.open_page()
    register_page.first = ''
    register_page.last = ''
    register_page.birth_month = 'January'
    register_page.birth_day = '1'
    register_page.birth_year = '2000'
    register_page.instrument = 'Violin'
    register_page.monday = True
    register_page.tueseday = False
    register_page.wednesday = True
    register_page.scroll_down()
    register_page.start_date_month = '11'
    register_page.start_date_day = '11'
    register_page.start_date_year = '1900'
    register_page.start_time_hours = '11'
    register_page.start_time_minutes = '10'
    register_page.ampm = 'PM'
    register_page.comment = 'autotest comment'
    register_page.submit = True
    assert register_page.birth_month == 'January'
    assert register_page.birth_day == '1'
    assert register_page.birth_year == '2000'
    assert register_page.instrument == 'Violin'
    assert register_page.monday == True
    assert register_page.tueseday == False
    assert register_page.wednesday == True
    assert register_page.start_date_month == '11'
    assert register_page.start_date_day == '11'
    assert register_page.start_date_year == '1900'
    assert register_page.start_time_hours == '11'
    assert register_page.start_time_minutes == '10'
    assert register_page.ampm == 'PM'
    assert register_page.comment == 'autotest comment'

def test_uc_3_submit_form(driver):
    register_page = RegisterPage(driver)
    success_page = SuccessSubmitPage(driver)
    register_page.open_page()
    register_page.first = 'selenium'
    register_page.last = 'autotest'
    register_page.birth_month = 'January'
    register_page.birth_day = '1'
    register_page.birth_year = '2000'
    register_page.instrument = 'Violin'
    register_page.monday = True
    register_page.scroll_down()
    register_page.comment = 'autotest comment'
    register_page.submit = True
    assert 'Your submission has been received' in success_page.success_text

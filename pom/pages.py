from .locators import RegFormLocators, SuccessSubmitPageLocators
from .element import *

class BasePage:
    def __init__(self, driver):
        self.driver = driver


class RegisterPage(BasePage):
    first = InputElement(RegFormLocators.first)
    last = InputElement(RegFormLocators.last)
    birth_month = SelectElement(RegFormLocators.birth_month)
    birth_day = SelectElement(RegFormLocators.birth_day)
    birth_year = SelectElement(RegFormLocators.birth_year)
    instrument = SelectElement(RegFormLocators.instrument)
    monday = CheckboxElement(RegFormLocators.monday)
    tueseday = CheckboxElement(RegFormLocators.tueseday)
    wednesday = CheckboxElement(RegFormLocators.wednesday)
    thursday = CheckboxElement(RegFormLocators.thursday)
    friday = CheckboxElement(RegFormLocators.friday)
    saturday = CheckboxElement(RegFormLocators.saturday)
    sunday = CheckboxElement(RegFormLocators.sunday)
    start_date_month = InputElement(RegFormLocators.start_date_month)
    start_date_day = InputElement(RegFormLocators.start_date_day)
    start_date_year = InputElement(RegFormLocators.start_date_year)
    start_time_hours = SelectElement(RegFormLocators.start_time_hours)
    start_time_minutes = SelectElement(RegFormLocators.start_time_minutes)
    ampm = SelectElement(RegFormLocators.ampm)
    comment = InputElement(RegFormLocators.comment)
    submit = ClickableElement(RegFormLocators.submit)
    error_message = TextElement(RegFormLocators.error_message)
    error_button_message = TextElement(RegFormLocators.button_error)

    def open_page(self):
        self.driver.get('https://form.jotformeu.com/92251830338354')

    def scroll_down(self):
        w_elem = self.driver.find_element(*RegFormLocators.submit)
        self.driver.execute_script("return arguments[0].scrollIntoView();", w_elem)

class SuccessSubmitPage(BasePage):
    success_text = TextElement(SuccessSubmitPageLocators.success_text)
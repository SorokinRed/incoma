from selenium.webdriver.common.by import By

class RegFormLocators:
    first = (By.ID, "first_3")
    last = (By.ID, "last_3")
    birth_month = (By.ID, "input_4_month") 
    birth_day = (By.ID, "input_4_day") 
    birth_year = (By.ID, "input_4_year") 
    instrument = (By.ID, "input_5") 
    monday = (By.ID, "input_6_0") 
    tueseday = (By.ID, "input_6_1") 
    wednesday = (By.ID, "input_6_2") 
    thursday = (By.ID, "input_6_3")
    friday = (By.ID, "input_6_4")
    saturday = (By.ID, "input_6_5")
    sunday = (By.ID, "input_6_6")
    start_date_month = (By.ID, "month_7")
    start_date_day = (By.ID, "day_7")
    start_date_year = (By.ID, "year_7")
    start_time_hours = (By.ID, "hour_7")
    start_time_minutes = (By.ID, "min_7")
    ampm = (By.ID, "ampm_7")
    comment = (By.ID, "input_8")
    submit = (By.ID, "input_2")
    error_message = (By.CLASS_NAME, 'form-error-message')
    button_error = (By.CLASS_NAME, 'form-button-error')


class SuccessSubmitPageLocators:
    success_text = (By.XPATH, "//*[contains(text(), 'Your submission has been received.')]")
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement:
    def __init__(self, locator):
        self.locator = locator

    def __set__(self, obj, value):
        pass

    def __get__(self, obj, owner):
        driver = obj.driver
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.locator)
        )
        return element.is_displayed()


class InputElement(BaseElement):
    def __set__(self, obj, value):
        driver = obj.driver
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.locator)
        )
        element.clear()
        element.send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        element = WebDriverWait(driver, 100).until(
            EC.element_to_be_clickable(self.locator)
        )
        return element.get_attribute("value")


class SelectElement(BaseElement):
    def __set__(self, obj, value):
        driver = obj.driver
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.locator)
        )
        element.send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        element = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located(self.locator)
        )
        return element.get_attribute("value")


class TextElement(BaseElement):
    def __set__(self, obj, value):
        raise Exception("Text can not be editable")

    def __get__(self, obj, owner):
        driver = obj.driver
        element = WebDriverWait(driver, 100).until(
            EC.element_to_be_clickable(self.locator)
        )
        return element.text


class ClickableElement(BaseElement):
    '''
    Для клика объекту присвоить True
    Да, неявно. Но я хз как сделать явно и коротко
    '''
    def __set__(self, obj, value):
        driver = obj.driver
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.locator)
        )
        if value:
            element.click()
            return True
        raise Exception("Element can not be editable. For click set True")

    def __get__(self, obj, owner):
        driver = obj.driver
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.locator)
        )
        return element.is_displayed()


class CheckboxElement(BaseElement):
    '''
    True - selected
    False - not selected
    None - actions not complete
    '''
    def __set__(self, obj, value):
        driver = obj.driver
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.locator)
        )
        if value and not element.is_selected():
            element.click()
            return element.is_selected()

        if not value and element.is_selected():
            element.click()
            return element.is_selected()
        
        return None

    def __get__(self, obj, owner):
        driver = obj.driver
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(self.locator)
        )
        return element.is_selected()

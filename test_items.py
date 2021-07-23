import pytest
import time
from selenium.common.exceptions import NoSuchElementException


# Тест будет проходить два раза. Первый успешно, второй раз тест упадет с ошибкой, т.к. на странице нет нужной кнопки.
@pytest.mark.parametrize('links', [" http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/", "http://selenium1py.pythonanywhere.com/"])
def test_button_presence(browser, links):
    try:
        browser.get(f"{links}")
        time.sleep(10)
        button = browser.find_element_by_class_name("btn-add-to-basket")
    except NoSuchElementException:
        pytest.fail("There is no buy button on the page")
        # assert False, "There is no buy button on the page"
        # Второй вариант вывода нужной ошибки.






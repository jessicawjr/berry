import pytest
from unittest import mock

from selenium import webdriver

from baidu.base import baidu


@pytest.fixture(scope="function")
def driver_mock():
    ''' Returns a mock selenium driver object
    '''
    return mock.create_autospec(webdriver.Firefox)


@pytest.fixture(scope="module")
def driver(request):
    '''
    Returns a Selenium driver object
    '''
    d = webdriver.Firefox()
    d.set_window_size(1000, 1500)

    def cleanup_driver():
        d.quit()

    request.addfinalizer(cleanup_driver)

    return d


@pytest.fixture(scope='function')
def bd(driver_mock):
    return baidu(driver_mock)

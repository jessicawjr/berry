from unittest.mock import MagicMock
from unittest.mock import call


def test_go_to_url(bd):
    bd.go_to_baidu()
    assert bd.driver.get.called


def test_login_click(driver_mock, bd):
    elem = MagicMock()
    driver_mock.find_element_by_link_text.return_value = elem
    bd.login_click()
    assert elem.click.called
    assert elem.click.call_count == 1


def test_login_baidu(driver_mock, bd):
    elem = MagicMock()
    driver_mock.find_element_by_xpath.return_value = elem
    bd.login_baidu('name', 'password')
    assert elem.send_keys.call_args_list == [call('name'), call('password')]
    assert elem.click.called
    assert elem.click.call_count == 1

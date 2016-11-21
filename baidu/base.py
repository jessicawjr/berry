from baidu.environments import bdEnvironment as ENV


class baidu(object):
    """ The base class baidu """
    def __init__(self, driver, env=ENV.WWW):
        self.driver = driver
        self.env = env

    def go_to_baidu(self):
        self.driver.get('http://www.baidu.com')

    def login_click(self):
        self.driver.find_element_by_link_text("登录").click()

    def login_baidu(self, username, password):
        username_xpath = "//input[@name='userName']"
        password_xpath = "//input[@name='password']"
        login_button_xpath = "//input[@value='登录']"
        self.driver.find_element_by_xpath(username_xpath).send_keys(username)
        self.driver.find_element_by_xpath(password_xpath).send_keys(password)
        self.driver.find_element_by_xpath(login_button_xpath).click()

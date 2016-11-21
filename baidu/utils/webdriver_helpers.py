class WebDriverContextManager(object):
    """
    Context manager for Selenium webdriver objects. Use when you need to ensure
    the webdriver object gets cleaned up correctly

    Example Usage:
    from . import WebDriverContextManager as WebDriverCM

    with WebDriverCM("chrome") as driver:
        driver.get("http://www.google.com")
    """

    def __init__(self, browser=None, grid_args=None):
        pass

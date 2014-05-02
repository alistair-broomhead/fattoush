"""
Functions for putting together sauce configuration,
be it from environmental variables or from a JSON string.
"""
from selenium.webdriver import DesiredCapabilities


class FattoushConfig(object):

    def run(self):
        pass

    def __init__(self, index, browser, server, lettuce):
        """
        :param index: int
        :param browser: dict
        :param server: dict
        :param lettuce: dict
        """
        self.index = index
        self.server = server
        self.browser = browser.copy()
        self.run_args = lettuce

    @property
    def command_executor(self):
        return 'http://127.0.0.1:4444/wd/hub'

    def desired_capabilities(self, scenario):
        """
        :param scenario: Scenario
        """
        capabilities = DesiredCapabilities.CHROME
        capabilities.update({"name": scenario.name})
        return capabilities

"""
The driver class shall be a subclass of WebDriver with a classmethod
`instance()` which takes the current step or feature and returns
the active WebDriver instance.
"""

from selenium.webdriver import Remote
from lettuce.core import Step, Scenario
from .. import world
from .sauce import Sauce, Local


class Driver(Remote):

    @classmethod
    def instance(cls, step_or_scenario):
        """
        :return : Driver
        """
        pass

    @classmethod
    def has_instance(cls, step_or_scenario):
        return False

    @classmethod
    def kill_instance(cls, scenario):
        cls.instance(scenario).quit()

    def __init__(self, config, scenario):
        """
        :param config: fattoush.config.FattoushConfig
        :param scenario: Scenario
        """
        self.fattoush_config = config

        super(Driver, self).__init__(config.command_executor,
                                     config.desired_capabilities(
                                         scenario))

        kwargs = dict(config=config,
                      browser=self)

        # For saucelabs you need a user name and an auth key
        if "user" in config.server:
            self.sauce = Sauce(**kwargs)
        else:
            self.sauce = Local(**kwargs)
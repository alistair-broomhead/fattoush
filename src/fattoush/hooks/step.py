"""
Hooks that run before and after steps
"""

from lettuce import world, before, after
import time
from selenium.common.exceptions import WebDriverException


@before.each_step
def hook_store_augmented_step_name(step):
    """
    Get a more meaningful step name that can be used in reporting
    while this step runs.
    """
    pass


@after.each_step
def hook_after_step(step):
    """
    Makes sure a screen shot is taken in Saucelabs after each test
    step. If the step passed leave it on the sever, if it failed we
    want a copy.
    """
    pass
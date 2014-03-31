"""
Hooks that run before and after scenarios
"""

from lettuce import before, after


@before.each_scenario
def hook_rename_scenario(scenario):
    pass

@after.each_scenario
def hook_destroy_sauce_connection(scenario):
    """
    Quits any sauce session in progress and removes the connection
    manager object from the world object namespace.
    """
    pass
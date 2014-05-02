"""
Hooks that run before and after features
"""

from lettuce import world, before


@before.each_feature
def hook_before_feature(feature):
    """
    Change the feature name to include information about where it is
    running - this will appear in the Saucelabs session and so
    having this information makes it easier to see where any
    unexpected behaviour may have occurred.
    """
    config = world.fattoush
    feature.name = "[{0}] {1}".format(config.name, feature.name)
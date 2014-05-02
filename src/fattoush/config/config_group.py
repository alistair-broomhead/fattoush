"""
Functions and classes for taking commandline arguments and forming an
object which will give you a set of FattoushConfig objects, each of
which contains all the information necessary to run lettuce against a
specified webdriver configuration, whither in saucelabs or local.
"""


class FattoushConfigGroup(object):

    @staticmethod
    def config_from_env():
        return {}

    @staticmethod
    def config_from_file(absolute_file_path):
        return {}

    @property
    def to_dict(self):
        """
        The returned dictionary gives a shallow copy of the data
        required to create a FeatureConfig.
        """
        return {}

    def run(self):
        pass
"""
I need to work out what this needs to be.
"""
from abc import ABCMeta, abstractmethod


class SauceInterface(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_session_configuration(self, **conf):
        pass

    @abstractmethod
    def fail_session(self):
        pass

    @abstractmethod
    def set_session_configuration(self, **conf):
        pass

    @abstractmethod
    def add_file_to_storage(self, binary_string, server_path,
                            overwrite=False):
        return "sauce:storage:NAME"


class Local(SauceInterface):
    pass


class Sauce(SauceInterface):
    pass
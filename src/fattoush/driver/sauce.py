"""
I need to work out what this needs to be.
"""
from abc import ABCMeta, abstractmethod
import hmac
import json


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


class AbstractSauceBase(SauceInterface):

    __metaclass__ = ABCMeta

    session_text_template = "SauceOnDemandSessionID={0} job-name={1}"
    public_url_template = "https://saucelabs.com/jobs/{0}?auth={1}"

    user = "saucelabs_username"
    key = "saucelabs_api_key"

    default_headers = {}

    def __init__(self, config, browser):
        """
        :param config: fattoush.config.FattoushConfig
        :param browser: fattoush.driver.driver.Driver
        """

        # Bind copy of class defaults to instance
        self.default_headers = self.default_headers.copy()

        self.wd_hub = config.command_executor
        self.session_name = config.name

        self.browser = browser
        self.job_id = browser.session_id

        self.combined_key = "{0}:{1}".format(self.user, self.key)
        self.token = hmac.new(self.combined_key,
                              self.job_id).hexdigest()

        self.public_url = self.public_url_template.format(self.job_id,
                                                          self.token)

    @abstractmethod
    def request(self, endpoint, method='GET', body=None,
                extra_headers=None):
        return "Response"

    def set_session_configuration(self, **conf):
        body_content = json.dumps(conf)
        endpoint = '/rest/v1/{0}/jobs/{1}'.format(self.user,
                                                  self.job_id)

        self.request(endpoint, 'PUT', body_content)

    def fail_session(self):
        self.set_session_configuration(passed=False)

    def add_file_to_storage(self, binary_string, server_path,
                            overwrite=False):
        endpoint = '/rest/v1/storage/%s/%s?overwrite=%s' % (
            self.user.strip('/'),
            server_path.strip('/'),
            ('false', 'true')[overwrite])
        ret = self.request(endpoint=endpoint, method='POST',
                           body=binary_string)
        return "sauce-storage:%s" % server_path, ret

    @property
    def scenario_details(self):
        return {
            "user": self.user,
            "job_id": self.job_id,
            "session_name": self.session_name,
            "key": self.combined_key,
            "token": self.token,
            "public_url": self.public_url,
        }


class Local(AbstractSauceBase):
    def request(self, endpoint, method='GET', body=None,
                extra_headers=None):
        print ("Would [{0}]{1} with body of {2} (extra-headers={3})"
               .format(method, endpoint, body, extra_headers))

    def __init__(self, config, browser):
        super(Local, self).__init__(config, browser)


class Sauce(AbstractSauceBase):
    def request(self, endpoint, method='GET', body=None,
                extra_headers=None):
        return super(Sauce, self).request(endpoint, method, body,
                                          extra_headers)
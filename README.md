Fattoush
========

Fattoush is a package that combines lettuce, webdriver and sauce to make a tasty UI testing salad.


Running
-------

Fattoush provides its own test runner which invokes lettuce such that it can run in saucelabs, with support of parallel test runs.

    $ fattoush --parallel=webdriver

By default Fattoush will run sets of tests in series with webdriver configuration should be read from environmental variables as described at [http://saucelabs.com/teamcity/3](http://saucelabs.com/teamcity/3). There is also support for running lettuce in a separate process for each webdriver configuration.

Usage
-----

Just write your lettuce tests as normal, but in your terrain file add

    from fattoush import Driver, hooks

and in each step definition module you are able to add

    from fattoush import Driver

The hooks module simply uses `lettuce.before` and `lettuce.after` to set up `lettuce.world` for each test feature, scenario, and step, ensuring that each scenario gets a fresh webdriver session and that each step is correctly logged.


Possible Future Work
--------------------

 - Test runner (not yet implemented)
 - Hooks (not yet implemented)
 - Driver (not yet implemented)
 - Page abstract class
# -*- coding: utf-8 -*-
import json

import mock

import fattoush

from fattoush.config import FattoushConfig


@fattoush.step_plain(u'Given I pass desired capabilities of "(.*)"')
def given_i_pass_desired_capabilities_of(capabilities_json):
    fattoush.per.scenario['capabilities'] = json.loads(capabilities_json)


@fattoush.step_plain(u'When fattoush creates a configurations from this')
def when_fattoush_creates_a_configurations_from_this():
    fattoush.per.scenario['config'] = FattoushConfig(
        index=None,
        browser={
            'capabilities': fattoush.per.scenario['capabilities']
        },
        server={},
        lettuce_cfg=mock.MagicMock(),
    )


@fattoush.step_plain(u'Then the configuration name is "([^"]*)"')
def then_the_configuration_name_is(expected):
    actual = fattoush.per.scenario['config'].name
    assert actual == expected, 'Expected {!r} but got {!r}'.format(
        expected, actual
    )


@fattoush.step_plain(u'Then it does not crash')
def then_it_does_not_crash():
    # This is a no-op, as it is essentially just saying that
    # the previous step did not raise an exception - if that
    # were not true we would never reach this step.
    pass

import pytest
from appdaemontestframework import HassMocks, AssertThatWrapper, GivenThatWrapper, TimeTravelWrapper, automation_fixture

class DeprecatedDict(dict):
    """Helper class that will give a deprectaion warning when accessing any of it's members"""
    def __getitem__(self, key):
        message = textwrap.dedent(
            """
            Usage of the `hass_functions` test fixture is deprecated.
            Replace `hass_functions` with the `hass_mocks` test fixture and access the `hass_functions` property.
                hass_functions['{0}'] ==becomes==> hass_mocks.hass_functions['{0}']
            """.format(key))
        warnings.warn(message, DeprecationWarning, stacklevel=2)
        return super().__getitem__(key)

@pytest.fixture
def hass_mocks():
    hass_mocks = HassMocks()
    yield hass_mocks
    hass_mocks.unpatch_mocks()

@pytest.fixture
def hass_functions(hass_mocks):
    return DeprecatedDict(hass_mocks.hass_functions)

@pytest.fixture
def given_that(hass_mocks):
    return GivenThatWrapper(hass_mocks)


@pytest.fixture
def assert_that(hass_mocks):
    return AssertThatWrapper(hass_mocks)


@pytest.fixture
def time_travel(hass_mocks):
    return TimeTravelWrapper(hass_mocks)
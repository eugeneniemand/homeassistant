import modules.lights as lights
import apps.RandomLights as RandomLights
from appdaemontestframework import HassMocks, AssertThatWrapper, GivenThatWrapper, TimeTravelWrapper, automation_fixture

light_states = {             
    'light.entrance': {'state': 'off'}, 
    'light.bathroom1': {'state': 'on'}, 
    'light.bathroom': {'state': 'on'},
    'light.master': {'state': 'on'}
}

@automation_fixture(RandomLights)
def random_lights:
    pass

def test_turn_on_random_light_and_timer(given_that, random_lights, assert_that):
    given_that.
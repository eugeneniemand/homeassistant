import copy
import modules.lights as lights
import random


light_states = {             
    'light.entrance': {'state': 'off'}, 
    'light.bathroom1': {'state': 'on'}, 
    'light.bathroom': {'state': 'on'},
    'light.master': {'state': 'on'}
}
timer_states = {             
    'timer.entrance': {'state': 'idle'}, 
    'timer.master': {'state': 'idle'}, 
    'timer.porch': {'state': 'idle'}, 
    'timer.bathroom': {'state': 'active'}
}

def test_get_on_lights():
    actual = lights.get_on_lights(light_states)
    expected = ['bathroom','master']
    assert actual == expected

def test_get_on_timers():
    actual = lights.get_idle_timers(timer_states)
    expected = ['entrance','master', 'porch']
    assert actual == expected

def test_get_lights_without_timers():        
    actual = lights.get_lights_without_timers(light_states,timer_states)
    expected = ['master']
    assert actual == expected

def test_build_message_one_light_count():
    actual = lights.build_message("LightsCount", light_states, timer_states)
    expected = "1 light on"
    assert actual == expected

def test_build_message_one_light_info():
    actual = lights.build_message("LightsInfo", light_states, timer_states)
    expected = "master"
    assert actual == expected

def test_build_message_two_light_count():
    tmp_light_states = copy.deepcopy(light_states)
    tmp_light_states['light.porch'] = {'state': 'on'}
    actual = lights.build_message("LightsCount", tmp_light_states, timer_states)
    expected = "2 lights on"
    assert actual == expected

def test_build_message_two_light_info():
    tmp_light_states = copy.deepcopy(light_states)
    tmp_light_states['light.porch'] = {'state': 'on'}
    actual = lights.build_message("LightsInfo", tmp_light_states, timer_states)
    expected = "master, porch"
    assert actual == expected

def test_get_random_light():
    random.seed(0)
    randomLight = lights.get_random_light(light_states)
    assert 'light.master' == randomLight
    random.seed(1)
    randomLight = lights.get_random_light(light_states)
    assert 'light.bathroom1' == randomLight

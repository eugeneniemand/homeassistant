from apps.NotificationEngine import NotificationEngine
from appdaemontestframework import HassMocks, AssertThatWrapper, GivenThatWrapper, TimeTravelWrapper, automation_fixture

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

@automation_fixture(NotificationEngine)
def notification_engine():
    pass

def test_callbacks_are_registered(given_that, notification_engine, assert_that):
    assert_that(notification_engine) \
        .listens_to.event('MQTT_MESSAGE', topic = "homeassistant/notification/tts") \
        .with_callback(notification_engine.mqtt_message_recieved_event)
    
def test_during_night_light_turn_on(given_that, notification_engine, assert_that):
    given_that.state_of('light').is_set_to(light_states)    
    given_that.state_of('timer').is_set_to(timer_states)
    notification_engine.mqtt_message_recieved_event(None, {'topic': 'homeassistant/notification/tts', 'payload': '{"Messages":["Windows","Doors","LightsCount","Tele"]}'},  None)
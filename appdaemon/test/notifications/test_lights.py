import unittest
import copy
import lights 

class MyTest(unittest.TestCase):
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

    def test_get_on_lights(self):
         actual = lights.get_on_lights(self.light_states)
         expected = ['bathroom','master']
         self.assertCountEqual(actual,expected)

    def test_get_on_timers(self):
         actual = lights.get_idle_timers(self.timer_states)
         expected = ['entrance','master', 'porch']
         self.assertCountEqual(actual,expected)

    def test_get_lights_without_timers(self):        
        actual = lights.get_lights_without_timers(self.light_states,self.timer_states)
        expected = ['master']
        self.assertCountEqual(actual,expected)

    def test_build_message_one_light_count(self):
        actual = lights.build_message("LightsCount", self.light_states, self.timer_states)
        expected = "1 light on"
        self.assertEqual(actual,expected)

    def test_build_message_one_light_info(self):
        actual = lights.build_message("LightsInfo", self.light_states, self.timer_states)
        expected = "master"
        self.assertEqual(actual,expected)

    def test_build_message_two_light_count(self):
        tmp_light_states = copy.deepcopy(self.light_states)
        tmp_light_states['light.porch'] = {'state': 'on'}
        actual = lights.build_message("LightsCount", tmp_light_states, self.timer_states)
        expected = "2 lights on"
        self.assertEqual(actual,expected)

    def test_build_message_two_light_info(self):
        tmp_light_states = copy.deepcopy(self.light_states)
        tmp_light_states['light.porch'] = {'state': 'on'}
        actual = lights.build_message("LightsInfo", tmp_light_states, self.timer_states)
        expected = "master, porch"
        self.assertCountEqual(actual,expected)

if __name__ == '__main__':
    unittest.main()
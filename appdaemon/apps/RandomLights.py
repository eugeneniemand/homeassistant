import appdaemon.plugins.hass.hassapi as hass
class HassApp(hass.Hass):
     
    
    def mqtt_message_recieved_event(self, event_name, data, kwargs):
        self.log(event_name)
        
    def initialize(self):
        self.log("HassApp Init")
        self.set_namespace("mqtt")
        #self.listen_event(self.mqtt_message_recieved_event, "MQTT_MESSAGE")
        self.set_namespace("hass")
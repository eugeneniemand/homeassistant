import appdaemon.plugins.hass.hassapi as hass
import modules.utils as utils
import modules.lights as lights
import json

class NotificationEngine(hass.Hass):

    def message_builder(self, messageType): 
        return lights.build_message(messageType, self.get_state("light"), self.get_state("timer"))

    def mqtt_message_recieved_event(self, event_name, data, kwargs):        
        payload = json.loads(data["payload"])
        message = ""
        for msg in payload["Messages"]:
            message += self.message_builder(msg)

        if message != "":
            self.fire_event("MQTT_PUBLISH", topic = "appdaemon/notification/tts", message = json.dumps({"message": message})) 
        else:
            self.log("Nothing to publish")

    def initialize(self):
        self.log("NotitfyApp Init")
        self.set_namespace("mqtt")
        self.listen_event(self.mqtt_message_recieved_event, "MQTT_MESSAGE", topic = "homeassistant/notification/tts")
        self.set_namespace("hass")
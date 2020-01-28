import appdaemon.plugins.mqtt.mqttapi as mqtt
class MqttApp(mqtt.Mqtt):
        
    def mqtt_publish_event(self, event_name, data, kwargs):
        self.log(data)
        self.mqtt_publish(data["topic"], data["message"], qos = 0, retain = False)

    def initialize(self):
        self.log("MqttApp Init")
        self.set_namespace("hass")
        self.listen_event(self.mqtt_publish_event, "MQTT_PUBLISH")
        self.set_namespace("mqtt")

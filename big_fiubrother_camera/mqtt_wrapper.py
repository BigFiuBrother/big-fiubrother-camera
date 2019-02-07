import paho.mqtt.client as mqtt
import uuid
import logging

class MqttWrapper:

    def __init__(self, settings):
        self.host = settings['receiver_url']
        self.topic = settings['topic']
        self.qos = settings['qos']

        self.client = mqtt.Client(client_id=uuid.uuid1().hex,
                                  clean_session=True)

        self.client.username_pw_set(settings['user'], settings['password'])
        self.client.connect(self.host)
        self.client.loop_start()
    
        logging.debug('MqttWrapper created with host: {}, topic: {} and qos: {}'.format(self.host, self.topic, self.qos))

    def send(self, message):
        result = self.client.publish(topic=self.topic,
                                     payload=message,
                                     qos=self.qos)

        logging.debug('Message sent: {}'.format(message))

    def close(self):
        self.client.loop_stop()
        self.client.disconnect()
        logging.debug('MqttWrapper connection closed')
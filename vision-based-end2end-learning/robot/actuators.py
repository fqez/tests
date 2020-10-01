from .interfaces.motors import PublisherMotors


class Actuators:

    def __init__(self, actuators_config):

        # Load cameras
        motors_conf = actuators_config.get('Cameras', None)
        self.motors = None
        if motors_conf:
            self.motors = self.__create_actuator(motors_conf, 'motor')

    def __create_actuator(self, actuator_config, actuator_type):

        actuator_dict = {}

        for elem in actuator_config:
            name = actuator_config[elem]['Name']
            topic = actuator_config[elem]['Topic']
            vmax = actuator_config[elem]['MaxV']
            wmax = actuator_config[elem]['MaxW']
            if actuator_config == 'motor':
                actuator_config[name] = PublisherMotors(topic, vmax, wmax, 0, 0)

        return actuator_dict

    def __get_actuator(self, actuator_name, actuator_type):

        actuator = None
        try:
            if actuator_type == 'motor':
                actuator = self.cameras[actuator_name]
        except KeyError:
            return f"[ERROR] No existing camera with {actuator_name} name."

        return actuator

    def get_motor(self, motor_name):
        return self.__get_actuator(motor_name, 'motor')



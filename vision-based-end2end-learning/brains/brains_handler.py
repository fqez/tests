import importlib
from abc import ABC, abstractmethod

class Brains:

    def __init__(self, sensors, actuatrors):

        self.sensors = sensors
        self.actuatrors = actuatrors
        self.active_brain = None

    def load_brain(self, path):

        path_split = path.split("/")
        module_dir = path_split[-2]
        robot_type = path_split[-3]
        module_name = path_split[-1][:-3]  # removing .py extension
        import_name = 'brains.' + robot_type + '.' + module_dir + '.' + module_name
        module = importlib.import_module(import_name)

        Brain = getattr(module, 'Brain')
        self.active_brain = Brain(self.sensors, self.actuatrors)

    def get_image(self, camera_name):
        camera = self.sensors.get_camera(camera_name)
        return camera.getImage()

    def get_laser_data(self, laser_name):
        laser = self.sensors.get_laser(laser_name)
        return laser.getLaserData()

    def get_motors(self, motors_name):
        return self.actuatrors.get_motor(motors_name)


    @abstractmethod
    def execute(self):
        pass

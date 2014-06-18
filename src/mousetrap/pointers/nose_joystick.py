import mousetrap.pointers.interface as interface
from mousetrap.vision import FeatureDetector, FeatureNotFoundException
from mousetrap.gui import Gui, ScreenPointer, ScreenPointerEvent

from mousetrap.pointers.nose import NoseLocator


class Pointer(interface.Pointer):
    THRESHOLD = 5

    def __init__(self):
        self._nose_locator = NoseLocator()
        self._image = None

        self._pointer = ScreenPointer()

        self._initial_image_location = (0, 0)
        self._last_delta = (0, 0)

        self._location = self._pointer.get_position()

        self._tracking = False

    def update_image(self, image):
        self._image = image
        try:
            point_image = self._nose_locator.locate(image)
            self._tracking = True
            point_screen = self._convert_image_to_screen_point(*point_image)
            self._location = point_screen
        except FeatureNotFoundException:
            self._tracking = False
            location = self._pointer.get_position()
            self._location = self._apply_delta_to_point(location,
                                                        self._last_delta)

    def _apply_delta_to_point(self, point, delta):
        delta_x, delta_y = delta
        point_x, point_y = point

        if delta_x == 0 and delta_y == 0:
            return None

        point_x += delta_x
        point_y += delta_y

        return (point_x, point_y)

    def _convert_image_to_screen_point(self, image_x, image_y):
        initial_x, initial_y = self._initial_image_location

        if initial_x == 0 and initial_y == 0:
            self._initial_image_location = (image_x, image_y)

            return self._initial_image_location

        delta_x = initial_x - image_x
        delta_y = image_y - initial_y

        if abs(delta_x) < self.THRESHOLD:
            delta_x = 0

        if abs(delta_y) < self.THRESHOLD:
            delta_y = 0

        delta = (delta_x, delta_y)

        self._last_delta = delta

        location = self._pointer.get_position()

        return self._apply_delta_to_point(location, delta)

#    def get_new_position(self):
#        return self._location

    def is_tracking(self):
        return self._tracking

    def get_pointer_events(self):
        if self._location is None:
            return []
        else:
            return [ScreenPointerEvent(ScreenPointer.EVENT_MOVE, self._location)]

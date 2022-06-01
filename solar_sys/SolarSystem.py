from PyQt5.QtCore import QTimer

from CelestialObject import Sun, Earth, Moon, Pluto


class SolarSystem:
    def __init__(self, w):
        self._sun = Sun(w)
        self._earth = Earth(w)
        self._moon = Moon(w)
        self._pluto = Pluto(w)

        self._timer = QTimer()
        self._timer.timeout.connect(self.animate)
        self._timer.start(20)

        self._time = 0

        self._sun.draw(w)
        self._earth.draw(w)
        self._moon.draw(w)
        self._pluto.draw(w)

    def animate(self):
        self._pluto.animate(self._time)
        coordinate_vector = self._earth.animate(self._time)
        self._moon.animate(self._time, coordinate_vector[0][0], coordinate_vector[0][1], coordinate_vector[0][2] - self._earth.radius)
        self._time += 1
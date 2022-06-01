import pyqtgraph.opengl as gl
import numpy
import math

from Formulas import Formulas
from Orbit import Orbit


class SpaceObject:
    def __init__(self):
        self._pts = None
        self.global_phi = None
        self.global_theta = None
        self.global_psi = None
        self.angle_step = 1

    def calculate_position(self, time):
        coordinate_vector = numpy.matmul(self._pts, Formulas.get_rot_mat('z', math.radians(self.angle_step * time)))

        rotate_matrix = Formulas.get_3d_rot_mat(_psi_rad=math.radians(self.global_psi),
                                                _theta_rad=math.radians(self.global_theta),
                                                _phi_rad=math.radians(self.global_phi))

        coordinate_vector = numpy.matmul(coordinate_vector, rotate_matrix)

        return coordinate_vector


class Sun:
    def __init__(self, w):
        self.meshData = None
        self.glMeshItem = None
        self.objectRadius = 3

    def draw(self, w):
        self.meshData = gl.MeshData.sphere(rows=10, cols=20, radius=self.objectRadius)
        self.glMeshItem = gl.GLMeshItem(
            meshdata=self.meshData,
            color=(0.95, 0.85, 0.09, 1)
        )
        w.addItem(self.glMeshItem)


class Earth(SpaceObject):
    def __init__(self, w):
        super().__init__()
        self.earth_orbit = Orbit(10, 0, w)
        self.md = None
        self._pts = None
        self.m1 = None
        self.angle_degree_step = 1
        self.radius = 2

        self.global_phi = 0
        self.global_psi = 0
        self.global_theta = 0

    def draw(self, w):
        self.md = gl.MeshData.sphere(rows=10, cols=20, radius=self.radius)
        self._pts = self.md.vertexes()
        self.m1 = gl.GLMeshItem(
            meshdata=self.md,
            color=(0.140, 0.39, 0.5, 1)
        )

        self._pts = numpy.add(self._pts, [0, 10, 0])
        self.md.setVertexes(self._pts)
        w.addItem(self.m1)

        self.earth_orbit.rotate(math.radians(self.global_psi),
                                math.radians(self.global_theta),
                                math.radians(self.global_phi))

    def animate(self, _time):
        coordinate_vector = self.calculate_position(_time)
        self.md.setVertexes(coordinate_vector)
        self.m1.setMeshData(meshdata=self.md)
        return coordinate_vector


class Moon(SpaceObject):
    def __init__(self, w):
        super().__init__()
        self.moon_orbit = Orbit(5, 0, w)
        self.md = None
        self.m1 = None
        self._pts = None
        self.angle_step = 2.25
        self.radius = 0.5
        self.global_phi = 30
        self.global_theta = 30
        self.global_psi = 30

    def draw(self, w):
        self.md = gl.MeshData.sphere(rows=10, cols=20, radius=self.radius)
        self._pts = self.md.vertexes()
        self.m1 = gl.GLMeshItem(
            meshdata=self.md,
            color=(0.5, 0.5, 0.5, 1)
        )

        self._pts = numpy.add(self._pts, [0, 5, 0])
        self.md.setVertexes(self._pts)
        w.addItem(self.m1)

        _psi_rad = math.radians(self.global_psi)
        _theta_rad = math.radians(self.global_theta)
        _phi_rad = math.radians(self.global_phi)
        self.moon_orbit.rotate(_psi_rad, _theta_rad, _phi_rad)

    def animate(self, _time, parent_x, parent_y, parent_z):
        coordinate_vector = self.calculate_position(_time)
        coordinate_vector = numpy.add(coordinate_vector, [parent_x, parent_y, parent_z])

        self.moon_orbit.set_position(parent_x, parent_y, parent_z)
        self.md.setVertexes(coordinate_vector)
        self.m1.setMeshData(meshdata=self.md)



class Pluto(SpaceObject):
    def __init__(self, w):
        super().__init__()
        self.pluto_orbit = Orbit(20, 0, w)
        self.md = None
        self._pts = None
        self.m1 = None
        self.angle_degree_step = 1
        self.radius = 1

        self.global_phi = 50
        self.global_psi = 30
        self.global_theta = -20

    def draw(self, w):
        self.md = gl.MeshData.sphere(rows=10, cols=20, radius=self.radius)
        self._pts = self.md.vertexes()
        self.m1 = gl.GLMeshItem(
            meshdata=self.md,
            color=(0.5, 0.2, 0.5, 1)
        )

        self._pts = numpy.add(self._pts, [0, 20, 0])
        self.md.setVertexes(self._pts)
        w.addItem(self.m1)

        self.pluto_orbit.rotate(math.radians(self.global_psi),
                                math.radians(self.global_theta),
                                math.radians(self.global_phi))

    def animate(self, _time):
        coordinate_vector = self.calculate_position(_time)
        self.md.setVertexes(coordinate_vector)
        self.m1.setMeshData(meshdata=self.md)
        return coordinate_vector


from Formulas import Formulas
import pyqtgraph.opengl as gl
import numpy


class Orbit:
    def __init__(self, _orbit_a, _orbit_e, w):

        self.__pts = Formulas.get_ellipse_pts_shifted(_orbit_a, _orbit_e)
        self.__psi = 0
        self.__theta = 0
        self.__phi = 0
        self.__plt = gl.GLLinePlotItem(pos=self.__pts, color=(0, 1, 0, 1), width=2)
        w.addItem(self.__plt)

    def set_position(self, coordinate_x, coordinate_y, coordinate_z):

        pts = numpy.add(self.__pts, [coordinate_x, coordinate_y, coordinate_z])
        self.__plt.setData(pos=pts)

    def rotate(self, _psi_rad, _theta_rad, _phi_rad):

        rot_mat = Formulas.get_3d_rot_mat(_psi_rad=_psi_rad, _theta_rad=_theta_rad, _phi_rad=_phi_rad)
        pts = numpy.dot(self.__pts, rot_mat)
        self.__plt.setData(pos=pts)
        self.__pts = pts
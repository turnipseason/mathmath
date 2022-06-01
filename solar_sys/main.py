import sys

from pyqtgraph.Qt import QtCore, QtGui, QtWidgets
import pyqtgraph.opengl as gl

from SolarSystem import SolarSystem


if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseDesktopOpenGL)
    application = QtWidgets.QApplication(sys.argv)
    w = gl.GLViewWidget()
    w.opts['distance'] = 40
    w.showMaximized()
    gridsize = QtGui.QVector3D(40,40,40)
    gx = gl.GLGridItem(size=gridsize)
    gx.rotate(90, 0, 1, 0)
    gx.translate(-20, 0, 0)
    w.addItem(gx)
    gy = gl.GLGridItem(size=gridsize)
    gy.rotate(90, 1, 0, 0)
    gy.translate(0, -20, 0)
    w.addItem(gy)
    gz = gl.GLGridItem(size=gridsize)
    gz.translate(0, 0, -20)
    w.addItem(gz)

    # AXIS
    size = QtGui.QVector3D(15, 15, 15)
    axis = gl.GLAxisItem(size, antialias=False)
    # z - green
    # y - yellow
    # x - blue
    w.addItem(axis)

    system = SolarSystem(w)
    system.animate()

    sys.exit(application.exec_())
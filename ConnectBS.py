from symbol import factor

from shiboken2 import wrapInstance

import os
import maya.cmds as cm
# import pymel.core as pm
import maya.OpenMaya as om
import maya.OpenMayaUI as omui

from PySide2 import QtWidgets, QtCore, QtGui
from maya.mel import eval


# import sys


class QHLine(QtWidgets.QFrame):

    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(self.HLine)
        self.setFrameShadow(self.Sunken)


class QVLine(QtWidgets.QFrame):

    def __init__(self):
        super(QVLine, self).__init__()
        self.setFrameShape(self.VLine)
        self.setFrameShadow(self.Sunken)


class QHLineName(QtWidgets.QGridLayout):

    def __init__(self, name):
        super(QHLineName, self).__init__()
        name_lb = QtWidgets.QLabel(name)
        name_lb.setAlignment(QtCore.Qt.AlignCenter)
        name_lb.setStyleSheet("font: italic 9pt;" "color: azure;")
        self.addWidget(name_lb, 0, 0, 1, 1)
        self.addWidget(QHLine(), 0, 1, 1, 2)


# noinspection PyAttributeOutsideInit
class ConnectBS(QtWidgets.QWidget):
    blendshape_list = {
        1: 'eyeBlinkLeft',
        2: 'eyeLookDownLeft',
        3: 'eyeLookInLeft',
        4: 'eyeLookOutLeft',
        5: 'eyeLookUpLeft',
        6: 'eyeSquintLeft',
        7: 'eyeWideLeft',
        8: 'eyeBlinkRight',
        9: 'eyeLookDownRight',
        10: 'eyeLookInRight',
        11: 'eyeLookOutRight',
        12: 'eyeLookUpRight',
        13: 'eyeSquintRight',
        14: 'eyeWideRight',
        15: 'jawForward',
        16: 'jawLeft',
        17: 'jawRight',
        18: 'jawOpen',
        19: 'mouthClose',
        20: 'mouthFunnel',
        21: 'mouthPucker',
        22: 'mouthLeft',
        23: 'mouthRight',
        24: 'mouthSmileLeft',
        25: 'mouthSmileRight',
        26: 'mouthFrownLeft',
        27: 'mouthFrownRight',
        28: 'mouthDimpleLeft',
        29: 'mouthDimpleRight',
        30: 'mouthStretchLeft',
        31: 'mouthStretchRight',
        32: 'mouthRollLower',
        33: 'mouthRollUpper',
        34: 'mouthShrugLower',
        35: 'mouthShrugUpper',
        36: 'mouthPressLeft',
        37: 'mouthPressRight',
        38: 'mouthLowerDownLeft',
        39: 'mouthLowerDownRight',
        40: 'mouthUpperUpLeft',
        41: 'mouthUpperUpRight',
        42: 'browDownLeft',
        43: 'browDownRight',
        44: 'browInnerUp',
        45: 'browOuterUpLeft',
        46: 'browOuterUpRight',
        47: 'cheekPuff',
        48: 'cheekSquintLeft',
        49: 'cheekSquintRight',
        50: 'noseSneerLeft',
        51: 'noseSneerRight',
        52: 'tongueOut',
    }

    def __init__(self):
        super(ConnectBS, self).__init__()

        self.create_widgets()
        self.create_layouts()
        self.create_connections()

    def create_widgets(self):
        self.driver_name_lb = QtWidgets.QLabel("Driver:")
        self.driver_name_lb.setToolTip("Ten node cua blendshape hoac control se dieu khien")
        self.driver_name_le = QtWidgets.QLineEdit()

        self.driven_name_lb = QtWidgets.QLabel("Driven:")
        self.driven_name_lb.setToolTip("Ten node cua blendshape hoac control se bi dieu khien")
        self.driven_name_le = QtWidgets.QLineEdit()

        self.fraction_lb = QtWidgets.QLabel("Fraction:")
        self.fraction_lb.setToolTip("Ty le quy doi")
        self.fraction_le = QtWidgets.QLineEdit()
        self.connect_bs_btn = QtWidgets.QPushButton("Connect BS")
        self.connect_bs_btn.setToolTip("Ket noi blendshape vao control hoac blenshape khac da chon")

    def create_layouts(self):
        first_layout = QtWidgets.QGridLayout()
        first_layout.addWidget(self.driver_name_lb, 0, 0)
        first_layout.addWidget(self.driver_name_le, 0, 1)
        first_layout.addWidget(self.driven_name_lb, 1, 0)
        first_layout.addWidget(self.driven_name_le, 1, 1)
        first_layout.addWidget(self.fraction_lb, 2, 0)
        first_layout.addWidget(self.fraction_le, 2, 1)

        second_layout = QtWidgets.QHBoxLayout()
        second_layout.addWidget(self.connect_bs_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(first_layout)
        main_layout.addLayout(second_layout)

    def create_connections(self):
        self.connect_bs_btn.clicked.connect(self.connect_blendshape)

    def connect_blendshape(self):
        fraction = self.fraction_le.text()
        if fraction:
            fraction = int(fraction)
        else:
            om.MGlobal_displayError("Dien ty le vao tro trong")

        driver_name = self.driver_name_le.text()
        print(driver_name)

        driven_name = self.driven_name_le.text()
        print(driven_name)

        if driven_name and driver_name:

            for i in range(1, 53):
                name_bs = self.blendshape_list.get(i)
                uc_node = cm.createNode("unitConversion", n=f"{driver_name}_{driven_name}_{name_bs}_uC")

                cm.setAttr(f"{uc_node}.conversionFactor", fraction)
                cm.connectAttr(f"{driver_name}.{name_bs}", f"{uc_node}.input",
                               f=True)
                cm.connectAttr(f"{uc_node}.output", f"{driven_name}.{name_bs}",
                               f=True)

        else:
            om.MGlobal_displayError("Lam on dien vao cho trong")


# noinspection PyMethodMayBeStatic,PyAttributeOutsideInit,PyMethodOverriding


class MainWindow(QtWidgets.QDialog):
    WINDOW_TITLE = "Connect blendshape ARKit"

    SCRIPTS_DIR = cm.internalVar(userScriptDir=True)
    ICON_DIR = os.path.join(SCRIPTS_DIR, 'Thi/Icon')

    dlg_instance = None

    @classmethod
    def display(cls):
        if not cls.dlg_instance:
            cls.dlg_instance = MainWindow()

        if cls.dlg_instance.isHidden():
            cls.dlg_instance.show()

        else:
            cls.dlg_instance.raise_()
            cls.dlg_instance.activateWindow()

    @classmethod
    def maya_main_window(cls):
        """

        Returns: The Maya main window widget as a Python object

        """
        main_window_ptr = omui.MQtUtil.mainWindow()
        return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)

    def __init__(self):
        super(MainWindow, self).__init__(self.maya_main_window())

        self.setWindowTitle(self.WINDOW_TITLE)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.geometry = None

        self.setMinimumSize(400, 150)
        self.setMaximumSize(400, 150)
        self.create_widget()
        self.create_layouts()
        self.create_connections()

    def create_widget(self):
        self.content_layout = QtWidgets.QHBoxLayout()
        self.content_layout.addWidget(ConnectBS())

        self.close_btn = QtWidgets.QPushButton("Close")

    def create_layouts(self):

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(self.content_layout)

    def create_connections(self):
        self.close_btn.clicked.connect(self.close)

    def showEvent(self, e):
        super(MainWindow, self).showEvent(e)

        if self.geometry:
            self.restoreGeometry(self.geometry)

    def closeEvent(self, e):
        super(MainWindow, self).closeEvent(e)

        self.geometry = self.saveGeometry()

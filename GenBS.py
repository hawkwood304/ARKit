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
class GenBS(QtWidgets.QWidget):
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
        super(GenBS, self).__init__()

        self.create_widgets()
        self.create_layouts()
        self.create_connections()

    def create_widgets(self):
        self.name_mesh_lb = QtWidgets.QLabel("Mesh name:")
        self.name_mesh_le = QtWidgets.QLineEdit()

        self.name_bs_node_lb = QtWidgets.QLabel("BlendShape node name:")
        self.name_bs_node_le = QtWidgets.QLineEdit()

        self.gen_bs_btn = QtWidgets.QPushButton("Gen BS")
        self.m2_bs_btn = QtWidgets.QPushButton("M2 connect")

    def create_layouts(self):
        first_layout = QtWidgets.QHBoxLayout()
        first_layout.addWidget(self.name_mesh_lb)
        first_layout.addWidget(self.name_mesh_le)

        second_layout = QtWidgets.QHBoxLayout()
        second_layout.addWidget(self.name_bs_node_lb)
        second_layout.addWidget(self.name_bs_node_le)

        third_layout = QtWidgets.QHBoxLayout()
        third_layout.addWidget(self.gen_bs_btn)
        third_layout.addWidget(self.m2_bs_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(first_layout)
        main_layout.addLayout(second_layout)
        main_layout.addLayout(third_layout)

    def create_connections(self):
        self.gen_bs_btn.clicked.connect(self.gen_bs)
        self.m2_bs_btn.clicked.connect(self.m2_connect_blendshape)

    def gen_bs(self):

        name_bs_node = self.name_bs_node_le.text()
        name_mesh = self.name_mesh_le.text()

        grp = cm.group(name=f"{name_bs_node}_grp", world=True, r=True, empty=True)
        cm.select(clear=True)
        if name_bs_node and name_mesh:
            for i in range(1, 53):
                name_bs = self.blendshape_list.get(i)
                cm.setAttr(f"{name_bs_node}.{name_bs}", 1)
                dup = cm.duplicate(name_mesh, name=name_bs, rr=False)
                cm.parent(dup, grp)
                cm.setAttr(f"{name_bs_node}.{name_bs}", 0)
        else:
            om.MGlobal_displayError("Need name blendshape node to compile")

    def m2_connect_blendshape(self):
        list_name_bs_node = ["blendShape__head_ply", "blendShape__teethGum_ply", "blendShape__eyelashesLower_ply",
                             "blendShape__eyelashesUpper_ply", "eyeLBS", "eyeRBS", "blendShape__eyebrow_ply",
                             "blendShape__eyeshell_ply", "blendShape__clothInside01_ply",
                             "blendShape__clothInside02_ply",
                             "blendShape__lowerLashes_ply", "blendShape__upperLashes_ply"]
        control_ARKit_name = "ctrlARKitBS_M"
        for my_blendShape_node in list_name_bs_node:
            if cm.objExists(my_blendShape_node):
                print(my_blendShape_node)
                for i in range(1, 53):
                    name_bs = self.blendshape_list.get(i)
                    uc_node = cm.createNode("unitConversion", n="{}_{}_uC".format(my_blendShape_node, name_bs))
                    cm.setAttr("{}.conversionFactor".format(uc_node), 0.1)
                    cm.connectAttr("{}.{}".format(control_ARKit_name, name_bs), "{}.input".format(uc_node),
                                   f=True)
                    cm.connectAttr("{}.output".format(uc_node), "{}.{}".format(my_blendShape_node, name_bs),
                                   f=True)


# noinspection PyMethodMayBeStatic,PyAttributeOutsideInit,PyMethodOverriding
class MainWindow(QtWidgets.QDialog):
    WINDOW_TITLE = "Gen BS"

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
        self.content_layout.addWidget(GenBS())

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

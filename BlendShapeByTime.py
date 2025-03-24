from shiboken2 import wrapInstance

import os
import maya.cmds as cm
import pymel.core as pm
import maya.OpenMaya as oMaya
import maya.OpenMayaUI as oMayaUI

from PySide2 import QtWidgets, QtCore, QtGui
from maya.mel import eval

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


# import sys

# noinspection PyAttributeOutsideInit
class BlendShapeByTime(QtWidgets.QWidget):

    def __init__(self):
        super(BlendShapeByTime, self).__init__()

        self.create_widgets()
        self.create_layouts()
        self.create_connections()

    def create_widgets(self):
        self.file_path_lb = QtWidgets.QLabel("File path: ")
        self.file_path_le = QtWidgets.QLineEdit()

        self.select_file_path_btn = QtWidgets.QPushButton('')
        self.select_file_path_btn.setIcon(QtGui.QIcon(':fileOpen.png'))
        self.select_file_path_btn.setToolTip('Select File')

        self.mesh_name_lb = QtWidgets.QLabel("Mesh name:")
        self.mesh_name_le = QtWidgets.QLineEdit()
        self.mesh_name_btn = QtWidgets.QPushButton("Assign")

        self.execution_btn = QtWidgets.QPushButton("Execution")
        self.execution_btn.setStyleSheet(
            'QPushButton {background-color: lightyellow; color: black;}'
        )

    def create_layouts(self):
        first_layout = QtWidgets.QGridLayout()
        first_layout.addWidget(self.file_path_lb, 0, 0, 1, 1)
        first_layout.addWidget(self.file_path_le, 0, 1, 1, 5)
        first_layout.addWidget(self.select_file_path_btn, 0, 6, 1, 1)

        first_layout.addWidget(self.mesh_name_lb, 1, 0, 1, 1)
        first_layout.addWidget(self.mesh_name_le, 1, 1, 1, 5)
        first_layout.addWidget(self.mesh_name_btn, 1, 6, 1, 1)

        second_layout = QtWidgets.QHBoxLayout()
        second_layout.addWidget(self.execution_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(first_layout)
        main_layout.addLayout(second_layout)

    def create_connections(self):
        self.select_file_path_btn.clicked.connect(self.show_file_select_dialog)
        self.mesh_name_btn.clicked.connect(self.assign_mesh_button)
        self.execution_btn.clicked.connect(self.execution_button)

    @staticmethod
    def execute_mel_command(command):
        try:
            eval(command)
            # logger.info(f"MEL command executed: {command}")
        except RuntimeError as e:
            logger.error(f"Failed to execute MEL command: {command} - {e}")

    def fbx_export_option(self, path):

        self.execute_mel_command("FBXExportSmoothingGroups -v true")
        self.execute_mel_command("FBXExportHardEdges -v false")
        self.execute_mel_command("FBXExportTangents -v false")
        self.execute_mel_command("FBXExportSmoothMesh -v true")
        self.execute_mel_command("FBXExportInstances -v false")
        self.execute_mel_command("FBXExportReferencedAssetsContent -v false")

        self.execute_mel_command('FBXExportBakeComplexAnimation -v false')

        self.execute_mel_command("FBXExportUseSceneName -v false")
        self.execute_mel_command("FBXExportQuaternion -v euler")
        self.execute_mel_command("FBXExportShapes -v true")
        self.execute_mel_command("FBXExportSkins -v true")

        # Constraints
        self.execute_mel_command("FBXExportConstraints -v false")
        # Cameras
        self.execute_mel_command("FBXExportCameras -v true")
        # Lights
        self.execute_mel_command("FBXExportLights -v true")
        # Embed Media
        self.execute_mel_command("FBXExportEmbeddedTextures -v false")
        # Connections
        self.execute_mel_command("FBXExportInputConnections -v true")
        # Axis Conversion
        self.execute_mel_command("FBXExportUpAxis y")
        # Version
        self.execute_mel_command('FBXExportFileVersion -v FBX201900')

        # Export!

        self.execute_mel_command('FBXExport -f "{0}" -s'.format(path))

    def show_file_select_dialog(self):
        self.file_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select directory')

        self.file_path_le.setText(self.file_path)

    def get_convert_file_path(self):
        """
        Converts the input file path to a normalized format and validates its existence.

        Returns:
            str: The converted file path with forward slashes if it exists.
            None: If the file path doesn't exist, displays an error and returns None.
        """
        # Get the raw file path from the input field
        raw_path = self.file_path_le.text().strip()

        if raw_path:
            # Normalize the file path (replace backslashes with forward slashes)
            normalized_path = raw_path.replace("\\", "/")

            # Check if the directory exists
            if os.path.isdir(normalized_path):
                logger.info(f"Valid file path: {normalized_path}")
                return normalized_path
            else:
                logger.error(f"File path does not exist: {normalized_path}")
                oMaya.MGlobal.displayError("File path doesn't exist. Please select a valid directory.")
                return None
        else:
            logger.warning("File path input is empty.")
            oMaya.MGlobal.displayError("File path cannot be empty.")
            return None

    def assign_mesh_button(self):
        """
        Assigns selected cameras from the Maya scene to the tool's camera name field.

        This function checks for selected objects in the Maya scene and filters out any non-camera objects.
        If no cameras are found or if nothing is selected, appropriate errors are logged and displayed.
        """
        try:
            # Get the currently selected objects in the Maya scene
            selected_objects = cm.ls(selection=True)
            if not selected_objects:
                oMaya.MGlobal.displayError("Please select at least one camera.")
                return

            # Filter out cameras from the selected objects
            selected_mesh = []
            for obj in selected_objects:
                # Check if the object or its children are cameras
                obj_children = cm.listRelatives(obj, children=True, fullPath=True) or []
                for child in obj_children or [obj]:
                    if cm.objectType(child) == 'mesh':
                        selected_mesh.append(obj)
                        break  # Only add the first valid camera per object

            if not selected_mesh:
                # Log and display an error if no cameras were found in the selection
                logger.warning("No mesh selected or found in the selected objects.")
                oMaya.MGlobal.displayError("No mesh detected in the selected objects.")
                return

            # Format the list of selected cameras as a comma-separated string
            formatted_mesh = ", ".join(selected_mesh)
            self.mesh_name_le.setText(formatted_mesh)

            # Log the successful assignment of cameras
            logger.info(f"Assigned mesh: {formatted_mesh}")

        except Exception as e:
            logger.error(f"Unexpected error in assign_mesh_button: {e}")
            oMaya.MGlobal.displayError(f"Error occurred while assigning mesh: {e}")

    def get_list_mesh_name(self):
        """
        Fetches and returns a cleaned list of mesh names from the input field.

        Returns:
            list: A list of mesh names if valid input exists.
                  An empty list if the input is empty or invalid.
        """
        # Get raw input from the mesh name field
        raw_input = self.mesh_name_le.text().strip()

        if raw_input:
            # Clean the input by removing unnecessary spaces and splitting by commas
            mesh_names = [name.strip() for name in raw_input.split(",") if name.strip()]

            # Log and return the cleaned list of mesh names
            if mesh_names:
                logger.info(f"mesh names extracted: {mesh_names}")
                return mesh_names
            else:
                logger.warning("Input contains only whitespace or invalid mesh names.")
                return []
        else:
            logger.warning("mesh name input is empty.")
            return []

    def generate_bs_by_time(self, mesh):
        """
        Generates a duplicate of a specified mesh for each frame of a predefined blendshape sequence.
        Each duplicate is named based on the corresponding blendshape name.

        Parameters:
        - mesh (str): The name of the mesh to duplicate.

        Preconditions:
        - A valid mesh name must be provided.
        - Time frames should correspond to blendshapes (sequentially named).

        Steps:
        1. Checks if the mesh exists.
        2. Creates a group for organizing all duplicates if it doesn't already exist.
        3. Iterates through blendshape names, setting time frames and creating duplicates for each.
        """

        # Predefined blendshape list
        blendshape_list = {
            i: name for i, name in enumerate([
                'eyeBlinkLeft', 'eyeLookDownLeft', 'eyeLookInLeft', 'eyeLookOutLeft', 'eyeLookUpLeft',
                'eyeSquintLeft', 'eyeWideLeft', 'eyeBlinkRight', 'eyeLookDownRight', 'eyeLookInRight',
                'eyeLookOutRight', 'eyeLookUpRight', 'eyeSquintRight', 'eyeWideRight', 'jawForward',
                'jawLeft', 'jawRight', 'jawOpen', 'mouthClose', 'mouthFunnel', 'mouthPucker', 'mouthLeft',
                'mouthRight', 'mouthSmileLeft', 'mouthSmileRight', 'mouthFrownLeft', 'mouthFrownRight',
                'mouthDimpleLeft', 'mouthDimpleRight', 'mouthStretchLeft', 'mouthStretchRight',
                'mouthRollLower', 'mouthRollUpper', 'mouthShrugLower', 'mouthShrugUpper', 'mouthPressLeft',
                'mouthPressRight', 'mouthLowerDownLeft', 'mouthLowerDownRight', 'mouthUpperUpLeft',
                'mouthUpperUpRight', 'browDownLeft', 'browDownRight', 'browInnerUp', 'browOuterUpLeft',
                'browOuterUpRight', 'cheekPuff', 'cheekSquintLeft', 'cheekSquintRight', 'noseSneerLeft',
                'noseSneerRight', 'tongueOut'
            ], start=1)
        }

        if not mesh:
            cm.warning("No mesh specified. Please provide a valid mesh name.")
            return

        try:
            # Check if the mesh exists
            if not cm.objExists(mesh):
                cm.warning(f"The specified mesh '{mesh}' does not exist.")
                return

            # Create a group to organize duplicates
            group_name = f"{mesh}_grp"
            if not cm.objExists(group_name):
                cm.group(empty=True, world=True, name=group_name)

            # Iterate through blendshape names and create duplicates
            for frame, blendshape_name in blendshape_list.items():
                # Set current time to the frame index
                cm.currentTime(frame)

                # Duplicate the mesh and rename it based on the blendshape name
                duplicate_name = f"{blendshape_name}"
                new_duplicate = cm.duplicate(mesh, name=duplicate_name, returnRootsOnly=False)

                # Parent the duplicate under the group
                cm.parent(new_duplicate, group_name)
                print(f"Created duplicate for {blendshape_name}: {duplicate_name}")

            print("Blendshape duplicates generated successfully.")

            filepath = self.get_convert_file_path()

            # Create the export directory
            export_dir = os.path.join(filepath).replace(os.sep, '/')
            export_dir = str(export_dir)
            if not os.path.isdir(export_dir):
                os.mkdir(export_dir)

            cm.select(group_name)
            self.export_mesh(group_name, export_dir)

            cm.delete(group_name)

        except Exception as e:
            cm.warning(f"Error in generate_bs_by_time: {e}")

    def export_mesh(self, group_name, export_dir):

        try:
            # Export FBX
            mesh_filename = f"{group_name}.fbx"
            mesh_output_path = os.path.join(export_dir, mesh_filename).replace(os.sep, '/')
            self.fbx_export_option(mesh_output_path)

            logger.info(f"Exported mesh {group_name} to {mesh_output_path}")

        except Exception as e:
            logger.error(f"Failed to export mesh '{group_name}': {e}")
            oMaya.MGlobal.displayError(f"Error exporting mesh '{group_name}': {e}")

    def execution_button(self):
        try:
            # Get configured paths, settings, and time ranges
            mesh = self.get_list_mesh_name()

            if mesh:
                for i in mesh:
                    self.generate_bs_by_time(i)

        except RuntimeError as e:
            logger.error(f"Runtime error encountered during FBX export: {e}")
            oMaya.MGlobal.displayError(f"FBX export failed: {e}")
        except Exception as e:
            logger.error(f"Unexpected error during FBX export: {e}")
            oMaya.MGlobal.displayError(f"Error: {e}")


# noinspection PyMethodMayBeStatic,PyAttributeOutsideInit,PyMethodOverriding
class MainWindow(QtWidgets.QDialog):
    WINDOW_TITLE = "Blend Shape By Time"

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
        main_window_ptr = oMayaUI.MQtUtil.mainWindow()
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
        self.content_layout.addWidget(BlendShapeByTime())

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

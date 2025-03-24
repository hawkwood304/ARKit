import maya.cmds as cm
import os


def bs52_connect():
    """
    Connect 52 blendshapes to a control rig using unit conversion nodes.
    """
    # Define blendshape names
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

    try:
        selected_mesh = cm.ls(selection=True)
        if not selected_mesh:
            raise RuntimeError("No mesh selected. Please select a mesh to connect blendshapes.")

        # Ensure the correct time unit
        cm.currentUnit(time="ntsc")

        # Load control rig if not already in the scene
        maya_script_folder = cm.internalVar(userScriptDir=True)
        rig_path = os.path.join(maya_script_folder, "ctrlARKitBS_M.ma").replace(os.sep, '/')
        if not cm.objExists("ctrlARKitBS_M"):
            cm.file(rig_path, i=True)

        # Identify the blendShape node for the selected mesh
        blendshape_node = cm.ls(cm.listHistory(selected_mesh), type='blendShape')[0]
        if not blendshape_node:
            raise RuntimeError("No blendshape node found for the selected mesh.")

        # Connect each blendshape
        for index, name_bs in blendshape_list.items():
            # Create and configure unit conversion nodes
            uc_node = cm.createNode("unitConversion", name=f"{name_bs}_UE_uC")
            cm.setAttr(f"{uc_node}.conversionFactor", 10)

            # Handle exceptions for specific blendshape names
            if name_bs in ["mouthFrownLeft", "mouthFrownRight", "cheekSquintLeft", "cheekSquintRight", "mouthClose"]:
                blendshape_attr = name_bs.replace('mouthFrown', 'mouthFrow').replace('cheekSquint', 'cheeSquint')
                if cm.objExists(f"{blendshape_node}.{blendshape_attr}"):
                    cm.connectAttr(f"{blendshape_node}.{blendshape_attr}", f"{uc_node}.input", force=True)
                    cm.connectAttr(f"{uc_node}.output", f"ctrlARKitBS_M.{name_bs}", force=True)
                else:
                    continue  # Skip if the specific attribute does not exist
            else:
                if cm.objExists(f"{blendshape_node}.{name_bs}"):
                    cm.connectAttr(f"{blendshape_node}.{name_bs}", f"{uc_node}.input", force=True)
                    cm.connectAttr(f"{uc_node}.output", f"ctrlARKitBS_M.{name_bs}", force=True)
                else:
                    continue

        # Adjust playback options based on blendshape animation time
        all_keys = sorted(cm.keyframe(f"{blendshape_node}.jawOpen", query=True))
        if all_keys:
            min_time, max_time = round(all_keys[0]), round(all_keys[-1])
            cm.playbackOptions(
                animationStartTime=min_time, animationEndTime=max_time,
                minTime=min_time, maxTime=max_time
            )
        else:
            min_time = cm.playbackOptions(q=True, min=True)
            max_time = cm.playbackOptions(q=True, max=True)

        # Bake results for control rig
        cm.select("ctrlARKitBS_M")
        cm.bakeResults(
            simulation=True, t=(min_time, max_time), sampleBy=1,
            oversamplingRate=1, disableImplicitControl=True, preserveOutsideKeys=True,
            sparseAnimCurveBake=False, removeBakedAttributeFromLayer=False,
            removeBakedAnimFromLayer=False, bakeOnOverrideLayer=False,
            minimizeRotation=True, controlPoints=False, shape=False
        )
        print("Blendshape connections completed successfully.")
    except Exception as e:
        cm.warning(f"Error in bs52_connect: {str(e)}")


def connect_bs():
    """
    Connect blendshape attributes for multiple body parts like head, eyes, and teeth.
    """
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

    maya_script_folder = cm.internalVar(userScriptDir=True)
    rig_path = os.path.join(maya_script_folder, "ctrlARKitBS_M.ma").replace(os.sep, '/')

    if not cm.objExists("ctrlARKitBS_M"):
        cm.file(rig_path, i=True)
        if cm.objExists("ctrlBox"):
            cm.parent("ctrlBoxARKitBS_M", "ctrlBox")

    for index, name_bs in blendshape_list.items():
        uc_node = cm.createNode("unitConversion", name=f"{name_bs}_uC")
        cm.setAttr(f"{uc_node}.conversionFactor", 0.1)
        cm.connectAttr(f"ctrlARKitBS_M.{name_bs}", f"{uc_node}.input", force=True)

        for body_part in (
                "headBS", "eyeLBS", "toungeBS", "eyeRBS", "eyeLashBS", "teethBS", "lipBS", "noseBS", "eyeBS",
                "eyebrowBS", "upperteethBS", "lowerteethBS", "mouthinsideBS", "mouthBS"):
            if cm.objExists(body_part):
                if cm.objExists(f"{body_part}.{name_bs}"):
                    cm.connectAttr(f"{uc_node}.output", f"{body_part}.{name_bs}", force=True)
                else:
                    continue


def connect_bs_custom(control, bs_node):
    """
    Connect blendshape attributes for multiple body parts like head, eyes, and teeth.
    """
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
            'noseSneerRight', 'tongueOut', 'good', 'angry', 'closedeyes', 'o', 'happy', 'l_eye_close', 'r_eye_close',
            'mischievous', 'AA', 'SS', 'OO', 'UU', 'mischiev_lipsync', 'happy_lypsync', 'mad', 'smile', 'O_cỉrcle',
            'very_angry', 'surprised', 'confident', 'determination'
        ], start=1)
    }

    for index, name_bs in blendshape_list.items():
        uc_node = cm.createNode("unitConversion", name=f"{name_bs}_uC")
        cm.setAttr(f"{uc_node}.conversionFactor", 0.1)
        if cm.objExists(f"{control}.{name_bs}"):
            cm.connectAttr(f"{control}.{name_bs}", f"{uc_node}.input", force=True)

            if cm.objExists(bs_node):
                if cm.objExists(f"{bs_node}.{name_bs}"):
                    cm.connectAttr(f"{uc_node}.output", f"{bs_node}.{name_bs}", force=True)
                else:
                    continue


def connect_bs_arkit():
    """
    Connect ARKit blendshape attributes from a LiveLink control rig to a Maya control rig
    using unit conversion nodes for proper scaling.
    """
    # ARKit / Maya blendshape mapping
    csv_blendshape_list = {
        i: name for i, name in enumerate([
            'EyeBlinkLeft', 'EyeLookDownLeft', 'EyeLookInLeft', 'EyeLookOutLeft', 'EyeLookUpLeft',
            'EyeSquintLeft', 'EyeWideLeft', 'EyeBlinkRight', 'EyeLookDownRight', 'EyeLookInRight',
            'EyeLookOutRight', 'EyeLookUpRight', 'EyeSquintRight', 'EyeWideRight', 'JawForward',
            'JawLeft', 'JawRight', 'JawOpen', 'MouthClose', 'MouthFunnel', 'MouthPucker', 'MouthLeft',
            'MouthRight', 'MouthSmileLeft', 'MouthSmileRight', 'MouthFrownLeft', 'MouthFrownRight',
            'MouthDimpleLeft', 'MouthDimpleRight', 'MouthStretchLeft', 'MouthStretchRight',
            'MouthRollLower', 'MouthRollUpper', 'MouthShrugLower', 'MouthShrugUpper', 'MouthPressLeft',
            'MouthPressRight', 'MouthLowerDownLeft', 'MouthLowerDownRight', 'MouthUpperUpLeft',
            'MouthUpperUpRight', 'BrowDownLeft', 'BrowDownRight', 'BrowInnerUp', 'BrowOuterUpLeft',
            'BrowOuterUpRight', 'CheekPuff', 'CheekSquintLeft', 'CheekSquintRight', 'NoseSneerLeft',
            'NoseSneerRight', 'TongueOut'
        ], start=1)
    }

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

    try:
        # Load the Maya control rig if it is not already loaded
        maya_script_folder = cm.internalVar(userScriptDir=True)
        rig_path = os.path.join(maya_script_folder, "ctrlARKitBS_M.ma").replace(os.sep, '/')
        if not cm.objExists("ctrlARKitBS_M"):
            cm.file(rig_path, i=True)

        # Connect ARKit blendshapes to Maya rig using unitConversion nodes
        for i in range(1, 53):
            # Retrieve blendshape names
            name_bs = blendshape_list.get(i)
            csv_bs = csv_blendshape_list.get(i)

            if not name_bs or not csv_bs:
                print(f"Skipping blendshape index {i}: Name not found.")
                continue

            # Create a unitConversion node
            uc_node = cm.createNode("unitConversion", name=f"{csv_bs}_csv_uC")
            cm.setAttr(f"{uc_node}.conversionFactor", 10)

            # Ensure required attributes and connections exist
            if not cm.objExists(f"T1_LiveLink.{csv_bs}"):
                cm.warning(f"LiveLink attribute for {csv_bs} does not exist. Skipping connection.")
                continue

            # Connect ARKit to the Maya control rig
            try:
                cm.connectAttr(
                    f"T1_LiveLink.{csv_bs}", f"{uc_node}.input", force=True
                )
                cm.connectAttr(
                    f"{uc_node}.output", f"ctrlARKitBS_M.{name_bs}", force=True
                )
                print(f"Connected {csv_bs} (ARKit) to {name_bs} (Maya).")
            except RuntimeError as e:
                cm.warning(f"Failed to connect {csv_bs} to {name_bs}: {e}")

        print("All ARKit blendshape connections completed.")
    except Exception as e:
        cm.warning(f"Error in connect_bs_arkit: {e}")


def bs_wrap(bs_node_name, mesh_dup):
    """
    Generates blendshape duplicates for every blendshape weight in the specified blendshape node.

    Steps:
    1. Iterates through all blendshape weights of a blendshape node.
    2. Activates each weight one at a time.
    3. Creates a mesh duplicate corresponding to each activated blendshape.
    4. Names the duplicate meshes after the respective blendshape weights.

    Requirements:
    - A blendshape node (e.g., "headBS") must exist in the scene.
    - A target mesh (e.g., "head_lod2_mesh_AS_new") must also exist.
    """

    try:
        # Create a group to store blendshape mesh in after generate
        if not cm.objExists(f"{bs_node_name}_BS_grp"):
            root_grp = cm.group(name=f"{bs_node_name}_BS_grp", world=True, relative=True, empty=True)
        else:
            root_grp = cm.group(name=f"{bs_node_name}_BS_grp", world=True, relative=True, empty=True)

        # Validate that the blendshape node exists
        if not cm.objExists(bs_node_name):
            cm.warning(f"Blendshape node '{bs_node_name}' does not exist in the scene.")
            return

        # Validate that the target mesh exists
        if not cm.objExists(mesh_dup):
            cm.warning(f"Target mesh '{mesh_dup}' does not exist in the scene.")
            return

        # Retrieve the list of blendshape attributes
        list_blendshapes = cm.listAttr(f"{bs_node_name}.w", multi=True)
        if not list_blendshapes:
            cm.warning(f"No blendshape weights found in the node '{bs_node_name}'.")
            return

        # Generate duplicates for each blendshape
        for bs_name in list_blendshapes:
            # Set the blendshape weight to 1
            cm.setAttr(f"{bs_node_name}.{bs_name}", 1)

            # Duplicate the target mesh and rename it with the blendshape name
            duplicate_name = f"{bs_name}_mesh"
            new_duplicate = cm.duplicate(mesh_dup, name=duplicate_name, rr=True)
            cm.parent(new_duplicate, root_grp)

            # Reset the blendshape weight to 0 after duplication
            cm.setAttr(f"{bs_node_name}.{bs_name}", 0)

            # Feedback
            print(f"Created duplicate for blendshape '{bs_name}': {new_duplicate[0]}")

        print("Blendshape wrapping completed successfully.")

    except Exception as e:
        cm.warning(f"Error in bs_wrap: {e}")


def generate_bs_by_time(mesh):
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

    except Exception as e:
        cm.warning(f"Error in generate_bs_by_time: {e}")


def connect_bs_to_cube(bs_node, cube):
    """
    Connects blendshape attributes from an existing blendshape node (e.g., "headBS")
    to a "cube" (or a control object) using unit conversion nodes. This allows scaling
    or modifying the output of the blendshape weights before passing them to the cube.

    The cube acts as a visual controller for blendshape weights.

    Requirements:
    - A valid blendshape node and a cube object must exist in the Maya scene.
    - The blendshape node attributes must be connected to manipulable cube attributes.
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

    # Inputs
    blendshape_node = bs_node  # The blendshape node
    cube = cube  # The cube object to connect to

    try:
        # Validate that the blendshape node exists
        if not cm.objExists(blendshape_node):
            cm.warning(f"Blendshape node '{blendshape_node}' does not exist in the scene.")
            return

        # Validate that the cube exists
        if not cm.objExists(cube):
            cm.warning(f"Specified cube '{cube}' does not exist in the scene.")
            return

        # Connect each blendshape attribute to the cube
        for index, blendshape_name in blendshape_list.items():
            # Check if the blendshape attribute exists in the blendshape node
            if not cm.objExists(f"{blendshape_node}.{blendshape_name}"):
                cm.warning(
                    f"Blendshape attribute '{blendshape_name}' does not exist on '{blendshape_node}'. Skipping...")
                continue

            # Check if the corresponding attribute exists on the cube
            if not cm.objExists(f"{cube}.{blendshape_name}"):
                # Add the attribute if it doesn't exist
                cm.addAttr(cube, longName=blendshape_name, attributeType="float", defaultValue=0.0, minValue=0.0,
                           maxValue=1.0, keyable=True)
                print(f"Added attribute '{blendshape_name}' to '{cube}'.")

            # Create a unit conversion node for scaling (if needed)
            uc_node = cm.createNode("unitConversion", name=f"{blendshape_name}_uC")
            cm.setAttr(f"{uc_node}.conversionFactor", 10.0)

            # Connect the blendshape to the unit conversion
            cm.connectAttr(f"{blendshape_node}.{blendshape_name}", f"{uc_node}.input", force=True)

            # Connect the output of the unit conversion to the cube
            cm.connectAttr(f"{uc_node}.output", f"{cube}.{blendshape_name}", force=True)
            print(f"Connected '{blendshape_name}' from '{blendshape_node}' to '{cube}' via '{uc_node}'.")

        print("All blendshape attributes successfully connected to the cube.")

    except Exception as e:
        cm.warning(f"Error in connect_bs_to_cube: {e}")


def select_control_m2(name_space=""):
    """
    Selects specific controllers in Maya based on predefined naming conventions
    or selection rules.

    Steps:
    1. Validates the existence of the target controller group.
    2. Clears the current selection.
    3. Selects the predefined controls if they exist in the scene.

    Requirements:
    - The specified controls must exist in the Maya scene.
    - Maya's selection and object existence methods are used.

    """

    # List of predefined control names to be selected
    controls_to_select = [
        'head_ctrl',
        'neck_ctrl',
        'spine_ctrl',
        'root_ctrl',
        'arm_ctrl_L',
        'arm_ctrl_R',
        'leg_ctrl_L',
        'leg_ctrl_R'
    ]

    try:
        # Clears the current Maya selection
        cm.select(clear=True)

        # Iterate through the controls to select each one (if it exists)
        for control in controls_to_select:
            control = f"{name_space}:{control}"
            if cm.objExists(control):
                cm.select(control, add=True)
                print(f"Selected: {control}")
            else:
                print(f"Control '{control}' does not exist. Skipping...")

        # Provide feedback if the selection is empty after iteration
        current_selection = cm.ls(selection=True)
        if not current_selection:
            cm.warning("No controls were selected. Ensure that the controls exist in the scene.")
        else:
            print(f"Controls selected: {current_selection}")

    except Exception as e:
        cm.warning(f"An error occurred in select_control_m2: {e}")


def generate_bs_by_attr(mesh, bs_node):
    """
    Generates a duplicate of the specified mesh for each weight (target) in a blendshape node.
    Each duplicate is named after the corresponding blendshape weight.

    Parameters:
    - mesh (str): The name of the mesh to duplicate.
    - bs_node (str): The name of the blendshape node.

    Preconditions:
    - The mesh must exist in the Maya scene.
    - The blendshape node must be valid and have defined weights.

    Workflow:
    1. Validates the mesh and blendshape node existence.
    2. Retrieves all blendshape weight names from the blendshape node.
    3. Creates a group to organize the generated duplicates.
    4. Iterates through blendshape weights and:
        a. Activates each weight one at a time.
        b. Duplicates the mesh with the activated blendshape weight.
        c. Resets the blendshape weight to zero.
    """

    try:
        # Validate that the blendshape node exists
        if not cm.objExists(bs_node):
            cm.warning(f"Blendshape node '{bs_node}' not found.")
            return

        # Validate that the mesh exists
        if not cm.objExists(mesh):
            cm.warning(f"Mesh '{mesh}' not found in the scene.")
            return

        # Retrieve the weight names of the blendshape node
        weight_names = []
        alias_list = cm.aliasAttr(bs_node, query=True) or []
        for i in range(0, len(alias_list), 2):
            if alias_list[i + 1].startswith('weight['):
                weight_names.append(alias_list[i])

        if not weight_names:
            cm.warning(f"No weights found in blendshape node '{bs_node}'.")
            return

        # Create a group to organize duplicates
        group_name = f"{bs_node}_grp"
        if not cm.objExists(group_name):
            group_name = cm.group(name=group_name, empty=True, world=True)
        else:
            print(f"Group '{group_name}' already exists. Using existing group.")

        # Generate duplicates for each blendshape weight
        for weight in weight_names:
            if not cm.getAttr(f"{bs_node}.{weight}", lock=True):
                # Activate the blendshape weight

                cm.setAttr(f"{bs_node}.{weight}", 2)
            else:
                continue

            # Duplicate the mesh with the activated blendshape
            duplicate_name = f"{weight}"
            duplicate = cm.duplicate(mesh, name=duplicate_name, returnRootsOnly=True)[0]

            # Parent the duplicate to the group
            cm.parent(duplicate, group_name)

            # Reset the blendshape weight to zero
            cm.setAttr(f"{bs_node}.{weight}", 0)

            # Provide feedback
            print(f"Created duplicate for blendshape '{weight}': {duplicate}")

        print(f"All duplicates created successfully and stored under '{group_name}'.")

    except Exception as e:
        cm.warning(f"Error in generate_bs_by_attr: {e}")

def generate_bs_by_attr_from_control(mesh, control_name):
    try:
        # Validate that the blendshape node exists
        if not cm.objExists(control_name):
            cm.warning(f"Blendshape node '{control_name}' not found.")
            return

        # Validate that the mesh exists
        if not cm.objExists(mesh):
            cm.warning(f"Mesh '{mesh}' not found in the scene.")
            return

        # Retrieve the weight names of the blendshape node
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

        # Create a group to organize duplicates
        group_name = f"{control_name}_grp"
        if not cm.objExists(group_name):
            group_name = cm.group(name=group_name, empty=True, world=True)
        else:
            print(f"Group '{group_name}' already exists. Using existing group.")

        # Generate duplicates for each blendshape weight
        for index, name_bs in blendshape_list.items():
            # Create and configure unit conversion nodes
            cm.setAttr(f"{control_name}.{name_bs}", 10)

            # Duplicate the mesh with the activated blendshape
            duplicate_name = f"{name_bs}"
            duplicate = cm.duplicate(mesh, name=duplicate_name, returnRootsOnly=True)[0]

            # Parent the duplicate to the group
            cm.parent(duplicate, group_name)

            # Reset the blendshape weight to zero
            cm.setAttr(f"{control_name}.{name_bs}", 0)

            # Provide feedback
            print(f"Created duplicate for blendshape '{name_bs}': {duplicate}")

        print(f"All duplicates created successfully and stored under '{group_name}'.")

    except Exception as e:
        cm.warning(f"Error in generate_bs_by_attr: {e}")
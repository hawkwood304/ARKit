//Maya ASCII 2022 scene
//Name: ctrlARKitBS_M.ma
//Last modified: Mon, Jun 03, 2024 01:31:17 PM
//Codeset: 1252
requires maya "2022";
requires "stereoCamera" "10.0";
requires "mtoa" "5.0.0.4";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2022";
fileInfo "version" "2022";
fileInfo "cutIdentifier" "202303271415-baa69b5798";
fileInfo "osv" "Windows 10 Pro v2009 (Build: 19045)";
fileInfo "UUID" "EDB67ABB-4AA6-A56D-DE5A-F99D41B473CB";
createNode transform -n "ctrlBoxARKitBS_M";
	rename -uid "1028E17D-48B9-EE83-28E7-F08FED8E78B0";
	setAttr ".t" -type "double3" 21.043696238840798 146.34407755888796 6.2164864540100027 ;
	setAttr ".s" -type "double3" 1.9078304640677017 1.9078304640677017 1.9078304640677017 ;
createNode nurbsCurve -n "ctrlBoxARKitBS_MShape" -p "|ctrlBoxARKitBS_M";
	rename -uid "AECA2E64-4951-B948-8D1C-19BAF7088D66";
	setAttr -k off ".v";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		-1 1 0
		1 1 0
		1 -1 0
		-1 -1 0
		-1 1 0
		;
createNode transform -n "ctrlARKitBS_M" -p "|ctrlBoxARKitBS_M";
	rename -uid "A914E010-4C7B-72E2-9E92-E8954D879A14";
	addAttr -ci true -sn "createCtrlMode" -ln "createCtrlMode" -min 0 -max 1 -at "bool";
	addAttr -ci true -k true -sn "eyeBlinkLeft" -ln "eyeBlinkLeft" -smn 0 -smx 10 -at "double";
	addAttr -ci true -k true -sn "eyeLookDownLeft" -ln "eyeLookDownLeft" -smn 0 -smx 
		10 -at "double";
	addAttr -ci true -k true -sn "eyeLookInLeft" -ln "eyeLookInLeft" -smn 0 -smx 10 
		-at "double";
	addAttr -ci true -k true -sn "eyeLookOutLeft" -ln "eyeLookOutLeft" -smn 0 -smx 10 
		-at "double";
	addAttr -ci true -k true -sn "eyeLookUpLeft" -ln "eyeLookUpLeft" -smn 0 -smx 10 
		-at "double";
	addAttr -ci true -k true -sn "eyeSquintLeft" -ln "eyeSquintLeft" -smn 0 -smx 10 
		-at "double";
	addAttr -ci true -k true -sn "eyeWideLeft" -ln "eyeWideLeft" -smn 0 -smx 10 -at "double";
	addAttr -ci true -k true -sn "eyeBlinkRight" -ln "eyeBlinkRight" -smn 0 -smx 10 
		-at "double";
	addAttr -ci true -k true -sn "eyeLookDownRight" -ln "eyeLookDownRight" -smn 0 -smx 
		10 -at "double";
	addAttr -ci true -k true -sn "eyeLookInRight" -ln "eyeLookInRight" -smn 0 -smx 10 
		-at "double";
	addAttr -ci true -k true -sn "eyeLookOutRight" -ln "eyeLookOutRight" -smn 0 -smx 
		10 -at "double";
	addAttr -ci true -k true -sn "eyeLookUpRight" -ln "eyeLookUpRight" -smn 0 -smx 10 
		-at "double";
	addAttr -ci true -k true -sn "eyeSquintRight" -ln "eyeSquintRight" -smn 0 -smx 10 
		-at "double";
	addAttr -ci true -k true -sn "eyeWideRight" -ln "eyeWideRight" -smn 0 -smx 10 -at "double";
	addAttr -ci true -k true -sn "jawForward" -ln "jawForward" -smn 0 -smx 10 -at "double";
	addAttr -ci true -k true -sn "jawLeft" -ln "jawLeft" -smn 0 -smx 10 -at "double";
	addAttr -ci true -k true -sn "jawRight" -ln "jawRight" -smn 0 -smx 10 -at "double";
	addAttr -ci true -k true -sn "jawOpen" -ln "jawOpen" -smn 0 -smx 10 -at "double";
	addAttr -ci true -k true -sn "mouthClose" -ln "mouthClose" -smn 0 -smx 10 -at "double";
	addAttr -ci true -k true -sn "mouthFunnel" -ln "mouthFunnel" -smn 0 -smx 10 -at "double";
	addAttr -ci true -k true -sn "mouthPucker" -ln "mouthPucker" -smn 0 -smx 10 -at "double";
	addAttr -ci true -k true -sn "mouthLeft" -ln "mouthLeft" -smn 0 -smx 10 -at "double";
	addAttr -ci true -k true -sn "mouthRight" -ln "mouthRight" -smn 0 -smx 10 -at "double";
	addAttr -ci true -k true -sn "mouthSmileLeft" -ln "mouthSmileLeft" -smn 0 -smx 10 
		-at "double";
	addAttr -ci true -k true -sn "mouthSmileRight" -ln "mouthSmileRight" -smn 0 -smx 
		10 -at "double";
	addAttr -ci true -k true -sn "mouthFrownLeft" -ln "mouthFrownLeft" -smn 0 -smx 10 
		-at "double";
	addAttr -ci true -k true -sn "mouthFrownRight" -ln "mouthFrownRight" -smn 0 -smx 
		10 -at "double";
	addAttr -ci true -k true -sn "mouthDimpleLeft" -ln "mouthDimpleLeft" -smn 0 -smx 
		10 -at "double";
	addAttr -ci true -k true -sn "mouthDimpleRight" -ln "mouthDimpleRight" -smn 0 -smx 
		10 -at "double";
	addAttr -ci true -k true -sn "mouthStretchLeft" -ln "mouthStretchLeft" -smn 0 -smx 
		10 -at "double";
	addAttr -ci true -k true -sn "mouthStretchRight" -ln "mouthStretchRight" -smn 0 
		-smx 10 -at "double";
	addAttr -ci true -k true -sn "mouthRollLower" -ln "mouthRollLower" -smn 0 -smx 10 
		-at "double";
	addAttr -ci true -k true -sn "mouthRollUpper" -ln "mouthRollUpper" -smn 0 -smx 10 
		-at "double";
	addAttr -ci true -k true -sn "mouthShrugLower" -ln "mouthShrugLower" -smn 0 -smx 
		10 -at "double";
	addAttr -ci true -k true -sn "mouthShrugUpper" -ln "mouthShrugUpper" -smn 0 -smx 
		10 -at "double";
	addAttr -ci true -k true -sn "mouthPressLeft" -ln "mouthPressLeft" -smn 0 -smx 10 
		-at "double";
	addAttr -ci true -k true -sn "mouthPressRight" -ln "mouthPressRight" -smn 0 -smx 
		10 -at "double";
	addAttr -ci true -k true -sn "mouthLowerDownLeft" -ln "mouthLowerDownLeft" -smn 
		0 -smx 10 -at "double";
	addAttr -ci true -k true -sn "mouthLowerDownRight" -ln "mouthLowerDownRight" -smn 
		0 -smx 10 -at "double";
	addAttr -ci true -k true -sn "mouthUpperUpLeft" -ln "mouthUpperUpLeft" -smn 0 -smx 
		10 -at "double";
	addAttr -ci true -k true -sn "mouthUpperUpRight" -ln "mouthUpperUpRight" -smn 0 
		-smx 10 -at "double";
	addAttr -ci true -k true -sn "browDownLeft" -ln "browDownLeft" -smn 0 -smx 10 -at "double";
	addAttr -ci true -k true -sn "browDownRight" -ln "browDownRight" -smn 0 -smx 10 
		-at "double";
	addAttr -ci true -k true -sn "browInnerUp" -ln "browInnerUp" -smn 0 -smx 10 -at "double";
	addAttr -ci true -k true -sn "browOuterUpLeft" -ln "browOuterUpLeft" -smn 0 -smx 
		10 -at "double";
	addAttr -ci true -k true -sn "browOuterUpRight" -ln "browOuterUpRight" -smn 0 -smx 
		10 -at "double";
	addAttr -ci true -k true -sn "cheekPuff" -ln "cheekPuff" -smn 0 -smx 10 -at "double";
	addAttr -ci true -k true -sn "cheekSquintLeft" -ln "cheekSquintLeft" -smn 0 -smx 
		10 -at "double";
	addAttr -ci true -k true -sn "cheekSquintRight" -ln "cheekSquintRight" -smn 0 -smx 
		10 -at "double";
	addAttr -ci true -k true -sn "noseSneerLeft" -ln "noseSneerLeft" -smn 0 -smx 10 
		-at "double";
	addAttr -ci true -k true -sn "noseSneerRight" -ln "noseSneerRight" -smn 0 -smx 10 
		-at "double";
	addAttr -ci true -k true -sn "tongueOut" -ln "tongueOut" -smn 0 -smx 10 -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -k on ".eyeBlinkLeft";
	setAttr -k on ".eyeLookDownLeft";
	setAttr -k on ".eyeLookInLeft";
	setAttr -k on ".eyeLookOutLeft";
	setAttr -k on ".eyeLookUpLeft";
	setAttr -k on ".eyeSquintLeft";
	setAttr -k on ".eyeWideLeft";
	setAttr -k on ".eyeBlinkRight";
	setAttr -k on ".eyeLookDownRight";
	setAttr -k on ".eyeLookInRight";
	setAttr -k on ".eyeLookOutRight";
	setAttr -k on ".eyeLookUpRight";
	setAttr -k on ".eyeSquintRight";
	setAttr -k on ".eyeWideRight";
	setAttr -k on ".jawForward";
	setAttr -k on ".jawLeft";
	setAttr -k on ".jawRight";
	setAttr -k on ".jawOpen";
	setAttr -k on ".mouthClose";
	setAttr -k on ".mouthFunnel";
	setAttr -k on ".mouthPucker";
	setAttr -k on ".mouthLeft";
	setAttr -k on ".mouthRight";
	setAttr -k on ".mouthSmileLeft";
	setAttr -k on ".mouthSmileRight";
	setAttr -k on ".mouthFrownLeft";
	setAttr -k on ".mouthFrownRight";
	setAttr -k on ".mouthDimpleLeft";
	setAttr -k on ".mouthDimpleRight";
	setAttr -k on ".mouthStretchLeft";
	setAttr -k on ".mouthStretchRight";
	setAttr -k on ".mouthRollLower";
	setAttr -k on ".mouthRollUpper";
	setAttr -k on ".mouthShrugLower";
	setAttr -k on ".mouthShrugUpper";
	setAttr -k on ".mouthPressLeft";
	setAttr -k on ".mouthPressRight";
	setAttr -k on ".mouthLowerDownLeft";
	setAttr -k on ".mouthLowerDownRight";
	setAttr -k on ".mouthUpperUpLeft";
	setAttr -k on ".mouthUpperUpRight";
	setAttr -k on ".browDownLeft";
	setAttr -k on ".browDownRight";
	setAttr -k on ".browInnerUp";
	setAttr -k on ".browOuterUpLeft";
	setAttr -k on ".browOuterUpRight";
	setAttr -k on ".cheekPuff";
	setAttr -k on ".cheekSquintLeft";
	setAttr -k on ".cheekSquintRight";
	setAttr -k on ".noseSneerLeft";
	setAttr -k on ".noseSneerRight";
	setAttr -k on ".tongueOut";
createNode nurbsCurve -n "ctrlARKitBS_MShape" -p "|ctrlBoxARKitBS_M|ctrlARKitBS_M";
	rename -uid "138D95DC-43BA-25C9-4DA3-B2830F7BE7E7";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 16 0 no 3
		21 0 0 0 0.20948400980000001 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 15 15
		19
		0.63846096129999996 0.32252763420000002 0
		0.59087384300000001 0.3884819491 0
		0.30837388100000002 0.57310297310000002 0
		-0.001582089678 0.31814299950000002 0
		-0.24170475850000001 0.58581709920000002 0
		-0.73451460069999996 0.30795786939999997 0
		-0.70856300900000002 -0.31016186060000001 0
		-0.47735791910000003 -0.6994357363 0
		-0.26980622770000001 -0.8657313257 0
		0.018081559090000001 -0.67584338020000001 0
		0.29429525229999998 -0.86144015039999999 0
		0.48890166909999999 -0.71951976009999996 0
		0.62095782099999997 -0.51069688749999997 0
		0.68102676569999998 -0.35164017669999997 0
		0.68102673790000001 -0.35164018520000001 0
		0.53121265409999996 -0.2608227488 0
		0.4075067953 -0.02349589283 0
		0.51116180170000003 0.2631323928 0
		0.63966206999999997 0.32252762540000002 0
		;
createNode nurbsCurve -n "ctrlARKitBS_MShape2" -p "|ctrlBoxARKitBS_M|ctrlARKitBS_M";
	rename -uid "72746D44-4821-1396-2153-E9AC588E59D8";
	setAttr ".ihi" 0;
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 0 no 3
		13 0 0 0 1 2 3 4 5 6 7 8 8 8
		11
		0.32320616940000002 0.90970256540000005 0
		0.33632375209999998 0.79643922190000005 0
		0.2438975552 0.61384955190000001 0
		0.096720387960000001 0.52143484979999999 0
		-0.013701450780000001 0.51344955869999997 0
		-0.013701450509999999 0.51344956239999995 0
		-0.013701450509999999 0.51344956239999995 0
		-0.016698808629999999 0.61187047130000005 0
		0.039354082110000001 0.76744943629999995 0
		0.20185915560000001 0.9000563211 0
		0.32320615689999999 0.90970254809999995 0
		;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -k on ".fzn";
	setAttr -av -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 0;
	setAttr -av -k on ".unw";
	setAttr -av -k on ".etw";
	setAttr -av -k on ".tps";
	setAttr -av -k on ".tms";
select -ne :hardwareRenderingGlobals;
	setAttr -av -k on ".cch";
	setAttr -k on ".fzn";
	setAttr -av -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".rm";
	setAttr -k on ".lm";
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr -k on ".hom";
	setAttr -k on ".hodm";
	setAttr -k on ".xry";
	setAttr -k on ".jxr";
	setAttr -k on ".sslt";
	setAttr -k on ".cbr";
	setAttr -k on ".bbr";
	setAttr -av -k on ".mhl";
	setAttr -k on ".cons";
	setAttr -k on ".vac";
	setAttr -av -k on ".hwi";
	setAttr -k on ".csvd";
	setAttr -av -k on ".ta";
	setAttr -av -k on ".tq";
	setAttr -k on ".ts";
	setAttr -av -k on ".etmr";
	setAttr -av -k on ".tmr";
	setAttr -av -k on ".aoon" yes;
	setAttr -av -k on ".aoam";
	setAttr -av -k on ".aora";
	setAttr -av -k on ".aofr";
	setAttr -av -k on ".aosm";
	setAttr -av -k on ".hff";
	setAttr -av -k on ".hfd";
	setAttr -av -k on ".hfs";
	setAttr -av -k on ".hfe";
	setAttr -av ".hfc";
	setAttr -av -k on ".hfcr";
	setAttr -av -k on ".hfcg";
	setAttr -av -k on ".hfcb";
	setAttr -av -k on ".hfa";
	setAttr -av -k on ".mbe";
	setAttr -k on ".mbt";
	setAttr -av -k on ".mbsof";
	setAttr -k on ".mbsc";
	setAttr -k on ".mbc";
	setAttr -k on ".mbfa";
	setAttr -k on ".mbftb";
	setAttr -k on ".mbftg";
	setAttr -k on ".mbftr";
	setAttr -k on ".mbfta";
	setAttr -k on ".mbfe";
	setAttr -k on ".mbme";
	setAttr -k on ".mbcsx";
	setAttr -k on ".mbcsy";
	setAttr -k on ".mbasx";
	setAttr -k on ".mbasy";
	setAttr -av -k on ".blen";
	setAttr -k on ".blth";
	setAttr -k on ".blfr";
	setAttr -k on ".blfa";
	setAttr -av -k on ".blat";
	setAttr -av -k on ".msaa" yes;
	setAttr -av -k on ".aasc";
	setAttr -k on ".aasq";
	setAttr -k on ".laa";
	setAttr -k on ".fprt" yes;
	setAttr -k on ".rtfm";
select -ne :renderPartition;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 19 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 22 ".s";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 500 ".u";
select -ne :defaultRenderingList1;
	setAttr -av -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 38 ".r";
select -ne :defaultTextureList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 11 ".tx";
select -ne :lambert1;
select -ne :standardSurface1;
	setAttr ".b" 0.80000001192092896;
	setAttr ".bc" -type "float3" 1 1 1 ;
	setAttr ".s" 0.20000000298023224;
select -ne :initialShadingGroup;
	setAttr -av -k on ".cch";
	setAttr -k on ".fzn";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".bbx";
	setAttr -k on ".vwm";
	setAttr -k on ".tpv";
	setAttr -k on ".uit";
	setAttr -s 5 ".dsm";
	setAttr -k on ".mwc";
	setAttr -av -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
	setAttr -s 2 ".gn";
	setAttr -cb on ".ai_override";
	setAttr -k on ".ai_surface_shader";
	setAttr -cb on ".ai_surface_shaderr";
	setAttr -cb on ".ai_surface_shaderg";
	setAttr -cb on ".ai_surface_shaderb";
	setAttr -k on ".ai_volume_shader";
	setAttr -cb on ".ai_volume_shaderr";
	setAttr -cb on ".ai_volume_shaderg";
	setAttr -cb on ".ai_volume_shaderb";
select -ne :initialParticleSE;
	setAttr -av -k on ".cch";
	setAttr -k on ".fzn";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".bbx";
	setAttr -k on ".vwm";
	setAttr -k on ".tpv";
	setAttr -k on ".uit";
	setAttr -k on ".mwc";
	setAttr -av -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
	setAttr -cb on ".ai_override";
	setAttr -k on ".ai_surface_shader";
	setAttr -cb on ".ai_surface_shaderr";
	setAttr -cb on ".ai_surface_shaderg";
	setAttr -cb on ".ai_surface_shaderb";
	setAttr -k on ".ai_volume_shader";
	setAttr -cb on ".ai_volume_shaderr";
	setAttr -cb on ".ai_volume_shaderg";
	setAttr -cb on ".ai_volume_shaderb";
select -ne :initialMaterialInfo;
select -ne :defaultRenderGlobals;
	addAttr -ci true -h true -sn "dss" -ln "defaultSurfaceShader" -dt "string";
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -av -k on ".macc";
	setAttr -av -k on ".macd";
	setAttr -av -k on ".macq";
	setAttr -av -k on ".mcfr";
	setAttr -cb on ".ifg";
	setAttr -av -k on ".clip";
	setAttr -av -k on ".edm";
	setAttr -av -k on ".edl";
	setAttr -av -cb on ".ren" -type "string" "arnold";
	setAttr -av -k on ".esr";
	setAttr -av -k on ".ors";
	setAttr -cb on ".sdf";
	setAttr -av -k on ".outf" 51;
	setAttr -av -cb on ".imfkey" -type "string" "exr";
	setAttr -av -k on ".gama";
	setAttr -av -k on ".exrc";
	setAttr -av -k on ".expt";
	setAttr -av -k on ".an";
	setAttr -cb on ".ar";
	setAttr -av -k on ".fs";
	setAttr -av -k on ".ef";
	setAttr -av -k on ".bfs";
	setAttr -av -cb on ".me";
	setAttr -cb on ".se";
	setAttr -av -k on ".be";
	setAttr -av -cb on ".ep";
	setAttr -av -k on ".fec";
	setAttr -av -k on ".ofc";
	setAttr -cb on ".ofe";
	setAttr -cb on ".efe";
	setAttr -cb on ".oft";
	setAttr -cb on ".umfn";
	setAttr -cb on ".ufe";
	setAttr -av -k on ".pff";
	setAttr -av -cb on ".peie";
	setAttr -av -cb on ".ifp";
	setAttr -k on ".rv";
	setAttr -av -k on ".comp";
	setAttr -av -k on ".cth";
	setAttr -av -k on ".soll";
	setAttr -av -cb on ".sosl";
	setAttr -av -k on ".rd";
	setAttr -av -k on ".lp";
	setAttr -av -k on ".sp";
	setAttr -av -k on ".shs";
	setAttr -av -k on ".lpr";
	setAttr -cb on ".gv";
	setAttr -cb on ".sv";
	setAttr -av -k on ".mm";
	setAttr -av -k on ".npu";
	setAttr -av -k on ".itf";
	setAttr -av -k on ".shp";
	setAttr -cb on ".isp";
	setAttr -av -k on ".uf";
	setAttr -av -k on ".oi";
	setAttr -av -k on ".rut";
	setAttr -av -k on ".mot";
	setAttr -av -k on ".mb";
	setAttr -av -k on ".mbf";
	setAttr -av -k on ".mbso";
	setAttr -av -k on ".mbsc";
	setAttr -av -k on ".afp";
	setAttr -av -k on ".pfb";
	setAttr -av -k on ".pram";
	setAttr -av -k on ".poam";
	setAttr -av -k on ".prlm";
	setAttr -av -k on ".polm";
	setAttr -av -cb on ".prm";
	setAttr -av -cb on ".pom";
	setAttr -cb on ".pfrm";
	setAttr -cb on ".pfom";
	setAttr -av -k on ".bll";
	setAttr -av -k on ".bls";
	setAttr -av -k on ".smv";
	setAttr -av -k on ".ubc";
	setAttr -av -k on ".mbc";
	setAttr -cb on ".mbt";
	setAttr -av -k on ".udbx";
	setAttr -av -k on ".smc";
	setAttr -av -k on ".kmv";
	setAttr -cb on ".isl";
	setAttr -cb on ".ism";
	setAttr -cb on ".imb";
	setAttr -av -k on ".rlen";
	setAttr -av -k on ".frts";
	setAttr -av -k on ".tlwd";
	setAttr -av -k on ".tlht";
	setAttr -av -k on ".jfc";
	setAttr -cb on ".rsb";
	setAttr -av -k on ".ope";
	setAttr -av -k on ".oppf";
	setAttr -av -k on ".rcp";
	setAttr -av -k on ".icp";
	setAttr -av -k on ".ocp";
	setAttr -cb on ".hbl";
	setAttr ".dss" -type "string" "lambert1";
select -ne :defaultResolution;
	setAttr -av -k on ".cch";
	setAttr -av -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av -k on ".w";
	setAttr -av -k on ".h";
	setAttr -av -k on ".pa" 1;
	setAttr -av -k on ".al";
	setAttr -av -k on ".dar";
	setAttr -av -k on ".ldar";
	setAttr -av -k on ".dpi";
	setAttr -av -k on ".off";
	setAttr -av -k on ".fld";
	setAttr -av -k on ".zsl";
	setAttr -av -k on ".isu";
	setAttr -av -k on ".pdu";
select -ne :defaultColorMgtGlobals;
	setAttr ".cfe" yes;
	setAttr ".cfp" -type "string" "<MAYA_RESOURCES>/OCIO-configs/Maya2022-default/config.ocio";
	setAttr ".vtn" -type "string" "ACES 1.0 SDR-video (sRGB)";
	setAttr ".vn" -type "string" "ACES 1.0 SDR-video";
	setAttr ".dn" -type "string" "sRGB";
	setAttr ".wsn" -type "string" "ACEScg";
	setAttr ".ovt" no;
	setAttr ".povt" no;
	setAttr ".otn" -type "string" "ACES 1.0 SDR-video (sRGB)";
	setAttr ".potn" -type "string" "ACES 1.0 SDR-video (sRGB)";
select -ne :hardwareRenderGlobals;
	setAttr -av -k on ".cch";
	setAttr -av -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -av -k off -cb on ".ctrs" 256;
	setAttr -av -k off -cb on ".btrs" 512;
	setAttr -av -k off -cb on ".fbfm";
	setAttr -av -k off -cb on ".ehql";
	setAttr -av -k off -cb on ".eams";
	setAttr -av -k off -cb on ".eeaa";
	setAttr -av -k off -cb on ".engm";
	setAttr -av -k off -cb on ".mes";
	setAttr -av -k off -cb on ".emb";
	setAttr -av -k off -cb on ".mbbf";
	setAttr -av -k off -cb on ".mbs";
	setAttr -av -k off -cb on ".trm";
	setAttr -av -k off -cb on ".tshc";
	setAttr -av -k off -cb on ".enpt";
	setAttr -av -k off -cb on ".clmt";
	setAttr -av -k off -cb on ".tcov";
	setAttr -av -k off -cb on ".lith";
	setAttr -av -k off -cb on ".sobc";
	setAttr -av -k off -cb on ".cuth";
	setAttr -av -k off -cb on ".hgcd";
	setAttr -av -k off -cb on ".hgci";
	setAttr -av -k off -cb on ".mgcs";
	setAttr -av -k off -cb on ".twa";
	setAttr -av -k off -cb on ".twz";
	setAttr -av -cb on ".hwcc";
	setAttr -av -cb on ".hwdp";
	setAttr -av -cb on ".hwql";
	setAttr -av -k on ".hwfr";
	setAttr -av -k on ".soll";
	setAttr -av -k on ".sosl";
	setAttr -av -k on ".bswa";
	setAttr -av -k on ".shml";
	setAttr -av -k on ".hwel";
select -ne :ikSystem;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av -k on ".gsn";
	setAttr -k on ".gsv";
	setAttr -s 4 ".sol";
dataStructure -fmt "raw" -as "name=externalContentTablZ:string=nodZ:string=key:string=upath:uint32=upathcrc:string=rpath:string=roles";
// End of ctrlARKitBS_M.ma

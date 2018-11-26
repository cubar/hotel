; generated by Slic3r 1.2.9 on 2018-11-03 at 12:15:32

; external perimeters extrusion width = 0.50mm
; perimeters extrusion width = 0.72mm
; infill extrusion width = 0.72mm
; solid infill extrusion width = 0.72mm
; top infill extrusion width = 0.72mm

M107
M104 S200 ; set temperature
G28 ; home all axes
G1 Z5 F5000 ; lift nozzle

M109 S200 ; wait for temperature to be reached
G21 ; set units to millimeters
G90 ; use absolute coordinates
M82 ; use absolute distances for extrusion
G92 E0
G1 Z0.350 F7800.000
G1 E-2.00000 F2400.00000
G92 E0
G1 X94.740 Y94.925 F7800.000
G1 E2.00000 F2400.00000
G1 X95.268 Y94.429 E2.02243 F600.000
G1 X95.845 Y93.986 E2.04494
G1 X96.552 Y93.555 E2.07055
G1 X97.222 Y93.239 E2.09346
G1 X97.940 Y92.987 E2.11704
G1 X98.656 Y92.815 E2.13982
G1 X99.384 Y92.716 E2.16252
G1 X100.136 Y92.692 E2.18583
G1 X100.843 Y92.739 E2.20775 F600.000
G1 X101.238 Y92.796 E2.22007
G1 X101.923 Y92.948 E2.24181
G1 X102.613 Y93.173 E2.26426
G1 X103.275 Y93.465 E2.28664
G1 X103.623 Y93.651 E2.29885
G1 X104.260 Y94.060 E2.32227
G1 X104.607 Y94.325 E2.33579
G1 X105.175 Y94.838 E2.35948
G1 X105.473 Y95.155 E2.37294
G1 X105.941 Y95.742 E2.39615
G1 X106.366 Y96.409 E2.42063
G1 X106.567 Y96.791 E2.43398
G1 X106.864 Y97.487 E2.45738
G1 X107.094 Y98.237 E2.48166
G1 X107.185 Y98.655 E2.49491
G1 X107.276 Y99.299 E2.51501
G1 X107.307 Y99.817 E2.53109
G1 X107.298 Y100.405 E2.54929
G1 X107.227 Y101.092 E2.57066
G1 X107.056 Y101.905 E2.59635
G1 X106.829 Y102.604 E2.61910
G1 X106.534 Y103.276 E2.64180
G1 X106.210 Y103.854 E2.66230
G1 X105.795 Y104.454 E2.68487
G1 X105.324 Y105.008 E2.70738
G1 X104.801 Y105.511 E2.72983
G1 X104.232 Y105.959 E2.75224
G1 X103.592 Y106.365 E2.77570
G1 X102.805 Y106.749 E2.80277
G1 X102.125 Y106.993 E2.82513
G1 X101.353 Y107.183 E2.84974
G1 X100.493 Y107.292 E2.87656
G1 X99.777 Y107.306 E2.89873
G1 X98.991 Y107.239 E2.92311
G1 X98.149 Y107.071 E2.94969
G1 X97.472 Y106.858 E2.97164
G1 X96.904 Y106.622 E2.99068
G1 X96.360 Y106.339 E3.00966
G1 X95.741 Y105.941 E3.03242
G1 X95.149 Y105.469 E3.05586
G1 X94.855 Y105.192 E3.06834
G1 X94.398 Y104.696 E3.08922
G1 X93.956 Y104.110 E3.11192
G1 X93.739 Y103.774 E3.12430
G1 X93.397 Y103.137 E3.14666
G1 X93.118 Y102.464 E3.16921
G1 X92.994 Y102.086 E3.18151
G1 X92.834 Y101.440 E3.20212
G1 X92.726 Y100.724 E3.22452
G1 X92.690 Y100.003 E3.24685
G1 X92.703 Y99.565 E3.26041
G1 X92.791 Y98.786 E3.28468
G1 X92.877 Y98.359 E3.29816
G1 X93.078 Y97.651 E3.32093
G1 X93.230 Y97.243 E3.33438
G1 X93.560 Y96.542 E3.35837
G1 X93.776 Y96.167 E3.37177
G1 X94.189 Y95.565 E3.39434
G1 X94.688 Y94.979 E3.41814
G1 E1.41814 F2400.00000
G92 E0
M104 S0 ; turn off temperature
G28 X0  ; home X axis
M84     ; disable motors

; filament used = 1.4mm (0.0cm3)

; avoid_crossing_perimeters = 0
; bed_shape = 0x0,200x0,200x200,0x200
; bed_temperature = 0
; before_layer_gcode = 
; bridge_acceleration = 0
; bridge_fan_speed = 100
; brim_width = 0
; complete_objects = 0
; cooling = 1
; default_acceleration = 0
; disable_fan_first_layers = 3
; duplicate_distance = 6
; end_gcode = M104 S0 ; turn off temperature\nG28 X0  ; home X axis\nM84     ; disable motors\n
; extruder_clearance_height = 20
; extruder_clearance_radius = 20
; extruder_offset = 0x0
; extrusion_axis = E
; extrusion_multiplier = 1
; fan_always_on = 0
; fan_below_layer_time = 60
; filament_colour = #FFFFFF
; filament_diameter = 3
; first_layer_acceleration = 0
; first_layer_bed_temperature = 0
; first_layer_extrusion_width = 200%
; first_layer_speed = 30
; first_layer_temperature = 200
; gcode_arcs = 0
; gcode_comments = 0
; gcode_flavor = reprap
; infill_acceleration = 0
; infill_first = 0
; layer_gcode = 
; max_fan_speed = 100
; max_print_speed = 80
; max_volumetric_speed = 0
; min_fan_speed = 35
; min_print_speed = 10
; min_skirt_length = 0
; notes = 
; nozzle_diameter = 0.5
; only_retract_when_crossing_perimeters = 1
; ooze_prevention = 0
; output_filename_format = [input_filename_base].gcode
; perimeter_acceleration = 0
; post_process = 
; pressure_advance = 0
; resolution = 0
; retract_before_travel = 2
; retract_layer_change = 0
; retract_length = 2
; retract_length_toolchange = 10
; retract_lift = 0
; retract_restart_extra = 0
; retract_restart_extra_toolchange = 0
; retract_speed = 40
; skirt_distance = 6
; skirt_height = 1
; skirts = 1
; slowdown_below_layer_time = 5
; spiral_vase = 0
; standby_temperature_delta = -5
; start_gcode = G28 ; home all axes\nG1 Z5 F5000 ; lift nozzle\n
; temperature = 200
; threads = 2
; toolchange_gcode = 
; travel_speed = 130
; use_firmware_retraction = 0
; use_relative_e_distances = 0
; use_volumetric_e = 0
; vibration_limit = 0
; wipe = 0
; z_offset = 0
; dont_support_bridges = 1
; extrusion_width = 0
; first_layer_height = 0.35
; infill_only_where_needed = 0
; interface_shells = 0
; layer_height = 0.3
; raft_layers = 0
; seam_position = aligned
; support_material = 0
; support_material_angle = 0
; support_material_contact_distance = 0.2
; support_material_enforce_layers = 0
; support_material_extruder = 1
; support_material_extrusion_width = 0
; support_material_interface_extruder = 1
; support_material_interface_layers = 3
; support_material_interface_spacing = 0
; support_material_interface_speed = 100%
; support_material_pattern = pillars
; support_material_spacing = 2.5
; support_material_speed = 60
; support_material_threshold = 0
; xy_size_compensation = 0
; bottom_solid_layers = 3
; bridge_flow_ratio = 1
; bridge_speed = 60
; external_fill_pattern = rectilinear
; external_perimeter_extrusion_width = 0
; external_perimeter_speed = 50%
; external_perimeters_first = 0
; extra_perimeters = 1
; fill_angle = 45
; fill_density = 20%
; fill_pattern = honeycomb
; gap_fill_speed = 20
; infill_every_layers = 1
; infill_extruder = 1
; infill_extrusion_width = 0
; infill_overlap = 15%
; infill_speed = 80
; overhangs = 1
; perimeter_extruder = 1
; perimeter_extrusion_width = 0
; perimeter_speed = 60
; perimeters = 3
; small_perimeter_speed = 15
; solid_infill_below_area = 70
; solid_infill_every_layers = 0
; solid_infill_extruder = 1
; solid_infill_extrusion_width = 0
; solid_infill_speed = 20
; thin_walls = 1
; top_infill_extrusion_width = 0
; top_solid_infill_speed = 15
; top_solid_layers = 3

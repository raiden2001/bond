#Parallel Simulation
# create n_evns scene

import genesis as gs 
import torch
################ init ##########################
gs.init(backend=gs.gpu)
############################## create a scene #####################
scene = gs.scene(
    show_viewer = True,
    viewer_options = gs.options.ViewerOptions(
        camera_pos = (3.5,-1.0,2.5),
        camera_lookat = (0.0,0.0,0.5),
        camera_fov = 40,
    ),
    rigid_otions = gs.options.RigidOptions(
        dt                  = 0.01,            
    ),
                 
)
###########################entities##############################
plane = scene.add_entity(
    gs.morphs.Plane(),
)

franka = scene.add_entity(
    gs.morphs.MJCF(file = 'xml/franka_emika_panda/panda.xml'),
)
################################ build ###########################
# create 20 parallel environments

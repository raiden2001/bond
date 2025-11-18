import genesis as gs 
gs.init(backend=gs.cpu)

scene = gs.Scene(
    show_viewer = True,
    viewer_options = gs.options.ViewerOptions(
        res           =(1280,960),
        camera_pos    =(3.5,0.0,2.5),
        camera_lookat = (0.0,0.0,0.5),
        camera_fov    = 40,
        max_FPS       = 60,
    ),
    vis_options = gs.options.VisOptions(
        show_world_frame = True, # visualize the coordinate frame of `world` at its orgina
        world_frame_size = 1.0,#length of world fram in meter 
        show_link_frame  = False,# do not visualizae frames of entity links
        show_cameras     = False, #do not visualize mesh and frustum of cameras added 
        plane_reflection = True, #turn on plane reflection
        ambient_light    = (0.1,0.1,0.1), # ambient light setting

    ),             
    renderer = gs.renderers.Rasterizer(), #using rasterizer for camera rendering 
) #shows the scene 
plane = scene.add_entity(gs.morphs.Plane())
franka = scene.add_entity(gs.morphs.MJCF(file='xml/franka_emika_panda/panda.xml'),)
scene.build() #builds the entity

for i in range(1000):
    scene.step()

#Quaternion representing a 90-degree rotation around the z-axis
rotation = [0.707,0,0,0.707] #[w,x,y,z]
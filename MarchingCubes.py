from ursina import *
from marchingTools import *

shape = (10, 10, 10)
noiseScale = 0.15
surface = 0
noise = getNoiseGrid(shape, noiseScale)

app = Ursina()
EditorCamera()
camera.fov = 90
window.borderless = False
window.render_mode = 'wireframe'

## Draw spheres representing the noise grid.
# halfShape = Vec3(tuple(x/2 for x in shape))
# for y in range(shape[1]):
#     for z in range(shape[2]):
#         for x in range(shape[0]):
#             Entity(model='sphere', position=-halfShape+Vec3(x + .5, y + .5, z + .5),
#                 color=(color.white if noise[y][z][x] >= surface else color.black), scale=0.1)

world = Entity(model = generateMeshFromNoise(noise, surface))
app.run()

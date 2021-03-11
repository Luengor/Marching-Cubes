from ursina import *
from marchingTools import *

shape = (20, 20, 20)
noiseScale = 0.15
surface = 0
noise = getNoiseGrid(shape, s=noiseScale)

app = Ursina()
EditorCamera()
camera.fov = 90
window.borderless = False
window.render_mode = 'wireframe'

world = Entity(model = generateMeshFromNoise(noise, surface))
app.run()

from ursina import *
from marchingTools import *
import time

shape = (20, 20, 20)
noiseScale = 0.15
surface = 0
noise = getNoiseGrid(shape, s=noiseScale)

app = Ursina()
EditorCamera()
camera.fov = 90
window.borderless = False
window.render_mode = 'wireframe'

# Generate 12x12x12: 3.50 seconds -> 0.25 seconds
world = Entity(model = generateMeshFromNoise(noise, surface))
app.run()

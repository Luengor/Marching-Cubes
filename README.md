# Marching-Cubes
Marching cubes algorithm in ursina.
   
   
## Brief explanation
The marching cubes algorithm works by creating a 3d grid of perlin noise. Once this noise is generated, starts the construction of the mesh. The mesh is created by "joining" the points of the grid which value is greater than a threshold (the surface level). To triangulate the faces I used the following triangulation [table](http://paulbourke.net/geometry/polygonise/table2.txt). Finally, all vertices and triangles are combined into a single mesh removing any duplicates.
    
    
## Dependencies
For this project I used the following:
|  Package  |  Version  |
|-----------|-----------|
|Python     |   3.9.5   |
|Ursina     |   3.5.0   |
|OpenSimplex|   0.3     |
     
     
## Sources
The idea came from [this](https://youtu.be/M3iI2l0ltbE) Sebastian Lague's video and the needed info from [here](http://paulbourke.net/geometry/polygonise/).
# Marching-Cubes
Marching cubes algorithm in ursina.

## Brief explanation
The marching cubes algorithm works by creating a 3d grid of perlin noise.
Once this noise is generated, starts the construction of the mesh. The mesh
is created by "joining" the points of the grid which value is greater than a
threshold (the surface level). To triangulate the faces I used the following
triangulation [table](http://paulbourke.net/geometry/polygonise/table2.txt). Finally,
all vertices and triangles are added to a single mesh.

## Sources
Most of the data and the triangulation table came from [here](http://paulbourke.net/geometry/polygonise/).

# Blender Script for basic cube house (Still a work in progress end goal is to make actual houses prcedually)

import bpy
import random

# Function to create a tower
def create_tower(x, y, z, scale):
    bpy.ops.mesh.primitive_cylinder_add(radius=scale, depth=z, location=(x, y, z/2))

# Function to create a wall with battlements
def create_wall(x1, y1, x2, y2, z, thickness):
    bpy.ops.mesh.primitive_cube_add(location=((x1 + x2) / 2, (y1 + y2) / 2, z))
    bpy.context.object.scale = (abs(x2 - x1), abs(y2 - y1), thickness)

    # Create battlements
    bpy.ops.mesh.primitive_cube_add(location=((x1 + x2) / 2, y1 + 1, z + thickness * 2))
    bpy.context.object.scale = (abs(x2 - x1), 1, thickness)

    bpy.ops.mesh.primitive_cube_add(location=((x1 + x2) / 2, y2 - 1, z + thickness * 2))
    bpy.context.object.scale = (abs(x2 - x1), 1, thickness)

# Function to create a house
def create_house(x, y, z, width, depth, height):
    bpy.ops.mesh.primitive_cube_add(location=(x, y, z + height/2))
    bpy.context.object.scale = (width, depth, height)
    bpy.ops.mesh.primitive_cube_add(location=(x, y, z + height))
    bpy.context.object.scale = (width * 0.8, depth * 0.8, height * 0.2)

    # Add roof
    bpy.ops.mesh.primitive_cone_add(vertices=12, radius1=width*0.55, depth=height*0.6, location=(x, y, z + height * 1.2))

# Function to create a marketplace stall
def create_stall(x, y, z, width, depth, height):
    bpy.ops.mesh.primitive_cube_add(location=(x, y, z + height/2))
    bpy.context.object.scale = (width, depth, height)
    bpy.ops.mesh.primitive_cylinder_add(radius=width/3, depth=height*0.4, location=(x, y, z + height))

# Function to create a church
def create_church(x, y, z, width, depth, height):
    bpy.ops.mesh.primitive_cube_add(location=(x, y, z + height/2))
    bpy.context.object.scale = (width, depth, height)

    # Add roof
    bpy.ops.mesh.primitive_cone_add(vertices=12, radius1=width/2, depth=height/2, location=(x, y, z + height))

    # Add cross
    bpy.ops.mesh.primitive_cube_add(location=(x, y, z + height*1.3))
    bpy.context.object.scale = (width*0.1, depth*0.1, height*0.2)

# Parameters
num_towers = 8
tower_scale = 5.0
wall_thickness = 0.5
castle_size = 200
num_houses = 80
num_stalls = 20
num_churches = 5
village_size = 300
min_distance = 35

# Generate castle
for i in range(num_towers):
    x = random.uniform(-castle_size, castle_size)
    y = random.uniform(-castle_size, castle_size)
    z = random.uniform(20, 40)  # Adjust height as needed
    create_tower(x, y, z, tower_scale)

create_wall(-castle_size, -castle_size, castle_size, -castle_size, 0, wall_thickness)
create_wall(-castle_size, -castle_size, -castle_size, castle_size, 0, wall_thickness)
create_wall(castle_size, -castle_size, castle_size, castle_size, 0, wall_thickness)
create_wall(-castle_size, castle_size, castle_size, castle_size, 0, wall_thickness)

# Generate medieval village
# Generate houses
for i in range(num_houses):
    while True:
        x = random.uniform(-village_size, village_size)
        y = random.uniform(-village_size, village_size)
        # Check if the new position is too close to existing buildings
        if all(((x - b.location.x)**2 + (y - b.location.y)**2) >= min_distance**2 for b in bpy.data.objects if b.type == 'MESH'):
            break
    z = 0  # Houses are on the ground level
    width = random.uniform(10, 20)
    depth = random.uniform(10, 20)
    height = random.uniform(15, 30)
    create_house(x, y, z, width, depth, height)

# Generate marketplace stalls
for i in range(num_stalls):
    while True:
        x = random.uniform(-village_size, village_size)
        y = random.uniform(-village_size, village_size)
        # Check if the new position is too close to existing buildings
        if all(((x - b.location.x)**2 + (y - b.location.y)**2) >= min_distance**2 for b in bpy.data.objects if b.type == 'MESH'):
            break
    z = 0  # Stalls are on the ground level
    width = random.uniform(5, 10)
    depth = random.uniform(5, 10)
    height = random.uniform(10, 20)
    create_stall(x, y, z, width, depth, height)

# Generate churches
for i in range(num_churches):
    while True:
        x = random.uniform(-village_size, village_size)
        y = random.uniform(-village_size, village_size)
        # Check if the new position is too close to existing buildings
        if all(((x - b.location.x)**2 + (y - b.location.y)**2) >= min_distance**2 for b in bpy.data.objects if b.type == 'MESH'):
            break
    z = 0  # Churches are on the ground level
    width = random.uniform(20, 40)
    depth = random.uniform(20, 40)
    height = random.uniform(30, 50)
    create_church(x, y, z, width, depth, height)

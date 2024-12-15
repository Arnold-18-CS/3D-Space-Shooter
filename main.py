# Introduction to VPython

# importing vpython module
from screeninfo import get_monitors
from vpython import *
from time import *
import numpy as np

window = get_monitors()[0]
scene = canvas(width=window.width, height=window.height, background=color.gray(0.3))

# Disable zooming (scroll functionality)
scene.autoscale = False  # Disable the automatic scaling of the scene
scene.range = 20  # Set the range of the camera view (adjust as needed)

mRadius = 1
wallThickness = .3
roomWidth, roomDepth, roomHeight = 20,20,20

floor       = box(pos=vector(0,-roomHeight/2,0), color=color.white, size=vector(roomWidth,wallThickness,roomDepth))
# ceiling     = box(pos=vector(0,roomHeight/2,0),  color=color.white, size=vector(roomWidth,wallThickness,roomDepth))
# right_wall  = box(pos=vector(roomWidth/2,0,0),  color=color.white, size=vector(wallThickness,roomHeight,roomDepth))
left_wall   = box(pos=vector(-roomWidth/2,0,0), color=color.white, size=vector(wallThickness,roomHeight,roomDepth))
back_wall   = box(pos=vector(0,0,-roomDepth/2), color=color.white, size=vector(roomWidth,roomHeight,wallThickness))

xPos, yPos, zPos = 0, 0, 0
marble      = sphere(pos=vector(xPos, yPos, zPos), color=color.red, radius=mRadius)

# Room boundaries
RWEdge = roomWidth / 2 - wallThickness / 2
LWEdge = -roomWidth / 2 + wallThickness / 2
CEdge = roomHeight / 2 - wallThickness / 2
FlEdge = -roomHeight / 2 + wallThickness / 2
BEdge = roomDepth / 2 + wallThickness / 2
FrEdge = - roomDepth / 2 + wallThickness / 2

velocity = vector(0,0,0)

# Store the initial mouse position
mouse_dragging = False
previous_mouse_pos = vector(0, 0, 0)

# Function to handle keypress
# def handle_keydown(event):
#     global velocity, move_marble
#     move_marble = True
    
#     if event.key == 'w':
#         velocity.y += 0.1
        
#     elif event.key == 's':
#         velocity.y -= 0.1
 
#     elif event.key == 'a':
#         velocity.x -= 0.1
 
#     elif event.key == 'd':
#         velocity.x += 0.1
 
#     elif event.key == 'j':
#         velocity.z -= 0.1
 
#     elif event.key == 'l':
#         velocity.z += 0.1
        
# def handle_keyup(event):
#     global velocity, move_marble
#     move_marble = False
#     velocity = vector(0,0,0)
    
# scene.bind('keydown', handle_keydown)
# scene.bind('keyup', handle_keyup)

# Mouse event handlers
def on_mouse_click(evt):
    global mouse_dragging, previous_mouse_pos
    # When mouse is clicked, start dragging
    mouse_dragging = True
    previous_mouse_pos = scene.mouse.pos  # Track where the mouse is clicked

def on_mouse_release(evt):
    global mouse_dragging
    # When mouse is released, stop dragging
    mouse_dragging = False

def on_mouse_move(evt):
    global mouse_dragging, previous_mouse_pos, marble
    # If the mouse is being dragged
    if mouse_dragging:
        # Move the marble to the new mouse position
        mouse_pos = scene.mouse.pos
        marble.pos = vector(mouse_pos.x, mouse_pos.y, marble.pos.z)  # Update marble position based on mouse
        previous_mouse_pos = mouse_pos

# Bind mouse events
scene.bind('mousedown', on_mouse_click)
scene.bind('mouseup', on_mouse_release)
scene.bind('mousemove', on_mouse_move)


while True:
    rate(30) # To change the speed of animation
   
    xPos += velocity.x
    yPos += velocity.y
    zPos += velocity.z

    xRMEdge = xPos + mRadius
    xLMEdge = xPos - mRadius
    yTMEdge = yPos + mRadius
    yBMEdge = yPos - mRadius
    zBMEdge = zPos + mRadius
    zFMEdge = zPos - mRadius

    marble.pos = vector(xPos,yPos,zPos)

    if xRMEdge > RWEdge or xLMEdge < LWEdge:
            velocity.x *= -1
            marble.color = color.white

    if yTMEdge > CEdge or yBMEdge < FlEdge:
            velocity.y *= -1
            marble.color = color.black

    if zBMEdge > BEdge or zFMEdge < FrEdge:
            velocity.z *= -1
            marble.color = color.blue 
            
    move_marble = False
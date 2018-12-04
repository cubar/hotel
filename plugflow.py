#!/usr/bin/env python2

import sys, time, os
dir = '/usr/lib64/freecad/lib' # path to your FreeCAD.so or FreeCAD.dll file
if not os.path.isdir(dir):
  dir = '/usr/lib/freecad/lib'

sys.path.append(dir)
workDir = os.getcwd()
import FreeCAD as App
import FreeCADGui as Gui
import math
doc = App.newDocument("hotel")
App.setActiveDocument("hotel")
App.ActiveDocument=App.getDocument("hotel")
Gui.ActiveDocument=Gui.getDocument("hotel")
Gui.activeDocument().activeView().viewAxonometric()
Gui.SendMsgToActiveView("ViewFit")
dui = Gui.getDocument("hotel")

tankSize = [9,3,6]
brickSize = [30,15,12]
brickAnimationDelay = 0
joint =.3 # brickwork joint
inletFunnelRadius = 30
inletFunnelThickness = 5
inletTubeRadius = 4
inletTubeThickness = .5
inletAngle = 150
inletAnimationDelay = 1
outletRadius = 4
outletTubeThickness = .5
outletAngle = 50
outletAnimationDelay = 1

noRotation = App.Rotation(App.Vector(0,0,0), 0)

class Tank:
  size = tankSize
  length = size[0]
  width = size[1]
  height = size[2]
  bricks = (length+width)*2*height


class Brick:
  size = brickSize
  length = size[0]
  width = size[1]
  height = size[2]
  delay = brickAnimationDelay
  n = 0

  def __init__(self):
    Brick.n += 1
    self.name = "Brick%03d" % Brick.n
    self.b = doc.addObject("Part::Box", self.name)
    b = self.b
    (b.Length, b.Width, b.Height) = Brick.size
    #App.ActiveDocument.recompute()

  @classmethod
  def fuse(self):
    fuse = doc.addObject("Part::MultiFuse","Tank")
    fuse.Shapes = doc.findObjects("Part::Box")

  def place(self, position, angle):
    b = self.b
    placement = App.Placement(position, App.Rotation(App.Vector(0,0,1), angle))
    doc.getObject(self.name).Placement = placement
    dui.getObject(self.name).ShapeColor = (1.00,0.67,0.40)
    Gui.activeDocument().activeView().viewAxonometric()
    Gui.updateGui()
    time.sleep(Brick.delay)

  @classmethod
  def reset(self):
    Brick.n = 0


class Inlet:
  class Funnel:
    thickness = inletFunnelThickness
    radius = inletFunnelRadius
    radiusCut = inletFunnelRadius - inletFunnelThickness

  class Chopper:
    size = [3 * inletFunnelRadius for i in range(3)]

  class Tube:
    radius = inletTubeRadius
    thickness = inletTubeThickness
    length = Tank.height*Brick.height - .4*Brick.height + inletFunnelRadius
    size = [radius, length]
    sizeCut = [radius-thickness, length]
    position = App.Vector(inletFunnelRadius/2,0,0)

  angle = inletAngle
  position0 = App.Vector(
    -3*Brick.width,
    (Tank.width * Brick.length + 2 * Brick.width) / 2,
    Tank.height*Brick.height+inletFunnelRadius
  )
  position = App.Vector(
    0,
    (Tank.width * Brick.length + 2 * Brick.width) / 2,
    Tank.height*Brick.height+inletFunnelRadius
  )
  rotation = App.Rotation(App.Vector(0,1,0), angle)
  delay = inletAnimationDelay

  def __init__(self):
# Make a solid funnel
    self.sphere(Inlet.Funnel.radius, 'inletSphere')
    self.cube(Inlet.Chopper.size, 'inletFunnelCut')
    difference('inletFunnel', 'inletSphere', 'inletFunnelCut')

# add a cylinder to the funnel
    cyl('inletCyl', Inlet.Tube.size, Inlet.Tube.position)
    shapes = [doc.getObject('inletCyl'), doc.getObject('inletFunnel')]
    union('inletSolid', shapes)

# make the cylinder hollow using a smaller cylinder
    cyl('inletCylCut', Inlet.Tube.sizeCut, Inlet.Tube.position)
    difference('inletSphereTube', 'inletSolid', 'inletCylCut')

# hollow out the funnel using a smaller sphere
    self.sphere(Inlet.Funnel.radiusCut, 'inletSphereCut')
    difference('inlet', 'inletSphereTube', 'inletSphereCut')

# save the object
    self.inlet = doc.getObject('inlet')

  def sphere(self, radius, name):
    sphere = doc.addObject("Part::Sphere", name)
    sphere.Radius = radius
    dui.getObject(name).ShapeColor = (.8,.8,.8)

  def cube(self, size, name):
    b = doc.addObject("Part::Box", name)
    length = b.Length=b.Width=b.Height = Inlet.Funnel.radius * 3
    Hypotenusa = math.sqrt(length**2*5/4)
    position = App.Vector(
      -Hypotenusa * cos(180-Inlet.angle),
      -length / 2,
      -Hypotenusa * sin(180-Inlet.angle),
    )
    rotation = App.Rotation(App.Vector(0,1,0), 180-Inlet.angle)
    b.Placement = App.Placement(position, rotation)


class Outlet:
  class Tube:
    radius = outletRadius
    length = (Tank.height-1)*(Brick.height+joint)+Brick.height/2
    size = [radius, length]
    sizeCut = [radius-outletTubeThickness, length+20]


  position0 = App.Vector(
    Tank.length*(Brick.length+joint)+2*Brick.width,
    (Tank.width+1)*(Brick.length+joint)/2,
    Brick.height/2
  )
  position = App.Vector(
    Tank.length*(Brick.length+joint)-2*Brick.width,
    (Tank.width+1)*(Brick.length+joint)/2,
    Brick.height
  )
  angle = outletAngle
  rotation = App.Rotation(App.Vector(0,1,0), outletAngle)
  delay = outletAnimationDelay

  def __init__(self):
    cyl('outletCyl', Outlet.Tube.size, App.Vector(0,0,Brick.height/2))
    cyl('outletCylCut', Outlet.Tube.sizeCut)
    difference('outlet', 'outletCyl', 'outletCylCut')
    place(doc.getObject('outlet'), Outlet.position0, Outlet.rotation)
    time.sleep(Outlet.delay)
    place(doc.getObject('outlet'), Outlet.position, Outlet.rotation)


#out=Outlet(); v()




def south(layer, z):
  # Tank wall south
  length = Tank.length
  v = joint
  if layer % 2 == 0:
    x = 0
  else:
    v = (Tank.length - 1) * joint / Tank.length
    x = Brick.width + v
    length -= 1
  for n in range(length):
    b = Brick()
    b.place(position=App.Vector(x, 0, z), angle=0)
    x += Brick.length + v

def north(layer, z):
  # Tank wall north
  length = Tank.length
  v = joint
  if layer % 2 == 0:
    x = Tank.length * (Brick.length + v)
  else:
    v = (Tank.length - 1) * joint / Tank.length
    x = -Brick.width - v + Tank.length * (Brick.length + v)
    length -= 1
  y = Tank.width * (Brick.length + v) + Brick.width + v
  for n in range(length-1, -1, -1):
    b = Brick()
    x -= Brick.length + v
    b.place(position=App.Vector(x, y, z), angle=0)

def east(layer, z):
  # Tank wall east
  width = Tank.width
  v = joint
  if layer % 2 == 0:
    y = Brick.width + joint
  else:
    v = (Tank.width - 1) * joint / Tank.width
    y = 0
    width += 1
  x = Tank.length * (Brick.length + v) - v
  for n in range(width):
    b = Brick()
    b.place(position=App.Vector(x, y, z), angle=90)
    y += Brick.length + v

def west(layer, z):
  # Tank wall west
  width = Tank.width
  v = joint
  if layer % 2 == 0:
    y = Tank.width * (Brick.length + v) - Brick.width
  else:
    v = (Tank.width - 1) * joint / Tank.width
    width += 1
    y = -Brick.length - v + width * (Brick.length + v)
  x = Brick.width
  for n in range(width-1, -1, -1):
    b = Brick()
    b.place(position=App.Vector(x, y, z), angle=90)
    y -= Brick.length + v

def tank():
  for layer in range(Tank.height):
    z = layer * Brick.height
    south(layer, z)
    east(layer, z)
    north(layer, z)
    west(layer, z)

def i():
  global o
  o = Inlet()

def outlet():
  out=Outlet()

def v():
  App.ActiveDocument.recompute()
  Gui.activeDocument().activeView().viewAxonometric()
  Gui.SendMsgToActiveView("ViewFit")
  Gui.updateGui()

def d():
  for obj in doc.Objects:
    doc.removeObject(obj.Label)
  Brick.reset()

def r():
  d()
  tank()
  v()
  #Brick.fuse(); v()
  o = Inlet()
  place(o.inlet, Inlet.position0, Inlet.rotation)
  v()
  time.sleep(Inlet.delay)
  place(o.inlet, Inlet.position, Inlet.rotation)
  v()
  outlet()
  v()

def difference(name, base, tool):
  cut = doc.addObject("Part::Cut",name)
  cut.Base = doc.getObject(base)
  cut.Tool = doc.getObject(tool)

def union(name, shapes):
  fuse = doc.addObject("Part::MultiFuse",name)
  fuse.Shapes = shapes

def place(shape, position=App.Vector(0,0,0), rotation=None):
  shape.Placement = App.Placement(position, rotation)

def sin(degrees):
  return math.sin(math.radians(degrees))

def cos(degrees):
  return math.cos(math.radians(degrees))

def cyl(name, size, position=App.Vector(0,0,0), rotation=noRotation, color=(.0,.0,.0)):
  cyl = doc.addObject("Part::Cylinder", name)
  (cyl.Radius, cyl.Height) = size
  cyl.Placement = App.Placement(position, rotation)
  dui.getObject(name).ShapeColor = color


r()





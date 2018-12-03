#!/usr/bin/env python2

import sys, time, os
dir = '/usr/lib64/freecad/lib' # path to your FreeCAD.so or FreeCAD.dll file
if not os.path.isdir(dir):
  dir = '/usr/lib/freecad/lib'

sys.path.append(dir)
workDir = os.getcwd()
import FreeCAD as App
import FreeCADGui as Gui
doc = App.newDocument("hotel")
App.setActiveDocument("hotel")
App.ActiveDocument=App.getDocument("hotel")
Gui.ActiveDocument=Gui.getDocument("hotel")
Gui.activeDocument().activeView().viewAxonometric()
Gui.SendMsgToActiveView("ViewFit")
dui = Gui.getDocument("hotel")

sleep = 0
voeg = 0.3
class Tank:
  length = 9
  width = 3
  height = 3
  size = [length, width, height]
  aantal = (length+width)*2*height


class Brik:
  length = 30
  width = 15
  height = 12
  size = [length, width, height]


class Inle:
  class Funnel:
    thickness = 5
    radius = 30

  class Tube:
    radius = 4
    length = (Tank.height+.5) * Brik.height + Inle.Funnel.radius
    thickness = 0.5
    size = [radius, length]
    position = (Inle.Funnel.radius/2)

  class Part:
    position0 = App.Vector(
      -3*Brik.width,
      (Tank.width * Brik.length + 2 * Brik.width) / 2,
      Tank.height*Brik.height+Inle.Funnel.radius
    )
    position = App.Vector(
      -Brik.width,
      (Tank.width * Brik.length + 2 * Brik.width) / 2,
      Tank.height*Brik.height+Inle.Funnel.radius
    )
    rotation = App.Rotation(App.Vector(0,1,0), 150)


class Inlet:
  def __init__(self):
    self.tube()
    self.funnel()
    self.fuse()
    self.tubeSubtract()
    self.funnelSubtract()
    self.place(Inle.Part.position0)
    v()

  @classmethod
  def place(self, position):
    placement = App.Placement(position, Inle.Part.rotation)
    doc.getObject("inletFunnelHollow").Placement = placement

  def fuse(self):
    App.activeDocument().addObject("Part::MultiFuse","inletFusion")
    App.activeDocument().inletFusion.Shapes = [
      App.activeDocument().inletTube,App.activeDocument().funnel]
    Gui.activeDocument().inletTube.Visibility=False
    Gui.activeDocument().funnel.Visibility=False

  def tube(self, type=''):
    if type=='Inner':
      size = [Inle.Tube.size[0]-Inle.Tube.thickness, Inle.Tube.size[1]+1]
    else:
      size = Inle.Tube.size
    name = "inletTube%s" % type
    tube = doc.addObject("Part::Cylinder", name)
    (tube.Radius, tube.Height) = size
    tube.Placement.Position = Inle.Tube.position
    Gui.getDocument("hotel").getObject(name).ShapeColor = (.0,.0,.0)

  def tubeSubtract(self):
    self.tube('Inner')
    App.activeDocument().addObject("Part::Cut","inletTubeCut")
    App.activeDocument().inletTubeCut.Base = App.activeDocument().inletFusion
    App.activeDocument().inletTubeCut.Tool = App.activeDocument().inletTubeInner
    Gui.activeDocument().inletFusion.Visibility=False
    Gui.activeDocument().inletTubeInner.Visibility=False

  def funnel(self, type=''):
    radius = Inle.Funnel.radius
    name = 'funnel' + type
    if type=='Inner':
      radius -= Inle.Funnel.thickness

    funnel = doc.addObject("Part::Sphere", name)
    funnel.Radius = radius
    Gui.getDocument("hotel").getObject(name).ShapeColor = (.8,.8,.8)

  def funnelSubtract(self):
    self.funnel('Inner')
    App.activeDocument().addObject("Part::Cut","inletFunnelHollow")
    App.activeDocument().inletFunnelHollow.Base = App.activeDocument().inletTubeCut
    App.activeDocument().inletFunnelHollow.Tool = App.activeDocument().funnelInner
    Gui.activeDocument().inletTubeCut.Visibility=False
    Gui.activeDocument().funnelInner.Visibility=False

  def chop(self):
    box = doc.addObject("Part::Box","inletFunnelChopper")
    App.activeDocument().inletFunnelHollow.Base = App.activeDocument().inletTubeCut
    App.activeDocument().inletFunnelHollow.Tool = App.activeDocument().funnelInner
    Gui.activeDocument().inletTubeCut.Visibility=False
    Gui.activeDocument().funnelInner.Visibility=False


#d(); i();



class Brick:
  n = 0
  def __init__(self):
    Brick.n += 1
    self.name = "Brik%03d" % Brick.n
    self.b = doc.addObject("Part::Box", self.name)
    b = self.b
    (b.Length, b.Width, b.Height) = Brik.size
    App.ActiveDocument.recompute()

  @classmethod
  def fuse(self):
    fuse = doc.addObject("Part::MultiFuse","brickFusion")
    fuse.Shapes = doc.findObjects("Part::Box")

  def place(self, position, angle):
    b = self.b
    placement = App.Placement(position, App.Rotation(App.Vector(0,0,1), angle))
    doc.getObject(self.name).Placement = placement
    dui.getObject(self.name).ShapeColor = (1.00,0.67,0.40)
    Gui.activeDocument().activeView().viewAxonometric()
    Gui.updateGui()
    time.sleep(sleep)

  @classmethod
  def reset(self):
    Brick.n = 0


def south(layer, z):
  # Tank wall south
  length = Tank.length
  v = voeg
  if layer % 2 == 0:
    x = 0
  else:
    v = (Tank.length - 1) * voeg / Tank.length
    x = Brik.width + v
    length -= 1
  for n in range(length):
    b = Brick()
    b.place(position=App.Vector(x, 0, z), angle=0)
    x += Brik.length + v

def north(layer, z):
  # Tank wall north
  length = Tank.length
  v = voeg
  if layer % 2 == 0:
    x = Tank.length * (Brik.length + v)
  else:
    v = (Tank.length - 1) * voeg / Tank.length
    x = -Brik.width - v + Tank.length * (Brik.length + v)
    length -= 1
  y = Tank.width * (Brik.length + v) + Brik.width + v
  for n in range(length-1, -1, -1):
    b = Brick()
    x -= Brik.length + v
    b.place(position=App.Vector(x, y, z), angle=0)

def east(layer, z):
  # Tank wall east
  width = Tank.width
  v = voeg
  if layer % 2 == 0:
    y = Brik.width + voeg
  else:
    v = (Tank.width - 1) * voeg / Tank.width
    y = 0
    width += 1
  x = Tank.length * (Brik.length + v) - v
  for n in range(width):
    b = Brick()
    b.place(position=App.Vector(x, y, z), angle=90)
    y += Brik.length + v

def west(layer, z):
  # Tank wall west
  width = Tank.width
  v = voeg
  if layer % 2 == 0:
    y = Tank.width * (Brik.length + v) - Brik.width
  else:
    v = (Tank.width - 1) * voeg / Tank.width
    width += 1
    y = -Brik.length - v + width * (Brik.length + v)
  x = Brik.width
  for n in range(width-1, -1, -1):
    b = Brick()
    b.place(position=App.Vector(x, y, z), angle=90)
    y -= Brik.length + v

def tank():
  for layer in range(Tank.height):
    z = layer * Brik.height
    south(layer, z)
    east(layer, z)
    north(layer, z)
    west(layer, z)

def inlet():
  i = Inlet()
  #i.place()

def outlet():
  pass

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
  tank()
  Brick.fuse()
  v()
  inlet()
  time.sleep(1)
  Inlet.place(Inle.Part.position)
  outlet()

i=inlet
o=outlet
t=tank

d()
r()

def cut(name, base, tool):
  cut = doc.addObject("Part::Cut",name)
  cut.Base = base
  cut.Tool = tool

def fuse(name, shapes):
  fuse = doc.addObject("Part::MultiFuse",name)
  fuse.Shapes = shapes

def place(shape, position=None, rotation=None):
  if not position:
    position = App.Vector(0,0,0)
  shape.Placement = App.Placement(position, rotation)

def fuseTest():
  d()
  box = doc.addObject("Part::Box", "box")
  box = doc.addObject("Part::Cylinder", "cyl")
  bol = doc.addObject("Part::Sphere", "bol")
  fuse("fuse", doc.findObjects())
  v()


def cutTest():
  d()
  box = doc.addObject("Part::Box", "box")
  cyl = doc.addObject("Part::Cylinder", "cyl")
  bol = doc.addObject("Part::Sphere", "bol")
  cut('cut', cyl, bol)
  v()



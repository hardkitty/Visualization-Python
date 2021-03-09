import vtk
import sys
import argparse
sys.path.append('D:\\vtk tests')

class class1():
    def __init__(self):
        super(class1,self).__init__()

   
    def function1(self):
        reader1=vtk.vtkSTLReader()

        #Reading STL file
        reader1.SetFileName('assignment.stl')
    
        mapper=vtk.vtkDataSetMapper()
        mapper.SetInputConnection(reader1.GetOutputPort())
        actor=vtk.vtkActor()
        actor.SetMapper(mapper)
        self.window=vtk.vtkRenderWindow()
        self.inter=vtk.vtkRenderWindowInteractor()
        self.renderer=vtk.vtkRenderer()

        colors=vtk.vtkNamedColors()
       
        #Declaring cutter,mapper,actor and plane for z-height=10.0
        #1st
                
        cutter1=vtk.vtkCutter()
        mapper1=vtk.vtkPolyDataMapper()
        actor1=vtk.vtkActor()
        plane1=vtk.vtkPlane()
        plane1.SetOrigin(0.0,10.0,0.0)
        plane1.SetNormal(0.0,1.0,0.0)

        #Inputting implicit plane function as z-height mentioned for sectioning
        cutter1.SetCutFunction(plane1)
        cutter1.SetInputConnection(reader1.GetOutputPort())
        mapper1.SetInputConnection(cutter1.GetOutputPort())
        actor1.SetMapper(mapper1)

        actor1.GetProperty().SetColor(colors.GetColor3d('Cyan'))
        actor1.GetProperty().SetAmbient(1.0)
        actor1.GetProperty().SetLineWidth(2)

        self.renderer.AddActor(actor1)

    

        #2nd
        #Declaring cutter,mapper,actor and plane for z-height=30.0

        cutter2=vtk.vtkCutter()
        mapper2=vtk.vtkPolyDataMapper()
        actor2=vtk.vtkActor()
        plane2=vtk.vtkPlane()
        plane2.SetOrigin(0.0,30.0,0.0)
        plane2.SetNormal(0.0,1.0,0.0)
        cutter2.SetCutFunction(plane2)
        cutter2.SetInputConnection(reader1.GetOutputPort())
        mapper2.SetInputConnection(cutter2.GetOutputPort())
        actor2.SetMapper(mapper2)

        actor2.GetProperty().SetColor(colors.GetColor3d('Red'))
        actor2.GetProperty().SetAmbient(1.0)
        actor2.GetProperty().SetLineWidth(2)

        self.renderer.AddActor(actor2)

        #3rd
        #Declaring cutter,mapper,actor and plane for z-height=50.0

                
        cutter3=vtk.vtkCutter()
        mapper3=vtk.vtkPolyDataMapper()
        actor3=vtk.vtkActor()
        plane3=vtk.vtkPlane()
        plane3.SetOrigin(0.0,50.0,0.0)
        plane3.SetNormal(0.0,1.0,0.0)
        cutter3.SetCutFunction(plane1)
        cutter3.SetInputConnection(reader1.GetOutputPort())
        mapper3.SetInputConnection(cutter3.GetOutputPort())
        actor3.SetMapper(mapper1)

        actor3.GetProperty().SetColor(colors.GetColor3d('Blue'))
        actor3.GetProperty().SetAmbient(1.0)
        actor3.GetProperty().SetLineWidth(2)

        self.renderer.AddActor(actor3)

        camera = vtk.vtkCamera()
        camera.SetPosition(200,200,200)

        self.actors=vtk.vtkActorCollection()
      
        #camera.SetFocalPoint(0,1.0, 0)

        self.style1=vtk.vtkInteractorStyleRubberBandPick()
        #self.style1.SetInteractor(self.inter)

                
        #Setting up camera for a tilted view
        
        self.renderer.SetActiveCamera(camera)
        
        style=vtk.vtkInteractorStyleTrackballCamera()
        self.inter.SetInteractorStyle(style)

        self.inter.AddObserver('OnMouseMove',self.callback)
        self.inter.AddObserver('LeftButtonPressEvent',self.callback)

        #Renderring objects into screen and initializing user interaction
        self.window.AddRenderer(self.renderer)
        self.window.SetSize(1000,1000)
        self.window.SetWindowName('Problem 1')

        
        self.inter.SetRenderWindow(self.window)

        
        self.inter.Initialize()
        self.window.Render()
       
        self.inter.Start()
    def callback(self):
        print('mouse')


if __name__=='__main__':
    c=class1()
    c.function1()

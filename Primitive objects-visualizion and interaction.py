import vtk
import sys
import argparse
sys.path.append('D:\\vtk tests')

class class1():
    def __init__(self):
        super(class1,self).__init__()

        self.function1()
   
    def function1(self):
        reader1=vtk.vtkSTLReader()
        #reader1=vtk.vtkOBJReader()
        reader1.SetFileName('assignment.stl')
        sphere=vtk.vtkSphereSource()
        sphere.SetRadius(5.0)
        cube=vtk.vtkCubeSource()
        cube.SetXLength(10.0)
        cube.SetYLength(10.0)
        cube.SetZLength(10.0)
        
        mapper=vtk.vtkDataSetMapper()
        mapper.SetInputConnection(reader1.GetOutputPort())
        actor=vtk.vtkActor()
        actor.SetMapper(mapper)
        self.window=vtk.vtkRenderWindow()
        self.inter=vtk.vtkRenderWindowInteractor()
        self.renderer=vtk.vtkRenderer()

        colors=vtk.vtkNamedColors()
        #User enters number of z-height inputs 
        n=int(input('enter number of inputs'))

        #Declaring dict objetcs for holding cutter collection,mappers collection,planes collection and actors collection
        
        l1=[]
        cutters={}
        planes={}
        mappers={}
        actors={}

        input('Press any key to exit')

        #For each z-height cutter,mapper,actor and plane are declared and stored in dict and is assigned for rendering
                #Rendering and Interaction initialization


        mapper1=vtk.vtkPolyDataMapper()
        mapper1.SetInputConnection(sphere.GetOutputPort())
        actor1=vtk.vtkActor()
        actor1.SetMapper(mapper1)

        mapper2=vtk.vtkPolyDataMapper()
        mapper2.SetInputConnection(cube.GetOutputPort())
        actor2=vtk.vtkActor()
        actor2.SetMapper(mapper1)

        
        self.renderer.AddActor(actor1)
        self.renderer.AddActor(actor2)
        
        self.window.AddRenderer(self.renderer)
        self.Window.SetSize(1000,1000)
        self.window.SetWindowName('Problem 2')
        
        self.inter.SetRenderWindow(self.window)

        self.window.Render()
       
      
        self.inter.Initialize()

        input('Press any key to exit')

if __name__=='__main__':
    c=class1()

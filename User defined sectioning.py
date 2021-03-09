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
        for i in range(n):
            l1.append(float(input()))
        for i in range(len(l1)):
            cutters[i]=vtk.vtkCutter()
            mappers[i]=vtk.vtkPolyDataMapper()
            actors[i]=vtk.vtkActor()
            planes[i]=vtk.vtkPlane()
            planes[i].SetOrigin(0.0,0.0,l1[i])
            planes[i].SetNormal(0.0,0.0,1.0)
            cutters[i].SetCutFunction(planes[i])
            cutters[i].SetInputConnection(reader1.GetOutputPort())
            mappers[i].SetInputConnection(cutters[i].GetOutputPort())
            actors[i].SetMapper(mappers[i])

            actors[i].GetProperty().SetColor(colors.GetColor3d('Yellow'))
            actors[i].GetProperty().SetAmbient(1.0)
            actors[i].GetProperty().SetLineWidth(2)

            self.renderer.AddActor(actors[i])

        #Rendering and Interaction initialization
        self.window.AddRenderer(self.renderer)
        self.Window.SetSize(1000,1000)
        self.window.SetWindowName('Problem 2')
        
        self.inter.SetRenderWindow(self.window)

        self.window.Render()
       
      
        self.inter.Initialize()

        input('Press any key to exit')

if __name__=='__main__':
    c=class1()

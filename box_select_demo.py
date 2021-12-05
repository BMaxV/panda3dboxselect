from direct.showbase.ShowBase import ShowBase
from panda3d.core import Geom, GeomTriangles, GeomLines
from panda3d.core import GeomVertexFormat, GeomVertexData, GeomVertexWriter
from panda3d.core import Texture, GeomNode

#from panda3d.core import render2d
#from direct.gui.DirectGui import render2d

class wrapper:
    def __init__(self):
        self.b=ShowBase()

def draw_shape_2d(shape=None):
    if shape==None:
        shape=()
    
    
    #prepare new interface object container
    tformat=GeomVertexFormat.getV3t2()
    #this is the format we'll be using.
    vdata = GeomVertexData('convexPoly', tformat, Geom.UHStatic)

    #these are access shortcuts
    vertex = GeomVertexWriter(vdata, 'vertex')
    uv = GeomVertexWriter(vdata, "texcoord")
    vdata.setNumRows(2)# define  number of points.
    poly = Geom(vdata)
    ci=0


    p1=[-0.8, 0, 0.5]
    
    p2=[-0.5, 0, 0.5]
        
    verts=[p1,p2]
    
    for p in verts:
        color_t=(255,255,0)
        vertex.addData3(p[0],p[1],p[2])
        uv.addData2(p[0],p[1])
    
    tris = GeomLines(Geom.UHStatic)
    #add index to geometry.
    tris.addVertices(ci,ci+1)
    tris.closePrimitive()
    
    poly.addPrimitive(tris)
    
    snode = GeomNode('Object1')
    snode.addGeom(poly)
    path=NodePath(snode)
    path.reparent_to(render2d)
    #text_obs.append(path)
    return path
    #this should do ti completely.
    
def demo_main():
    w=wrapper()
    draw_shape_2d([(0.1,0),(0.1,0.1),(0,0.1),(0,0)])
    
if __name__=="__main__":
    demo_main()
    

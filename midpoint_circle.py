from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *



def init():
   glClearColor(0.0,0.0,0.0,1.0)
   glColor3f(0.0,0.0,1.0)
   glPointSize(2.0)
   glMatrixMode(GL_PROJECTION)
   glLoadIdentity()
   gluOrtho2D(-100,100,-100,100)
   
def plot(x,y):
  glBegin(GL_POINTS)
  glVertex2i(x,y)
  glEnd()
  glFlush()
  
     
def mid ( xc , yc, r):
   x = r
   y = 0
   
   plot (x + xc, y + yc )
   
   if r > 0 :
    plot ( x + xc , -y + yc )
    plot ( y +xc , x + yc)
    plot ( y + xc , x + yc )
    plot ( -y + xc , x + yc )
   
   p = 1 - r
   while x > y :
    y = y + 1
    
    if p <= 0:
      p = p + 2 * y + 1
    else:
      x -= 1
      p = p + 2 * y - 2 * x + 1
       
    if  x < y:
      break
      
    plot ( x + xc, y + yc)
    plot ( -x + xc, y + yc)
    plot ( x + xc, -y + yc)
    plot (-x + xc, -y + yc)
      
    if x != y :
      plot (y + xc, x + yc)
      plot (-y + xc, x + yc)
      plot (y + xc, -x + yc)
      plot (-y + xc, -x + yc)
           
    
def Display():
  glClear(GL_COLOR_BUFFER_BIT)
  x=int(input('x coordinate: '))
  y=int(input ('y coordinate: '))
  r=int(input('radius: '))
  mid(x,y,r)
     
def main():
   glutInit()
   glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
   glutInitWindowSize(500,500)
   glutInitWindowPosition(200,200)
   glutCreateWindow("mid")
   glutDisplayFunc(Display)
   init()

   glutMainLoop()
 
main()
      
   
   
   

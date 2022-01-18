add_library('peasycam')


x = 0.01
y = 0
z = 0

sigma = 10
rho = 28
beta = 8.0 / 3

dt = 0.01

points = []
r = PI / 5
rotate = 0

def setup():
    size(800, 800, P3D)
    colorMode(HSB)
    cam = PeasyCam(this, 500)

def draw():
    global x, y, z, dt, rotate
    rotateY(rotate)
    rotate += r * dt
    
    frameRate(60)
    background(0)

    dx = (sigma * (y - x)) * dt 
    dy = (x * (rho - z) - y) * dt
    dz = (x * y - beta * z) * dt
    
    x += dx
    y += dy
    z += dz
    
    points.append((x, y, z))
    
    translate(0, 0, -80)
    scale(5)
   
    hue = 0
    noFill()
    beginShape()
    for px, py, pz in points:
        stroke(hue, 255, 255)
        # vertex(px + sin(x * px) * 0.1, py + sin(y * py) * 0.1, pz + sin(z * pz) * 0.1)
        vertex(px, py, pz)
        hue = (hue + 0.1) % 255
    endShape()
    
    # saveFrame("#######.tif")

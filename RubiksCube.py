from ursina import *
app=Ursina()
text1=Text(text="Seconds:",y=0.25)
pl=EditorCamera(position=(-0.081,3.1,-0.7),rotation=(33+1/3,44,0))
uER1=0
for x in range(2):
    for z in range(2):
        uER1+=1
        exec(f'b{uER1}=Entity(model="plane",color=color.blue,texture="rubix_cube",x=x,z=z)')
for xd in [0,1]:
    for yd in [-1.5,-0.5]:
        exec('Entity(model="plane",color=color.red,texture="rubix_cube",x=xd,y=yd,z=-0.5,rotation_x=90,rotation_y=180)')
for xp in [0,1]:
    for yp in [-1.5,-0.5]:
        exec('Entity(model="plane",color=color.orange,texture="rubix_cube",x=xp,y=yp,z=1.5,rotation_x=90)')
for xl in range(2):
    for zl in range(2):
        exec('Entity(model="plane",color=color.green,texture="rubix_cube",x=xl,z=zl,y=-2,rotation_z=180)')
uER=0
for zt in [0,1]:
    for yt in [-1.5,-0.5]:
        uER+=1
        exec(f'u{uER}=Entity(model="plane",color=color.yellow,texture="rubix_cube",x=-0.5,z=zt,y=yt,rotation_z=270)')

for zu in [0,1]:
    for yu in [-1.5,-0.5]:
        exec(f'Entity(model="plane",color=color.white,texture="rubix_cube",x=1.5,z=zu,y=yu,rotation_z=90)')

def left():
    kxb = scene.entities[-19].color
    kxt = scene.entities[-17].color
    scene.entities[-17].color = scene.entities[-1].color
    scene.entities[-19].color = scene.entities[-3].color#3
    scene.entities[-1].color = scene.entities[-15].color#13
    scene.entities[-3].color = scene.entities[-13].color#15
    scene.entities[-13].color = scene.entities[-5].color
    scene.entities[-15].color = scene.entities[-7].color
    scene.entities[-5].color = kxb
    scene.entities[-7].color = kxt
    pO1=b1.color
    b1.color = b3.color
    b3.color=b4.color
    b4.color=b2.color
    b2.color = pO1


#scene.entities[-13].color = color.azure

#scene.entities[-3].color=color.pink
def down():
    kzb=scene.entities[-19].color
    kzt=scene.entities[-20].color
    scene.entities[-19].color=scene.entities[-23].color
    scene.entities[-20].color=scene.entities[-24].color
    scene.entities[-23].color=scene.entities[-15].color
    scene.entities[-24].color=scene.entities[-16].color
    scene.entities[-15].color=scene.entities[-11].color
    scene.entities[-16].color=scene.entities[-12].color
    scene.entities[-11].color=kzb
    scene.entities[-12].color=kzt
    pOg=u1.color
    u1.color=u2.color
    u2.color=u4.color
    u4.color=u3.color
    u3.color=pOg
#scene.entities[-19].color=color.pink
#scene.entities[-7].color=color.gray
def generatePosition():
    e=["left()","left(),left(),left()","down()","down(),down(),down()"]
    for i in range(10):
        dg=e[random.randint(0,len(e)-1)]
        eval(dg)
        def qg():
            if dg == "left(),left(),left()":
                return "left"
            if dg=="left()":
                return "right"
            if dg=="down(),down(),down()":
                return "down"
            if dg=="down()":
                return "up"
        print(qg()) #<-: That's the step-by-step solution to solve it...
generatePosition()
timeIt=0
seconds=0
def update():
    global timeIt,seconds
    timeIt+=1
    if timeIt>=int(window.fps_counter.text):
        seconds+=1
        timeIt=0
    text1.text="Seconds: "+str(seconds)
def input(key):
    if key=="left arrow up":left()
    if key=="right arrow up":left();left();left()
    if key=="down arrow up":down()
    if key=="up arrow up":down();down();down()
app.run()

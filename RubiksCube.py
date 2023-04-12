from ursina import *
app=Ursina()
text1=Text(text="Seconds:",y=0.25)
pl=EditorCamera(position=(-0.081,3.1,-0.7),rotation=(33+1/3,44,0))
for x in range(2):
    for z in range(2):
        exec(f'k{x}{z}=Entity(model="plane",color=color.blue,texture="rubix_cube",x=x,z=z)')
for xd in [0,1]:
    for yd in [-1.5,-0.5]:
        exec(f'd{str(xd).replace("-","m").replace(".","c")}{str(yd).replace("-","m").replace(".","c")}=Entity(model="plane",color=color.red,texture="rubix_cube",x=xd,y=yd,z=-0.5,rotation_x=90,rotation_y=180)')
for xp in [0,1]:
    for yp in [-1.5,-0.5]:
        exec(f'p{str(xp).replace("-","m").replace(".","c")}{str(yp).replace("-","m").replace(".","c")}=Entity(model="plane",color=color.orange,texture="rubix_cube",x=xp,y=yp,z=1.5,rotation_x=90)')
for xl in range(2):
    for zl in range(2):
        exec(f'l{str(xl).replace("-","m").replace(".","c")}{str(zl).replace("-","m").replace(".","c")}=Entity(model="plane",color=color.green,texture="rubix_cube",x=xl,z=zl,y=-2,rotation_z=180)')
for zt in [0,1]:
    for yt in [-1.5,-0.5]:
        exec(f't{str(yt).replace("-", "m").replace(".", "c")}{str(zt).replace("-", "m").replace(".", "c")}=Entity(model="plane",color=color.yellow,texture="rubix_cube",x=-0.5,z=zt,y=yt,rotation_z=270)')
for zu in [0,1]:
    for yu in [-1.5,-0.5]:
        exec(f'u{str(yu).replace("-", "m").replace(".", "c")}{str(zu).replace("-", "m").replace(".", "c")}=Entity(model="plane",color=color.white,texture="rubix_cube",x=1.5,z=zu,y=yu,rotation_z=90)')
def left():
    kxb = scene.entities[-17].color
    kxt = scene.entities[-19].color
    scene.entities[-17].color = scene.entities[-1].color
    scene.entities[-19].color = scene.entities[-3].color
    scene.entities[-1].color = scene.entities[-13].color
    scene.entities[-3].color = scene.entities[-15].color
    scene.entities[-13].color = scene.entities[-5].color
    scene.entities[-15].color = scene.entities[-7].color
    scene.entities[-5].color = kxb
    scene.entities[-7].color = kxt
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
def generatePosition():
    cubeList=["green","orange","blue","yellow","white","red"]
    cubeDict={"green":4,"orange":4,"blue":4,"yellow":4,"white":4,"red":4}
    for entPlane in range(24):
        p=cubeList[random.randint(0,5)]
        while not cubeDict[p]<=0:
            exec(f"cubeDict['{p}']-=1")
            p=cubeList[random.randint(0,5)]
        scene.entities[-entPlane].color=eval(f"color.{p}")
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

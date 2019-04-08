from tkinter import *;
import time;
from Ball import Ball;
import PhysicsHelper as ph;
import random;

#GUI handler
tk = Tk();
tk.title("Collision Simulator");
tk.resizable(0,0);
tk.wm_attributes("-topmost", 1);
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0);
canvas.pack();
tk.update();



#ma = float(input("Mass of ball A:"));
#mb = float(input("Mass of ball B:"));
#xia =float(input("x velocity  of ball A:"));
#yia = float(input("y velocity  of ball A:"));
#xib =float(input("x velocity of ball B:"));
#yib = float(input("y velocity of ball B:"));

#Creates two spheres on screen
#sphere_a = Ball(canvas, 'red', 4, 4, 3, 245, 0);
#sphere_b = Ball(canvas, 'blue', 4, -4, 4, 245, 375);
#sphere_a.set_other(sphere_b);
#sphere_b.set_other(sphere_a);
#sphere_c = Ball(canvas, 'green', 4, 5, 4, 200, 0);
#sphere_a.is_inelastic_collision = False;
#sphere_b.is_inelastic_collision = False;
spheres = [];
stringpacks = [];
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange'];
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
for x in range(1,3):
    ball = None;

    ball = Ball(canvas, colors[x%len(colors)], 3, random.randint(1,7), random.randint(1,10), 245, random.randint(100,200));
    ball.set_id(letters[x-1:x]);
    spheres.append(ball);
    stringvar = StringVar();
    Label(tk, textvariable=stringvar).pack();
    stringpacks.append(stringvar);
for sphere in spheres:
    print(sphere.get_mass());
totals = StringVar();
Label(tk, textvariable=totals).pack();
#display = Label(tk, text="")
#v = StringVar();
#Label(tk, textvariable=v).pack()
#z = StringVar();
#Label(tk, textvariable=z).pack();
def main():

    while True:
        for sphere in spheres:
            sphere.draw();
        collides = ph.collide_detector(spheres, canvas);
        if(collides != None):
            ph.elastic_collision(collides[0], collides[1]);
       
        for x in range(0, len(spheres)):
            stringpacks[x].set(spheres[x]);


        tk.update_idletasks();
        tk.update();


        time.sleep(0.01);


main();
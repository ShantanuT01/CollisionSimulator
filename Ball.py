from tkinter import *;
import random;
import time;
import PhysicsHelper as Math;
import math;
class Ball:
    def __init__(self, canvas, color, xv, yv, mass, x, y):
        self.canvas = canvas;
        self.hasNotCollided = True;
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color);
        self.canvas.move(self.id, x, y);
        self.mass = mass;
        self.x_velocity = xv;
        self.y_velocity = yv;
        self.canvasHeight = self.canvas.winfo_height();
        self.canvasWidth = self.canvas.winfo_width();
        self.is_inelastic_collision = False;
    def draw(self):

        self.canvas.move(self.id, self.x_velocity, self.y_velocity);
        pos = self.canvas.coords(self.id);
        # y direction
        if (pos[1] < 11):
            self.y_velocity = -1 * self.y_velocity;

        if (pos[3] > self.canvasHeight-11):
            self.y_velocity = -1 * self.y_velocity;





        # x direction
        if (pos[0] < 11):
            self.x_velocity = -1 * self.x_velocity;

        if (pos[2] > self.canvasWidth-11):
            self.x_velocity = -1 * self.x_velocity;



    def hitBall(self):
        pos = self.canvas.coords(self.id);
        otherPos = self.canvas.coords(self.other.id);
        if (pos[2] >= otherPos[0] and pos[0] <= otherPos[2]):
            if (pos[3] >= otherPos[1] and pos[3] <= otherPos[3]):
                return True;
        return False;

    def set_other(self, other):
        self.other = other;

    def set_mass(self, mass):
        old_mass = self.mass;
        self.mass = mass;
        return old_mass;
    def get_mass(self):
        return self.mass;
    def get_x_velocity(self):
        return self.x_velocity;
    def get_y_velocity(self):
        return self.y_velocity;
    def set_x_velocity(self, x):
        self.x_velocity = x;
    def set_y_velocity(self, y):
        self.y_velocity = y;
    def set_velocity(self, x,y):
        self.set_x_velocity(x);
        self.set_y_velocity(y);
    def get_velocity(self):

        return math.hypot(self.x_velocity, self.y_velocity);

    def get_momentum(self):
        return self.mass * self.get_velocity();
    def __str__(self):
        return "Speed of " + self.name + ": " + str(round(self.get_velocity(), 3)) + " m/s, (" + str(self.get_x_velocity()) +","+ str(self.get_y_velocity()) + ")";
    def set_id(self, string):
        self.name = string;

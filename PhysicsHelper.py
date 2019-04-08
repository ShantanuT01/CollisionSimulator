
def elastic_collision(o1, o2):
    print(find_y_momentum(o1) + find_y_momentum(o2));
    v1fx = (subtract_masses(o1, o2))/(add_masses(o1,o2)) * o1.get_x_velocity() + (2*o2.get_mass())/(add_masses(o1,o2)) * o2.get_x_velocity();
    v2fx = (2*o1.get_mass())/(add_masses(o1,o2)) * o1.get_x_velocity() + (subtract_masses(o2,o1))/(add_masses(o1,o2)) * o2.get_x_velocity();
    v1fy = (subtract_masses(o1, o2)) / (add_masses(o1, o2)) * o1.get_y_velocity() + (2 * o2.get_mass()) / (add_masses(o1, o2)) * o2.get_y_velocity();
    v2fy = (2 * o1.get_mass()) / (add_masses(o1, o2)) * o1.get_y_velocity() + (subtract_masses(o2, o1)) / (add_masses(o1, o2)) * o2.get_y_velocity();
    o1.set_velocity(v1fx,v1fy);
    o2.set_velocity(v2fx, v2fy);
    print(find_y_momentum(o1) + find_y_momentum(o2));
def inelastic_collision(a,b):

    x = (find_x_momentum(a) + find_x_momentum(b))/(a.get_mass() + b.get_mass());
    y = (find_y_momentum(a) + find_y_momentum(b))/(a.get_mass() + b.get_mass());
    a.set_velocity(x,y)
    b.set_velocity(x,y);
def if_collide(a, b,canvas):

    ac = canvas.coords(a.id);
    bc = canvas.coords(b.id)
    if (ac[2] >= bc[0] and ac[0] <= bc[2]):
        if (ac[3] >= bc[1] and ac[3] <= bc[3]):
            return True;
    return False;

def find_x_momentum(a):
    return a.get_mass() * a.get_x_velocity();
def find_y_momentum(a):
    return a.get_mass() * a.get_y_velocity();
def add_masses(o1, o2):
    return o1.get_mass() + o2.get_mass();
def subtract_masses(o1, o2):
    return o1.get_mass()-o2.get_mass();
def collide_detector(objects,canvas):

    for i in range(0, len(objects)):
        for j in range(0, len(objects)):
            if i == j:
                continue;
            else:
                bool = if_collide(objects[i], objects[j], canvas);
                if(bool):
                    return [objects[i], objects[j]];
    return None;

def createList(list):
    ret = list();
    for i in range(0, len(list)):
        for j in range(0, len(list)):
            if(i!=j):
                temp = [list[i], list[j]];
                ret.append(temp);

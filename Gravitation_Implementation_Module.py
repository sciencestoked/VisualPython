# Defining Gravitation Simulation Function
from vpython import *
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import display


def gforce(s, e):
    val = s.wt * e.wt / (((s.pos - e.pos).mag) ** 3)
    return val * (e.pos - s.pos)


def Gravitation_Implementation(objlist):

    t = 0
    dt = 0.01
    total_runtime = 100
    all_time_matrix = []

    while t < total_runtime:
        rate(1000)
        t += dt

        all_objs_mat = []

        for curr_obj_id in range(len(objlist)):

            current_obj = objlist[curr_obj_id]
            current_obj.pos += current_obj.vel * dt

            for second_obj_id in range(len(objlist)):

                if second_obj_id != curr_obj_id:

                    second_obj = objlist[second_obj_id]

                    current_obj.vel += dt * (
                        (gforce(current_obj, second_obj)) / current_obj.wt
                    )

            currmat = []
            currmat.append(current_obj.pos.x)
            currmat.append(current_obj.pos.y)
            currmat.append(current_obj.pos.z)
            all_objs_mat.append(currmat)

        all_time_matrix.append(all_objs_mat)

        # Show Percent Completion of simulation
        print(f"Simulation { int(1000*t/total_runtime)/10 } % completed . . .")

        # bool done = False

    return all_time_matrix


# sun = sphere(radius=0.5, color=color.yellow, wt=100,pos=vector(0,0,0), vel=vector(0,0,0) )
# earth = sphere(radius=0.5, color=color.cyan, wt=10,pos=vector(10,0,0), vel=vector(0,2,0) )
# moon = sphere(radius=0.3, color=color.white, wt=1,pos=vector(14,0,0), vel=vector(0,-2,1) )

# matrx =[sun,earth,moon]

matrx = []

colormat = [color.white, color.yellow, color.cyan, color.green, color.red]

for i in range(5):
    matrx.append(
        sphere(
            radius=0.5,
            color=colormat[i],
            wt=100 / (i + 1),
            pos=vector(0, 5 * i, 5 * i),
            vel=vector(i, 0, 0),
        )
    )

ans = np.array(Gravitation_Implementation(matrx))

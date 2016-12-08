import math
import random

def generate_simple_pair(n_elements_per_set):

    radius = 1.0

    x0 = -0.375
    y0 = -0.1

    x1 = 0.375
    y1 = 0.1

    set_0 = []
    set_1 = []

    for i in range(0, n_elements_per_set):

        theta = random.random() * math.pi
        radius_local = (radius/2.0) * (random.random() + 1.0)

        x = x0 + math.cos(theta)*radius_local
        y = y0 + math.sin(theta)*radius_local

        set_0.append([x, y])

    for i in range(0, n_elements_per_set):

        theta = random.random() * math.pi
        radius_local = (radius/2.0) * (random.random() + 1.0)

        x = x1 + math.cos(theta)*radius_local
        y = y1 - math.sin(theta)*radius_local

        set_1.append([x, y])

    return [set_0, set_1]

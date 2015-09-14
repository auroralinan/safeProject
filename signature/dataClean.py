__author__ = 'Administrator'
# -*- coding: utf-8 -*-

import math

def speed(o, args):
    v = []
    if args == 4 or args == 5:
        for i in range(0,len(o)):
            if o[i][8] == "DOWN" or o[i][8] == "UP":
                v += [0.0]
            else:
                sss = (abs(o[i][args] - o[i-1][args]) + abs(o[i+1][args] - o[i][args]))/float(o[i+1][3]-o[i-1][3])
                v += [sss]
    else:
        for i in range(0,len(o)):
            if o[i][8] == "DOWN" or o[i][8] == "UP":
                v += [0.0]
            else:
                sss = math.sqrt(pow(abs(o[i][4] - o[i-1][4]),2) + pow(abs(o[i+1][4] - o[i][4]),2)) + math.sqrt(pow(abs(o[i][5] - o[i-1][5]),2) + pow(abs(o[i+1][5] - o[i][5]),2))/float(o[i+1][3]-o[i-1][3])
                v += [sss]
    return v

def acceleration(o, v):
    a = []
    for i in range(0,len(o)):
        if o[i][8] == "DOWN" or o[i][8] == "UP" or o[i-1][8] == "DOWN" or o[i-1][8] == "UP" or o[i+1][8] == "DOWN" or o[i+1][8] == "UP":
            a += [9999.9]
        else:
            aaa = (v[i+1] - v[i-1])/float(o[i+1][3]-o[i-1][3])
            a += [aaa]
    return a

def average(av):
    s = sum(av)
    l = len(av)
    avg = s/l
    return avg

def calc_data(o):

    features = []

    pressure = []
    for p in o:
        pressure += [p[6]]

    size = []
    for p in o:
        size += [p[7]]

    x = []
    for p in o:
        x += [p[4]]

    y = []
    for p in o:
        y += [p[5]]

#calc speed
    v_x = speed(o, 4)
    v_y = speed(o, 5)
    v = speed(o, 6)

#calc acceleration
    a_x = acceleration(o, v_x)
    a_y = acceleration(o, v_y)
    a = acceleration(o, v)


#break times
    break_times = 0
    for p in o:
        if p[8] == "UP":
            break_times += 1

#total_time
    total_time = o[-1][3] - o[0][3]
    total_time = int(total_time)
#total_point
    total_point = len(o)

#maximum and minimun features and position
    #calc maximum_speed_whole
    maximum_speed_whole = max(v)
    maximum_speed_whole_po = (o[v.index(maximum_speed_whole)][3] - o[0][3])/float(total_time)


    #calc maximum_speed_x
    maximum_speed_x = max(v_x)
    maximum_speed_x_po = (o[v_x.index(maximum_speed_x)][3] - o[0][3])/float(total_time)

    #calc maximum_speed_y
    maximum_speed_y = max(v_y)
    maximum_speed_y_po = (o[v_y.index(maximum_speed_y)][3] - o[0][3])/float(total_time)

    #calc minimum_speed_whole
    minimum_speed_whole = 9999.9
    for i in v:
        if i != 0.0 and i < minimum_speed_whole:
            minimum_speed_whole = i
    minimum_speed_whole_po = (o[v.index(minimum_speed_whole)][3] - o[0][3])/float(total_time)

    #calc minimum_speed_x
    minimum_speed_x = 9999.9
    for i in v_x:
        if i != 0.0 and i < minimum_speed_x:
            minimum_speed_x = i
    minimum_speed_x_po = (o[v_x.index(minimum_speed_x)][3] - o[0][3])/float(total_time)

    #calc minimum_speed_y
    minimum_speed_y = 9999.9
    for i in v_y:
        if i != 0.0 and i < minimum_speed_y:
            minimum_speed_y = i
    minimum_speed_y_po = (o[v_y.index(minimum_speed_y)][3] - o[0][3])/float(total_time)

    #calc maximum_acceleration_whole
    maximum_acceleration = -9999.9
    for i in a:
        if i > maximum_acceleration and i != 9999.9:
            maximum_acceleration = i
    maximum_acceleration_po = (o[a.index(maximum_acceleration)][3] - o[0][3])/float(total_time)

    #calc maximum_acceleration_x
    maximum_acceleration_x = -9999.9
    for i in a_x:
        if i > maximum_acceleration_x and i != 9999.9:
            maximum_acceleration_x = i
    maximum_acceleration_x_po = (o[a_x.index(maximum_acceleration_x)][3] - o[0][3])/float(total_time)

    #calc maximum_acceleration_y
    maximum_acceleration_y = -9999.9
    for i in a_y:
        if i > maximum_acceleration_y and i != 9999.9:
            maximum_acceleration_y = i
    maximum_acceleration_y_po = (o[a_y.index(maximum_acceleration_y)][3] - o[0][3])/float(total_time)

    #calc minimum_acceleration_whole
    minimum_acceleration = 9999.9
    for i in a:
        if i < minimum_acceleration:
            minimum_acceleration = i
    minimum_acceleration_po = (o[a.index(minimum_acceleration)][3] - o[0][3])/float(total_time)

    #calc minimum_acceleration_x
    minimum_acceleration_x = 9999.9
    for i in a_x:
        if i < minimum_acceleration_x:
            minimum_acceleration_x = i
    minimum_acceleration_x_po = (o[a_x.index(minimum_acceleration_x)][3] - o[0][3])/float(total_time)

    #calc minimum_acceleration_y
    minimum_acceleration_y = 9999.9
    for i in a_y:
        if i < minimum_acceleration_y:
            minimum_acceleration_y = i
    minimum_acceleration_y_po = (o[a_y.index(minimum_acceleration_y)][3] - o[0][3])/float(total_time)

    #calc maximum_pressure
    maximum_p = max(pressure)
    maximum_p_position = (o[pressure.index(maximum_p)][3] - o[0][3])/float(total_time)

    #calc maximum_size
    maximum_s = max(size)
    maximum_s_position = (o[size.index(maximum_s)][3] - o[0][3])/float(total_time)

    #calc minimum_pressure
    minimum_p = min(pressure)
    minimum_p_position = (o[pressure.index(minimum_p)][3] - o[0][3])/float(total_time)

    #calc minimum_size
    minimum_s = min(size)
    minimum_s_position = (o[size.index(minimum_s)][3] - o[0][3])/float(total_time)

    #calc maximum_x
    maximum_x = max(x)
    maximum_x_position = (o[x.index(maximum_x)][3] - o[0][3])/float(total_time)

    #calc maximum_y
    maximum_y = max(y)
    maximum_y_position = (o[y.index(maximum_y)][3] - o[0][3])/float(total_time)

    #calc minimum_x
    minimum_x = min(x)
    minimum_x_position = (o[x.index(minimum_x)][3] - o[0][3])/float(total_time)

    #calc minimum_y
    minimum_y = min(y)
    minimum_y_position = (o[y.index(minimum_y)][3] - o[0][3])/float(total_time)


#average
    #calc average_speed_whole
    average_speed = average(v)

    #calc average_speed_x
    average_speed_x = average(v_x)

    #calc average_speed_y
    average_speed_y = average(v_y)

    #calc average_acceleration_whole
    s = 0.0
    l = 0
    for i in a:
        if i != 9999.9:
            s += i
            l += 1
    average_acceleration = s/l

    #calc average_acceleration_x
    s = 0.0
    l = 0
    for i in a_x:
        if i != 9999.9:
            s += i
            l += 1
    average_acceleration_x = s/l

    #calc average_acceleration_y
    s = 0.0
    l = 0
    for i in a_y:
        if i != 9999.9:
            s += i
            l += 1
    average_acceleration_y = s/l

    #calc average_pressure
    average_p = average(pressure)

    #calc average_size
    average_s = average(size)

    #calc average_coordination_x
    average_x = average(x)

    #calc average_coordination_y
    average_y = average(y)

#whole distance of move
    #whole distance of move x
    whole_distance_x = 0.0
    for i in range(0,len(o)-1):
        whole_distance_x += abs(x[i+1] - x[i])

    #whole distance of move y
    whole_distance_y = 0.0
    for i in range(0,len(o)-1):
        whole_distance_y += abs(y[i+1] - y[i])

    #whole distance of move whole
    whole_distance = 0.0
    for i in range(0,len(o)-1):
        whole_distance += math.sqrt(pow(x[i+1]-x[i], 2) + pow(y[i+1]-y[i], 2))
#size of whole signature
    size_of_signature = (maximum_x - minimum_x) * (maximum_y - minimum_y)

    #3
    features += [break_times]
    features += [total_time]
    features += [total_point]
    #12
    features += [maximum_speed_whole]
    features += [maximum_speed_whole_po]
    features += [maximum_speed_x]
    features += [maximum_speed_x_po]
    features += [maximum_speed_y]
    features += [maximum_speed_y_po]
    features += [minimum_speed_whole]
    features += [minimum_speed_whole_po]
    features += [minimum_speed_x]
    features += [minimum_speed_x_po]
    features += [minimum_speed_y]
    features += [minimum_speed_y_po]
    #12
    features += [maximum_acceleration]
    features += [maximum_acceleration_po]
    features += [maximum_acceleration_x]
    features += [maximum_acceleration_x_po]
    features += [maximum_acceleration_y]
    features += [maximum_acceleration_y_po]
    features += [minimum_acceleration]
    features += [minimum_acceleration_po]
    features += [minimum_acceleration_x]
    features += [minimum_acceleration_x_po]
    features += [minimum_acceleration_y]
    features += [minimum_acceleration_y_po]
    #16
    features += [maximum_p]
    features += [maximum_p_position]
    features += [maximum_s]
    features += [maximum_s_position]
    features += [maximum_x]
    features += [maximum_x_position]
    features += [maximum_y]
    features += [maximum_y_position]
    features += [minimum_p]
    features += [minimum_p_position]
    features += [minimum_s]
    features += [minimum_s_position]
    features += [minimum_x]
    features += [minimum_x_position]
    features += [minimum_y]
    features += [minimum_y_position]
    #10
    features += [average_speed]
    features += [average_speed_x]
    features += [average_speed_y]
    features += [average_acceleration]
    features += [average_acceleration_x]
    features += [average_acceleration_y]
    features += [average_p]
    features += [average_s]
    features += [average_x]
    features += [average_y]
    #4
    features += [whole_distance]
    features += [whole_distance_x]
    features += [whole_distance_y]
    features += [size_of_signature]

    return features

from brian2 import *
import matplotlib.pyplot as plt
import numpy as np
import time
import sys
import json
import random

start = time.time()
print("START!!")

prefs.codegen.target = 'cython'
f = open("para_070111.json")
current_seed = random.randint(0,10000)
seed(current_seed)
paras = json.load(f)

#####input#######
def inputgoal(goalangle):
    inp_g = goalangle%361

    goal_angle = [15,45,75,105,135,165,195,225,255,285,315,345]

    goaln1 = 1999
    goaln2 = 1999


    #####goal#####
    for k in range(0,11):
        if inp_g == goal_angle[k]:
            goaln1 = k
            if k==11:
                goaln2 = 0
            elif k==0:
                goaln2=1

            else:
                goaln2 = k+1
            break
        if inp_g == 345:
            goaln1=11
            break
        if inp_g > 345 or inp_g <15:
            goaln1 = 11
            goaln2 = 0
            break
        if inp_g > goal_angle[k] and inp_g < goal_angle[k+1] :
            goaln1 = k
            goaln2 = k+1
            goaln3 = k-1
            break


    ratio_g = 0

    if inp_g < 15:
        ratio_g = (inp_g+15)/30
    elif inp_g > 345:
        ratio_g = (360-inp_g+15)/30
        ratio_g = 1-ratio_g
    elif goaln2 == 1999:
        ratio_g = 0
        goaln2 = goaln1
    else:
        ratio_g = (inp_g-goal_angle[goaln1])/30


    gIn1 = 1*(1-ratio_g)
    gIn2 = 1*ratio_g

    return goaln1,goaln2,gIn1,gIn2



def inputhead(headangle):

    inp_h = headangle%361
    head_angle = [337.5,22.5,67.5,112.5,157.5,202.5,247.5,292.5]

    headn1 = 1999
    headn2 = 1999
    #####head#####
    for k in range(1,7):
        if inp_h == head_angle[k]:
            headn1 = inp_h
            break
        if inp_h > 337.5 or inp_h < 22.5:
            headn1 = 0
            headn2 = 1
            break
        if inp_h > 292.5 and inp_h <337.5:
            headn1 = 7
            headn2 = 0
            break
        if inp_h > head_angle[k] and inp_h < head_angle[k+1] :
            headn1 = k
            headn2 = k+1
            break

    ratio_h = 0

    if inp_h < 22.5:
        ratio_h = (22.5+inp_h)/45
    elif inp_h > 337.5:
        ratio_h = (360-inp_h+22.5)/45
        ratio_h = 1-ratio_h
    elif headn2 == 1999:
        ratio_h = 0
        headn2 = headn1
    else:
        ratio_h = (inp_h-head_angle[headn1])/45


    hIn1 = 1*(1-ratio_h)
    hIn2 = 1*ratio_h
    
    return headn1,headn2,hIn1,hIn2



#########Neuron Group#########
# @title Firing rate model with sigmoid activation function
start_scope()  # This is to start a new session so that the networks 
               # defined in the cells above will not be simulated. 
n = 24

a=22.09*Hz
b=2.33
c=-0.52
d=0.67

S1_10 = paras["activation_funcs"][0]["S1_10"]
S2_10 = paras["activation_funcs"][0]["S2_10"]
S1_14 = paras["activation_funcs"][1]["S1_14"]
S2_14 = paras["activation_funcs"][1]["S2_14"]
S1_18 = paras["activation_funcs"][2]["S1_18"]
S2_18 = paras["activation_funcs"][2]["S2_18"]
S1_40 = paras["activation_funcs"][3]["S1_40"]
S2_40 = paras["activation_funcs"][3]["S2_40"]
S1_46 = paras["activation_funcs"][4]["S1_46"]
S2_46 = paras["activation_funcs"][4]["S2_46"]
S1_121 = paras["activation_funcs"][5]["S1_121"]
S2_121 = paras["activation_funcs"][5]["S2_121"]
S1_dn1 = paras["activation_funcs"][6]["S1_dn1"]
S2_dn1 = paras["activation_funcs"][6]["S2_dn1"]
S1_dn2 = paras["activation_funcs"][7]["S1_dn2"]
S2_dn2 = paras["activation_funcs"][7]["S2_dn2"]
S1_dn3 = paras["activation_funcs"][8]["S1_dn3"]
S2_dn3 = paras["activation_funcs"][8]["S2_dn3"]
S1_dn4 = paras["activation_funcs"][9]["S1_dn4"]
S2_dn4 = paras["activation_funcs"][9]["S2_dn4"]
S1_dn13 = paras["activation_funcs"][10]["S1_dn13"]
S2_dn13 = paras["activation_funcs"][10]["S2_dn13"]
S1_73 = paras["activation_funcs"][11]["S1_73"]
S2_73 = paras["activation_funcs"][11]["S2_73"]
S1_141 = paras["activation_funcs"][12]["S1_141"]
S2_141 = paras["activation_funcs"][12]["S2_141"]
S1_122 = paras["activation_funcs"][13]["S1_122"]
S2_122 = paras["activation_funcs"][13]["S2_122"]
S1_126 = paras["activation_funcs"][14]["S1_126"]
S2_126 = paras["activation_funcs"][14]["S2_126"]
S1_17 = paras["activation_funcs"][15]["S1_17"]
S2_17 = paras["activation_funcs"][15]["S2_17"]
S1_153 = paras["activation_funcs"][16]["S1_153"]
S2_153 = paras["activation_funcs"][16]["S2_153"]

sigma = 0.03

#PFL3
PFL3 = NeuronGroup(n,'''
dr/dt = (- r+ Iin)/tau + a*log(1 + exp(b*(Ihead + d*IFC2+c))) +sigma*sqrt(2/tau)*xi : 1
IFC2 : 1 # input from FC2
Ihead : 1 #input from delta7/EPG
Iin : 1
tau : second # time constant of the neuron
H:1
G:1
''',threshold='r<0',reset='r=0', method='euler')

PFL3.r = 0.0
PFL3.IFC2 = 0.0
PFL3.tau = 10*ms
PFL3.Iin = 0.0

PFL2 = NeuronGroup(12, '''
dr/dt=(- r+ Iin)/tau + (1/(1 + exp(-s1*(Ihead_2 + IFC2-s2))))/tau +sigma*sqrt(2/tau)*xi: 1
IFC2 : 1 # input from FC2
Ihead_2 : 1 #input from delta7/EPG
Iin : 1
s1: 1
s2: 1
H: 1
G: 1
tau : second # time constant of the neuron
''', threshold='r<0',reset='r=0', method='euler')
PFL2.r = 0.0
PFL2.IFC2 = 0.0
PFL2.tau = 10*ms
PFL2.Iin = 0.0
PFL2.s1 = 2.5
PFL2.s2 = 2


FC2 = NeuronGroup(12,'''
dr/dt = (-r + I_FC2 + Iin)/tau : 1
tau : second
I_FC2 : 1
Iin : 1
''',threshold='r<0',reset='r=0', method='exact')

FC2.r = 0.0
FC2.tau = 10*ms
FC2.Iin = 0.0

headinput = NeuronGroup(16,'''
dr/dt = (-r +Iin+(Iin_1+Iin_2)/2)/tau : 1
tau : second
Iin : 1
Iin_1 : 1
Iin_2 : 1
''',threshold='r<0',reset='r=0', method='exact')

headinput.r = 0.0
headinput.tau = 10*ms
headinput.Iin = 0.0
headinput.Iin_1 = 0.0
headinput.Iin_2 = 0.0

# LAL
LAL010 = NeuronGroup(2,'''
dr/dt = -r/tau + (1/(1+exp(-s1 * ((I_pfl3 + I_pfl2 + I_lal + I)-s2))))/tau: 1
tau : second
s1: 1
s2: 1
I: 1
I_pfl3 : 1
I_pfl2 : 1
I_lal = I_lal014 + I_lal040 + I_lal121 + I_lal141 + I_dn3: 1
I_lal014: 1
I_lal141 = I_lal14110: 1
I_lal14110: 1
I_lal040 = I_lal4010_RL + I_lal4010_LR + I_lal4010_RR + I_lal4010_LL: 1
I_lal4010_RL: 1
I_lal4010_LR: 1
I_lal4010_RR: 1
I_lal4010_LL: 1
I_lal121 = I_lal12110_LR + I_lal12110_RL: 1
I_lal12110_RL: 1
I_lal12110_LR: 1
I_dn3 = I_dn3lal10: 1
I_dn3lal10: 1
''',threshold='r<0',reset='r=0', method='euler')

LAL010.r = 0.0
LAL010.tau = 10*ms
LAL010.s1 = S1_10
LAL010.s2 = S2_10
LAL010.I = 0
LAL010.I_pfl3 = 0.0
LAL010.I_pfl2 = 0.0
LAL010.I_lal014 = 0.0
LAL010.I_lal4010_RL = 0.0
LAL010.I_lal4010_LR = 0.0
LAL010.I_lal4010_RR = 0.0
LAL010.I_lal4010_LL = 0.0
LAL010.I_lal12110_RL = 0.0
LAL010.I_lal12110_LR = 0.0
LAL010.I_lal14110 = 0.0
LAL010.I_dn3lal10 = 0.0

LAL014 = NeuronGroup(2,'''
dr/dt = -r/tau + (1/(1+exp(-s1 * (((I_pfl3 + I_pfl2 + I_lal + I))-s2))))/tau : 1
tau : second
s1: 1
s2: 1
I: 1
I_pfl3 : 1
I_pfl2 : 1
I_lal = I_lal010 + I_lal040 + I_lal121 + I_lal122 + I_lal153 + I_dn3: 1
I_lal010 = I_lal1014_RR + I_lal1014_LL: 1
I_lal1014_RR: 1
I_lal1014_LL: 1
I_lal040 = I_lal4014_RL + I_lal4014_LR: 1
I_lal4014_RL: 1
I_lal4014_LR: 1
I_lal121 = I_lal12114_RL + I_lal12114_LR: 1
I_lal12114_RL: 1
I_lal12114_LR: 1
I_lal122 = I_lal12214: 1
I_lal12214: 1
I_lal153 = I_lal15314: 1
I_lal15314: 1
I_dn3 = I_dn3lal14: 1
I_dn3lal14: 1
''',threshold='r<0',reset='r=0', method='euler')

LAL014.r = 0.0
LAL014.tau = 10*ms
LAL014.s1 = S1_14
LAL014.s2 = S2_14
LAL014.I = 0.0
LAL014.I_pfl3 = 0.0
LAL014.I_pfl2 = 0.0
LAL014.I_lal1014_RR = 0.0
LAL014.I_lal1014_LL = 0.0
LAL014.I_lal4014_RL = 0.0
LAL014.I_lal4014_LR = 0.0
LAL014.I_lal12114_RL = 0.0
LAL014.I_lal12114_LR = 0.0
LAL014.I_lal12214 = 0.0
LAL014.I_lal15314 = 0.0
LAL014.I_dn3lal14 = 0.0

LAL018 = NeuronGroup(2,'''
dr/dt = -r/tau + (1/(1+exp(-s1 * (((I_pfl3 + I_lal + I))-s2))))/tau : 1
tau : second
s1: 1
s2: 1
I: 1
I_pfl3 : 1
I_lal = I_lal010 + I_lal1418_RR + I_lal040 + I_lal046 + I_lal141 + I_lal126 + I_lal153 + I_dn3 + I_dn2: 1
I_lal141 = I_lal14118: 1
I_lal14118: 1
I_lal010 = I_lal1018_RR + I_lal1018_LL: 1
I_lal1018_RR: 1
I_lal1018_LL: 1
I_lal1418_RR: 1
I_lal040 = I_lal4018_RL + I_lal4018_LR: 1
I_lal4018_RL: 1
I_lal4018_LR: 1
I_lal046 = I_lal4618_RR + I_lal4618_LL: 1
I_lal4618_RR: 1
I_lal4618_LL: 1
I_lal126 = I_lal12618: 1
I_lal12618: 1
I_lal153 = I_lal15318: 1
I_lal15318: 1
I_dn3 = I_dn3lal18: 1
I_dn3lal18: 1 
I_dn2 = I_dn2lal18: 1
I_dn2lal18: 1
''',threshold='r<0',reset='r=0', method='euler')

LAL018.r = 0.0
LAL018.tau = 10*ms
LAL018.s1 = S1_18
LAL018.s2 = S2_18
LAL018.I = 0.0
LAL018.I_pfl3 = 0.0
LAL018.I_lal1018_RR = 0.0
LAL018.I_lal1018_LL = 0.0
LAL018.I_lal1418_RR = 0.0
LAL018.I_lal4018_RL = 0.0
LAL018.I_lal4018_LR = 0.0
LAL018.I_lal4618_LL = 0.0
LAL018.I_lal4618_RR = 0.0
LAL018.I_lal14118 = 0.0
LAL018.I_lal12618 = 0.0
LAL018.I_lal15318 = 0.0 
LAL018.I_dn3lal18 = 0.0 
LAL018.I_dn2lal18 = 0.0 

LAL040 = NeuronGroup(2,'''
dr/dt = -r/tau + (1/(1+exp(-s1 * (((I_pfl3 + I_lal + I))-s2))))/tau : 1
tau : second
s1: 1
s2: 1
I: 1
I_pfl3 : 1
I_lal = I_lal010 + I_lal073 + I_lal141: 1
I_lal141 = I_lal14140: 1
I_lal14140: 1
I_lal073 = I_lal7340:1 
I_lal7340:1 
I_lal010 = I_lal1040_RR + I_lal1040_LL: 1
I_lal1040_RR: 1
I_lal1040_LL: 1
''',threshold='r<0',reset='r=0', method='euler')

LAL040.r = 0.0
LAL040.tau = 10*ms
LAL040.s1 = S1_40
LAL040.s2 = S2_40
LAL040.I = 0.0
LAL040.I_pfl3 = 0.0
LAL040.I_lal1040_RR = 0.0
LAL040.I_lal1040_LL = 0.0
LAL040.I_lal7340 = 0.0
LAL040.I_lal14140 = 0.0

LAL046 = NeuronGroup(2,'''
dr/dt = -r/tau + (1/(1+exp(-s1 * (((I_pfl3 + I_pfl2 + I_lal + I))-s2))))/tau : 1
tau : second
s1: 1
s2: 1
I: 1
I_pfl3 : 1
I_pfl2 : 1
I_lal = I_lal010 + I_lal018 + I_lal040 + I_lal121 + I_lal126 + I_dn3 + I_dn2: 1
I_lal010 = I_lal1046_RR + I_lal1046_LL: 1
I_lal1046_RR: 1
I_lal1046_LL: 1
I_lal018 = I_lal1846_RR + I_lal1846_LL: 1
I_lal1846_RR: 1
I_lal1846_LL: 1
I_lal040 = I_lal4046_RL + I_lal4046_LR: 1
I_lal4046_RL: 1
I_lal4046_LR: 1
I_lal121 = I_lal12146_RL + I_lal12146_LR: 1
I_lal12146_RL: 1
I_lal12146_LR: 1
I_lal126 = I_lal12646: 1
I_lal12646: 1
I_dn3 = I_dn3lal46: 1
I_dn3lal46: 1
I_dn2 = I_dn2lal46: 1
I_dn2lal46: 1
''',threshold='r<0',reset='r=0', method='euler')

LAL046.r = 0.0
LAL046.tau = 10*ms
LAL046.s1 = S1_46
LAL046.s2 = S2_46
LAL046.I = 0.0
LAL046.I_pfl3 = 0.0
LAL046.I_pfl2 = 0.0
LAL046.I_lal1046_RR = 0.0
LAL046.I_lal1046_LL = 0.0
LAL046.I_lal1846_RR = 0.0
LAL046.I_lal1846_LL = 0.0
LAL046.I_lal4046_RL = 0.0
LAL046.I_lal4046_LR = 0.0
LAL046.I_lal12146_RL = 0.0
LAL046.I_lal12146_LR = 0.0
LAL046.I_lal12646 = 0.0
LAL046.I_dn3lal46 = 0.0
LAL046.I_dn2lal46 = 0.0

LAL121 = NeuronGroup(2,'''
dr/dt = -r/tau + (1/(1+exp(-s1 * (((I_pfl3 + I_lal + I))-s2))))/tau : 1
tau : second
s1: 1
s2: 1
I: 1
I_pfl3 : 1
I_lal = I_lal046 + I_lal121 + I_lal073 + I_lal141 + I_lal017: 1
I_lal141 = I_lal141121: 1
I_lal141121: 1
I_lal073 = I_lal73121: 1
I_lal73121: 1
I_lal046 = I_lal46121_RR + I_lal46121_LL: 1
I_lal46121_RR: 1
I_lal46121_LL: 1
I_lal121 = I_lal121121_RL + I_lal121121_LR: 1
I_lal121121_RL: 1
I_lal121121_LR: 1
I_lal017 = I_lal17121: 1
I_lal17121: 1
''',threshold='r<0',reset='r=0', method='euler')

LAL121.r = 0.0
LAL121.tau = 10*ms
LAL121.s1 = S1_121
LAL121.s2 = S2_121
LAL121.I = 0.0
LAL121.I_pfl3 = 0.0
LAL121.I_lal46121_RR = 0.0
LAL121.I_lal46121_LL = 0.0
LAL121.I_lal121121_RL = 0.0
LAL121.I_lal121121_LR = 0.0
LAL121.I_lal73121 = 0.0
LAL121.I_lal141121 = 0.0
LAL121.I_lal17121 = 0.0

LAL073 = NeuronGroup(2,'''
dr/dt = -r/tau + (1/(1+exp(-s1 * (((I_pfl3 + I_pfl2 + I_lal + I_DN + I))-s2))))/tau : 1
tau : second
s1: 1
s2: 1
I: 1
I_pfl3 : 1
I_pfl2: 1
I_lal = I_lal010 + I_lal014 + I_lal121 + I_lal122 + I_lal126 + I_lal153: 1
I_DN = I_DN3lal73: 1
I_DN3lal73: 1
I_lal010 = I_lal1073: 1
I_lal1073: 1
I_lal121 = I_lal12173: 1
I_lal12173: 1
I_lal014 = I_lal1473: 1
I_lal1473: 1
I_lal122 = I_lal12273: 1
I_lal12273: 1
I_lal126 = I_lal12673: 1
I_lal12673: 1
I_lal153 = I_lal15373: 1
I_lal15373: 1
''',threshold='r<0',reset='r=0', method='euler')
LAL073.r = 0.0
LAL073.tau = 10*ms
LAL073.s1 = S1_73
LAL073.s2 = S2_73
LAL073.I = 0.0
LAL073.I_pfl3 = 0.0
LAL073.I_lal1073 = 0.0
LAL073.I_lal1473 = 0.0
LAL073.I_lal12173 = 0.0
LAL073.I_DN3lal73 = 0.0
LAL073.I_lal12273 = 0.0
LAL073.I_lal12673 = 0.0
LAL073.I_lal15373 = 0.0
LAL073.I_pfl2 = 0.0
# LAL141
LAL141 = NeuronGroup(2,'''
dr/dt = -r/tau + (1/(1+exp(-s1 * (((I_pfl3 + I_lal + I))-s2))))/tau : 1
tau : second
s1: 1
s2: 1
I: 1
I_pfl3 : 1
I_lal = I_lal073 + I_lal040 + I_lal010 + I_lal121: 1
I_lal010 = I_lal10141: 1
I_lal10141: 1
I_lal121 = I_lal121141: 1
I_lal121141: 1
I_lal073 = I_lal73141: 1
I_lal73141: 1
I_lal040 = I_lal40141_RRLL + I_lal40141_RLLR: 1
I_lal40141_RRLL: 1
I_lal40141_RLLR: 1
''',threshold='r<0',reset='r=0', method='euler')
LAL141.r = 0.0
LAL141.tau = 10*ms
LAL141.s1 = S1_141
LAL141.s2 = S2_141
LAL141.I = 0.0
LAL141.I_pfl3 = 0.0
LAL141.I_lal73141 = 0.0
LAL141.I_lal40141_RRLL = 0.0
LAL141.I_lal40141_RLLR = 0.0
LAL141.I_lal10141 = 0.0
LAL141.I_lal121141 = 0.0

# LAL122
LAL122 = NeuronGroup(2,'''
dr/dt = -r/tau + (1/(1+exp(-s1 * (((I_pfl3 + I_lal + I_dn + I))-s2))))/tau : 1
tau : second
s1: 1
s2: 1
I: 1
I_pfl3 : 1
I_lal = I_lal040 + I_lal010 + I_lal014 + I_lal046 + I_lal017 + I_lal153: 1
I_lal010 = I_lal10122: 1
I_lal10122: 1
I_lal040 = I_lal40122: 1
I_lal40122: 1
I_lal014 = I_lal14122: 1
I_lal14122: 1
I_lal046 = I_lal46122: 1
I_lal46122: 1
I_dn = I_dn3lal122_RRLL + I_dn3lal122_RLLR: 1
I_dn3lal122_RRLL: 1
I_dn3lal122_RLLR: 1
I_lal017 = I_lal17122_RRLL + I_lal17122_RLLR: 1
I_lal17122_RRLL: 1
I_lal17122_RLLR: 1
I_lal153 = I_lal153122_RRLL + I_lal153122_RLLR: 1
I_lal153122_RRLL: 1
I_lal153122_RLLR: 1
''',threshold='r<0',reset='r=0', method='euler')
LAL122.r = 0.0
LAL122.tau = 10*ms
LAL122.s1 = S1_122
LAL122.s2 = S2_122
LAL122.I = 0.0
LAL122.I_pfl3 = 0.0
LAL122.I_lal10122 = 0.0
LAL122.I_lal40122 = 0.0
LAL122.I_lal14122 = 0.0
LAL122.I_lal46122 = 0.0
LAL122.I_dn3lal122_RRLL = 0.0
LAL122.I_dn3lal122_RLLR = 0.0
LAL122.I_lal17122_RLLR = 0.0
LAL122.I_lal17122_RRLL = 0.0
LAL122.I_lal153122_RRLL = 0.0
LAL122.I_lal153122_RLLR = 0.0


LAL126 = NeuronGroup(4,'''
dr/dt = -r/tau + (1/(1+exp(-s1 * (((I_pfl3 + I_lal + I))-s2))))/tau : 1
tau : second
s1: 1
s2: 1
I: 1
I_pfl3 : 1
I_lal = I_lal040 + I_lal073 + I_lal018 + I_lal046 + I_lal017: 1
I_lal018 = I_lal18126: 1
I_lal18126: 1
I_lal040 = I_lal40126: 1
I_lal40126: 1
I_lal073 = I_lal73126: 1
I_lal73126: 1
I_lal046 = I_lal46126: 1
I_lal46126: 1
I_lal017 = I_lal17126: 1
I_lal17126: 1
''',threshold='r<0',reset='r=0', method='euler')
LAL126.r = 0.0
LAL126.tau = 10*ms
LAL126.s1 = S1_126
LAL126.s2 = S2_126
LAL126.I = 0.0
LAL126.I_pfl3 = 0.0
LAL126.I_lal73126 = 0.0
LAL126.I_lal40126 = 0.0
LAL126.I_lal18126 = 0.0
LAL126.I_lal46126 = 0.0
LAL126.I_lal17126 = 0.0 

LAL017 = NeuronGroup(2,'''
dr/dt = -r/tau + (1/(1+exp(-s1 * ((I_lal+I)-s2))))/tau : 1
tau : second
s1: 1
s2: 1
I: 1
I_lal = I_lal010 + I_lal122 + I_lal153 + I_lal121 + I_DNa03: 1
I_lal010 = I_lal1017: 1
I_lal1017: 1
I_lal122 = I_lal12217: 1
I_lal12217: 1
I_lal153 = I_lal15317: 1
I_lal15317: 1
I_lal121 = I_lal12117: 1
I_lal12117: 1
I_DNa03 = I_dn3lal17: 1
I_dn3lal17: 1
''',threshold='r<0',reset='r=0', method='euler')
LAL017.r = 0.0
LAL017.tau = 10*ms
LAL017.s1 = S1_17
LAL017.s2 = S2_17
LAL017.I = 0.0
LAL017.I_lal1017 = 0.0
LAL017.I_lal12217 = 0.0
LAL017.I_lal15317 = 0.0
LAL017.I_lal12117 = 0.0
LAL017.I_dn3lal17 = 0.0

LAL153 = NeuronGroup(2,'''
dr/dt = -r/tau + (1/(1+exp(-s1 * ((I_lal+I)-s2))))/tau : 1
tau : second
s1: 1
s2: 1
I: 1
I_lal = I_lal010 + I_lal014 + I_lal040 + I_lal122 + I_lal153: 1
I_lal010 = I_lal10153: 1
I_lal10153: 1
I_lal122 = I_lal122153_RRLL + I_lal122153_RLLR: 1
I_lal122153_RRLL: 1
I_lal122153_RLLR: 1
I_lal153 = I_lal153153: 1
I_lal153153: 1
I_lal014 = I_lal14153: 1
I_lal14153: 1
I_lal040 = I_lal40153: 1
I_lal40153: 1
''',threshold='r<0',reset='r=0', method='euler')
LAL153.r = 0.0
LAL153.tau = 10*ms
LAL153.s1 = S1_153
LAL153.s2 = S2_153
LAL153.I = 0.0
LAL153.I_lal10153 = 0.0
LAL153.I_lal14153 = 0.0
LAL153.I_lal153153 = 0.0
LAL153.I_lal40153 = 0.0
LAL153.I_lal122153_RRLL = 0.0
LAL153.I_lal122153_RLLR = 0.0

# DNs
DNa01 = NeuronGroup(2,'''
dr/dt = -r/tau + (1/(1+exp(-s1 * (((I_lal))-s2))))/tau : 1
tau : second
s1: 1
s2: 1
I_lal = I_lal014 + I_lal018 + I_lal040 + I_lal046 + I_dn2dn1_RR + I_lal126 + I_lal017: 1
I_dn2dn1_RR: 1
I_lal014 = I_lal14dn1_RR + I_lal14dn1_LL: 1
I_lal14dn1_RR: 1
I_lal14dn1_LL: 1
I_lal018 = I_lal18dn1_RR + I_lal18dn1_LL: 1
I_lal18dn1_RR: 1
I_lal18dn1_LL: 1
I_lal040 = I_lal40dn1_RL + I_lal40dn1_LR: 1
I_lal40dn1_RL: 1
I_lal40dn1_LR: 1
I_lal046 = I_lal46dn1_RR + I_lal46dn1_LL: 1
I_lal46dn1_RR: 1
I_lal46dn1_LL: 1
I_lal126 = I_lal126dn1: 1
I_lal126dn1: 1
I_lal017 = I_lal17dn1: 1
I_lal17dn1: 1
''',threshold='r<0',reset='r=0', method='euler')
DNa01.r = 0.0
DNa01.tau = 10*ms
DNa01.s1 = S1_dn1
DNa01.s2 = S2_dn1
DNa01.I_lal14dn1_LL = 0.0
DNa01.I_lal14dn1_RR = 0.0
DNa01.I_lal18dn1_LL = 0.0
DNa01.I_lal18dn1_RR = 0.0
DNa01.I_lal40dn1_RL = 0.0
DNa01.I_lal40dn1_LR = 0.0
DNa01.I_lal46dn1_LL = 0.0
DNa01.I_lal46dn1_RR = 0.0
DNa01.I_dn2dn1_RR = 0.0
DNa01.I_lal126dn1 = 0.0
DNa01.I_lal17dn1 = 0.0

DNa02 = NeuronGroup(2,'''
dr/dt = -r/tau + (1/(1+exp(-s1 * (((I_pfl3 + I_lal))-s2))))/tau : 1
tau : second
s1: 1
s2: 1
I_lal = I_lal010 + I_lal014 + I_lal018 + I_lal040 + I_lal046 + I_lal121 + I_dna01 + I_dna03 + I_dna04 + I_lal126: 1
I_lal010 = I_lal10dn2_RR + I_lal10dn2_LL: 1
I_lal10dn2_RR: 1
I_lal10dn2_LL: 1
I_lal014 = I_lal14dn2_RR + I_lal14dn2_LL: 1
I_lal14dn2_RR: 1
I_lal14dn2_LL: 1
I_lal018 = I_lal18dn2_RR + I_lal18dn2_LL: 1
I_lal18dn2_RR: 1
I_lal18dn2_LL: 1
I_lal040 = I_lal40dn2_RL + I_lal40dn2_LR: 1
I_lal40dn2_RL: 1
I_lal40dn2_LR: 1
I_lal046 = I_lal46dn2_RR + I_lal46dn2_LL: 1
I_lal46dn2_RR: 1
I_lal46dn2_LL: 1
I_lal121 = I_lal121dn2_RL + I_lal121dn2_LR: 1
I_lal121dn2_RL: 1
I_lal121dn2_LR: 1
I_pfl3: 1
I_dna01 = I_dn1dn2_RR + I_dn1dn2_LL: 1
I_dn1dn2_RR: 1
I_dn1dn2_LL: 1
I_dna03 = I_dn3dn2_RR + I_dn3dn2_LL: 1
I_dn3dn2_RR: 1
I_dn3dn2_LL: 1
I_dna04 = I_dn4dn2_LL: 1
I_dn4dn2_LL: 1
I_lal126 = I_lal126dn2: 1
I_lal126dn2: 1
''',threshold='r<0',reset='r=0', method='euler')

DNa02.r = 0.0
DNa02.tau = 10*ms
DNa02.s1 = S1_dn2
DNa02.s2 = S2_dn2
DNa02.I_lal10dn2_RR = 0.0
DNa02.I_lal10dn2_LL = 0.0
DNa02.I_lal14dn2_RR = 0.0
DNa02.I_lal14dn2_LL = 0.0
DNa02.I_lal18dn2_RR = 0.0
DNa02.I_lal18dn2_LL = 0.0
DNa02.I_lal40dn2_RL = 0.0
DNa02.I_lal40dn2_LR = 0.0
DNa02.I_lal46dn2_RR = 0.0
DNa02.I_lal46dn2_LL = 0.0
DNa02.I_lal121dn2_RL = 0.0
DNa02.I_lal121dn2_LR = 0.0
DNa02.I_lal126dn2 = 0.0
DNa02.I_pfl3 = 0.0
DNa02.I_dn1dn2_RR = 0.0
DNa02.I_dn1dn2_LL = 0.0
DNa02.I_dn3dn2_RR = 0.0
DNa02.I_dn3dn2_LL = 0.0
DNa02.I_dn4dn2_LL = 0.0

DNa03 = NeuronGroup(2,'''
dr/dt = -r/tau + (1/(1+exp(-s1 * (((I_pfl3 + I_pfl2 + I_lal))-s2))))/tau: 1
tau : second
s1: 1
s2: 1
I_pfl2: 1
I_lal = I_lal010 + I_lal014 + I_lal018 + I_lal040 + I_lal046 + I_lal121 + I_dna02 + I_lal073 + I_lal122 + I_lal153: 1
I_lal073 = I_lal73dn3: 1
I_lal73dn3: 1
I_lal010 = I_lal10dn3_RR + I_lal10dn3_LL: 1
I_lal10dn3_RR: 1
I_lal10dn3_LL: 1
I_lal014 = I_lal14dn3_RR + I_lal14dn3_LL: 1
I_lal14dn3_RR: 1
I_lal14dn3_LL: 1
I_lal018 = I_lal18dn3_RR + I_lal18dn3_LL: 1
I_lal18dn3_RR: 1
I_lal18dn3_LL: 1
I_lal040 = I_lal40dn3_RL + I_lal40dn3_LR: 1
I_lal40dn3_RL: 1
I_lal40dn3_LR: 1
I_lal046 = I_lal46dn3_RR + I_lal46dn3_LL: 1
I_lal46dn3_RR: 1
I_lal46dn3_LL: 1
I_lal121 = I_lal121dn3_RL + I_lal121dn3_LR: 1
I_lal121dn3_RL: 1
I_lal121dn3_LR: 1
I_pfl3: 1
I_dna02: 1
I_lal122 = I_lal122dn3: 1
I_lal122dn3: 1
I_lal153 = I_lal153dn3: 1
I_lal153dn3: 1
''',threshold='r<0',reset='r=0', method='euler')

DNa03.r = 0.0
DNa03.tau = 10*ms
DNa03.s1 = S1_dn3
DNa03.s2 = S2_dn3
DNa03.I_lal10dn3_RR = 0.0
DNa03.I_lal10dn3_LL = 0.0
DNa03.I_lal14dn3_RR = 0.0
DNa03.I_lal14dn3_LL = 0.0
DNa03.I_lal18dn3_RR = 0.0
DNa03.I_lal18dn3_LL = 0.0
DNa03.I_lal40dn3_RL = 0.0
DNa03.I_lal40dn3_LR = 0.0
DNa03.I_lal46dn3_RR = 0.0
DNa03.I_lal46dn3_LL = 0.0
DNa03.I_lal121dn3_RL = 0.0
DNa03.I_lal121dn3_LR = 0.0
DNa03.I_lal73dn3 = 0.0
DNa03.I_pfl3 = 0.0
DNa03.I_dna02 = 0.0
DNa03.I_lal122dn3 = 0.0
DNa03.I_lal153dn3 = 0.0
DNa03.I_pfl2 = 0.0

DNa04 = NeuronGroup(2,'''
dr/dt = -r/tau + (1/(1+exp(-s1 * (((I_pfl3 + I_lal))-s2))))/tau: 1
tau : second
s1: 1
s2: 1
I_lal = I_lal010 + I_lal018 + I_lal040 + I_lal046 + I_dna02 + I_dna03: 1
I_lal010 = I_lal10dn4_RR + I_lal10dn4_LL: 1
I_lal10dn4_RR: 1
I_lal10dn4_LL: 1
I_lal018 = I_lal18dn4_RR + I_lal18dn4_LL: 1
I_lal18dn4_RR: 1
I_lal18dn4_LL: 1
I_lal040 = I_lal40dn4_RL + I_lal40dn4_LR: 1
I_lal40dn4_RL: 1
I_lal40dn4_LR: 1
I_lal046 = I_lal46dn4_RR + I_lal46dn4_LL: 1
I_lal46dn4_RR: 1
I_lal46dn4_LL: 1
I_pfl3: 1
I_dna02 = I_dn2dn4_RR: 1
I_dn2dn4_RR: 1
I_dna03 = I_dn3dn4_RR + I_dn3dn4_LL: 1
I_dn3dn4_RR: 1
I_dn3dn4_LL: 1
''',threshold='r<0',reset='r=0', method='euler')

DNa04.r = 0.0
DNa04.tau = 10*ms
DNa04.s1 = S1_dn4
DNa04.s2 = S2_dn4
DNa04.I_lal10dn4_RR = 0.0
DNa04.I_lal10dn4_LL = 0.0
DNa04.I_lal18dn4_RR = 0.0
DNa04.I_lal18dn4_LL = 0.0
DNa04.I_lal40dn4_RL = 0.0
DNa04.I_lal40dn4_LR = 0.0
DNa04.I_lal46dn4_RR = 0.0
DNa04.I_lal46dn4_LL = 0.0
DNa04.I_pfl3 = 0.0
DNa04.I_dn2dn4_RR = 0.0
DNa04.I_dn3dn4_RR = 0.0
DNa04.I_dn3dn4_LL = 0.0

DNg13 = NeuronGroup(2,'''
dr/dt = -r/tau + (1/(1+exp(-s1 * (((I_lal))-s2))))/tau : 1
tau : second
s1: 1
s2: 1
I_lal = I_lal014 + I_lal018dn13 + I_lal040 + I_lal046 + I_dn1 + I_lal073: 1
I_lal073 = I_lal73dn13: 1
I_lal73dn13: 1
I_lal014 = I_lal014dn13_RR + I_lal014dn13_LL: 1
I_lal014dn13_RR: 1
I_lal014dn13_LL: 1
I_lal018dn13: 1
I_lal040 = I_lal040dn13_RL + I_lal040dn13_LR: 1
I_lal040dn13_RL: 1
I_lal040dn13_LR: 1
I_lal046 = I_lal046dn13_RR + I_lal046dn13_LL: 1
I_lal046dn13_RR: 1
I_lal046dn13_LL: 1
I_dn1 = I_dn1dn13_LL + I_dn1dn13_RR: 1
I_dn1dn13_LL: 1
I_dn1dn13_RR: 1
''',threshold='r<0',reset='r=0', method='euler')
DNg13.r = 0.0
DNg13.tau = 10*ms
DNg13.s1 = S1_dn13
DNg13.s2 = S2_dn13
DNg13.I_lal014dn13_RR = 0.0
DNg13.I_lal014dn13_LL = 0.0
DNg13.I_lal018dn13 = 0.0
DNg13.I_lal040dn13_RL = 0.0
DNg13.I_lal040dn13_LR = 0.0
DNg13.I_lal046dn13_RR = 0.0
DNg13.I_lal046dn13_LL = 0.0
DNg13.I_dn1dn13_LL = 0.0
DNg13.I_dn1dn13_RR = 0.0
DNg13.I_lal73dn13 = 0.0

#########Synapase#########

#PFL3 input
#FC2-PFL3 connection
S_pfpc = Synapses(FC2, PFL3, '''
             w : 1 # synaptic weight
             IFC2_post = w * r_pre : 1 (summed)
             ''')
for k in range(0,11):
    S_pfpc.connect(i=k,j=2*k)
for k in range(0,11):
    S_pfpc.connect(i=k,j=2*k+1)
S_pfpc.w = 0.0

S_pfpc_2 = Synapses(FC2, PFL2, '''
             w : 1 # synaptic weight
             IFC2_post = w * r_pre : 1 (summed)
             ''')
S_pfpc_2.connect(i='j')

S_pfpc_2.w = 0.0

S_pfhead = Synapses(headinput, PFL3, '''
             w : 1 # synaptic weight
             Ihead_post = w * r_pre : 1 (summed)
             ''')
S_pfhead.connect(i=0, j=[0])
S_pfhead.connect(i=1, j=[2])
S_pfhead.connect(i=2, j=[4,6])
S_pfhead.connect(i=3, j=[8])
S_pfhead.connect(i=4, j=[10])
S_pfhead.connect(i=5, j=[12])
S_pfhead.connect(i=6, j=[1,14])
S_pfhead.connect(i=7, j=[3,16,18])
S_pfhead.connect(i=8, j=[5,7,20])
S_pfhead.connect(i=9, j=[9,22])
S_pfhead.connect(i=10, j=[11])
S_pfhead.connect(i=11, j=[13])
S_pfhead.connect(i=12, j=[15])
S_pfhead.connect(i=13, j=[17,19])
S_pfhead.connect(i=14, j=[21])
S_pfhead.connect(i=15, j=[23])
S_pfhead.w = 0.0

S_pfhead_2 = Synapses(headinput, PFL2, '''
             w : 1 # synaptic weight
             Ihead_2_post = w * r_pre : 1 (summed)
             ''')
S_pfhead_2.connect(i=2, j=[0])
S_pfhead_2.connect(i=3, j=[1])
S_pfhead_2.connect(i=4, j=[2])
S_pfhead_2.connect(i=5, j=[3])
S_pfhead_2.connect(i=6, j=[4])
S_pfhead_2.connect(i=7, j=[5])
S_pfhead_2.connect(i=8, j=[6])
S_pfhead_2.connect(i=9, j=[7])
S_pfhead_2.connect(i=10, j=[8])
S_pfhead_2.connect(i=11, j=[9])
S_pfhead_2.connect(i=12, j=[10])
S_pfhead_2.connect(i=13, j=[11])

S_pfhead_2.w = 0.0

# PFL3 ->LAL
pflal_model='''
w : 1 # synaptic weight
I_pfl3_post = w * r_pre : 1 (summed)
'''
S_pflal010 = Synapses(PFL3, LAL010, pflal_model)
S_pflal010.connect(i=[0,2,4,6,8,10,12,14,16,18,20,22],j=0)
S_pflal010.connect(i=[1,3,5,7,9,11,13,15,17,19,21,23],j=1)

S_pflal014 = Synapses(PFL3, LAL014, pflal_model)
S_pflal014.connect(i=[0,2,4,6,8,10,12,14,16,18,20,22],j=0)
S_pflal014.connect(i=[1,3,5,7,9,11,13,15,17,19,21,23],j=1)

S_pflal018 = Synapses(PFL3, LAL018, pflal_model)
S_pflal018.connect(i=[0,2,4,6,8,10,12,14,16,18,20,22],j=0)
S_pflal018.connect(i=[1,3,5,7,9,11,13,15,17,19,21,23],j=1)

S_pflal040 = Synapses(PFL3, LAL040, pflal_model)
S_pflal040.connect(i=[0,2,4,6,8,10,12,14,16,18,20,22],j=0)
S_pflal040.connect(i=[1,3,5,7,9,11,13,15,17,19,21,23],j=1)

S_pflal046 = Synapses(PFL3, LAL046, pflal_model)
S_pflal046.connect(i=[0,2,4,6,8,10,12,14,16,18,20,22],j=0)
S_pflal046.connect(i=[1,3,5,7,9,11,13,15,17,19,21,23],j=1)

S_pflal121 = Synapses(PFL3, LAL121, pflal_model)
S_pflal121.connect(i=[0,2,4,6,8,10,12,14,16,18,20,22],j=0)
S_pflal121.connect(i=[1,3,5,7,9,11,13,15,17,19,21,23],j=1)

S_pflal073 = Synapses(PFL3, LAL073, pflal_model)
S_pflal073.connect()

S_pflal141 = Synapses(PFL3, LAL141, pflal_model)
S_pflal141.connect(i=[0,2,4,6,8,10,12,14,16,18,20,22],j=0)
S_pflal141.connect(i=[1,3,5,7,9,11,13,15,17,19,21,23],j=1)

S_pflal122 = Synapses(PFL3, LAL122, pflal_model)
S_pflal122.connect(i=[0,2,4,6,8,10,12,14,16,18,20,22],j=0)
S_pflal122.connect(i=[1,3,5,7,9,11,13,15,17,19,21,23],j=1)

S_pflal126 = Synapses(PFL3, LAL126, pflal_model)
S_pflal126.connect(i=[0,2,4,6,8,10,12,14,16,18,20,22],j=0)
S_pflal126.connect(i=[0,2,4,6,8,10,12,14,16,18,20,22],j=2)
S_pflal126.connect(i=[1,3,5,7,9,11,13,15,17,19,21,23],j=1)
S_pflal126.connect(i=[1,3,5,7,9,11,13,15,17,19,21,23],j=3)

S_pflal010.w = 0.0
S_pflal014.w = 0.0
S_pflal018.w = 0.0
S_pflal040.w = 0.0
S_pflal046.w = 0.0
S_pflal121.w = 0.0
S_pflal073.w = 0.0
S_pflal141.w = 0.0
S_pflal122.w = 0.0
S_pflal126.w = 0.0

# LAL->LAL

# -> LAL010
S_lal1410 = Synapses(LAL014, LAL010, '''
                    w: 1
                    I_lal014_post = w*r_pre: 1 (summed)
                    ''')
S_lal1410.connect(i='j')
S_lal1410.w = 0.0

S_lal4010_RL = Synapses(LAL040, LAL010, '''
                    w: 1
                    I_lal4010_RL_post = -w*r_pre: 1 (summed)
                    ''')
S_lal4010_RL.connect(i=[0], j=[1])
S_lal4010_LR = Synapses(LAL040, LAL010, '''
                    w: 1
                    I_lal4010_LR_post = -w*r_pre: 1 (summed)
                    ''')
S_lal4010_LR.connect(i=[1], j=[0])
S_lal4010_RR = Synapses(LAL040, LAL010, '''
                    w: 1
                    I_lal4010_RR_post = -w*r_pre: 1 (summed)
                    ''')
S_lal4010_RR.connect(i=[0], j=[0])
S_lal4010_LL = Synapses(LAL040, LAL010, '''
                    w: 1
                    I_lal4010_LL_post = -w*r_pre: 1 (summed)
                    ''')
S_lal4010_LL.connect(i=[1], j=[1])
S_lal4010_RL.w = 0.0
S_lal4010_LR.w = 0.0
S_lal4010_RR.w = 0.0
S_lal4010_LL.w = 0.0

S_lal12110_LR = Synapses(LAL121, LAL010, '''
                    w: 1
                    I_lal12110_LR_post = w*r_pre: 1 (summed)
                    ''')
S_lal12110_LR.connect(i=[1], j=[0])
S_lal12110_RL = Synapses(LAL121, LAL010, '''
                    w: 1
                    I_lal12110_RL_post = w*r_pre: 1 (summed)
                    ''')
S_lal12110_RL.connect(i=[0], j=[1])
S_lal12110_LR.w = 0.0
S_lal12110_RL.w = 0.0

S_lal14110 = Synapses(LAL141, LAL010, '''
                    w: 1
                    I_lal14110_post = w*r_pre: 1 (summed)
                    ''')
S_lal14110.connect(i='j')
S_lal14110.w = 0.0

S_dn3lal10 = Synapses(DNa03, LAL010, '''
                    w: 1
                    I_dn3lal10_post = w*r_pre: 1 (summed)
                    ''')
S_dn3lal10.connect(i='j')
S_dn3lal10.w = 0.0

S_pfl210 = Synapses(PFL2, LAL010, '''
                    w: 1
                    I_pfl2_post = w*r_pre: 1 (summed)
                    ''')
S_pfl210.connect()
S_pfl210.w = 0.0 

# -> LAL014
S_lal1014_RR = Synapses(LAL010, LAL014, '''
                    w: 1
                    I_lal1014_RR_post = w*r_pre: 1 (summed)
                    ''')
S_lal1014_RR.connect(i=[0], j=[0])
S_lal1014_LL = Synapses(LAL010, LAL014, '''
                    w: 1
                    I_lal1014_LL_post = w*r_pre: 1 (summed)
                    ''')
S_lal1014_LL.connect(i=[1], j=[1])
S_lal1014_RR.w = 0.0
S_lal1014_LL.w = 0.0

S_lal4014_RL = Synapses(LAL040, LAL014, '''
                    w: 1
                    I_lal4014_RL_post = -w*r_pre: 1 (summed)
                    ''')
S_lal4014_RL.connect(i=[0], j=[1])
S_lal4014_RL.w = 0.0
S_lal4014_LR = Synapses(LAL040, LAL014, '''
                    w: 1
                    I_lal4014_LR_post = -w*r_pre: 1 (summed)
                    ''')
S_lal4014_LR.connect(i=[1], j=[0])
S_lal4014_LR.w = 0.0

S_lal12114_RL = Synapses(LAL121, LAL014, '''
                    w: 1
                    I_lal12114_RL_post = w*r_pre: 1 (summed)
                    ''')
S_lal12114_RL.connect(i=[0], j=[1])
S_lal12114_LR = Synapses(LAL121, LAL014, '''
                    w: 1
                    I_lal12114_LR_post = w*r_pre: 1 (summed)
                    ''')
S_lal12114_LR.connect(i=[1], j=[0])
S_lal12114_RL.w = 0.0
S_lal12114_LR.w = 0.0

S_lal12214 = Synapses(LAL122, LAL014, '''
                    w: 1
                    I_lal12214_post = w*r_pre: 1 (summed)
                    ''')
S_lal12214.connect(i=[1], j=[0])
S_lal12214.connect(i=[0], j=[1])
S_lal12214.w = 0.0

S_lal15314 = Synapses(LAL153, LAL014, '''
                    w: 1
                    I_lal15314_post = w*r_pre: 1 (summed)
                    ''')
S_lal15314.connect(i=[1], j=[0])
S_lal15314.connect(i=[0], j=[1])
S_lal15314.w = 0.0

S_dn3lal14 = Synapses(DNa03, LAL014, '''
                    w: 1
                    I_dn3lal14_post = w*r_pre: 1 (summed)
                    ''')
S_dn3lal14.connect(i='j')
S_dn3lal14.w = 0.0

S_pfl214 = Synapses(PFL2, LAL014, '''
                    w: 1
                    I_pfl2_post = w*r_pre: 1 (summed)
                    ''')
S_pfl214.connect()
S_pfl214.w = 0.0 

# -> LAL018
S_lal1018_RR = Synapses(LAL010, LAL018, '''
                    w: 1
                    I_lal1018_RR_post = w*r_pre: 1 (summed)
                    ''')
S_lal1018_RR.connect(i=[0], j=[0])
S_lal1018_LL = Synapses(LAL010, LAL018, '''
                    w: 1
                    I_lal1018_LL_post = w*r_pre: 1 (summed)
                    ''')
S_lal1018_LL.connect(i=[1], j=[1])
S_lal1018_RR.w = 0.0
S_lal1018_LL.w = 0.0

S_lal1418_RR = Synapses(LAL014, LAL018, '''
                    w: 1
                    I_lal1418_RR_post = w*r_pre: 1 (summed)
                    ''')
S_lal1418_RR.connect(i='j')
S_lal1418_RR.w = 0.0

S_lal4018_RL = Synapses(LAL040, LAL018, '''
                    w: 1
                    I_lal4018_RL_post = -w*r_pre: 1 (summed)
                    ''')
S_lal4018_RL.connect(i=[0], j=[1])
S_lal4018_LR = Synapses(LAL040, LAL018, '''
                    w: 1
                    I_lal4018_LR_post = -w*r_pre: 1 (summed)
                    ''')
S_lal4018_LR.connect(i=[1], j=[0])
S_lal4018_RL.w = 0.0
S_lal4018_LR.w = 0.0

S_lal4618_RR = Synapses(LAL046, LAL018, '''
                    w: 1
                    I_lal4618_RR_post = -w*r_pre: 1 (summed)
                    ''')
S_lal4618_RR.connect(i=[0], j=[0])
S_lal4618_LL = Synapses(LAL046, LAL018, '''
                    w: 1
                    I_lal4618_LL_post = -w*r_pre: 1 (summed)
                    ''')
S_lal4618_LL.connect(i=[1], j=[1])
S_lal4618_RR.w = 0.0
S_lal4618_LL.w = 0.0

S_lal14118 = Synapses(LAL141, LAL018, '''
                    w: 1
                    I_lal14118_post = w*r_pre: 1 (summed)
                    ''')
S_lal14118.connect(i='j')
S_lal14118.w = 0.0

S_lal12618 = Synapses(LAL126, LAL018, '''
                    w: 1
                    I_lal12618_post = w*r_pre: 1 (summed)
                    ''')
S_lal12618.connect(i=[0, 2], j=[1])
S_lal12618.connect(i=[1, 3], j=[0])
S_lal12618.w = 0.0

S_lal15318 = Synapses(LAL153, LAL018, '''
                    w: 1
                    I_lal15318_post = w*r_pre: 1 (summed)
                    ''')
S_lal15318.connect(i=[0], j=[1])
S_lal15318.connect(i=[1], j=[0])
S_lal15318.w = 0.0

S_dn3lal18 = Synapses(DNa03, LAL018, '''
                    w: 1
                    I_dn3lal18_post = w*r_pre: 1 (summed)
                    ''')
S_dn3lal18.connect(i='j')
S_dn3lal18.w = 0.0

S_dn2lal18 = Synapses(DNa02, LAL018, '''
                    w: 1
                    I_dn2lal18_post = w*r_pre: 1 (summed)
                    ''')
S_dn2lal18.connect(i='j')
S_dn2lal18.w = 0.0

# -> LAL040
S_lal1040_RR = Synapses(LAL010, LAL040, '''
                    w: 1
                    I_lal1040_RR_post = w*r_pre: 1 (summed)
                    ''')
S_lal1040_RR.connect(i=[0], j=[0])
S_lal1040_RR.w = 0.0
S_lal1040_LL = Synapses(LAL010, LAL040, '''
                    w: 1
                    I_lal1040_LL_post = w*r_pre: 1 (summed)
                    ''')
S_lal1040_LL.connect(i=[1], j=[1])
S_lal1040_LL.w = 0.0

S_lal7340 = Synapses(LAL073, LAL040, '''
                    w: 1
                    I_lal7340_post = w*r_pre: 1 (summed)
                    ''')
S_lal7340.connect(i=[0], j=[1])
S_lal7340.connect(i=[1], j=[0])
S_lal7340.w = 0.0

S_lal14140 = Synapses(LAL141, LAL040, '''
                    w: 1
                    I_lal14140_post = w*r_pre: 1 (summed)
                    ''')
S_lal14140.connect(i='j')
S_lal14140.w = 0.0

# -> LAL046
S_lal1046_RR = Synapses(LAL010, LAL046, '''
                    w: 1
                    I_lal1046_RR_post = w*r_pre: 1 (summed)
                    ''')
S_lal1046_RR.connect(i=[0], j=[0])
S_lal1046_LL = Synapses(LAL010, LAL046, '''
                    w: 1
                    I_lal1046_LL_post = w*r_pre: 1 (summed)
                    ''')
S_lal1046_LL.connect(i=[1], j=[1])
S_lal1046_RR.w = 0.0
S_lal1046_LL.w = 0.0

S_lal1846_RR = Synapses(LAL018, LAL046, '''
                    w: 1
                    I_lal1846_RR_post = w*r_pre: 1 (summed)
                    ''')
S_lal1846_RR.connect(i=[0], j=[0])
S_lal1846_LL = Synapses(LAL018, LAL046, '''
                    w: 1
                    I_lal1846_LL_post = w*r_pre: 1 (summed)
                    ''')
S_lal1846_LL.connect(i=[1], j=[1])
S_lal1846_RR.w = 0.0
S_lal1846_LL.w = 0.0

S_lal4046_RL = Synapses(LAL040, LAL046, '''
                    w: 1
                    I_lal4046_RL_post = -w*r_pre: 1 (summed)
                    ''')
S_lal4046_RL.connect(i=[0], j=[1])
S_lal4046_RL.w = 0.0
S_lal4046_LR = Synapses(LAL040, LAL046, '''
                    w: 1
                    I_lal4046_LR_post = -w*r_pre: 1 (summed)
                    ''')
S_lal4046_LR.connect(i=[1], j=[0])
S_lal4046_LR.w = 0.0

S_lal12146_RL = Synapses(LAL121, LAL046, '''
                    w: 1
                    I_lal12146_RL_post = w*r_pre: 1 (summed)
                    ''')
S_lal12146_RL.connect(i=[0], j=[1])
S_lal12146_RL.w = 0.0
S_lal12146_LR = Synapses(LAL121, LAL046, '''
                    w: 1
                    I_lal12146_LR_post = w*r_pre: 1 (summed)
                    ''')
S_lal12146_LR.connect(i=[1], j=[0])
S_lal12146_LR.w = 0.0

S_lal12646 = Synapses(LAL126, LAL046, '''
                    w: 1
                    I_lal12646_post = w*r_pre: 1 (summed)
                    ''')
S_lal12646.connect(i=[1, 3], j=[0])
S_lal12646.connect(i=[0, 2], j=[1])
S_lal12646.w = 0.0

S_dn3lal46 = Synapses(DNa03, LAL046, '''
                    w: 1
                    I_dn3lal46_post = w*r_pre: 1 (summed)
                    ''')
S_dn3lal46.connect(i='j')
S_dn3lal46.w = 0.0

S_dn2lal46 = Synapses(DNa02, LAL046, '''
                    w: 1
                    I_dn2lal46_post = w*r_pre: 1 (summed)
                    ''')
S_dn2lal46.connect(i='j')
S_dn2lal46.w = 0.0

S_pfl246 = Synapses(PFL2, LAL046, '''
                    w: 1
                    I_pfl2_post = w*r_pre: 1 (summed)
                    ''')
S_pfl246.connect()
S_pfl246.w = 0.0 

# -> LAL121
S_lal46121_RR = Synapses(LAL046, LAL121, '''
                    w: 1
                    I_lal46121_RR_post = -w*r_pre: 1 (summed)
                    ''')
S_lal46121_RR.connect(i=[0], j=[0])
S_lal46121_RR.w = 0.0
S_lal46121_LL = Synapses(LAL046, LAL121, '''
                    w: 1
                    I_lal46121_LL_post = -w*r_pre: 1 (summed)
                    ''')
S_lal46121_LL.connect(i=[1], j=[1])
S_lal46121_LL.w = 0.0

S_lal121121_RL = Synapses(LAL121, LAL121, '''
                    w: 1
                    I_lal121121_RL_post = w*r_pre: 1 (summed)
                    ''')
S_lal121121_RL.connect(i=[0], j=[1])
S_lal121121_RL.w = 0.0
S_lal121121_LR = Synapses(LAL121, LAL121, '''
                    w: 1
                    I_lal121121_LR_post = w*r_pre: 1 (summed)
                    ''')
S_lal121121_LR.connect(i=[1], j=[0])
S_lal121121_LR.w = 0.0

S_lal73121 = Synapses(LAL073, LAL121, '''
                    w: 1
                    I_lal73121_post = w*r_pre: 1 (summed)
                    ''')
S_lal73121.connect(i=[0], j=[1])
S_lal73121.connect(i=[1], j=[0])
S_lal73121.w = 0.0

S_lal141121 = Synapses(LAL141, LAL121, '''
                    w: 1
                    I_lal141121_post = w*r_pre: 1 (summed)
                    ''')
S_lal141121.connect(i='j')
S_lal141121.w = 0.0

S_lal17121 = Synapses(LAL017, LAL121, '''
                    w: 1
                    I_lal17121_post = w*r_pre: 1 (summed)
                    ''')
S_lal17121.connect(i='j')
S_lal17121.w = 0.0

# LAL073
S_lal1073 = Synapses(LAL010, LAL073, '''
                    w: 1
                    I_lal1073_post = w*r_pre: 1 (summed)
                    ''')
S_lal1073.connect(i='j')
S_lal1073.w = 0.0 

S_lal1473 = Synapses(LAL014, LAL073, '''
                    w: 1
                    I_lal1473_post = w*r_pre: 1 (summed)
                    ''')
S_lal1473.connect(i='j')
S_lal1473.w = 0.0 

S_lal12173 = Synapses(LAL121, LAL073, '''
                    w: 1
                    I_lal12173_post = w*r_pre: 1 (summed)
                    ''')
S_lal12173.connect(i=[0], j=[1])
S_lal12173.connect(i=[1], j=[0])
S_lal12173.w = 0.0 

S_dn3lal73 = Synapses(DNa03, LAL073, '''
                    w: 1
                    I_DN3lal73_post = w*r_pre: 1 (summed)
                    ''')
S_dn3lal73.connect(i='j')
S_dn3lal73.w = 0.0 

S_lal12273 = Synapses(LAL122, LAL073, '''
                    w: 1
                    I_lal12273_post = w*r_pre: 1 (summed)
                    ''')
S_lal12273.connect(i=[0], j=[1])
S_lal12273.connect(i=[1], j=[0])
S_lal12273.w = 0.0 

S_lal12673 = Synapses(LAL126, LAL073, '''
                    w: 1
                    I_lal12673_post = w*r_pre: 1 (summed)
                    ''')
S_lal12673.connect(i=[0, 2], j=[1])
S_lal12673.connect(i=[1, 3], j=[0])
S_lal12673.w = 0.0 

S_lal15373 = Synapses(LAL153, LAL073, '''
                    w: 1
                    I_lal15373_post = w*r_pre: 1 (summed)
                    ''')
S_lal15373.connect(i=[0], j=[1])
S_lal15373.connect(i=[1], j=[0])
S_lal15373.w = 0.0 

S_pfl273 = Synapses(PFL2, LAL073, '''
                    w: 1
                    I_pfl2_post = w*r_pre: 1 (summed)
                    ''')
S_pfl273.connect()
S_pfl273.w = 0.0 

# LAL141
S_lal73141 = Synapses(LAL073, LAL141, '''
                    w: 1
                    I_lal73141_post = w*r_pre: 1 (summed)
                    ''')
S_lal73141.connect(i=[0], j=[1])
S_lal73141.connect(i=[1], j=[0])
S_lal73141.w = 0.0 

S_lal40141_RRLL = Synapses(LAL040, LAL141, '''
                    w: 1
                    I_lal40141_RRLL_post = -w*r_pre: 1 (summed)
                    ''')
S_lal40141_RRLL.connect(i='j')
S_lal40141_RRLL.w = 0.0 

S_lal40141_RLLR = Synapses(LAL040, LAL141, '''
                    w: 1
                    I_lal40141_RLLR_post = -w*r_pre: 1 (summed)
                    ''')
S_lal40141_RLLR.connect(i=[0], j=[1])
S_lal40141_RLLR.connect(i=[1], j=[0])
S_lal40141_RLLR.w = 0.0 

S_lal10141 = Synapses(LAL010, LAL141, '''
                    w: 1
                    I_lal10141_post = w*r_pre: 1 (summed)
                    ''')
S_lal10141.connect(i='j')
S_lal10141.w = 0.0 

S_lal121141 = Synapses(LAL121, LAL141, '''
                    w: 1
                    I_lal121141_post = w*r_pre: 1 (summed)
                    ''')
S_lal121141.connect(i=[0], j=[1])
S_lal121141.connect(i=[1], j=[0])
S_lal121141.w = 0.0 

# LAL122
S_lal10122 = Synapses(LAL010, LAL122, '''
                    w: 1
                    I_lal10122_post = w*r_pre: 1 (summed)
                    ''')
S_lal10122.connect(i='j')
S_lal10122.w = 0.0 

S_lal14122 = Synapses(LAL014, LAL122, '''
                    w: 1
                    I_lal14122_post = w*r_pre: 1 (summed)
                    ''')
S_lal14122.connect(i='j')
S_lal14122.w = 0.0

S_lal46122 = Synapses(LAL046, LAL122, '''
                    w: 1
                    I_lal46122_post = -w*r_pre: 1 (summed)
                    ''')
S_lal46122.connect(i='j')
S_lal46122.w = 0.0

S_lal40122 = Synapses(LAL040, LAL122, '''
                    w: 1
                    I_lal40122_post = -w*r_pre: 1 (summed)
                    ''')
S_lal40122.connect(i=[0], j=[1])
S_lal40122.connect(i=[1], j=[0])
S_lal40122.w = 0.0

S_dn3lal122_RLLR = Synapses(DNa03, LAL122, '''
                    w: 1
                    I_dn3lal122_RLLR_post = w*r_pre: 1 (summed)
                    ''')
S_dn3lal122_RLLR.connect(i=[0], j=[1])
S_dn3lal122_RLLR.connect(i=[1], j=[0])
S_dn3lal122_RLLR.w = 0.0

S_dn3lal122_RRLL = Synapses(DNa03, LAL122, '''
                    w: 1
                    I_dn3lal122_RRLL_post = w*r_pre: 1 (summed)
                    ''')
S_dn3lal122_RRLL.connect(i='j')
S_dn3lal122_RRLL.w = 0.0

S_lal17122_RLLR = Synapses(LAL017, LAL122, '''
                    w: 1
                    I_lal17122_RLLR_post = w*r_pre: 1 (summed)
                    ''')
S_lal17122_RLLR.connect(i=[0], j=[1])
S_lal17122_RLLR.connect(i=[1], j=[0])
S_lal17122_RLLR.w = 0.0

S_lal17122_RRLL = Synapses(LAL017, LAL122, '''
                    w: 1
                    I_lal17122_RRLL_post = w*r_pre: 1 (summed)
                    ''')
S_lal17122_RRLL.connect(i='j')
S_lal17122_RRLL.w = 0.0

S_lal153122_RRLL = Synapses(LAL153, LAL122, '''
                    w: 1
                    I_lal153122_RRLL_post = w*r_pre: 1 (summed)
                    ''')
S_lal153122_RRLL.connect(i='j')
S_lal153122_RRLL.w = 0.0

S_lal153122_RLLR = Synapses(LAL153, LAL122, '''
                    w: 1
                    I_lal153122_RLLR_post = w*r_pre: 1 (summed)
                    ''')
S_lal153122_RLLR.connect(i=[0], j=[1])
S_lal153122_RLLR.connect(i=[1], j=[0])
S_lal153122_RLLR.w = 0.0

# LAL126
S_lal46126 = Synapses(LAL046, LAL126, '''
                    w: 1
                    I_lal46126_post = -w*r_pre: 1 (summed)
                    ''')
S_lal46126.connect(i=[0], j=[0, 2])
S_lal46126.connect(i=[1], j=[1, 3])
S_lal46126.w = 0.0

S_lal18126 = Synapses(LAL018, LAL126, '''
                    w: 1
                    I_lal18126_post = w*r_pre: 1 (summed)
                    ''')
S_lal18126.connect(i=[0], j=[0, 2])
S_lal18126.connect(i=[1], j=[1, 3])
S_lal18126.w = 0.0

S_lal73126 = Synapses(LAL073, LAL126, '''
                    w: 1
                    I_lal73126_post = w*r_pre: 1 (summed)
                    ''')
S_lal73126.connect(i=[1], j=[0, 2])
S_lal73126.connect(i=[0], j=[1, 3])
S_lal73126.w = 0.0

S_lal40126 = Synapses(LAL040, LAL126, '''
                    w: 1
                    I_lal40126_post = -w*r_pre: 1 (summed)
                    ''')
S_lal40126.connect(i=[1], j=[0, 2])
S_lal40126.connect(i=[0], j=[1, 3])
S_lal40126.w = 0.0

S_lal17126 = Synapses(LAL017, LAL126, '''
                    w: 1
                    I_lal17126_post = w*r_pre: 1 (summed)
                    ''')
S_lal17126.connect(i=[0], j=[0, 2])
S_lal17126.connect(i=[1], j=[1, 3])
S_lal17126.w = 0.0

# LAL017

S_lal1017 = Synapses(LAL010, LAL017, '''
                    w: 1
                    I_lal1017_post = w*r_pre: 1 (summed)
                    ''')
S_lal1017.connect(i='j')
S_lal1017.w = 0.0

S_dn3lal17 = Synapses(DNa03, LAL017, '''
                    w: 1
                    I_dn3lal17_post = w*r_pre: 1 (summed)
                    ''')
S_dn3lal17.connect(i='j')
S_dn3lal17.w = 0.0

S_lal12217 = Synapses(LAL122, LAL017, '''
                    w: 1
                    I_lal12217_post = w*r_pre: 1 (summed)
                    ''')
S_lal12217.connect(i=[0], j=[1])
S_lal12217.connect(i=[1], j=[0])
S_lal12217.w = 0.0

S_lal15317 = Synapses(LAL153, LAL017, '''
                    w: 1
                    I_lal15317_post = w*r_pre: 1 (summed)
                    ''')
S_lal15317.connect(i=[0], j=[1])
S_lal15317.connect(i=[1], j=[0])
S_lal15317.w = 0.0

S_lal12117 = Synapses(LAL121, LAL017, '''
                    w: 1
                    I_lal12117_post = w*r_pre: 1 (summed)
                    ''')
S_lal12117.connect(i=[0], j=[1])
S_lal12117.connect(i=[1], j=[0])
S_lal12117.w = 0.0

# LAL153
S_lal10153 = Synapses(LAL010, LAL153, '''
                    w: 1
                    I_lal10153_post = w*r_pre: 1 (summed)
                    ''')
S_lal10153.connect(i='j')
S_lal10153.w = 0.0

S_lal14153 = Synapses(LAL014, LAL153, '''
                    w: 1
                    I_lal14153_post = w*r_pre: 1 (summed)
                    ''')
S_lal14153.connect(i='j')
S_lal14153.w = 0.0

S_lal40153 = Synapses(LAL040, LAL153, '''
                    w: 1
                    I_lal40153_post = -w*r_pre: 1 (summed)
                    ''')
S_lal40153.connect(i=[0], j=[1])
S_lal40153.connect(i=[1], j=[0])
S_lal40153.w = 0.0

S_lal122153_RLLR = Synapses(LAL122, LAL153, '''
                    w: 1
                    I_lal122153_RLLR_post = w*r_pre: 1 (summed)
                    ''')
S_lal122153_RLLR.connect(i=[0], j=[1])
S_lal122153_RLLR.connect(i=[1], j=[0])
S_lal122153_RLLR.w = 0.0

S_lal122153_RRLL = Synapses(LAL122, LAL153, '''
                    w: 1
                    I_lal122153_RRLL_post = w*r_pre: 1 (summed)
                    ''')
S_lal122153_RRLL.connect(i='j')
S_lal122153_RRLL.w = 0.0

S_lal153153 = Synapses(LAL153, LAL153, '''
                    w: 1
                    I_lal153153_post = w*r_pre: 1 (summed)
                    ''')
S_lal153153.connect(i=[0], j=[1])
S_lal153153.connect(i=[1], j=[0])
S_lal153153.w = 0.0

# DNs
# DNa01
S_14dn1_RR = Synapses(LAL014, DNa01, '''
                    w: 1
                    I_lal14dn1_RR_post = w*r_pre: 1 (summed)
                    ''')
S_14dn1_RR.connect(i=[0], j=[0])
S_14dn1_RR.w = 0.0

S_14dn1_LL = Synapses(LAL014, DNa01, '''
                    w: 1
                    I_lal14dn1_LL_post = w*r_pre: 1 (summed)
                    ''')
S_14dn1_LL.connect(i=[1], j=[1])
S_14dn1_LL.w = 0.0

S_18dn1_RR = Synapses(LAL018, DNa01, '''
                    w: 1
                    I_lal18dn1_RR_post = w*r_pre: 1 (summed)
                    ''')
S_18dn1_RR.connect(i=[0], j=[0])
S_18dn1_RR.w = 0.0

S_18dn1_LL = Synapses(LAL018, DNa01, '''
                    w: 1
                    I_lal18dn1_LL_post = w*r_pre: 1 (summed)
                    ''')
S_18dn1_LL.connect(i=[1], j=[1])
S_18dn1_LL.w = 0.0

S_40dn1_RL = Synapses(LAL040, DNa01, '''
                    w: 1
                    I_lal40dn1_RL_post = -w*r_pre: 1 (summed)
                    ''')
S_40dn1_RL.connect(i=[0], j=[1])
S_40dn1_RL.w = 0.0

S_40dn1_LR = Synapses(LAL040, DNa01, '''
                    w: 1
                    I_lal40dn1_LR_post = -w*r_pre: 1 (summed)
                    ''')
S_40dn1_LR.connect(i=[1], j=[0])
S_40dn1_LR.w = 0.0

S_46dn1_RR = Synapses(LAL046, DNa01, '''
                    w: 1
                    I_lal46dn1_RR_post = -w*r_pre: 1 (summed)
                    ''')
S_46dn1_RR.connect(i=[0], j=[0])
S_46dn1_RR.w = 0.0

S_46dn1_LL = Synapses(LAL046, DNa01, '''
                    w: 1
                    I_lal46dn1_LL_post = -w*r_pre: 1 (summed)
                    ''')
S_46dn1_LL.connect(i=[1], j=[1])
S_46dn1_LL.w = 0.0

S_dn2dn1_RR = Synapses(DNa02, DNa01, '''
                    w: 1
                    I_dn2dn1_RR_post = w*r_pre: 1 (summed)
                    ''')
S_dn2dn1_RR.connect(i='j')
S_dn2dn1_RR.w = 0.0

S_lal126dn1 = Synapses(LAL126, DNa01, '''
                    w: 1
                    I_lal126dn1_post = w*r_pre: 1 (summed)
                    ''')
S_lal126dn1.connect(i=[0, 2], j=[1])
S_lal126dn1.connect(i=[1, 3], j=[0])
S_lal126dn1.w = 0.0

S_lal17dn1 = Synapses(LAL017, DNa01, '''
                    w: 1
                    I_lal17dn1_post = w*r_pre: 1 (summed)
                    ''')
S_lal17dn1.connect(i='j')
S_lal17dn1.w = 0.0

# DNa02
S_pfdn2 = Synapses(PFL3, DNa02, '''
                    w: 1
                    I_pfl3_post = w*r_pre: 1 (summed)
                    ''')
S_pfdn2.connect(i=[0,2,4,6,8,10,12,14,16,18,20,22],j=0)
S_pfdn2.connect(i=[1,3,5,7,9,11,13,15,17,19,21,23],j=1)
S_pfdn2.w = 0.0

S_10dn2_RR = Synapses(LAL010, DNa02, '''
                    w: 1
                    I_lal10dn2_RR_post = w*r_pre: 1 (summed)
                    ''')
S_10dn2_RR.connect(i=[0], j=[0])
S_10dn2_RR.w = 0.0

S_10dn2_LL = Synapses(LAL010, DNa02, '''
                    w: 1
                    I_lal10dn2_LL_post = w*r_pre: 1 (summed)
                    ''')
S_10dn2_LL.connect(i=[1], j=[1])
S_10dn2_LL.w = 0.0

S_14dn2_RR = Synapses(LAL014, DNa02, '''
                    w: 1
                    I_lal14dn2_RR_post = w*r_pre: 1 (summed)
                    ''')
S_14dn2_RR.connect(i=[0], j=[0])
S_14dn2_RR.w = 0.0

S_14dn2_LL = Synapses(LAL014, DNa02, '''
                    w: 1
                    I_lal14dn2_LL_post = w*r_pre: 1 (summed)
                    ''')
S_14dn2_LL.connect(i=[1], j=[1])
S_14dn2_LL.w = 0.0

S_18dn2_RR = Synapses(LAL018, DNa02, '''
                    w: 1
                    I_lal18dn2_RR_post = w*r_pre: 1 (summed)
                    ''')
S_18dn2_RR.connect(i=[0], j=[0])
S_18dn2_RR.w = 0.0

S_18dn2_LL = Synapses(LAL018, DNa02, '''
                    w: 1
                    I_lal18dn2_LL_post = w*r_pre: 1 (summed)
                    ''')
S_18dn2_LL.connect(i=[1], j=[1])
S_18dn2_LL.w = 0.0

S_40dn2_RL = Synapses(LAL040, DNa02, '''
                    w: 1
                    I_lal40dn2_RL_post = -w*r_pre: 1 (summed)
                    ''')
S_40dn2_RL.connect(i=[0], j=[1])
S_40dn2_RL.w = 0.0

S_40dn2_LR = Synapses(LAL040, DNa02, '''
                    w: 1
                    I_lal40dn2_LR_post = -w*r_pre: 1 (summed)
                    ''')
S_40dn2_LR.connect(i=[1], j=[0])
S_40dn2_LR.w = 0.0

S_46dn2_RR = Synapses(LAL046, DNa02, '''
                    w: 1
                    I_lal46dn2_RR_post = -w*r_pre: 1 (summed)
                    ''')
S_46dn2_RR.connect(i=[0], j=[0])
S_46dn2_RR.w = 0.0

S_46dn2_LL = Synapses(LAL046, DNa02, '''
                    w: 1
                    I_lal46dn2_LL_post = -w*r_pre: 1 (summed)
                    ''')
S_46dn2_LL.connect(i=[1], j=[1])
S_46dn2_LL.w = 0.0

S_121dn2_RL = Synapses(LAL121, DNa02, '''
                    w: 1
                    I_lal121dn2_RL_post = w*r_pre: 1 (summed)
                    ''')
S_121dn2_RL.connect(i=[0], j=[1])
S_121dn2_RL.w = 0.0

S_121dn2_LR = Synapses(LAL121, DNa02, '''
                    w: 1
                    I_lal121dn2_LR_post = w*r_pre: 1 (summed)
                    ''')
S_121dn2_LR.connect(i=[1], j=[0])
S_121dn2_LR.w = 0.0

S_126dn2 = Synapses(LAL126, DNa02, '''
                    w: 1
                    I_lal126dn2_post = w*r_pre: 1 (summed)
                    ''')
S_126dn2.connect(i=[1, 3], j=[0])
S_126dn2.connect(i=[0, 2], j=[1])
S_126dn2.w = 0.0

S_dn1dn2_RR = Synapses(DNa01, DNa02, '''
                    w: 1
                    I_dn1dn2_RR_post = w*r_pre: 1 (summed)
                    ''')
S_dn1dn2_RR.connect(i=[0], j=[0])
S_dn1dn2_RR.w = 0.0

S_dn1dn2_LL = Synapses(DNa01, DNa02, '''
                    w: 1
                    I_dn1dn2_LL_post = w*r_pre: 1 (summed)
                    ''')
S_dn1dn2_LL.connect(i=[1], j=[1])
S_dn1dn2_LL.w = 0.0

S_dn3dn2_RR = Synapses(DNa03, DNa02, '''
                    w: 1
                    I_dn3dn2_RR_post = w*r_pre: 1 (summed)
                    ''')
S_dn3dn2_RR.connect(i=[0], j=[0])
S_dn3dn2_RR.w = 0.0

S_dn3dn2_LL = Synapses(DNa03, DNa02, '''
                    w: 1
                    I_dn3dn2_LL_post = w*r_pre: 1 (summed)
                    ''')
S_dn3dn2_LL.connect(i=[1], j=[1])
S_dn3dn2_LL.w = 0.0

S_dn4dn2_LL = Synapses(DNa04, DNa02, '''
                    w: 1
                    I_dn4dn2_LL_post = w*r_pre: 1 (summed)
                    ''')
S_dn4dn2_LL.connect(i='j')
S_dn4dn2_LL.w = 0.0


# DNa03
S_pfdn3 = Synapses(PFL3, DNa03, '''
                    w: 1
                    I_pfl3_post = w*r_pre: 1 (summed)
                    ''')
S_pfdn3.connect(i=[0,2,4,6,8,10,12,14,16,18,20,22],j=0)
S_pfdn3.connect(i=[1,3,5,7,9,11,13,15,17,19,21,23],j=1)
S_pfdn3.w = 0.0

S_10dn3_RR = Synapses(LAL010, DNa03, '''
                    w: 1
                    I_lal10dn3_RR_post = w*r_pre: 1 (summed)
                    ''')
S_10dn3_RR.connect(i=[0], j=[0])
S_10dn3_RR.w = 0.0

S_10dn3_LL = Synapses(LAL010, DNa03, '''
                    w: 1
                    I_lal10dn3_LL_post = w*r_pre: 1 (summed)
                    ''')
S_10dn3_LL.connect(i=[1], j=[1])
S_10dn3_LL.w = 0.0

S_14dn3_RR = Synapses(LAL014, DNa03, '''
                    w: 1
                    I_lal14dn3_RR_post = w*r_pre: 1 (summed)
                    ''')
S_14dn3_RR.connect(i=[0], j=[0])
S_14dn3_RR.w = 0.0

S_14dn3_LL = Synapses(LAL014, DNa03, '''
                    w: 1
                    I_lal14dn3_LL_post = w*r_pre: 1 (summed)
                    ''')
S_14dn3_LL.connect(i=[1], j=[1])
S_14dn3_LL.w = 0.0

S_18dn3_RR = Synapses(LAL018, DNa03, '''
                    w: 1
                    I_lal18dn3_RR_post = w*r_pre: 1 (summed)
                    ''')
S_18dn3_RR.connect(i=[0], j=[0])
S_18dn3_RR.w = 0.0

S_18dn3_LL = Synapses(LAL018, DNa03, '''
                    w: 1
                    I_lal18dn3_LL_post = w*r_pre: 1 (summed)
                    ''')
S_18dn3_LL.connect(i=[1], j=[1])
S_18dn3_LL.w = 0.0

S_40dn3_RL = Synapses(LAL040, DNa03, '''
                    w: 1
                    I_lal40dn3_RL_post = -w*r_pre: 1 (summed)
                    ''')
S_40dn3_RL.connect(i=[0], j=[1])
S_40dn3_RL.w = 0.0

S_40dn3_LR = Synapses(LAL040, DNa03, '''
                    w: 1
                    I_lal40dn3_LR_post = -w*r_pre: 1 (summed)
                    ''')
S_40dn3_LR.connect(i=[1], j=[0])
S_40dn3_LR.w = 0.0

S_46dn3_RR = Synapses(LAL046, DNa03, '''
                    w: 1
                    I_lal46dn3_RR_post = -w*r_pre: 1 (summed)
                    ''')
S_46dn3_RR.connect(i=[0], j=[0])
S_46dn3_RR.w = 0.0

S_46dn3_LL = Synapses(LAL046, DNa03, '''
                    w: 1
                    I_lal46dn3_LL_post = -w*r_pre: 1 (summed)
                    ''')
S_46dn3_LL.connect(i=[1], j=[1])
S_46dn3_LL.w = 0.0

S_121dn3_RL = Synapses(LAL121, DNa03, '''
                    w: 1
                    I_lal121dn3_RL_post = w*r_pre: 1 (summed)
                    ''')
S_121dn3_RL.connect(i=[0], j=[1])
S_121dn3_RL.w = 0.0

S_121dn3_LR = Synapses(LAL121, DNa03, '''
                    w: 1
                    I_lal121dn3_LR_post = w*r_pre: 1 (summed)
                    ''')
S_121dn3_LR.connect(i=[1], j=[0])
S_121dn3_LR.w = 0.0

S_73dn3 = Synapses(LAL073, DNa03, '''
                    w: 1
                    I_lal73dn3_post = w*r_pre: 1 (summed)
                    ''')
S_73dn3.connect(i='j')
S_73dn3.w = 0.0

S_dn2dn3 = Synapses(DNa02, DNa03, '''
                    w: 1
                    I_dna02_post = w*r_pre: 1 (summed)
                    ''')
S_dn2dn3.connect(i='j')
S_dn2dn3.w = 0.0

S_122dn3 = Synapses(LAL122, DNa03, '''
                    w: 1
                    I_lal122dn3_post = w*r_pre: 1 (summed)
                    ''')
S_122dn3.connect(i=[0], j=[1])
S_122dn3.connect(i=[1], j=[0])
S_122dn3.w = 0.0

S_153dn3 = Synapses(LAL153, DNa03, '''
                    w: 1
                    I_lal153dn3_post = w*r_pre: 1 (summed)
                    ''')
S_153dn3.connect(i=[0], j=[1])
S_153dn3.connect(i=[1], j=[0])
S_153dn3.w = 0.0

S_pfl2dn3 = Synapses(PFL2, DNa03, '''
                    w: 1
                    I_pfl2_post = w*r_pre: 1 (summed)
                    ''')
S_pfl2dn3.connect()
S_pfl2dn3.w = 0.0

# DNa04
S_pfdn4 = Synapses(PFL3, DNa04, '''
                    w: 1
                    I_pfl3_post = w*r_pre: 1 (summed)
                    ''')
S_pfdn4.connect(i=[0,2,4,6,8,10,12,14,16,18,20,22],j=0)
S_pfdn4.connect(i=[1,3,5,7,9,11,13,15,17,19,21,23],j=1)
S_pfdn4.w = 0.0

S_10dn4_RR = Synapses(LAL010, DNa04, '''
                    w: 1
                    I_lal10dn4_RR_post = w*r_pre: 1 (summed)
                    ''')
S_10dn4_RR.connect(i=[0], j=[0])
S_10dn4_RR.w = 0.0

S_10dn4_LL = Synapses(LAL010, DNa04, '''
                    w: 1
                    I_lal10dn4_LL_post = w*r_pre: 1 (summed)
                    ''')
S_10dn4_LL.connect(i=[1], j=[1])
S_10dn4_LL.w = 0.0

S_18dn4_RR = Synapses(LAL018, DNa04, '''
                    w: 1
                    I_lal18dn4_RR_post = w*r_pre: 1 (summed)
                    ''')
S_18dn4_RR.connect(i=[0], j=[0])
S_18dn4_RR.w = 0.0

S_18dn4_LL = Synapses(LAL018, DNa04, '''
                    w: 1
                    I_lal18dn4_LL_post = w*r_pre: 1 (summed)
                    ''')
S_18dn4_LL.connect(i=[1], j=[1])
S_18dn4_LL.w = 0.0

S_40dn4_RL = Synapses(LAL040, DNa04, '''
                    w: 1
                    I_lal40dn4_RL_post = -w*r_pre: 1 (summed)
                    ''')
S_40dn4_RL.connect(i=[0], j=[1])
S_40dn4_RL.w = 0.0

S_40dn4_LR = Synapses(LAL040, DNa04, '''
                    w: 1
                    I_lal40dn4_LR_post = -w*r_pre: 1 (summed)
                    ''')
S_40dn4_LR.connect(i=[1], j=[0])
S_40dn4_LR.w = 0.0

S_46dn4_RR = Synapses(LAL046, DNa04, '''
                    w: 1
                    I_lal46dn4_RR_post = -w*r_pre: 1 (summed)
                    ''')
S_46dn4_RR.connect(i=[0], j=[0])
S_46dn4_RR.w = 0.0

S_46dn4_LL = Synapses(LAL046, DNa04, '''
                    w: 1
                    I_lal46dn4_LL_post = -w*r_pre: 1 (summed)
                    ''')
S_46dn4_LL.connect(i=[1], j=[1])
S_46dn4_LL.w = 0.0

S_dn2dn4_RR = Synapses(DNa02, DNa04, '''
                    w: 1
                    I_dn2dn4_RR_post = w*r_pre: 1 (summed)
                    ''')
S_dn2dn4_RR.connect(i='j')
S_dn2dn4_RR.w = 0.0

S_dn3dn4_RR = Synapses(DNa03, DNa04, '''
                    w: 1
                    I_dn3dn4_RR_post = w*r_pre: 1 (summed)
                    ''')
S_dn3dn4_RR.connect(i=[0], j=[0])
S_dn3dn4_RR.w = 0.0

S_dn3dn4_LL = Synapses(DNa03, DNa04, '''
                    w: 1
                    I_dn3dn4_LL_post = w*r_pre: 1 (summed)
                    ''')
S_dn3dn4_LL.connect(i=[1], j=[1])
S_dn3dn4_LL.w = 0.0

# DNg13
S_14dn13_RR = Synapses(LAL014, DNg13, '''
                    w: 1
                    I_lal014dn13_RR_post = w*r_pre: 1 (summed)
                    ''')
S_14dn13_RR.connect(i=[0], j=[0])
S_14dn13_RR.w = 0.0

S_14dn13_LL = Synapses(LAL014, DNg13, '''
                    w: 1
                    I_lal014dn13_LL_post = w*r_pre: 1 (summed)
                    ''')
S_14dn13_LL.connect(i=[1], j=[1])
S_14dn13_LL.w = 0.0

S_18dn13 = Synapses(LAL018, DNg13, '''
                    w: 1
                    I_lal018dn13_post = w*r_pre: 1 (summed)
                    ''')
S_18dn13.connect(i='j')
S_18dn13.w = 0.0

S_40dn13_RL = Synapses(LAL040, DNg13, '''
                    w: 1
                    I_lal040dn13_RL_post = -w*r_pre: 1 (summed)
                    ''')
S_40dn13_RL.connect(i=[0], j=[1])
S_40dn13_RL.w = 0.0

S_40dn13_LR = Synapses(LAL040, DNg13, '''
                    w: 1
                    I_lal040dn13_LR_post = -w*r_pre: 1 (summed)
                    ''')
S_40dn13_LR.connect(i=[1], j=[0])
S_40dn13_LR.w = 0.0

S_46dn13_RR = Synapses(LAL046, DNg13, '''
                    w: 1
                    I_lal046dn13_RR_post = -w*r_pre: 1 (summed)
                    ''')
S_46dn13_RR.connect(i=[0], j=[0])
S_46dn13_RR.w = 0.0

S_46dn13_LL = Synapses(LAL046, DNg13, '''
                    w: 1
                    I_lal046dn13_LL_post = -w*r_pre: 1 (summed)
                    ''')
S_46dn13_LL.connect(i=[1], j=[1])
S_46dn13_LL.w = 0.0

S_73dn13 = Synapses(LAL073, DNg13, '''
                    w: 1
                    I_lal73dn13_post = w*r_pre: 1 (summed)
                    ''')
S_73dn13.connect(i=[0], j=[1])
S_73dn13.connect(i=[1], j=[0])
S_73dn13.w = 0.0

S_dn1dn13_RR = Synapses(DNa01, DNg13, '''
                    w: 1
                    I_dn1dn13_RR_post = w*r_pre: 1 (summed)
                    ''')
S_dn1dn13_RR.connect(i=[0], j=[0])
S_dn1dn13_RR.w = 0.0

S_dn1dn13_LL = Synapses(DNa01, DNg13, '''
                    w: 1
                    I_dn1dn13_LL_post = w*r_pre: 1 (summed)
                    ''')
S_dn1dn13_LL.connect(i=[1], j=[1])
S_dn1dn13_LL.w = 0.0

#########Monitor#########
trace = StateMonitor(PFL3, ('r','G','H'), record=True)
trace_FC2 = StateMonitor(FC2, ('r','I_FC2'), record=True)
trace_pfl2 = StateMonitor(PFL2, ('r', 'Ihead_2'), record=True)
trace_head = StateMonitor(headinput, ('r','Iin'), record=True)
trace_lal010 = StateMonitor(LAL010, ('r','I_pfl3'), record=True)
trace_lal014 = StateMonitor(LAL014, ('r','I_pfl3'), record=True)
trace_lal018 = StateMonitor(LAL018, ('r','I_pfl3'), record=True)
trace_lal040 = StateMonitor(LAL040, ('r','I_pfl3'), record=True)
trace_lal046 = StateMonitor(LAL046, ('r','I_pfl3'), record=True)
trace_lal121 = StateMonitor(LAL121, ('r','I_pfl3'), record=True)
trace_lal073 = StateMonitor(LAL073, ('r','I_pfl3'), record=True)
trace_lal141 = StateMonitor(LAL141, ('r','I_pfl3'), record=True)
trace_lal122 = StateMonitor(LAL122, ('r','I_pfl3'), record=True)
trace_lal126 = StateMonitor(LAL126, ('r','I_pfl3'), record=True)
trace_lal017 = StateMonitor(LAL017, ('r','I'), record=True)
trace_lal153 = StateMonitor(LAL153, ('r','I'), record=True)
trace_DNa01 = StateMonitor(DNa01, ('r'), record=True)
trace_DNa02 = StateMonitor(DNa02, ('r'), record=True)
trace_DNa03 = StateMonitor(DNa03, ('r'), record=True)
trace_DNa04 = StateMonitor(DNa04, ('r'), record=True)
trace_DNg13 = StateMonitor(DNg13, ('r'), record=True)

#########Input#########

#input neuron
inhead = NeuronGroup(8,'''dr/dt = (-r + I_inhead + I_inheadin + Iin)/tau : 1
            tau : second
            I_inhead : 1
            I_inheadin : 1
            Iin : 1''',threshold='r<0',reset='r=0', method='euler')
inheadin = NeuronGroup(1,'''dr/dt = (-r + I_inhead)/tau : 1
            tau : second
            I_inhead : 1
           ''',threshold='r<0',reset='r=0', method='euler')
ingoal = NeuronGroup(12,'''dr/dt = (-r + I_ingoal + I_ingoalin + Iin)/tau : 1
            tau : second
            I_ingoal : 1
            I_ingoalin : 1       
            Iin : 1''',threshold='r<0',reset='r=0', method='euler')
ingoalin =  NeuronGroup(1,'''dr/dt = (-r + I_ingoal)/tau : 1
            tau : second
            I_ingoal : 1
            ''',threshold='r<0',reset='r=0', method='euler')

ingoal.r = 0
ingoalin.r = 0
inhead.r = 0
inheadin.r = 0

ingoal.tau = 10*ms
ingoalin.tau = 10*ms
inhead.tau = 10*ms
inheadin.tau = 10*ms

#inputsynapse
###head###
S_inhead = Synapses(inhead, inhead, '''
             w : 1 # synaptic weight
             I_inhead_post = w * r_pre : 1 (summed)
             ''')
S_inhead.connect(condition='abs(i-j)==1 and i!=j')
S_inhead.connect(i=7,j=0)
S_inhead.connect(i=0,j=7)

S_inheadIn = Synapses(inhead, inheadin, '''
             w : 1 # synaptic weight
             I_inhead_post = w * r_pre : 1 (summed)
             ''')
for k in range(0,8):
    S_inheadIn.connect(i=k,j=0)

S_inheadin = Synapses(inheadin, inhead, '''
             w : 1 # synaptic weight
             I_inheadin_post = - w * r_pre : 1 (summed)
             ''')
for k in range(0,8):
    S_inheadin.connect(i=0,j=k)
####goal####
S_ingoal = Synapses(ingoal, ingoal, '''
             w : 1 # synaptic weight
             I_ingoal_post = w * r_pre : 1 (summed)
             ''')
S_ingoal.connect(condition='abs(i-j)==1 and i!=j')
S_ingoal.connect(i=11,j=0)
S_ingoal.connect(i=0,j=11)

S_ingoalIn = Synapses(ingoal, ingoalin, '''
             w : 1 # synaptic weight
             I_ingoal_post = w * r_pre : 1 (summed)
             ''')
for k in range(0,12):
    S_ingoalIn.connect(i=k,j=0)

S_ingoalin = Synapses(ingoalin, ingoal, '''
             w : 1 # synaptic weight
             I_ingoalin_post = - w * r_pre : 1 (summed)
             ''')
for k in range(0,12):
    S_ingoalin.connect(i=0,j=k)

S_inhead.w = 0.553 #EE
S_inheadIn.w = 0.045#EI
S_inheadin.w = 0.65 #IE

S_ingoal.w = 0.54 #EE
S_ingoalIn.w = 0.015#EI
S_ingoalin.w = 0.95 #IE

###to the system###
S_inhead_head = Synapses(inhead,headinput, '''
             w : 1 # synaptic weight
             Iin_post = w * r_pre : 1 (summed)
             ''')
S_inhead_head.connect(i=0,j=7)
S_inhead_head.connect(i=1,j=8)
S_inhead_head.connect(i=2,j=[0,9])
S_inhead_head.connect(i=3,j=[1,10])
S_inhead_head.connect(i=4,j=[2,12])
S_inhead_head.connect(i=5,j=[3,13])
S_inhead_head.connect(i=6,j=[5,14])
S_inhead_head.connect(i=7,j=[6,15])

S_inhead_head_411 = Synapses(inhead,headinput, '''
             w : 1 # synaptic weight
             Iin_1_post = w * r_pre : 1 (summed)
             ''')
S_inhead_head_411.connect(i=5,j=4)
S_inhead_head_411.connect(i=3,j=11)
S_inhead_head_411_2 = Synapses(inhead,headinput, '''
             w : 1 # synaptic weight
             Iin_2_post = w * r_pre : 1 (summed)
             ''')
S_inhead_head_411_2.connect(i=6,j=4)
S_inhead_head_411_2.connect(i=4,j=11)

S_ingoal_FC2 = Synapses(ingoal,FC2, '''
             w : 1 # synaptic weight
             Iin_post = w * r_pre : 1 (summed)
             ''')
S_ingoal_FC2.connect('i==j')

S_inhead_head.w = 0.0
S_inhead_head_411.w = 0.0
S_inhead_head_411_2.w = 0.0
S_ingoal_FC2.w = 0.0

trace_inhead = StateMonitor(inhead,'r',record=True)
trace_ingoal = StateMonitor(ingoal,'r',record=True)
trace_pfl3 = StateMonitor(PFL3, ('r','G','H'), record=True)

#########Motor##########
motor = NeuronGroup(1,'''
du/dt = -u/tau + A*(I_dnR - I_dnL)/tau : 1
tau : second
I_dnR : 1
I_dnL : 1
A : 1
''', method='euler')
motor.u = 0.0
mtau = 10
motor.tau = mtau*ms
mA = 0.15
motor.A = mA

S_motor_R = Synapses(DNa02,motor,'''
             w : 1 # synaptic weight
             I_dnR_post = w * r_pre : 1 (summed)
             ''')
S_motor_R.connect(i=[0], j=[0])
S_motor_R.w = 1.0

S_motor_L = Synapses(DNa02,motor,'''
             w : 1 # synaptic weight
             I_dnL_post = w * r_pre : 1 (summed)
             ''')
S_motor_L.connect(i=[1], j=[0])
S_motor_L.w = 1.0

trace_motor = StateMonitor(motor,'u',record=True)

#########Weight#########

sigma = float(sys.argv[1])
weight = 1.5
S_pfpc.w = 1.5
S_pfpc_2.w = 1.5
S_pfhead.w = weight
S_pfhead_2.w = weight
S_inhead_head.w = 0.3
S_inhead_head_411.w = 0.3
S_inhead_head_411_2.w = 0.3
S_ingoal_FC2.w = 0.3
modify = 1

pflal_w = paras["overall_weight"][0]["pfl_lal"]
pfl2lal_w = paras["overall_weight"][0]["pfl2_lal"]
lal_w = paras["overall_weight"][0]["lal_lal"]
dn_lal_w = paras["overall_weight"][0]["dn_lal"]
pfdn_w = paras["overall_weight"][0]["pfl_dn"]

fa = float(sys.argv[3])/100
fg = float(sys.argv[4])/100
fl = -(float(sys.argv[5])/100)

ad_10 = paras["overall_weight"][0]["lal010"]
ad_14 = paras["overall_weight"][0]["lal014"]
ad_18 = paras["overall_weight"][0]["lal018"]
ad_40 = paras["overall_weight"][0]["lal040"]
ad_46 = paras["overall_weight"][0]["lal046"]
ad_121 = paras["overall_weight"][0]["lal121"]
ad_73 = paras["overall_weight"][0]["lal073"]
ad_141 = paras["overall_weight"][0]["lal141"]
ad_122 = paras["overall_weight"][0]["lal122"]
ad_126 = paras["overall_weight"][0]["lal126"]
ad_17 = paras["overall_weight"][0]["lal017"]
ad_153 = paras["overall_weight"][0]["lal153"]
ad_dn1 = paras["overall_weight"][0]["dna01"]
ad_dn2 = paras["overall_weight"][0]["dna02"]
ad_dn3 = paras["overall_weight"][0]["dna03"]
ad_dn4 = paras["overall_weight"][0]["dna04"]
ad_dn13 = paras["overall_weight"][0]["dng13"]

S_pflal010.w = pflal_w*28.42*fa
S_pflal014.w = pflal_w*19*fa
S_pflal018.w = pflal_w*12.33*fa
S_pflal040.w = pflal_w*71.25*fa
S_pflal046.w = pflal_w*14.08*fa
S_pflal121.w = pflal_w*200.78*fa*modify     
S_pflal141.w = pflal_w*65.55*fa 
S_pflal122.w = pflal_w*9.6875*fa 
S_pflal126.w = pflal_w*23.7*fa

S_lal1410.w = lal_w*8*ad_14*fa
S_lal4010_RL.w = lal_w*46*ad_40*fg
S_lal4010_LR.w = lal_w*46*ad_40*fg
S_lal4010_RR.w = lal_w*26.5*ad_40*fg
S_lal4010_LL.w = lal_w*26.5*ad_40*fg
S_lal12110_LR.w = lal_w*245*ad_121*fl
S_lal12110_RL.w = lal_w*245*ad_121*fl
S_lal14110.w = lal_w*180.5*ad_141*fl
S_dn3lal10.w = dn_lal_w*7*ad_dn3*fa
S_pfl210.w = pfl2lal_w*8.9*fa

S_lal1014_RR.w = lal_w*25*ad_10*fa
S_lal1014_LL.w = lal_w*25*ad_10*fa
S_lal4014_RL.w = lal_w*14.5*ad_40*fg
S_lal4014_LR.w = lal_w*14.5*ad_40*fg
S_lal12114_RL.w = lal_w*123.5*ad_121*fl
S_lal12114_LR.w = lal_w*123.5*ad_121*fl
S_lal12214.w = lal_w*421*ad_122*fl
S_lal15314.w = lal_w*22.5*ad_153*fa
S_dn3lal14.w = dn_lal_w*13.5*ad_dn3*fa
S_pfl214.w = pfl2lal_w*12*fa

S_lal1018_RR.w = lal_w*53*ad_10*fa
S_lal1018_LL.w = lal_w*53*ad_10*fa
S_lal1418_RR.w = lal_w*11*ad_14*fa 
S_lal4018_RL.w = lal_w*77*ad_40*fg
S_lal4018_LR.w = lal_w*77*ad_40*fg
S_lal4618_RR.w = lal_w*12*ad_46*fg
S_lal4618_LL.w = lal_w*12*ad_46*fg
S_lal14118.w = lal_w*10*ad_141*fl
S_lal12618.w = lal_w*95*ad_126*fl
S_lal15318.w = lal_w*12*ad_153*fa
S_dn3lal18.w = dn_lal_w*73*ad_dn3*fa
S_dn2lal18.w = dn_lal_w*10*ad_dn2*fa

S_lal1040_RR.w = lal_w*26.5*ad_10*fa
S_lal1040_LL.w = lal_w*26.5*ad_10*fa
S_lal7340.w = lal_w*104.5*ad_73*fl
S_lal14140.w = lal_w*118.5*ad_141*fl

S_lal1046_RR.w = lal_w*30.5*ad_10*fa
S_lal1046_LL.w = lal_w*30.5*ad_10*fa
S_lal1846_RR.w = lal_w*37*ad_18*fa
S_lal1846_LL.w = lal_w*37*ad_18*fa
S_lal4046_RL.w = lal_w*199*ad_40*fg
S_lal4046_LR.w = lal_w*199*ad_40*fg
S_lal12146_RL.w = lal_w*62*ad_121*fl
S_lal12146_LR.w = lal_w*62*ad_121*fl
S_lal12646.w = lal_w*129.5*ad_126*fl
S_dn3lal46.w = dn_lal_w*16*ad_dn3*fa
S_dn2lal46.w = dn_lal_w*5.5*ad_dn2*fa
S_pfl246.w = pfl2lal_w*12.5*fa

S_lal46121_RR.w = lal_w*51*ad_46*fg*modify
S_lal46121_LL.w = lal_w*51*ad_46*fg*modify
S_lal121121_RL.w = lal_w*8.5*ad_121*fl*modify
S_lal121121_LR.w = lal_w*8.5*ad_121*fl*modify
S_lal73121.w = lal_w*5.5*ad_73*fl*modify
S_lal141121.w = lal_w*3*ad_141*fl*modify
S_lal17121.w = lal_w*225.5*ad_17*fa*modify

S_lal1073.w = lal_w*27.5*ad_10*fa
S_lal1473.w = lal_w*9*ad_14*fa
S_lal12173.w = lal_w*122.5*ad_121*fl
S_dn3lal73.w = dn_lal_w*76.5*ad_dn3*fa
S_lal12273.w = lal_w*16*ad_122*fl
S_lal12673.w = lal_w*25.75*ad_126*fl
S_lal15373.w = lal_w*60.5*ad_153*fa
S_pfl273.w = pfl2lal_w*23.125*fa

S_lal73141.w = lal_w*153*ad_73*fl
S_lal40141_RRLL = lal_w*8*ad_40*fg
S_lal40141_RLLR = lal_w*52*ad_40*fg
S_lal10141.w = lal_w*2.5*ad_10*fa
S_lal121141.w = lal_w*2.5*ad_121*fl

S_lal10122.w = lal_w*5*ad_10*fa
S_lal14122.w = lal_w*8*ad_14*fa
S_lal46122.w = lal_w*9*ad_46*fg
S_lal40122.w = lal_w*22*ad_40*fg
S_dn3lal122_RRLL.w = dn_lal_w*5*ad_dn3*fa
S_dn3lal122_RLLR.w = dn_lal_w*3*ad_dn3*fa
S_lal17122_RRLL.w = lal_w*237.5*ad_17*fa
S_lal17122_RLLR.w = lal_w*104.5*ad_17*fa
S_lal153122_RLLR.w = lal_w*83.5*ad_153*fa
S_lal153122_RRLL.w = lal_w*6*ad_153*fa

S_lal46126.w = lal_w*141.25*ad_46*fg
S_lal18126.w = lal_w*11.25*ad_18*fa
S_lal73126.w = lal_w*17.5*ad_73*fl
S_lal40126.w = lal_w*4.25*ad_40*fg
S_lal17126.w = lal_w*82.5*ad_17*fa


S_lal1017.w = lal_w*5*ad_10*fa
S_dn3lal17.w = dn_lal_w*ad_dn3*fa*7
S_lal12217.w = lal_w*435.5*ad_122*fl
S_lal15317.w = lal_w*73*ad_153*fa
S_lal12117.w = lal_w*2.5*ad_121*fl

S_lal10153.w = lal_w*23*ad_10*fa
S_lal14153.w = lal_w*5*ad_14*fa
S_lal40153.w = lal_w*18.5*ad_40*fg
S_lal122153_RRLL.w = lal_w*8*ad_122*fl
S_lal122153_RLLR.w = lal_w*259.5*ad_122*fl
S_lal153153.w = lal_w*22.5*ad_153*fa

laldn_w = paras["overall_weight"][0]["lal_dn"]

S_14dn1_RR.w = laldn_w*38.5*ad_14*fa
S_14dn1_LL.w = laldn_w*38.5*ad_14*fa
S_18dn1_RR.w = laldn_w*11*ad_18*fa
S_18dn1_LL.w = laldn_w*11*ad_18*fa
S_40dn1_RL.w = laldn_w*125.5*ad_40*fg
S_40dn1_LR.w = laldn_w*125.5*ad_40*fg
S_46dn1_RR.w = laldn_w*9*ad_46*fg
S_46dn1_LL.w = laldn_w*9*ad_46*fg
S_lal126dn1.w = laldn_w*101.75*ad_126*fl
S_lal17dn1.w = laldn_w*7.5*ad_17*fa

S_pfdn2.w = pfdn_w*30.56*fa
S_10dn2_RR.w = laldn_w*136*ad_10*fa
S_10dn2_LL.w = laldn_w*136*ad_10*fa
S_14dn2_RR.w = laldn_w*8*ad_14*fa
S_14dn2_LL.w = laldn_w*8*ad_14*fa
S_18dn2_RR.w = laldn_w*184*ad_18*fa
S_18dn2_LL.w = laldn_w*184*ad_18*fa
S_40dn2_RL.w = laldn_w*121*ad_40*fg
S_40dn2_LR.w = laldn_w*121*ad_40*fg
S_46dn2_RR.w = laldn_w*147.5*ad_46*fg
S_46dn2_LL.w = laldn_w*147.5*ad_46*fg
S_121dn2_RL.w = laldn_w*8*ad_121*fl
S_121dn2_LR.w = laldn_w*8*ad_121*fl
S_126dn2.w = laldn_w*98.75*ad_126*fl

S_pfdn3.w = pfdn_w*26.56*fa
S_10dn3_RR.w = laldn_w*107*ad_10*fa
S_10dn3_LL.w = laldn_w*107*ad_10*fa
S_14dn3_RR.w = laldn_w*388.5*ad_14*fa
S_14dn3_LL.w = laldn_w*388.5*ad_14*fa
S_18dn3_RR.w = laldn_w*9.5*ad_18*fa
S_18dn3_LL.w = laldn_w*9.5*ad_18*fa
S_40dn3_RL.w = laldn_w*56*ad_40*fg
S_40dn3_LR.w = laldn_w*56*ad_40*fg
S_46dn3_RR.w = laldn_w*22*ad_46*fg
S_46dn3_LL.w = laldn_w*22*ad_46*fg
S_121dn3_RL.w = laldn_w*409.5*ad_121*fl
S_121dn3_LR.w = laldn_w*409.5*ad_121*fl
S_73dn3.w = laldn_w*8*ad_73*fl
S_122dn3.w = laldn_w*365*ad_122*fl
S_153dn3.w = laldn_w*116*ad_153*fa
S_pfl2dn3.w = pfl2lal_w*52.5*fa

S_pfdn4.w = pfdn_w*28.11*fa
S_10dn4_RR.w = laldn_w*31*ad_10*fa
S_10dn4_LL.w = laldn_w*31*ad_10*fa
S_18dn4_RR.w = laldn_w*190.5*ad_18*fa
S_18dn4_LL.w = laldn_w*190.5*ad_18*fa
S_40dn4_RL.w = laldn_w*0*ad_40*fg
S_40dn4_LR.w = laldn_w*0*ad_40*fg
S_46dn4_RR.w = laldn_w*130.5*ad_46*fg
S_46dn4_LL.w = laldn_w*130.5*ad_46*fg

S_14dn13_RR.w = laldn_w*10.7*ad_14*fa
S_14dn13_LL.w = laldn_w*10.7*ad_14*fa
S_18dn13.w = laldn_w*1*ad_18*fa
S_40dn13_RL.w = laldn_w*2.14*ad_40*fg
S_40dn13_LR.w = laldn_w*2.14*ad_40*fg
S_46dn13_RR.w = laldn_w*2*ad_46*fg
S_46dn13_LL.w = laldn_w*2*ad_46*fg
S_73dn13.w = laldn_w*227.5*ad_73*fl

w_dndn = paras["overall_weight"][0]["dn_dn"]

S_dn2dn1_RR.w = w_dndn*6*fa

S_dn1dn2_RR.w = w_dndn*6.5*fa
S_dn1dn2_LL.w = w_dndn*6.5*fa
S_dn3dn2_RR.w = w_dndn*257*fa
S_dn3dn2_LL.w = w_dndn*257*fa
S_dn4dn2_LL.w = w_dndn*5*fa 

S_dn2dn3.w = w_dndn*10*fa

S_dn2dn4_RR.w = w_dndn*6*fa
S_dn3dn4_RR.w = w_dndn*10*fa
S_dn3dn4_LL.w = w_dndn*10*fa

S_dn1dn13_RR.w = w_dndn*10.5*fa
S_dn1dn13_LL.w = w_dndn*10.5*fa



##########Simulation#########
def angle_diff(a, b):
    diff = abs(a - b) % 360
    return min(diff, 360 - diff)

@network_operation(dt=1*ms)
def custom_network_operation(t):
    global initialgoal, head, goal

    # LAL121[0].r = 0
    # Phase 1: 0 ~ 50 ms - 初始設定
    if t < 50*ms:
        if t == 0*ms:
            initialgoal = int(sys.argv[2])
            head = initialgoal   # 設定頭部角度
            goal = initialgoal      # 設定目標角度
            # 呼叫 inputhead 與 inputgoal 取得相關參數，並將它們儲存為函數屬性
            custom_network_operation.headn1, custom_network_operation.headn2, custom_network_operation.hIn1, custom_network_operation.hIn2 = inputhead(head)
            custom_network_operation.goaln1, custom_network_operation.goaln2, custom_network_operation.gIn1, custom_network_operation.gIn2 = inputgoal(goal)
            inhead.Iin[custom_network_operation.headn2] = custom_network_operation.hIn2
            inhead.Iin[custom_network_operation.headn1] = custom_network_operation.hIn1
            ingoal.Iin[custom_network_operation.goaln2] = custom_network_operation.gIn2
            ingoal.Iin[custom_network_operation.goaln1] = custom_network_operation.gIn1

    # Phase 2: 50 ~ 51 ms - 重置目標神經元輸入
    elif t < 51*ms:
        ingoal.Iin[custom_network_operation.goaln2] = 0
        ingoal.Iin[custom_network_operation.goaln1] = 0

    # Phase 3: 51 ~ 101 ms - 更新頭部與目標 (將 goal 設為初始參數 initialgoal)
    elif t < 101*ms:
        if not hasattr(custom_network_operation, 'phase3_done'):
            head = initialgoal
            goal = 180
            custom_network_operation.headn1, custom_network_operation.headn2, custom_network_operation.hIn1, custom_network_operation.hIn2 = inputhead(head)
            custom_network_operation.goaln1, custom_network_operation.goaln2, custom_network_operation.gIn1, custom_network_operation.gIn2 = inputgoal(goal)
            inhead.Iin[custom_network_operation.headn2] = custom_network_operation.hIn2
            inhead.Iin[custom_network_operation.headn1] = custom_network_operation.hIn1
            ingoal.Iin[custom_network_operation.goaln2] = custom_network_operation.gIn2
            ingoal.Iin[custom_network_operation.goaln1] = custom_network_operation.gIn1
            print(ingoal.Iin[custom_network_operation.goaln2])
            PFL3.H = head
            PFL2.H = head
            custom_network_operation.phase3_done = True

    # Phase 4: 101 ~ 102 ms - 再次重置目標神經元輸入
    elif t < 102*ms:
        inhead.Iin[custom_network_operation.headn2] = 0
        inhead.Iin[custom_network_operation.headn1] = 0
        print(inhead.Iin[custom_network_operation.headn2])

    # Phase 5: t >= 102 ms - 進入主迴圈更新動作
    else:
        if not hasattr(custom_network_operation, 'loop_initialized'):
            custom_network_operation.loop_initialized = True
            custom_network_operation.ntime = 0
            custom_network_operation.stime = 991  # 起始索引
            custom_network_operation.curtime = custom_network_operation.stime
            custom_network_operation.check = 0
            # 記錄轉向、達到及平衡的時間
            custom_network_operation.turntime = None
            custom_network_operation.reachtime = None
            custom_network_operation.eqtime = None
            
        if t > 200*ms :   
            LAL153[1].I = int(sys.argv[6]) / 10.0
            LAL017[0].I = int(sys.argv[7]) / 10.0

        # 取得 trace_motor[0].u 區段的平均值作為轉向輸入
        turn = np.average(trace_motor[0].u[custom_network_operation.curtime:custom_network_operation.curtime+9])
        custom_network_operation.ntime += 1
        custom_network_operation.curtime = custom_network_operation.stime + custom_network_operation.ntime * 10
        head = (head - turn) % 360
        PFL3.H = head
        PFL2.H = head

        if custom_network_operation.check == 0 and angle_diff(initialgoal, head) > 1:
            custom_network_operation.turntime = custom_network_operation.curtime
            custom_network_operation.check = 1
        if abs(head-goal) <= 1.5 and custom_network_operation.check == 1:
            custom_network_operation.reachtime = custom_network_operation.curtime
            custom_network_operation.check = 2
        elif custom_network_operation.check == 2:
            if abs(turn) < 0.0001:
                custom_network_operation.eqtime = custom_network_operation.curtime
                f2 = open('Fullmodel.txt','a+')
                print(initialgoal,",",custom_network_operation.turntime,",",custom_network_operation.reachtime,",",custom_network_operation.eqtime,",",head,",",current_seed,file =f2)
                stop()
                #print("模擬結束，終止時間: ", custom_network_operation.eqtime)

        # 依據新的 goal 值重新取得目標神經元輸入參數
        custom_network_operation.headn1, custom_network_operation.headn2, custom_network_operation.hIn1, custom_network_operation.hIn2 = inputhead(head)
        inhead.Iin[custom_network_operation.headn2] = custom_network_operation.hIn2
        inhead.Iin[custom_network_operation.headn1] = custom_network_operation.hIn1
    
        if t >= 3199*ms:
            f2 = open('Fullmodel.txt','a+')
            print(initialgoal,",",custom_network_operation.turntime,",",custom_network_operation.reachtime,",",custom_network_operation.eqtime,",",head,",",current_seed,file =f2)
            stop() 
    



run(3200*ms)

# f2 = open('data.txt','a+')
# print(initialgoal,",",turntime,",",reachtime,",",eqtime,",",head,",",current_seed,file =f2)

fig,ax1 = plt.subplots()
ax2=ax1.twinx()
ax1.plot(trace_DNa02[0].t,trace_DNa02[0].r,color = "red",label="DNa02_R")
ax1.plot(trace_DNa02[1].t,trace_DNa02[1].r,color = "blue",label="DNa02_L")
ax2.scatter(trace_pfl3[1].t,trace_pfl3[1].H,color = "green",s=1,label="Head angle")
ax2.axhline(y=180,color = "red",label="180 dgree",linestyle='--')
ax1.set_xlabel('time(s)')
ax1.set_ylabel('r')
ax1.set_ylim(0,1.1)
ax2.set_ylabel('head angle')
ax2.set_ylim(0,360)
fig.legend(bbox_to_anchor=(0.9,0.4))
plt.savefig("cl11-1.png")

# Create and save the first set of subplots
fig, axs = plt.subplots(2, 3, sharex=False, sharey=False, figsize=[10, 8])
fig.suptitle('LAL_r')

# Define data for the first set of plots
lal_data = [
    (trace_lal010, 'LAL010'),
    (trace_lal014, 'LAL014'),
    (trace_lal018, 'LAL018'),
    (trace_lal040, 'LAL040'),
    (trace_lal046, 'LAL046'),
    (trace_lal121, 'LAL121')
]

# Plot each dataset
for ax, (data, title) in zip(axs.flat, lal_data):
    ax.plot(trace[0].t, data[0].r, color='red', label=f'right {title.lower()}')
    ax.plot(trace[0].t, data[1].r, color='blue', label=f'left {title.lower()}')
    ax.set_ylim(0, 1.1)
    ax.title.set_text(title)
    ax.set_ylabel('r')
    ax.legend(fontsize='small', loc='upper right', bbox_to_anchor=(1.1, 1.05))

# Add a common x-axis label
fig.text(0.5, 0.04, 'time (ms)', ha='center')

plt.savefig("11lal-a.png")

# Create and save the second set of subplots
fig, axs = plt.subplots(2, 3, sharex=False, sharey=False, figsize=[10, 8])
fig.suptitle('LAL_r')

# Define data for the second set of plots
lal_data2 = [
    (trace_lal073, 'LAL073'),
    (trace_lal126, 'LAL126'),
    (trace_lal122, 'LAL122'),
    (trace_lal017, 'LAL017'),
    (trace_lal153, 'LAL153')
]

# Plot each dataset
for ax, (data, title) in zip(axs.flat, lal_data2):
    ax.plot(trace[0].t, data[0].r, color='red', label=f'right {title.lower()}')
    ax.plot(trace[0].t, data[1].r, color='blue', label=f'left {title.lower()}')
    ax.set_ylim(0, 1.1)
    ax.title.set_text(title)
    ax.set_ylabel('r')
    ax.legend()

# Add a common x-axis label
fig.text(0.5, 0.04, 'time (ms)', ha='center')

plt.savefig("11lal-b.png")

# Create and save the third set of subplots
fig, axs = plt.subplots(2, 3, sharex=True, sharey=False)
fig.suptitle('DNs_r')

# Define data for the third set of plots
dn_data = [
    (trace_DNa01, 'DNa01'),
    (trace_DNa02, 'DNa02'),
    (trace_DNa03, 'DNa03'),
    (trace_DNa04, 'DNa04'),
    (trace_DNg13, 'DNg13')
]

# Plot each dataset
for ax, (data, title) in zip(axs.flat, dn_data):
    ax.plot(trace[0].t, data[0].r, color='red', label=f'right {title.lower()}')
    ax.plot(trace[0].t, data[1].r, color='blue', label=f'left {title.lower()}')
    ax.set_ylim(0, 1.1)
    ax.title.set_text(title)
    ax.set_ylabel('r')
    ax.legend()

# Add a common x-axis label
fig.text(0.5, 0.04, 'time (ms)', ha='center')

plt.savefig("11dn-a.png")

end  = time.time()
print("run time:",end - start,"s")
from brian2 import *
import matplotlib.pyplot as plt
import numpy as np
import time
import sys
import json

start = time.time()
print("START!!")

f = open("para_0701v14-4.json")
paras = json.load(f)

seed_ = np.random.randint(10000)
f3 = open("seed1014.txt",'a+')
print(f'{seed_}\n',file = f3)
seed(seed_)

# fa = 0.4
# fg = 0.1
# fl = -0.08
fa = 0.22
fg = 0.1
fl = -0.07
###input angle
inp_g = 180


inp_h = int(sys.argv[1])

goal_angle = [15,45,75,105,135,165,195,225,255,285,315,345]
head_angle = [337.5,22.5,67.5,112.5,157.5,202.5,247.5,292.5]

pfl2_head = [360, 45, 90, 135, 180, 225, 270, 315 ]

goaln1 = 999999
goaln2 = 999999

headn1 = 999999
headn2 = 999999

headn1_pfl2 = 999999
headn2_pfl2 = 999999

#####goal#####
for k in range(0,11):
    if inp_g == goal_angle[k]:
        goaln1 = k
        break
    if inp_g == 345:
        goaln1=345
        break
    if inp_g > 345 or inp_g <15:
        goaln1 = 11
        goaln2 = 0
        break
    if inp_g > goal_angle[k] and inp_g < goal_angle[k+1] :
        goaln1 = k
        goaln2 = k+1
        break


ratio_g = 0

if inp_g < 15:
    ratio_g = (inp_g+15)/30
elif inp_g > 345:
    ratio_g = (360-inp_g)/30
elif inp_g == 360:
    ratio_g = 0.5
elif goaln2 == 999999:
    ratio_g = 0
    goaln2 = goaln1
else:
    ratio_g = (inp_g-goal_angle[goaln1])/30

gIn1 = 1*(1-ratio_g)
gIn2 = 1*ratio_g



#####head#####
for k in range(1,7):
    if inp_h == head_angle[k]:
        headn1 = inp_h
        break
    elif inp_h > 337.5 or inp_h < 22.5:
        headn1 = 0
        headn2 = 1
        break
    elif inp_h > 292.5 and inp_h <337.5:
        headn1 = 7
        headn2 = 0
        break
    elif inp_h > head_angle[k] and inp_h < head_angle[k+1] :
        headn1 = k
        headn2 = k+1
        break

ratio_h =0

if inp_h < 22.5:
    ratio_h = (inp_h+22.5)/45
elif inp_h > 337.5:
    ratio_h = (360-inp_h)/45
elif inp_h == 360:
    ratio_h = 0.5
elif headn2 == 999999:
    ratio_h = 0
    headn2 = headn1
else:
    ratio_h = (inp_h-head_angle[headn1])/45

hIn1 = 1*(1-ratio_h)
hIn2 = 1*ratio_h

#########PFL2################
print('pfl2')
for k in range(8):
    if inp_h == pfl2_head[k]:
        headn1_pfl2 = inp_h
        break
    elif inp_h > 360 or inp_h < 45:
        headn1_pfl2 = 0
        headn2_pfl2 = 1
        break
    elif inp_h > 315 and inp_h <360:
        headn1_pfl2 = 7
        headn2_pfl2 = 0
        break
    elif inp_h >= pfl2_head[k] and inp_h <= pfl2_head[k+1] :
        print(k)
        headn1_pfl2 = k
        headn2_pfl2 = k+1
        break

ratio_h =0

if inp_h < 45:
    ratio_h = (inp_h+45)/45
elif inp_h > 315:
    ratio_h = (360-inp_h)/45
elif inp_h == 360:
    ratio_h = 0.5
elif headn2_pfl2 == 999999:
    ratio_h = 0
    headn2_pfl2 = headn1_pfl2
else:
    ratio_h = (inp_h-pfl2_head[headn1_pfl2])/45

# hIn1_pfl2 = 1*(1-ratio_h)
# hIn2_pfl2 = 1*ratio_h
headn1_pfl2 = headn1
headn2_pfl2 = headn2
hIn1_pfl2 = hIn1
hIn2_pfl2 = hIn2

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

sigma = 0

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

headinput_pfl2 = NeuronGroup(16,'''
dr/dt = (-r +Iin+(Iin_1+Iin_2)/2)/tau : 1
tau : second
Iin : 1
Iin_1 : 1
Iin_2 : 1
''',threshold='r<0',reset='r=0', method='exact')

headinput_pfl2.r = 0.0
headinput_pfl2.tau = 10*ms
headinput_pfl2.Iin = 0.0
headinput_pfl2.Iin_1 = 0.0
headinput_pfl2.Iin_2 = 0.0


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
trace_lal017 = StateMonitor(LAL017, ('r'), record=True)
trace_lal153 = StateMonitor(LAL153, ('r'), record=True)
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
inhead_pfl2 = NeuronGroup(8,'''dr/dt = (-r + I_inhead_pfl2 + I_inheadin_pfl2 + Iin)/tau : 1
            tau : second
            I_inhead_pfl2 : 1
            I_inheadin_pfl2 : 1
            Iin : 1''',threshold='r<0',reset='r=0', method='euler')
inheadin_pfl2 = NeuronGroup(1,'''dr/dt = (-r + I_inhead_pfl2)/tau : 1
            tau : second
            I_inhead_pfl2 : 1
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
inhead_pfl2.r = 0
inheadin_pfl2.r = 0

ingoal.tau = 10*ms
ingoalin.tau = 10*ms
inhead.tau = 10*ms
inheadin.tau = 10*ms
inhead_pfl2.tau = 10*ms
inheadin_pfl2.tau = 10*ms

trace_inheadin = StateMonitor(inheadin, ('r'), record=True)


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
####head_pfl2####
S_inhead_pfl2 = Synapses(inhead_pfl2, inhead_pfl2, '''
             w : 1 # synaptic weight
             I_inhead_pfl2_post = w * r_pre : 1 (summed)
             ''')
S_inhead_pfl2.connect(condition='abs(i-j)==1 and i!=j')
S_inhead_pfl2.connect(i=7,j=0)
S_inhead_pfl2.connect(i=0,j=7)

S_inheadIn_pfl2 = Synapses(inhead_pfl2, inheadin_pfl2, '''
             w : 1 # synaptic weight
             I_inhead_pfl2_post = w * r_pre : 1 (summed)
             ''')
for k in range(0,8):
    S_inheadIn_pfl2.connect(i=k,j=0)

S_inheadin_pfl2 = Synapses(inheadin_pfl2, inhead_pfl2, '''
             w : 1 # synaptic weight
             I_inheadin_pfl2_post = - w * r_pre : 1 (summed)
             ''')
for k in range(0,8):
    S_inheadin_pfl2.connect(i=0,j=k)
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

S_inhead_pfl2.w = 0.553 #EE
S_inheadIn_pfl2.w = 0.045#EI
S_inheadin_pfl2.w = 0.65 #IE

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

S_inhead_head_pfl2 = Synapses(inhead_pfl2,headinput_pfl2, '''
             w : 1 # synaptic weight
             Iin_post = w * r_pre : 1 (summed)
             ''')
S_inhead_head_pfl2.connect(i=0,j=7)
S_inhead_head_pfl2.connect(i=1,j=8)
S_inhead_head_pfl2.connect(i=2,j=[0, 9])
S_inhead_head_pfl2.connect(i=3,j=[1, 10])
S_inhead_head_pfl2.connect(i=4,j=[2, 12])
S_inhead_head_pfl2.connect(i=5,j=[3, 13])
S_inhead_head_pfl2.connect(i=6,j=[5, 14])
S_inhead_head_pfl2.connect(i=7,j=[6, 15])


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


S_inhead_head_411_pfl2 = Synapses(inhead_pfl2,headinput_pfl2, '''
             w : 1 # synaptic weight
             Iin_1_post = w * r_pre : 1 (summed)
             ''')
S_inhead_head_411_pfl2.connect(i=5,j=4)
S_inhead_head_411_pfl2.connect(i=3,j=11)
S_inhead_head_411_2_pfl2 = Synapses(inhead_pfl2,headinput_pfl2, '''
             w : 1 # synaptic weight
             Iin_2_post = w * r_pre : 1 (summed)
             ''')
S_inhead_head_411_2_pfl2.connect(i=6,j=4)
S_inhead_head_411_2_pfl2.connect(i=4,j=11)

S_ingoal_FC2 = Synapses(ingoal,FC2, '''
             w : 1 # synaptic weight
             Iin_post = w * r_pre : 1 (summed)
             ''')
S_ingoal_FC2.connect('i==j')

S_inhead_head.w = 0.0
S_inhead_head_pfl2.w = 0.0
S_inhead_head_411.w = 0.0
S_inhead_head_411_2.w = 0.0
S_inhead_head_411_pfl2.w = 0.0
S_inhead_head_411_2_pfl2.w = 0.0
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
mtau = 20
motor.tau = mtau*ms
mA = 0.25
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

sigma = float(sys.argv[2])
weight = 1.5
S_pfpc.w = weight
S_pfpc_2.w = weight
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

# fa = 0.25
# fg = 0.1
# fl = -0.2

fa = 0.20
fg = 0.09
fl = -0.04

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


store()

##########Simulation#########

restore()
# run(100*ms)





ingoal[goaln2].Iin = gIn2
ingoal[goaln1].Iin = gIn1

inhead[headn2].Iin = hIn2
inhead[headn1].Iin = hIn1

inhead_pfl2[headn2_pfl2].Iin = hIn2_pfl2
inhead_pfl2[headn1_pfl2].Iin = hIn1_pfl2

for i in range(12):
    PFL3[i*2+1].Iin += 0.00000000000000001
run(800*ms)





# ingoal[goaln2].Iin = 0
# ingoal[goaln1].Iin = 0

# inhead[headn2].Iin = 0
# inhead[headn1].Iin = 0

# run(800*ms)


# fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, sharex=False, sharey=True, figsize=[10, 8])
# fig.suptitle('LAL_r')

# ax1.plot(trace_lal010[0].t/ms, trace_lal010[0].r, color='red', label='right lal010')
# ax1.plot(trace_lal010[1].t/ms, trace_lal010[1].r, color='blue', label='left lal010')
# ax1.title.set_text('LAL010')
# # print(max(trace_lal010[0].r) - max(trace_lal010[1].r))

# ax2.plot(trace_lal014[0].t/ms, trace_lal014[0].r, color='red', label='right lal014')
# ax2.plot(trace_lal014[1].t/ms, trace_lal014[1].r, color='blue', label='left lal014')
# ax2.title.set_text('LAL014')

# ax3.plot(trace_lal018[0].t/ms, trace_lal018[0].r, color='red', label='right lal018')
# ax3.plot(trace_lal018[1].t/ms, trace_lal018[1].r, color='blue', label='left lal018')
# ax3.title.set_text('LAL018')

# ax4.plot(trace_lal040[0].t/ms, trace_lal040[0].r, color='red', label='right lal040')
# ax4.plot(trace_lal040[1].t/ms, trace_lal040[1].r, color='blue', label='left lal040')
# ax4.title.set_text('LAL040')

# ax5.plot(trace_lal046[0].t/ms, trace_lal046[0].r, color='red', label='right lal046')
# ax5.plot(trace_lal046[1].t/ms, trace_lal046[1].r, color='blue', label='left lal046')
# ax5.title.set_text('LAL046')

# ax6.plot(trace_lal121[0].t/ms, trace_lal121[0].r, color='red', label='right lal121')
# ax6.plot(trace_lal121[1].t/ms, trace_lal121[1].r, color='blue', label='left lal121')
# ax6.title.set_text('LAL121')

# plt.xlabel('time (ms)')
# plt.ylabel('r')
# plt.legend()
# plt.savefig(f'./pic_{180-int(sys.argv[1])}/lal1_{sys.argv[3]}_{seed_}.png') 


# fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True, sharey=True)
# fig.suptitle('DNs_r')

# ax1.plot(trace_DNa01[0].t/ms, trace_DNa01[0].r, color='red', label='right DNa01')
# ax1.plot(trace_DNa01[1].t/ms, trace_DNa01[1].r, color='blue', label='left DNa01')
# ax1.title.set_text('DNa01')

# ax2.plot(trace_DNa02[0].t/ms, trace_DNa02[0].r, color='red', label='right DNa02')
# ax2.plot(trace_DNa02[1].t/ms, trace_DNa02[1].r, color='blue', label='left DNa02')
# ax2.title.set_text('DNa02')

# ax3.plot(trace_DNa03[0].t/ms, trace_DNa03[0].r, color='red', label='right DNa03')
# ax3.plot(trace_DNa03[1].t/ms, trace_DNa03[1].r, color='blue', label='left DNa03')
# ax3.title.set_text('DNa03')

# ax4.plot(trace_DNa04[0].t/ms, trace_DNa04[0].r, color='red', label='right DNa04')
# ax4.plot(trace_DNa04[1].t/ms, trace_DNa04[1].r, color='blue', label='left DNa04')
# ax4.title.set_text('DNa04')

# # ax5.plot(trace_DNg13[0].t/ms, trace_DNg13[0].r, color='red', label='right DNg13')
# # ax5.plot(trace_DNg13[1].t/ms, trace_DNg13[1].r, color='blue', label='left DNg13')
# # ax5.title.set_text('DNg13')

# plt.xlabel('time(ms)')
# plt.ylabel('r')
# plt.legend()
# plt.savefig(f'./pic_{180-int(sys.argv[1])}/dn_{sys.argv[3]}_{seed_}.png')

# fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, sharex=False, sharey=True, figsize=[10, 8])
# fig.suptitle('LAL_r')

# ax1.plot(trace_lal073[0].t/ms, trace_lal073[0].r, color='red', label='right lal073')
# ax1.plot(trace_lal073[1].t/ms, trace_lal073[1].r, color='blue', label='left lal073')
# ax1.title.set_text('LAL073')

# ax2.plot(trace_lal126[0].t/ms, trace_lal126[0].r, color='red', label='right lal126')
# ax2.plot(trace_lal126[1].t/ms, trace_lal126[1].r, color='blue', label='left lal126')
# ax2.title.set_text('LAL126')

# ax3.plot(trace_lal122[0].t/ms, trace_lal122[0].r, color='red', label='right lal122')
# ax3.plot(trace_lal122[1].t/ms, trace_lal122[1].r, color='blue', label='left lal122')
# ax3.title.set_text('LAL122')

# ax4.plot(trace_lal017[0].t/ms, trace_lal017[0].r, color='red', label='right lal017')
# ax4.plot(trace_lal017[1].t/ms, trace_lal017[1].r, color='blue', label='left lal017')
# ax4.title.set_text('LAL017')

# ax5.plot(trace_lal153[0].t/ms, trace_lal153[0].r, color='red', label='right lal153')
# ax5.plot(trace_lal153[1].t/ms, trace_lal153[1].r, color='blue', label='left lal153')
# ax5.title.set_text('LAL153')

# plt.xlabel('time (ms)')
# plt.ylabel('r')
# plt.legend()
# plt.savefig(f'./pic_{180-int(sys.argv[1])}/lal2_{sys.argv[3]}_{seed_}.png') 

dna1_min = np.mean(trace_DNa01[0].r) - np.mean(trace_DNa01[1].r)
dna2_min = np.mean(trace_DNa02[0].r) - np.mean(trace_DNa02[1].r)
dna3_min = np.mean(trace_DNa03[0].r) - np.mean(trace_DNa03[1].r)
dna4_min = np.mean(trace_DNa04[0].r) - np.mean(trace_DNa04[1].r)
dng13_min = np.mean(trace_DNg13[0].r) - np.mean(trace_DNg13[1].r)

# f_dn = open(f'dna02_mean_{inp_g-inp_h}_{sys.argv[4]}_no10.txt', 'a')
# f_dn.write(f'{int(sys.argv[1])-180} {dna1_min} {dna2_min} {dna3_min} {dna4_min} {dng13_min} {seed_}\n')
# f_dn.close()


f = open(f'/home/chieh1102/FPLmodel/open-loop_v5/fig3d/data_no1014/dna02_{inp_g-inp_h}_{sys.argv[2]}_{sys.argv[3]}.txt', 'a')
for i in range(len(trace_DNa02[0].r)):
    f.write(f'{i} {trace_DNa02[1].r[i]-trace_DNa02[0].r[i]}\n')
# f.close()
# f_dna02 = open(f'dna02_time_{180-int(sys.argv[1])}_{sys.argv[4]}_no10.txt', 'a')
# seperate_t = 8000
# temp = 0
# for i in range(len(trace_DNa02[0].r)):
#     if abs(trace_DNa02[0].r[i]-trace_DNa02[1].r[i]) > 0.5:
#         temp += 1
#         if temp>500:
#             seperate_t = i
#             break
#     else:
#         temp = 0

# f_dna02.write(f'{seperate_t} {seed_}\n')
# f_dna02.close()


# f_dna02 = open(f'dna02_{180-int(sys.argv[1])}_{sys.argv[4]}_no10.txt', 'a')
# satsu = 0
# for i in range(200, 600):
#     satsu += trace_DNa02[0].r[i] - trace_DNa02[1].r[i]
# f_dna02.write(f'{satsu} {seed_}\n')
# f_dna02.close()


fig, ((ax1, ax2, ax3, ax4, ax5), (ax6, ax7, ax8, ax9, ax10)) = plt.subplots(2, 5, sharex= False, sharey=True, dpi=300, figsize=[14, 8])
fig.suptitle('no Exc. Core output  Δθ = 0°', fontsize=18)

ax1.plot(trace_lal010[0].t/ms, trace_lal010[0].r, color='red', label='right lal010')
ax1.plot(trace_lal010[1].t/ms, trace_lal010[1].r, color='blue', label='left lal010')
ax1.title.set_text('LAL010')
ax1.title.set_size(16)
ax1.tick_params(axis='both', labelsize=14)
ax1.set_ylabel('firing rate', fontsize=16)

ax2.plot(trace_lal014[0].t/ms, trace_lal014[0].r, color='red', label='right lal014')
ax2.plot(trace_lal014[1].t/ms, trace_lal014[1].r, color='blue', label='left lal014')
ax2.title.set_text('LAL014')
ax2.tick_params(axis='both', labelsize=14)
ax2.title.set_size(16)


ax3.plot(trace_lal018[0].t/ms, trace_lal018[0].r, color='red', label='right lal018')
ax3.plot(trace_lal018[1].t/ms, trace_lal018[1].r, color='blue', label='left lal018')
ax3.title.set_text('LAL018')
ax3.tick_params(axis='both', labelsize=14)
ax3.title.set_size(16)

ax6.plot(trace_lal040[0].t/ms, trace_lal040[0].r, color='red', label='right lal040')
ax6.plot(trace_lal040[1].t/ms, trace_lal040[1].r, color='blue', label='left lal040')
ax6.title.set_text('LAL040')
ax6.tick_params(axis='both', labelsize=14)
ax6.set_ylabel('firing rate', fontsize=16)
ax6.title.set_size(16)

ax7.plot(trace_lal046[0].t/ms, trace_lal046[0].r, color='red', label='right lal040')
ax7.plot(trace_lal046[1].t/ms, trace_lal046[1].r, color='blue', label='left lal040')
ax7.title.set_text('LAL046')
ax7.tick_params(axis='both', labelsize=14)
ax7.title.set_size(16)

ax8.plot(trace_lal121[0].t/ms, trace_lal121[0].r, color='red', label='right lal040')
ax8.plot(trace_lal121[1].t/ms, trace_lal121[1].r, color='blue', label='left lal040')
ax8.title.set_text('LAL121')
ax8.set_xlabel('Time (ms)', fontsize=16)
ax8.tick_params(axis='both', labelsize=14)
ax8.title.set_size(16)

ax4.plot(trace_DNa01[0].t/ms, trace_DNa01[0].r, color='red', label='right DNa01')
ax4.plot(trace_DNa01[1].t/ms, trace_DNa01[1].r, color='blue', label='left DNa01')
ax4.title.set_text('DNa01')
ax4.tick_params(axis='both', labelsize=14)
ax4.title.set_size(16)

ax5.plot(trace_DNa02[0].t/ms, trace_DNa02[0].r, color='red', label='right DNa02')
ax5.plot(trace_DNa02[1].t/ms, trace_DNa02[1].r, color='blue', label='left DNa02')
ax5.title.set_text('DNa02')
ax5.tick_params(axis='both', labelsize=14)
ax5.title.set_size(16)

ax9.plot(trace_DNa03[0].t/ms, trace_DNa03[0].r, color='red', label='right DNa03')
ax9.plot(trace_DNa03[1].t/ms, trace_DNa03[1].r, color='blue', label='left DNa03')
ax9.title.set_text('DNa03')
ax9.tick_params(axis='both', labelsize=14)
ax9.title.set_size(16)

ax10.plot(trace_DNa04[0].t/ms, trace_DNa04[0].r, color='red', label='right DNa04')
ax10.plot(trace_DNa04[1].t/ms, trace_DNa04[1].r, color='blue', label='left DNa04')
ax10.title.set_text('DNa04')
ax10.tick_params(axis='both', labelsize=14)
ax10.title.set_size(16)

plt.savefig('4a.png')
# plt.savefig(f'theta90+dn_{seed_}.png') 

end  = time.time()
print("run time:",end - start,"s")



    

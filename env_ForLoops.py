#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 19:03:12 2020

@author: berlindelaguila
"""

#sup = 1: supervisor sends command to system to park in parking lot 48
#sup = 2: supervisor sends command to system to park in parking lot 49
#sup = 3: supervisor sends command to system to park in parking lot 50
#sup = 4: supervisor sends command to system to park in parking lot 51
#sup = 5: supervisor sends command to system to park in parking lot 52
#sup = 6: supervisor sends command to system to park in parking lot 53
#sup = 7: supervisor waits for message from car
#sup = 8: supervisor tells system / car to leave the garage

# sup status ransitions consist of telling auton car to wait, park, & leave lot

sup_status_transitions =[(1, [7]), (2, [1,2,3,4,5,6]), (3, [8])]

#For peds: physical state 54= state1, 55=2, 39=3, 32=4, 56=5
peds_list = [(1,[1,2]),
              (2,[2,3]),
              (3,[3,4]),
              (4,[4,5]),
              (5,[5,1])]

sup_transitions_dict = dict(sup_transitions)
peds_list_dict = dict(peds_list)
env_trans = []

#create functions


#Want to iterate thru sup states and ped states 
    # While sup is in a given state, ped can be in a specific state 
    # i.e: if sup tells auton car to park in lot 49, ped can be in state 2 or something 
    
for sup_key, sup_val in sup_status_transitions:
    print(sup_key, sup_val)
    for ped_key, ped_val in peds_list:
        print(ped_key,ped_val)
        
    

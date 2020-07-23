#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 14:40:15 2020

@author: berlindelaguila
"""
from collections import OrderedDict 

# statusCar = 1: car sends message to supervisor asking for a parking spot
# statusCar = 2: car in process of going to parking spot
# statusCar = 3: car receives a message from supervisor
# statusCar = 4: waiting for response from supervisor 


#status_transitions = [(1,[4]),(2,[3]),(3,[2]),(4,[3,4])]
#status_transitions_dict= dict(status_transitions)

status_car = [[1,[1]],[2,[2]],[3,[3]],[4,[4]]]
status_car_dict = dict(status_car)
#print(status_car[3]) 

#parking_spots = [48,49,50,51,52,53]
sys_list = [(1,[1,2]),
            (2,[16,2]),
            (3,[3,4,9]),(4,[5,6,9])]

carA_transitions = sys_list
carA_transitions_dict = dict(carA_transitions)
system_trans_list= []
#phi = lambda carA_transitions, status_car: (4 * (carA_val - 1 for carA_val in carA_transitions) + (status_val for status_val in status_car))
#phi = lambda carA_transitions, status_car: 4 * (carA_transitions - 1) + status_car

phi = lambda carA_key, status: 4 * (carA_key - 1) + status
psi = lambda end_carA_transitions, status: 4 * (end_carA_transitions - 1) + status
for status, status_val in status_car:
    #print(status,status_val)
    for carA_key, carA_val in carA_transitions: 
        #print(carA_val, status)
        start_node= phi(carA_key, status)  
        print('carA_key,status: ',carA_key ,',',status)
        print('start_node= ',start_node,'\n')
      
        #for elem in carA_val: 
          # print(elem) #iterates through each value of carA 4 times (4x bc that's the length of status_car list)
                
           #start_node= [4 * (n-1 for n in carA_val)]
          
        for end_carA_transitions in carA_val:
           #print(end_carA_transitions)
           end_node = psi(end_carA_transitions, status)
           print('end_node= ', end_node)
           system_trans_list.append((start_node, end_node))
           print('system_trans_list= ',system_trans_list)
               
             
#Want an end node and start node for each status value 

    
       #start_sys = construct_state(key, s) 
       #print(start_sys)
       
     #  end_sys = [construct_state(s, k), for k in val]
      # sys_trans.append(start_sys)
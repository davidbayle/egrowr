#!/usr/bin/python3
##
## PYTHON 3 Egrowr Collector Script
##
## Purpose: Interact and decode local Egrowr data through simple TCP socket, output json datas.
## Author: David Bayle <bayle.db@gmail.com>
## Review: Geoffrey Jaubert <jeff@egrowr.com>
## Date: 15/10/2021
## Rev: 0.4
##
## Usage: python3 egrowrCollector.py [EGROWR_IP]
## Request example: python3 egrowrCollector.py 192.168.1.25
## Answer example: {"egrowr_1011123456":{"Air_Temperature":17.6,"Air_Humidity":59.8,"Water_Temperature":16.8,"Water_EC":0.62,"Water_pH":7.88,"Light_intensity":44.5,"Uptime":840822,"Writes_on_flash":47}}
## 
#
#

import sys
import math
import socket
import time

egrowip = sys.argv[1]
egrowport = 42001
message = '*R'

## Packet decoding function to json formatted output
def egrow_decode_to_json(data): 

    serial = bitconverter32(data, 4)
    water_pH_data = bitconverter16(data, 16)
    water_pH_value = float(water_pH_data)/100
    water_eC_data = bitconverter16(data, 18)
    water_eC_value = float(water_eC_data)/100
    water_temp_data = bitconverter16(data, 20)
    water_temp_value = float(water_temp_data)/10
    air_temp_data = bitconverter16(data, 22) 
    air_temp_value = float(air_temp_data)/10
    air_humidity_data = bitconverter16(data, 24) 
    air_humidity_value = float(air_humidity_data)/10
    light_data = bitconverter16(data, 26)
    light_value = float(round((math.pow(10,(light_data - 9362) / 9362)), 1))
    time_from_powerup = bitconverter32(data, 28)
    writes_on_flash = bitconverter32(data, 36)

    print('{"egrowr_' , serial , '":{"Air_Temperature":' , air_temp_value , ',"Air_Humidity":' , air_humidity_value , ',"Water_Temperature":' , water_temp_value , ',"Water_EC":' , water_eC_value , ',"Water_pH":' , water_pH_value , ',"Light_intensity":' , light_value , ',"Uptime":' , time_from_powerup , ',"Writes_on_flash":' , writes_on_flash , '}}',  sep = '')


def bitconverter16(Byte_array,index):
    return_value = 0
    return_value = Byte_array[index]
    return_value |= (Byte_array[index+1] << 8)
    return return_value


def bitconverter32(Byte_array,index):
    return_value = 0
    return_value = Byte_array[index]
    return_value |= (Byte_array[index+1] << 8)
    return_value |= (Byte_array[index+2] << 16)
    return_value |= (Byte_array[index+3] << 24)
    return return_value


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((egrowip, egrowport))
time.sleep(0.2);
s.sendall(message.encode())
data = s.recv(104)
egrow_decode_to_json(data)
time.sleep(0.2);
s.close()

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "graesslb"
__date__ = "$09.11.2016 14:25:24$"
import numpy as np
if __name__ == "__main__":
    print rand_16(2**5)
    print "Hello World"




def rand_16(size):
    return [np.float16(np.random.uniform(0,1e-5)) for i in range(size)]

def rand_32(size):
    return [np.float32(np.random.uniform(0,1e-5)) for i in range(size)]


def sum_index16(values):
    sum=np.float16(0)
    for i in range(len(values)):
        sum += values[i]
    return sum

def sum_index32(values):
    sum=np.float32(0)
    for i in range(len(values)):
        sum += values[i]
    return sum
    
def sum_value16(values):
    sum=np.float16(0)
    values.sort()
    for i in range(len(values)):
        sum+= values[i]
    return sum

def sum_value32(values):
    sum=np.float32(0)
    values.sort()
    for i in range(len(values)):
        sum+= values[i]
    return sum

def sum_kas(values):
    return values[0] if len(values)<2 else (sum_kas(values[:len(values)/2])+sum_kas(values[len(values)/2:]))

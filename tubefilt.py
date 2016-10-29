# -*- coding: utf-8 -*-
"""
tubefilt:
a sequence of operations for calculating quantities related to the design of
low-pass filters with lossy loaded dielectrics.

Created on Sat Oct 29 02:50:18 2016

@author: Evan Mayer, evanmayer@uchicago.edu, contactevanmayer@gmail.com
"""

import math


def tubefilt(i_d, e_r, z_o):
    '''
    Length units are decimal inches, unless otherwise specified
    377 Ohms is the impedance of free space
    
    Inputs:
        i_d: float, the inner diameter of the outer conductor in a coax
            transmission line (e.g. copper pipe)
        e_r: list of floats or ints, the real part of dielectric constants of material, 
            possibly varying as a function of frequency.
        z_o: float, the impedance of the circuit passing signal to the filter.
            matching to this impedance will be attempted.
    Returns:
        o_d: list of floats, the outer diameter of the inner conductor for each
            e_r
        awg: the nearest American Wire Gauge sizes for each o_d
        delta_z: the impedance error incurred by using awg instead of od in the
            filter
    '''
    
    # From Wollack, Chuss, et al. DOI : 10.1063/1.4869038
    o_d = []
    awg = []
    for i in e_r:
        o_d.append(i_d * math.e ** (
            -2 * math.pi * z_o / (math.sqrt(1 / i) * 377)))
    for j in o_d:
        awg.append(od_to_awg(j))
    # Now, calculate the impedance of a wire with o_d determined by awg, 
    # and difference with z_o
    zo_awg = []
    delta_z = []
    for k, val in enumerate(awg):
        # diameter in inches from an awg
        sugg = 0.005 * 92 ** ((36 - val) / 39) 
        zo_awg.append((377. / 2. / math.pi) * math.sqrt(1. / e_r[k]) * 
                      math.log(i_d / sugg ))
        delta_z.append(zo_awg[k] - z_o)
    return o_d, awg, delta_z
    
    
def od_to_awg(od):
    '''
    Takes od, returns nearest AWG, according to 
    http://www.powerstream.com/Wire_Size.htm
    '''
    
    awg = (36 - (math.log(od / 0.005) / math.log(92.)) * 39.)
    return round(awg)

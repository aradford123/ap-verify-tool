#!/usr/bin/env python
from __future__ import print_function
import jtextfsm as textfsm

sample='''
QBSS Load: cca_load: 0x64, rx_load: 0x0, tx_load: 0x51
'''
sample1='''
QBSS Load: 0x1 Tx 0 Rx 0 AP 0
'''

template = open("show_controllers.textfsm")
re_table = textfsm.TextFSM(template)
fsm_results = re_table.ParseText(sample)
print (fsm_results)
print (fsm_results[0][0])

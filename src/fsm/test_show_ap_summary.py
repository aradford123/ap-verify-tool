#!/usr/bin/env python
from __future__ import print_function
import jtextfsm as textfsm
sample='''

Number of APs.................................... 2

Global AP User Name.............................. sdn
Global AP Dot1x User Name........................ Not Configured

AP Name             Slots  AP Model              Ethernet MAC       Location          Country     IP Address       Clients   DSE Location  
------------------  -----  --------------------  -----------------  ----------------  ----------  ---------------  --------  --------------
adam-ap-office       2     AIR-CAP1702I-Z-K9     b0:aa:77:4e:07:f0  default location  AU          10.10.32.2         0       [0 ,0 ,0 ]
adam-ap-branch       2     AIR-CAP1702I-Z-K9     b0:aa:77:6a:17:88  default location  AU          192.168.12.130     1       [0 ,0 ,0 ]
adam-ap-office1       2     AIR-CAP1702I-Z-K9     b0:aa:77:4e:07:f0  default location  AU          10.10.32.2         0       [0 ,0 ,0 ]
adam-ap-branch1      2     AIR-CAP1702I-Z-K9     b0:aa:77:6a:17:88  default location  AU          192.168.12.130     1       [0 ,0 ,0 ]
'''


template = open("show_ap_summary.textfsm")
re_table = textfsm.TextFSM(template)
fsm_results = re_table.ParseText(sample)
print (fsm_results)

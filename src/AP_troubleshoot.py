#!/usr/bin/env python
from __future__ import print_function
import jtextfsm as textfsm
from SSH import ssh_cisco
import re
import sys
from config import AP_USER,AP_PASSWORD,WLC_USER,WLC_PASSWORD
from argparse import ArgumentParser

    
def show_ap(host, name):
    with ssh_cisco(host, AP_USER, AP_PASSWORD ) as w:
        w.execCLI("sh controllers dot11Radio 1 | i QBSS")
        print("APview %s: %s: %s" %(host,name,w.output))
def get_ap(wlc):
    ap_template = open('fsm/show_ap_autorf.textfsm')
    ap_re_table  = textfsm.TextFSM(ap_template)
    print ("Connecting as %s@%s" %(WLC_USER, wlc))
    with ssh_cisco(wlc, WLC_USER, WLC_PASSWORD, device_type='cisco_wlc' ) as w:
        w.execCLI("sh ap summary")
        #print(w.output)
        template = open("fsm/show_ap_summary.textfsm")
        re_table = textfsm.TextFSM(template)
        fsm_results = re_table.ParseText(w.output)
	for ap_entry in fsm_results:
            ap_re_table.Reset()            
            print ("AccessPoint:%s" % ap_entry[0])
            w.execCLI('show ap auto-rf 802.11a ' + ap_entry[0])
            ap_fsm_results = ap_re_table.ParseText(w.output)[0]

            if ap_fsm_results[1] >=0:
                print ("WLCView AP:%s, TX:%s, Util:%s, Client:%s" %(ap_entry[0],ap_fsm_results[0],ap_fsm_results[1], ap_fsm_results[2]))
                w.execCLI("config ap SSH enable " + ap_entry[0])
                print ("Enable ssh for %s: %s" % (ap_entry[0],w.output))
                show_ap(ap_entry[1], ap_entry[0])
                w.execCLI("config ap SSH disable " + ap_entry[0])
                print ("Disable ssh for %s: %s" % (ap_entry[0],w.output))

if __name__ == "__main__":

    parser = ArgumentParser(description='AP_troubleshoot -w <wlc>')
    parser.add_argument('-w', '--wlc', type=str,
                        help="IP address of WLC")

    args = parser.parse_args()
    get_ap(args.wlc)
    

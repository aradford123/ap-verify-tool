#!/usr/bin/env python
from __future__ import print_function
import sys
import logging
from netmiko import ConnectHandler

class ssh_cisco(object):
    def __init__(self, ip, username, password, device_type='cisco_ios'):
        # verbose mode
#        self.kws = {'device_type': device_type, 'verbose' : True, 'ip' : ip, 'username' : username, 'password' : password, 'secret' : password}
        self.kws = {'device_type': device_type, 'ip' : ip, 'username' : username, 'password' : password, 'secret' : password, 'global_delay_factor': 2}
        #self.kws = {'device_type': device_type, 'ip' : ip, 'username' : username, 'password' : password, 'secret' : password}
        self.output=""
    def connect(self):
        self.conn = ConnectHandler(**self.kws)
        self.conn.find_prompt()
        self.conn.send_command('term len 0')

    def _ping(self):
        return True

    def __enter__(self):
        logging.debug('SSH connect session')
        self.connect()
        return self if self._ping() else None

    def __exit__(self, exc_type, exc_val, exc_tb):
        logging.debug('SSH disconnect session')
        self.conn.disconnect()

    def execCLI(self, commands):
        self.output=""
        for cmd in commands.split("\n"):
            response = self.conn.send_command(cmd)
            self.output += response

    def config(self, commands):
        self.conn.enable()
        self.output = self.conn.send_config_set(commands)
        self.conn.exit_config_mode()

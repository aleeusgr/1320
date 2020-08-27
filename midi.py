#!/bin/python

import midi 
import rtmidi as rt
import time

midiout = rt.MidiOut()
available_ports = midiout.get_ports()
if available_ports:
    midiout.open_port(0)
else:
    midiout.open_virtual_port('port1')

input('inp:')
N = 60
with midiout:
    note_on = [0x90, N, 112] # channel 1, middle C, velocity 112
    note_off = [0x80, N, 0]
    midiout.send_message(note_on)
    time.sleep(0.5)
    
    midiout.send_message(note_off)
    time.sleep(0.1)

#del midiout
#script to interact with LaunchpadMINI.


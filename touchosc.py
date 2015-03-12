# Python3 on OSX controls OSC UDP iPad client TouchOSC
# with the monome128 template.
# H.Zimmerman, July 4, 2014.
 
from pythonosc import osc_message_builder
from pythonosc import udp_client
 
import random
import time
 
# Hardcoded IP of TouchOSC on my iPad and port 9000.
# TouchOSC has monome 128 template loaded.
 
client = udp_client.UDPClient('192.168.178.31', 9000)
 
# Turn on and off 100 times.
# We start with 1, else the TouchOSC LEDs are turned off first
# which suscipiciously looks like it isn't working.
 
for counter in range(1, 100):
 
    # Monome128 template has (duh) 128 buttons.
 
    for buttonIndex in range(128):
        # Build the OSC address of the pushbutton we want to control.
        buttonAdr = '/1/push' + str(buttonIndex)
 
        # Some console output for our nerdy debugging fun.
        print(buttonAdr)
 
        # Now construct an OSC message.
        msg = osc_message_builder.OscMessageBuilder(address=buttonAdr)
        msg.add_arg(int(counter % 2))
 
        # Send it to the iPad.
        client.send(msg.build())
 
        # Slow down, OSX, else it's over before we know it.
        time.sleep(.1)

from tkinter import E
import Pyshark

capture = Pyshark.live_capture('eth0')
for packet in capture:
    try:
        output= packet.telnet
        if 'Username' in str(output):
            print('Telnet username:')
            
        elif 'Password' in str(output):
            print('Telnet password:')

        if packet.telnet.data:
            print(output)    
    except:
         pass        

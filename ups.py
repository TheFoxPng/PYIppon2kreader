import usb.core
import usb.util
import re
import os


vendor_id = 0x0665
product_id = 0x5161
packet_size = 64
data = bytearray()
device = usb.core.find(idVendor=vendor_id, idProduct=product_id)

usb.util.claim_interface(device, 0)

while True:
    while len(data) < packet_size:
        packet = device.read(0x81, packet_size - len(data))
        if packet[0] == 35:
            data.extend(packet)
            while len(data) < packet_size:
                packet = device.read(0x81, packet_size - len(data))
                data.extend(packet)
        else:
            #print(packet)
            pass
    test = data.decode('utf8')
    numbers = re.findall(r'\d+(?:\.\d+)?', test)
    numbers = [float(num) for num in numbers]
    array = numbers
    os.system('cls')
    txt = f'IN: {array[6]}. OUT: {array[7]}. LOAD: {array[8]}. BAT:{array[10]} V.'
    print(f'''
    {array[6]} - INPUT
    {array[7]} - OUTPUT
    {array[8]} - LOAD
    {array[9]} - HZ
    {array[10]} - BAT_VOLTAGE
    {array[11]} - TEMP''', end='\r')
    packet = ''
    data = bytearray()
    
#-----------------   defining variables   ---------------------
IPaddress = 0
subnetMask = [0, 0, 0, 0]
CIDR = 0

#-----------------   input  ---------------------    
while True:
    IpAddress_cidr = input(">>> Enter a IP/Mask or IP/CIDR: ")
    print()
    (IPaddress, CIDR) = IpAddress_cidr.split('/')




#-----------------   seperatingSubnetOctets  ---------------------        
    subnetMask = [(((1 << 32) - 1) << (32 - int(CIDR)) >> i) & 255 for i in reversed(range(0, 32, 8))]
    octets = [format(int(i), '08b') for i in subnetMask]


#-----------------   addresses   ---------------------
    
    ipaddress = [int(x) for x in IPaddress.split(".")]
    networkAddress = [ipaddress[i] & subnetMask[i] for i in range(4)]
    broadcastAddress = [(ipaddress[i] & subnetMask[i]) | (255 ^ subnetMask[i]) for i in range(4)]
    

#-----------------   class   ---------------------
    FirstOctet = ipaddress[0]
    
    
    if 0 <= int(FirstOctet) <= 127:
        classIP = 'A'
    elif 128 <= int(FirstOctet) <= 191:
        classIP = 'B'
    elif 192 <= int(FirstOctet) <= 223:
        classIP = 'C'
    elif 224 <= int(FirstOctet) <= 239:
        classIP = 'D'
    else:
        classIP = 'E'
    
#-----------------   layout   ---------------------         
    print("        CIDR IP      |", IpAddress_cidr)
    print('{0}  {1:1}'.format(">>> IP Address          |", IPaddress))
    print('{0}  {1:1}'.format(">>> CIDR Subnet Mask    |", CIDR ))
    print('{0}  {1:1}'.format(">>> Subnet Mask         |", '.'.join(map(str, subnetMask))))
    print('{0}  {1:20}'.format(">>> Binary Subnet Mask  |", ("").join(octets)))
    print('{0}  {1:1}'.format(">>> IP Class            |", classIP))
    print('{0}  {1:1}'.format(">>> Network Address     |", '.'.join(map(str, networkAddress))))
    print('{0}  {1:1}'.format(">>> Number of Hosts     |", abs(pow(2, ("").join(octets).count("0")) - 2)))
    print('{0}  {1:1}'.format(">>> Broadcast Address   |", '.'.join(map(str, broadcastAddress))))
    print()

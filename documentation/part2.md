# Install the CSR1000v VM

## Task preperation and implementation
1. Ik heb de virtualbox software geinstalleerd [www.virtualbox.org](https://www.virtualbox.org/)
2. Ik ben naar de blackboard cursus gegaan en heb de VM gedownload.
3. Ik heb de stappen gevolgd van het instructiedocument om deze VM te installeren: 1.1.2 Lab - Install the Virtual Lab Environment.
4. Dan heb ik ssh ingesteld op de VM met volgende commandos.

```
S1# show ip ssh
S1# configure terminal
S1(config)# ip domain-name freedombox.be
S1(config)# crypto key generate rsa
S1(config)# username admin privilege 15 secret pxl
S1(config)# line vty 0 15
S1(config-line)# transport input ssh
S1(config-line)# login local
S1(config-line)# exit
S1(config)# ip ssh version 2
```

Doordat de ssh op de router ouder is moet je op een moderne client dit commando gebruiken.
```
ssh \
  -oKexAlgorithms=+diffie-hellman-group14-sha1 \
  -oHostKeyAlgorithms=+ssh-rsa \
  admin@192.168.129.149
```

## Task troubleshooting
Ik heb niet echt problemen ondervonden de instructies waren duidelijk.

## Task verification
Ik heb de taak geverifieerd door te checken of de VM naar de router was geboot. Wat het geval was.

Dan heb ik wat commandos getest:
```
show ip interface brief
show running-config brief
show startup-config brief
```
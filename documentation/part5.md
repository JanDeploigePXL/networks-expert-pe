# Use NETCONF to access an IOS XE Device

## Task preperation and implementation
Ik heb een ansible script gemaakt dat gebruikt maakt van NETCONF en yang xml configs.
Dit script maakt het gemakkelijk om de router te configureren

Deze playbook laat zien hoe je een Cisco IOS-XE apparaat kunt beheren met NETCONF via Ansible.
De playbook voert de volgende handelingen uit:
Interfacegegevens ophalen: Verzamelt de operationele status van alle interfaces.
Hostname instellen: Configureert de hostnaam van het apparaat.
Backup van de running-config: Slaat de huidige configuratie lokaal op voor herstel of auditing.
Systeeminformatie ophalen: Verzamelt apparaatniveau-informatie via NETCONF.
Domeinnaam configureren: Stelt de IP-domeinnaam van het apparaat in voor netwerkfuncties.
Taken voor het pushen van externe configuratiebestanden en het toepassen van interface-templates zijn aanwezig, maar momenteel uitgeschakeld dit omdat de lab omgeving gelimiteerd is.

## Task troubleshooting
Ik heb even vast gezeten bij het maken van bepaalde tasks in ansible omdat de lab vm maar 1 interface heeft kon ik die niet aanpassen met een actieve ssh connectie.

## Task verification
```
CSR1kv#show platform software yang-management process 
    confd            : Running 
    nesd             : Running 
    syncfd           : Running 
    ncsshd           : Running 
    dmiauthd         : Running 
    nginx            : Running 
    ndbmand          : Running 
    pubd             : Running
```
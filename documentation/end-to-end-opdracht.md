# Install the virtual lab environment

## Task preparation and implementation
Voor deze end‑to‑end opdracht heb ik een **Ansible Netconf script** ontwikkeld.  

- Als eerste heb ik de **router VM** opgezet vanuit opdracht 2.  
- Met de **default credentials** van de VM heb ik mijn Ansible script laten verbinden via **SSH**.  
- Vervolgens heb ik een **Python virtual environment** aangemaakt en geactiveerd volgens de instructies in venv.md.  
- Binnen deze venv heb ik alle dependencies geïnstalleerd met:  

  pip install -r requirements.txt

  Het bestand requirements.txt bevindt zich in de **ansible folder**.  
- Tot slot heb ik mijn Ansible script uitgevoerd met:  

  ./run.sh

## Task troubleshooting
Tijdens de implementatie ben ik enkele problemen tegengekomen en opgelost:

1. **Interface beperking**: er was slechts één interface beschikbaar. Dit heb ik opgelost door **loopback interfaces** toe te voegen.  
2. **Candidate datastore**: deze was niet aanwezig, daarom heb ik de **running datastore** gebruikt.  
3. **OSPF configuratie**: OSPF werkte aanvankelijk niet omdat ik het verkeerde **YANG‑model** had gebruikt. Dit heb ik gecorrigeerd door het model aan te passen.

## Task verification
Na het uitvoeren van mijn Ansible script heb ik gecontroleerd of de configuratie succesvol was.  
Naast het controleren van de Ansible output, heb ik ook enkele **show‑commando’s** gebruikt om de configuratie te verifiëren:

- **Controleer OSPF configuratie**  

  show ip ospf neighbor  
  show ip ospf interface  
  show ip route ospf  

- **Controleer loopback interfaces**  

  show ip interface brief  
  show running-config | include Loopback  

Met deze commando’s kan worden bevestigd dat:  
- OSPF correct is geconfigureerd en buren zijn opgebouwd.  
- De loopback interfaces bestaan en actief zijn.
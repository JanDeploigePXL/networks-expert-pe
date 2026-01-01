# Python Network automation with NETMIKO

## Task preperation and implementation
Om aan deze taak te beginnen heb je een router VM nodig die wordt beschreven in part2.md.

1. Ik heb de volgende github repos gebruikt voor voorbeelden om een beter beeld te krijgen van netmico.
    [PythonExperiments](https://github.com/wlepxl/PythonExperiments)
    [NetworkProgrammability](https://github.com/wlepxl/Network-Programmability_Basics/tree/master/programming_fundamentals/python_part_3)
2. Daarna ben ik begonnen aan het programmeren van een python scriptje om de gevraagde commando's uit te voeren.
3. Dit python scriptje heb ik dan modulair gemaakt door de verschillende functies in verschillende files te steken.

Deze opdracht is te vinden in de python folder in deze repo.

## Task troubleshooting
Het probleem wat ik had is dat ik niet direct aan de VM kon dit heb ik op de volgende manier opgelost.

1. Ik heb eerst mijn adapter van mijn VM aangepast naar bridge mode.
2. Daarna heb ik ssh ingesteld op de router via manuele IOS commandos.
3. Wanneer ssh opgezet was kon ik beginnen aan het maken van mijn python script met netmico.

## Task verification
Ik heb de taak geverifieerd door het script meerdere keren te testen en de output ervan te verifieren.
# Use RESTCONF to access an IOS XE device

## Task preperation and implementation
Ik heb een python scriptje gemaakt dat alle endpoints aanspreekt van RESTCONF op die manier gebruikt kan worden voor verder configuratie.

## Task troubleshooting
Deze taak ging zeer vlod heb niet echt problemen gehad, omdat wij al veel met rest apis hebben gewerkt was dit relatief simpel.

## Task verification
Ik heb het script uitgevoerd en output gekregen van het python script dat de requests successvol waren.

(Best dat je een python venv gebruikt, staat gedefinieerd in venv.md)

1. Open `python/part6` folder in deze repo.
2. Installeer alle dependencies voor pip met `python -r requirements.txt`
3. Zorg ervoor dat je VM opstaat met een ssh connectie.
4. Pas de values aan in het script naar de juiste values voor jou setup.
    ```
    device_ip = "192.168.129.149"
    username = "cisco"
    password = "cisco123!"
    ```
5. Run het script met `python main.py`
# Explore yang models

## Task preperation and implementation
### Benodigdheden
- pyang
- python
- ncclient
- ansible
- jxmlease

1. Ik heb eerst wat onderzoek gedaan naar hoe Yang models werken.
2. Daarna ben ik erachter gekomen dat ik dit ook kan gebruiken met een ansible playbook.
3. Ik heb een ansible playbook gemaakt om samen met yang modeling te gebruiken.

## Task troubleshooting
Het ansible script werkte niet van de eerste keer dus ik ben naar de ansible documentatie gegaan om verder te lezen over hoe ik yang modeling kon implementeren. 

[Ansible Documentation](https://docs.ansible.com/projects/ansible/latest/collections/ansible/netcommon/netconf_config_module.html)
[Yang Model Search](https://www.yangcatalog.org/yang-search)

## Task verification
Ik heb het ansible script uitgevoerd in de map ansible met het script run.sh.
Alles werkte naar behoren.
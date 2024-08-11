## UPDATER Scripts

Designed for add data from config.yaml to collection. Script updates only ONE collection at one run.

USAGE:
1. Make config.yaml script for particular collection.
For example, to add new ground station you should make some kind of that config file:
```
    name: HeadCompute Station
    specifications:
    radio1:
        antennaType: Patch
        frequencyRange: 2.3 GHz - 2.4GHz
        maxRange: 10 km
    radio2:
        antennaType: Yagi
        frequencyRange: 430 MHz - 434GHz
        maxRange: 14 km
    workingTime: 3h
    supply: battery
    operationalStatus: prototype 
    capabilities:
    - videoReceiving
    - telemetryReceiveing
    - commandSending
    developer: SPB
    tags:
    - development
    - prototype
    notes: Ground station for HeadCompute module
```

config.yaml.example consists examples of config files for different collections.

2. Run main.py to add config data to collection:

```
python3 main.py <path_to_config.yaml> <db_collection_name>
```

If collection does not exists, script creates newone.
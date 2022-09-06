import yaml

with open('/home/collinp/Documents/GitHub/AlarmClock/alarms_sample.yaml') as f:
    
    alarms = yaml.load(f, Loader=yaml.FullLoader)
    print(alarms)

    print(alarms['Walk_Dog']['Time'])
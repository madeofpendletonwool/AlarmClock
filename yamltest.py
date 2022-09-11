import yaml

with open('/home/collinp/Documents/GitHub/pyArmClock/alarms_sample.yaml') as f:
    
    alarms = yaml.load(f, Loader=yaml.FullLoader)

    print(dict.keys(alarms))

    print(dict.values(alarms))
    print(alarms['Alarm1'][0]['Alarm_Name'])
    print(f'Wake up to {alarms["Alarm1"][0]["Alarm_Name"]}')
    print(alarms['Alarm1'][0]['Time'])

    #print(alarms)

    #print(alarms['Walk_Dog'][0]['Time'])
import requests
import json

bridge_ip = "192.168.0.2"
bridge_username = "soduBL8lu551zb71pFnoxwZFAgoCzcPWvk1z9K4g"

# Beispiel:
# turn_on_group('kitchen')
def turn_off_group(where):
    groups = { 'lights': 1, 'kitchen': 2, 'bedRoom': 3 }
    group_id = groups[where]

    payload = {"on":True}
    headers = {'content-type': 'application/json'}
    r = requests.put("http://"+bridge_ip+"/api/"+bridge_username+"/groups/"+str(group_id)+"/action", data=json.dumps(payload), headers=headers)

# Beispiel:
# turn_off_group('kitchen')
def turn_off_group(where):
    groups = { 'lights': 1, 'kitchen': 2, 'bedRoom': 3 }
    group_id = groups[where]

    payload = {"on":False}
    headers = {'content-type': 'application/json'}
    r = requests.put("http://"+bridge_ip+"/api/"+bridge_username+"/groups/"+str(group_id)+"/action", data=json.dumps(payload), headers=headers)

#turn_on_group('lights')
# {"1":{"name":"Azar","lights":["4","3","2","1"],"sensors":[],"type":"Room","state":{"all_on":true,"any_on":true},"recycle":false,"class":"Bedroom","action":{"on":true,"bri":254,"hue":50996,"sat":42,"effect":"none","xy":[0.3616,0.3315],"ct":222,"alert":"none","colormode":"xy"}},"2":{"name":"Entertainment-Bereich 1","lights":["1","2"],"sensors":[],"type":"Entertainment","state":{"all_on":true,"any_on":true},"recycle":false,"class":"TV","stream":{"proxymode":"auto","proxynode":"/lights/1","active":false,"owner":null},"locations":{"1":[-0.01,0.29,0.00],"2":[0.00,1.00,0.00]},"action":{"on":true,"bri":254,"hue":8402,"sat":140,"effect":"none","xy":[0.4575,0.4099],"ct":366,"alert":"none","colormode":"xy"}},"3":{"name":"Entertainment-Bereich 2","lights":["2"],"sensors":[],"type":"Entertainment","state":{"all_on":true,"any_on":true},"recycle":false,"class":"TV","stream":{"proxymode":"auto","proxynode":"/lights/2","active":false,"owner":null},"locations":{"2":[0.00,1.00,0.00]},"action":{"on":true,"bri":254,"hue":8402,"sat":140,"effect":"none","xy":[0.4575,0.4099],"ct":366,"alert":"none","colormode":"xy"}}}
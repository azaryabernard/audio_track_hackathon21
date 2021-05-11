import requests
import json
import urllib
from requests.api import request
from rgbxy import Converter
import webcolors

converter = Converter()

bridge_ip = "192.168.0.2"
bridge_username = "soduBL8lu551zb71pFnoxwZFAgoCzcPWvk1z9K4g"

groups = { 'lights': 1, 'kitchen': 2, 'bedRoom': 3 }

# Beispiel:
# turn_on_group('kitchen')
def turn_on_group(where):
    group_id = groups[where]

    payload = {"on":True}
    headers = {'content-type': 'application/json'}
    r = requests.put("http://"+bridge_ip+"/api/"+bridge_username+"/groups/"+str(group_id)+"/action", data=json.dumps(payload), headers=headers)

# Beispiel:
# turn_off_group('kitchen')
def turn_off_group(where):
    group_id = groups[where]

    payload = {"on":False}
    headers = {'content-type': 'application/json'}
    r = requests.put("http://"+bridge_ip+"/api/"+bridge_username+"/groups/"+str(group_id)+"/action", data=json.dumps(payload), headers=headers)


def set_brightness_group(where, bright):
    group_id = groups[where]

    bri = bright / 100 * 254
    payload = {"bri": int(bri)}
    headers = {'content-type': 'application/json'}
    r = requests.put("http://"+bridge_ip+"/api/"+bridge_username+"/groups/"+str(group_id)+"/action", data=json.dumps(payload), headers=headers)

def get_brightness_group(where):
    group_id = groups[where]
    r = urllib.request.urlopen("http://"+bridge_ip+"/api/"+bridge_username+"/groups/"+str(group_id))
    return int(str(r.read()).split('"bri":')[1].split(',')[0]) / 254 * 100

def decrease_brightness_group(where):
    bri = get_brightness_group(where)
    if bri > 20:
        set_brightness_group(where, bri - 20)
    elif:
        set_brightness_group(where, 0)


def increase_brightness_group(where):
    bri = get_brightness_group(where)
    if bri < 80:
        set_brightness_group(where, bri + 20)
    elif:
        set_brightness_group(where, 0)

def set_color(where, color):
    group_id = groups[where]
    xy = [0, 0]
    if color:
        clr = webcolors.name_to_hex(color).split('#')[1]
        print(clr)
        if clr and clr != '000000':
            xy = converter.hex_to_xy(clr)
            payload = {"xy": xy}
            headers = {'content-type': 'application/json'}
            r = requests.put("http://"+bridge_ip+"/api/"+bridge_username+"/groups/"+str(group_id)+"/action", data=json.dumps(payload), headers=headers)

   


#turn_on_group('lights')
# {"1":{"name":"Azar","lights":["4","3","2","1"],"sensors":[],"type":"Room","state":{"all_on":true,"any_on":true},"recycle":false,"class":"Bedroom","action":{"on":true,"bri":254,"hue":50996,"sat":42,"effect":"none","xy":[0.3616,0.3315],"ct":222,"alert":"none","colormode":"xy"}},"2":{"name":"Entertainment-Bereich 1","lights":["1","2"],"sensors":[],"type":"Entertainment","state":{"all_on":true,"any_on":true},"recycle":false,"class":"TV","stream":{"proxymode":"auto","proxynode":"/lights/1","active":false,"owner":null},"locations":{"1":[-0.01,0.29,0.00],"2":[0.00,1.00,0.00]},"action":{"on":true,"bri":254,"hue":8402,"sat":140,"effect":"none","xy":[0.4575,0.4099],"ct":366,"alert":"none","colormode":"xy"}},"3":{"name":"Entertainment-Bereich 2","lights":["2"],"sensors":[],"type":"Entertainment","state":{"all_on":true,"any_on":true},"recycle":false,"class":"TV","stream":{"proxymode":"auto","proxynode":"/lights/2","active":false,"owner":null},"locations":{"2":[0.00,1.00,0.00]},"action":{"on":true,"bri":254,"hue":8402,"sat":140,"effect":"none","xy":[0.4575,0.4099],"ct":366,"alert":"none","colormode":"xy"}}}

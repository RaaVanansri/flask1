import os
import pandas as pd

def macAnalysis(filename):

    os.system(f'tshark -r {os.getcwd()}/{filename} -T fields -e wlan.fc.type -E header=y -E separator=, -E quote=d -E occurrence=f > mac.csv')
    mgt = "Total Managment Frames : ";ctrl = "Total Control Frames : ";data = "Total Data Frames : "
    mac = (pd.read_csv('mac.csv').groupby(['wlan.fc.type']))
    try:mgt += str(mac.groups[0].size)
    except:mgt += str(0)
    try:ctrl += str(mac.groups[1].size)
    except:ctrl += str(0)
    try:data += str(mac.groups[2].size)
    except:data += str(0)
    
    return [mgt,ctrl,data]
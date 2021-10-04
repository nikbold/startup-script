# Nik's Startup Script

#### What Script has to do:

## VPN
# Connect to Full-Tunnel VPN

import os
openvpn =r'"C:\Program Files\OpenVPN\bin\openvpn-gui.exe" --connect Zynstra-Bath-full.ovpn'
os.system(openvpn)

## Chrome
import webbrowser

url = 'https://github.com/nikbold/' # Open GIT:
url1 = 'http://192.168.11.10/glpi/' # GLPI
url2 = 'https://github.com/nikbold?tab=repositories' # Open CI Team Board:
url3 = 'https://rundeck.dev.zynstra.com/project/deployments/activity' # Open Rundeck:
webbrowser.open_new(url)
webbrowser.open_new(url1)
webbrowser.open_new(url2)
webbrowser.open_new(url3)

## WSL2

# Open New Window

## Outlook
# Scrape new emails
# Open Outlook
import os
#os.startfile("outlook")
import psutil ## https://topic.alibabacloud.com/a/installing-psutil-430-in-windows-10-with-pip_1_15_30862932.html#:~:text=%20Installing%20Psutil%204.3.0%20in%20Windows%2010%20with,use%20CMD%20to%20install%203.5%20psutil%20More%20

def is_outlook_running():
    for p in psutil.process_iter(attrs=['pid', 'name']):
        if "OUTLOOK.EXE" in p.info['name']:
            print("Yes", p.info['name'], "is running")
            break
    else:
        print("No, Outlook is not running")
        os.startfile("outlook")
        print("Outlook is starting now...")
## Open Slack

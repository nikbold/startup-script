# Nik's Startup Script

# Load modules:
import os
import webbrowser

## VPN
# Connect to Dev VPN
openvpn =r'"C:\Program Files\OpenVPN\bin\openvpn-gui.exe" --connect Zynstra-Bath-full.ovpn'
os.system(openvpn)

## Chrome
url = 'https://github.com/nikbold/' # Open GIT:
url1 = 'http://192.168.11.10/glpi/' # GLPI
url2 = 'https://github.com/nikbold?tab=repositories' # Open CI Team Board:
url3 = 'https://rundeck.dev.zynstra.com/project/deployments/activity' # Open Rundeck:
webbrowser.open_new(url)
webbrowser.open_new(url1)
webbrowser.open_new(url2)
webbrowser.open_new(url3)

## WSL2

# Open New Terminal Window
os.system('wt -p "Ubuntu-18.04"')

## Open VSCode
os.startfile(r"C:\Users\NB250346\AppData\Local\Programs\Microsoft VS Code\Code.exe")

## Outlook
# Scrape new emails

# Open Outlook
os.startfile("outlook")

## Open Slack
slack =r'"C:\Users\NB250346\AppData\Local\slack\slack.exe"'
os.startfile(slack)

## Open Teams
os.startfile(r"C:\Users\NB250346\AppData\Local\Microsoft\Teams\current\Teams.exe")

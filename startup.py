# Nik's Startup Script

# Load modules:
import os
import webbrowser
import subprocess

## VPN
# Connect to Dev VPN
openvpn =r'"C:\Program Files\OpenVPN\bin\openvpn-gui.exe" --connect Zynstra-Bath-full.ovpn'
os.system(openvpn)

## Chrome
url = 'https://github.com/nikbold/' # Open GIT:
url1 = 'http://192.168.11.10/glpi/' # GLPI
url2 = 'https://github.com/nikbold?tab=repositories' # Open CI Team Board:
url3 = 'https://rundeck.dev.zynstra.com/project/deployments/activity' # Open Rundeck:
url4 = 'https://open.spotify.com/?_ga=2.52563432.1109292248.1634282273-918053379.1631270212' # Open spotify
webbrowser.open_new(url)
webbrowser.open_new(url1)
webbrowser.open_new(url2)
webbrowser.open_new(url3)
webbrowser.open_new(url4)

## WSL2

# Open New Window
os.system('wt -p "Ubuntu-18.04"')

## Outlook
# Scrape new emails

# Open Outlook
os.startfile("outlook")

## Open Slack
slack =r'"C:\Users\NB250346\AppData\Local\slack\slack.exe"'
os.startfile(slack)

## Open Teams

#teams =r'"C:\Users\NB250346\AppData\Local\Microsoft\Teams\Update.exe" --processStart Teams.exe"')
#os.startfile(r"C:\Users\NB250346\AppData\Local\Microsoft\Teams\current\Teams.exe")
os.system(r"C:\Users\NB250346\AppData\Local\Microsoft\Teams\Update.exe --processStart 'Teams.exe'")

## Open MSPaint
os.startfile(r"\WINDOWS\system32\mspaint.exe")

## Open Notepad++

notepadplusplus = r'"C:\Program Files (x86)\Notepad++\notepad++.exe"'
os.system(notepadplusplus)

## Open VSCode
os.startfile(r"C:\Users\NB250346\AppData\Local\Programs\Microsoft VS Code\Code.exe")

## RDP to Laptop VM
rdpLaptop = r'"C:\Users\NB250346\OneDrive - NCR Corporation\Desktop\laptop.rdp"'
os.system(rdpLaptop)

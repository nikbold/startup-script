# Nik's Startup Script

#### What Script has to do:

## VPN
# Connect to Dev VPN

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
os.startfile("outlook")

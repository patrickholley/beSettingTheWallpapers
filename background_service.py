import csv
import os
import subprocess
import time
import sys

def run_subprocess_command(command):
  process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
  return process.communicate()[0].strip().decode('utf-8')
  
def get_gsettings_prefix(getOrSet = "set"):
  return f"gsettings {getOrSet} org.gnome.desktop.background picture-"
  
def get_process_command(processName):
  return f'pgrep -f "{processName}"'

connectedCommand = 'echo "$(xrandr | grep -io " connected " | wc -l)"'
getActiveWallpaperCommand = f"{get_gsettings_prefix('get')}uri"
setActiveWallpaperCommandPrefix = f"{get_gsettings_prefix()}uri"
setActiveWallpaperSpannedCommand = f"{get_gsettings_prefix()}options 'spanned'"

pathSuffix = "Settings.csv"
applicationSettingsPath = f"{sys.argv[0]}/application{pathSuffix}"
defaultSettingsPath = f"{sys.argv[0]}/default{pathSuffix}"
previousSettingsPath = f"{sys.argv[0]}/previous{pathSuffix}"
tempPreviousSettingsPath = f"{sys.argv[0]}/tempPrevious{pathSuffix}"
imgActive = f"{sys.argv[0]}/active.png"

def set_wallpaper():
  applicationSettingsFile = open(applicationSettingsPath)
  applicationSettings = list(csv.reader(applicationSettingsFile))
  applicationSettingsFile.close()
  defaultSettingsFile = open(defaultSettingsPath)
  defaultSettings = list(csv.reader(defaultSettingsFile))
  defaultSettingsFile.close()
  previousSettingsFile = open(previousSettingsPath)
  previousSettings = list(csv.reader(previousSettingsFile))
  previousSettingsFile.close()
  prevImg1 = previousSettings[0][1]
  prevImg2 = previousSettings[1][1]
  prevIsImg1Left = previousSettings[2][1]
  prevConnected = previousSettings[3][1]
  img1 = defaultSettings[0][1]
  img2 = defaultSettings[1][1]
  isImg1Left = defaultSettings[2][1] == "True"
  connected = run_subprocess_command(connectedCommand)
  if connected == "1" and (prevConnected == "2" or prevImg1 != img1):
    previousSettings[0][1] = img1
    previousSettings[3][1] = connected
    run_subprocess_command(f"cp {img1} {imgActive}")
  elif connected == "2":
    for i in range(0, len(applicationSettings)):
      processCommand = get_process_command(applicationSettings[i][2])
      matchedProcesses = run_subprocess_command(processCommand).splitlines()
      if len(matchedProcesses) > 1:
        img2 = applicationSettings[i][1]
    if prevImg1 != img1 or prevImg2 != img2 or prevConnected != connected or prevIsImg1Left != f"{isImg1Left}":
      previousSettings[0][1] = img1
      previousSettings[1][1] = img2
      previousSettings[2][1] = isImg1Left
      previousSettings[3][1] = connected
      run_subprocess_command(f"convert {f'{img1} {img2}' if isImg1Left else f'{img2} {img1}'} -resize 1920x1080 -background black -gravity center -extent 1920x1080 +append {imgActive}")
  tempCsvFile = open(tempPreviousSettingsPath, "w")
  csv.writer(tempCsvFile).writerows(previousSettings)
  tempCsvFile.close()
  os.rename(tempPreviousSettingsPath, previousSettingsPath)
  prevFileActive = run_subprocess_command(getActiveWallpaperCommand)
  fileActive = f"'file://{imgActive}'"
  if prevFileActive != fileActive:
    run_subprocess_command(setActiveWallpaperSpannedCommand)
    run_subprocess_command(f"{setActiveWallpaperCommandPrefix} {fileActive}")

def run_background_service(app):
  throttle = 0
  while not app.stopped:
    throttle += 1
    if throttle == 5:
      throttle = 0
      set_wallpaper()
    time.sleep(1)

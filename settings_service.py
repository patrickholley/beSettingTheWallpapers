import csv
import os

settingsPath = "settings.csv"

csvFile = open(settingsPath)
settingsList = list(csv.reader(csvFile))
csvFile.close()

def save_settings():
  tempSettingsPath = "tempSettings.csv"
  tempCsvFile = open(tempSettingsPath, "w")
  csv.writer(tempCsvFile).writerows(settingsList)
  tempCsvFile.close()
  os.rename(tempSettingsPath, settingsPath)

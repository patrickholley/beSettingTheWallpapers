import csv
import os

settingsPath = "settings.csv"

settingsList = list()

def read_settings_list():
  global settingsList
  csvFile = open(settingsPath)
  settingsList = list(csv.reader(csvFile))
  csvFile.close()

def save_settings(settingsListToSave):
  tempSettingsPath = "tempSettings.csv"
  tempCsvFile = open(tempSettingsPath, "w")
  csv.writer(tempCsvFile).writerows(settingsListToSave)
  tempCsvFile.close()
  os.rename(tempSettingsPath, settingsPath)
  read_settings_list()

read_settings_list()

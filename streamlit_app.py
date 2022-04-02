#!pip install selenium
#!apt-get update # to update ubuntu to correctly run apt install
#!apt install chromium-chromedriver
#!cp /usr/lib/chromium-browser/chromedriver /usr/bin
import sys
#sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
from selenium import webdriver
import pandas as pd
from datetime import date
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)

def app_check():
  wd.get('https://telegov.njportal.com/njmvc/AppointmentWizard/19')
  tarihler = []
  listeler = [i.text for i in wd.find_elements(By.XPATH,"//*[contains(@id, 'dateText')]")]
  for i in listeler:
    if i == 'No Appointments Available':
      pass
    else:
      tarihler.append((pd.to_datetime(i.split(' ')[4], format='%m/%d/%Y') - pd.to_datetime(date.today(), format='%Y/%m/%d')).days)
  gun_var = str(min(tarihler))
  print(gun_var)


calculate = st.button('Calculate the Price')

if calculate:
  app_check()
  


import sys
from selenium import webdriver
import pandas as pd
from datetime import date
from selenium.webdriver.common.by import By
import streamlit as st


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
wd.get('https://telegov.njportal.com/njmvc/AppointmentWizard/19')
tarihler = []
listeler = [i.text for i in wd.find_elements(By.XPATH,"//*[contains(@id, 'dateText')]")]
for i in listeler:
  if i == 'No Appointments Available':
    pass
  else:
    tarihler.append((pd.to_datetime(i.split(' ')[4], format='%m/%d/%Y') - pd.to_datetime(date.today(), format='%Y/%m/%d')).days)
argument = str(min(tarihler))
  


st.text(argument)

if st.button('say hello'):
  st.text('hello')
 

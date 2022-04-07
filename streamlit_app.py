import sys
from selenium import webdriver
import pandas as pd
from datetime import date
from selenium.webdriver.common.by import By
import streamlit as st



def exam_counter():
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
    return str(min(tarihler) + 'days to nearest appointment in ' + tarihler.count(min(tarihler)))
 
def six_points_counter():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
    wd.get('https://telegov.njportal.com/njmvc/AppointmentWizard/15')
    tarihler = []
    listeler = [i.text for i in wd.find_elements(By.XPATH,"//*[contains(@id, 'dateText')]")]
    #butonlar = wd.find_elements(By.XPATH,"//*[contains(@id, 'makebtn')]")
    #butonlar = [i.get_attribute('href') for i in butonlar]
    for i in listeler:
      if i == 'No Appointments Available':
        pass
      else:
        tarihler.append((pd.to_datetime(i.split(' ')[4], format='%m/%d/%Y') - pd.to_datetime(date.today(), format='%Y/%m/%d')).days)
    return str(min(tarihler) + 'days to nearest appointment in ' + tarihler.count(min(tarihler)))
    #index = tarihler.index(min(tarihler))
    #days = str(min(tarihler))
    #link = butonlar.index(min(tarihler))




if st.button('DMV Initial Permit Nearest Appointment'):
    st.text(six_points_counter())
    link = '[GO TO PAGE](https://telegov.njportal.com/njmvc/AppointmentWizard/15)'
    st.markdown(link, unsafe_allow_html=True)


    
if st.button('DMV Exam Nearest Appointment'):
    st.text(exam_counter())
    link = '[GO TO PAGE](https://telegov.njportal.com/njmvc/AppointmentWizard/19)'
    st.markdown(link, unsafe_allow_html=True)

 
  

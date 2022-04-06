import streamlit as st

class appointment_check(self):
    def __init__(self):
        import sys
        from selenium import webdriver as webdriver
        import pandas as pd
        from datetime import self.date
        from selenium.webdriver.common.by import By

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
    def counter(self, website):
        self.wd.get(website)
        tarihler = []
        listeler = [i.text for i in self.wd.find_elements(self.By.XPATH,"//*[contains(@id, 'dateText')]")]
        for i in listeler:
          if i == 'No Appointments Available':
            pass
          else:
            tarihler.append((pd.to_datetime(i.split(' ')[4], format='%m/%d/%Y') - pd.to_datetime(self.date.today(), format='%Y/%m/%d')).days)
        return str(min(tarihler))


if st.button('DMV Initial Permit Nearest Appointment'):
    st.text(appointment_check.counter('https://telegov.njportal.com/njmvc/AppointmentWizard/15') + ' DAYS TO NEAREST APPOINTMENT')
    link = '[GO TO PAGE](https://telegov.njportal.com/njmvc/AppointmentWizard/15)'
    st.markdown(link, unsafe_allow_html=True)


    
if st.button('DMV Exam Nearest Appointment'):
    st.text(appointment_check.counter('https://telegov.njportal.com/njmvc/AppointmentWizard/19') + ' DAYS TO NEAREST APPOINTMENT')
    link = '[GO TO PAGE](https://telegov.njportal.com/njmvc/AppointmentWizard/19)'
    st.markdown(link, unsafe_allow_html=True)

 
  

import streamlit as st

class appointment_check(self):
    def __init__(self):
        import sys as self.sys
        from selenium import webdriver as self.webdriver
        import pandas as self.pd
        from datetime import self.date
        from selenium.webdriver.common.by import self.By

        self.chrome_options = self.webdriver.ChromeOptions()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        self.wd = self.webdriver.Chrome('chromedriver',chrome_options=self.chrome_options)
    def counter(self, website):
        self.wd.get(website)
        tarihler = []
        listeler = [i.text for i in self.wd.find_elements(self.By.XPATH,"//*[contains(@id, 'dateText')]")]
        for i in listeler:
          if i == 'No Appointments Available':
            pass
          else:
            tarihler.append((self.pd.to_datetime(i.split(' ')[4], format='%m/%d/%Y') - self.pd.to_datetime(self.date.today(), format='%Y/%m/%d')).days)
        return str(min(tarihler))


if st.button('DMV Initial Permit Nearest Appointment'):
    st.text(appointment_check.counter('https://telegov.njportal.com/njmvc/AppointmentWizard/15') + ' DAYS TO NEAREST APPOINTMENT')
    link = '[GO TO PAGE](https://telegov.njportal.com/njmvc/AppointmentWizard/15)'
    st.markdown(link, unsafe_allow_html=True)


    
if st.button('DMV Exam Nearest Appointment'):
    st.text(appointment_check.counter('https://telegov.njportal.com/njmvc/AppointmentWizard/19') + ' DAYS TO NEAREST APPOINTMENT')
    link = '[GO TO PAGE](https://telegov.njportal.com/njmvc/AppointmentWizard/19)'
    st.markdown(link, unsafe_allow_html=True)

 
  

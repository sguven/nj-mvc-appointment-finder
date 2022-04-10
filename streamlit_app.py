import sys
from selenium import webdriver
import pandas as pd
from datetime import date
from selenium.webdriver.common.by import By
import streamlit as st
from PIL import Image
image = Image.open('dmv.gif')
st.text('TODAY IS ' + str(date.today()))
st.text('PLEASE PUSH THE BUTTON BELOW THAT YOU ARE LOOKING FOR AN APPOINTMENT FOR')


def counter(webpage):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
    wd.get(webpage)
    locations = [i.text.split('\n')[0] for i in wd.find_elements(By.XPATH,"//*[contains(@style,'font-weight:bold;')]")]
    day_counts = []
    web_page_dates = [i.text for i in wd.find_elements(By.XPATH,"//*[contains(@id, 'dateText')]")]
    for i in web_page_dates:
        if i == 'No Appointments Available':
            day_counts.append(1000)
        else:
            day_counts.append((pd.to_datetime(i.split(' ')[4], format='%m/%d/%Y') - pd.to_datetime(date.today(), format='%Y/%m/%d')).days)
    indices = [i for i, x in enumerate(day_counts) if x == min(day_counts)]
    new_locations = [locations[i] for i in indices]
    return str(min(day_counts)) + ' day(s) to nearest appointment in ' + str(new_locations)


if st.button('DMV Initial Permit Nearest Appointment'):
    #st.text(six_points_counter())
    st.markdown("<h1 style='color: red;'>" + counter('https://telegov.njportal.com/njmvc/AppointmentWizard/15') + "</h1>", unsafe_allow_html=True)
    link = '[GO TO PAGE](https://telegov.njportal.com/njmvc/AppointmentWizard/15)'
    st.markdown(link, unsafe_allow_html=True)

    
if st.button('DMV Exam Nearest Appointment'):
    #st.text(exam_counter())
    st.markdown("<h1 style='color: red;'>" + counter('https://telegov.njportal.com/njmvc/AppointmentWizard/19') + "</h1>", unsafe_allow_html=True)
    link = '[GO TO PAGE](https://telegov.njportal.com/njmvc/AppointmentWizard/19)'
    st.markdown(link, unsafe_allow_html=True)

 
st.image(image)

import streamlit as st
import requests
import os
from PIL import Image
import numpy as np
import pandas as pd

image_path = os.path.dirname(os.path.abspath(__file__)) + "/images/sydney.jpeg"

image = Image.open(image_path)
st.image(image, use_column_width=True)#, width=600)


'''
# Will it rain tomorrow ?
'''

info_location = """
<br/>
<div style="font-weight:700">Select city</div>
"""

city_list = ['Adelaide',  'Albany',  'Albury',  'Alice Springs',
             'Badgerys Creek',  'Ballarat',  'Bendigo',  'Brisbane',
             'Cairns',  'Canberra',  'Cobar',  'Coffs Harbour',  'Dartmoor',
             'Darwin',  'Gold Coast',  'Hobart',  'Katherine',  'Launceston',
             'Melbourne',  'Melbourne Airport',  'Mildura',  'Moree',
             'Mount Gambier',  'Mount Ginini',  'Newcastle',  'Nhil',
             'Norah Head',  'Norfolk Island',  'Nuriootpa',  'Pearce RAAF',
             'Penrith',  'Perth',  'Perth Airport',  'Portland',  'Richmond',
             'Sale',  'Salmon Gums',  'Sydney',  'Sydney Airport',
             'Townsville',  'Tuggeranong',  'Uluru',  'Wagga Wagga',
             'Walpole',  'Watsonia',  'Williamtown',  'Witchcliffe',
             'Wollongong',  'Woomera']



info_Location = """
<br/>
<div style="font-weight:700">Select location</div>
"""
st.write(info_Location, unsafe_allow_html=True)

Location = st.selectbox('Australian city to predict rainfall tomorrow', city_list)


info_humidity3pm = """
<br/>
<div style="font-weight:700">Select humidity this afternoon [%]</div>
"""
st.write(info_humidity3pm, unsafe_allow_html=True)

humidity3pm = st.number_input('Humidity (percent) at 3pm', step=0.5, min_value=0.0, max_value=100.0, value=30.)


info_windGustSpeed = """
<br/>
<div style="font-weight:700">Select wind gust speed today [km/h]</div>
"""
st.write(info_windGustSpeed, unsafe_allow_html=True)


windgustspeed = st.number_input("The speed (km/h) of the strongest wind gust in the 24 hours to midnight", step=1., min_value=0.0, max_value=100.0, value=44.)


info_pressure9am = """
<br/>
<div style="font-weight:700">Select pressure this morning [hpa]</div>
"""
st.write(info_pressure9am, unsafe_allow_html=True)

pressure9am = st.slider('Atmospheric pressure (hpa) reduced to mean sea level at 9am', 980.5, 1041.0, 1000.)


info_mintemp = """
<br/>
<div style="font-weight:700">Select min temperature today [°C]</div>
"""
st.write(info_mintemp, unsafe_allow_html=True)

mintemp = st.slider('The minimum temperature in degrees celsius', -8.5, 33.9, 22.)



#url = f"https://titanic-n2o267u7cq-ew.a.run.app/survivor_predict?Sex={gender}&Age={age}&Fare={fare}&Pclass={pclass}"
url = f"http://127.0.0.1:8000/predict_rain?Humidity3pm={humidity3pm}&WindGustSpeed={windgustspeed}&Location={Location}&Pressure9am={pressure9am}&MinTemp={mintemp}"
response = requests.get(url).json()
response
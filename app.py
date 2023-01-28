import streamlit as st
import datetime as dt
import numpy as np
import pandas as pd

import requests

'''
# TaxiFare Model
'''

st.markdown('''
#TaxiFareModel
## with le wagon API, as mine did not decide to work
let's say its because of Mac M1 and not me :p
''')


d = st.date_input("Date of the pick-up", min_value=dt.datetime(2010,1,1), max_value=dt.datetime(2025,12,31))
t = st.time_input("at what time do you travel?")

date_time = dt.datetime(d.year, d.month, d.day, t.hour, t.minute, t.second)

plon = st.text_input('Pickup Longitude')
pla = st.text_input('Pickup Latitude')
dlon = st.text_input('DropOff Longitude')
dla = st.text_input('DropOff Latitude')

p = st.selectbox("Number of passenger", np.arange(1,10,1))

#l = np.ndarray((plon, pla),(dlon, dla))
#df = pd.Dataframe(l, columns=['lat','lon'])

#st.map(df)
GOOGLE_API_KEY= st.secrets('google_api_key')
GEOCODE_URL_pickup = f'https://maps.googleapis.com/maps/api/geocode/json?address={pick_up_adress}&key={GOOGLE_API_KEY}'


url = 'https://taxifare.lewagon.ai/predict'

#if url == 'https://taxifare.lewagon.ai/predict':

 #   st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')



while not d or not t or not plon or not pla or not dlon or not dla or not p:
    st.stop()

parameters =  {
    'pickup_datetime' : date_time,
    'pickup_longitude':plon,
    'pickup_latitude':pla,
    'dropoff_longitude':dlon,
    'dropoff_latitude':dla,
    'passenger_count':p}

r = requests.get(url, params=parameters).json()

fare = r['fare']

st.write(fare)


import streamlit as st
import requests
from datetime import datetime
import pandas as pd
import plotly.graph_objs as go
import pytz

API_Key = 'd53b69ec9282d40807744cff66ea890d'
Base_url="https://api.openweathermap.org/data/2.5/"

st.set_page_config(layout="wide")
st.title('🌤️ Weather Forecast Dashboard 🌤️')
st.markdown("Get real-time weather updates by selecting a country and entering a city name.")
city=st.text_input("Enter city name")

if st.button("Click here"):
    Current_url=f"{Base_url}weather?q={city}&appid=d53b69ec9282d40807744cff66ea890d&units=metric"
    res=requests.get(Current_url).json()

    if res.get("cod") == 200:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader(f"📍{res['name']},{res['sys']['country']}")
           # icon = res['weather'][0]['icon']
            #st.image(f"http://openweathermap.org/img/wn/{icon}@2x.png, width =100")
            st.markdown(f"## {res['main']['temp']}°C")
            st.markdown(f"**{res['weather'][0]['description'].title()}**")
            st.write(f"Feels like: **{res['main']['feels_like']} °C**")
            st.write(f"Humidity: **{res['main']['humidity']}%**")
            st.write(f"Pressure: **{res['main']['pressure']} hPa**")
            st.write(f"Visibility: **{res['visibility'] / 1000} km**")
            st.write(f"Cloudiness: **{res['clouds']['all']}%**")

        with col2:
            st.subheader("🌐 Additional Weather Info")
            st.write(f"Min Temp: **{res['main']['temp_min']} °C**")
            st.write(f"Max Temp: **{res['main']['temp_max']} °C**")
            st.write(f"Sea Level: **{res['main'].get('sea_level', 'N/A')} hPa**")
            st.write(f"Ground Level: **{res['main'].get('grnd_level', 'N/A')} hPa**")
            st.write(f"Wind Speed: **{res['wind']['speed']} m/s**")
            st.write(f"Wind Direction: **{res['wind']['deg']}°**")
            st.write(f"Wind Gust: **{res['wind'].get('gust', 'N/A')} m/s**")

          # Convert timestamp to local time

        tz = pytz.FixedOffset(res['timezone'] // 60)
        sunrise = datetime.fromtimestamp(res['sys']['sunrise'], tz).strftime("%I:%M %p")
        sunset = datetime.fromtimestamp(res['sys']['sunset'], tz).strftime("%I:%M %p")

        st.write(f"Sunrise: 🌅 **{sunrise}**")
        st.write(f"Sunset: 🌇 **{sunset}**")


        st.markdown("---")
        st.json(res)  # Show full raw response at the bottom (optional)

    else:
        st.error("City not found or API error")




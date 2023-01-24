import streamlit as st
import pandas as pd
import folium
from folium import Map
from streamlit_folium import st_folium
from streamlit_folium import folium_static


# Read the CSV file into a dataframe
file = r'D:\Checkers.csv'
data = pd.read_csv(file)

st.sidebar.title("Data Uploader")

def main():
    file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])
    if file is not None:
        display_map(file)

st.header('Checkers KwaZulu-Natal Store Finder')
st.text('Locations of Checkers Stores in KwaZulu-Natal')


def display_map(file):
    data = pd.read_csv(file)
    m = Map(location=[data['Latitude'].mean(), data['Longitude'].mean()], zoom_start=8)
    for i, row in data.iterrows():
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],
            popup=row['NAME'],
            icon=folium.Icon(color='blue')
        ).add_to(m)
    # st.write(m)
    folium_static(m)


if __name__ == '__main__':
    main()



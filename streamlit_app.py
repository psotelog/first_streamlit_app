import streamlit

streamlit.title ('My Parents New Healthy Diner')
streamlit.header ('Breakfast  Menu')
streamlit.text ('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text ('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text ('🐔 Hard-Boiledd Free-Range Egg')
streamlit.text ('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Añadimos la librería pandas para poder importarun fichero del bucket y lo vamos a visualizar como una tabla mediante un DataFrame
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe (my_fruit_list)

# Incluimos una lista que me permita seleccionar los registros que quiera 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

import streamlit

streamlit.title ('My Parents New Healthy Diner')
streamlit.header ('Breakfast  Menu')
streamlit.text ('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text ('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text ('🐔 Hard-Boiledd Free-Range Egg')
streamlit.text ('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Añadimos la librería pandas para poder importar un fichero del bucket para poder visualizarlo  luego mediante un DataFrame
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#Esto nos permite que el índice de la  tabla no vaya por id, si no por el campo Fruit (Nombre)
my_fruit_list = my_fruit_list.set_index('Fruit')

# Incluimos una lista que me permita seleccionar los registros que quiera 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Si  queremos que por defecto en la lista de selección aparezcan ya  varias frutas seleccionadas: 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Visualizamos el dataframe con los datos del fichero
streamlit.dataframe (my_fruit_list)

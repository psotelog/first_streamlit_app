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
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Visualizamos el dataframe con los datos del fichero
#streamlit.dataframe (my_fruit_list)

# Quermeos msotrar las frutas que ha seleccionado el cliente en su propia tabla
  # creamos un objeto que contenga  el resultado seleccionado
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
  
  # generamos  un grupo de registros y columnas  sobre el DF mediante .loc
  # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html
  
fruits_to_show = my_fruit_list.loc[fruits_selected]
  
  #visualizamos el grupo de valores seleccionados
streamlit.dataframe (fruits_to_show)
  
# Nueva sección para mostrar la respuesta de la API fruityvice
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
#le pasammos por parámetro el nombre de la fruta que queremos mostrar
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

#streamlit.text(fruityvice_response.json())  #solo muestra los datos en la pantalla

#cogemos el json de la respuesta y lo normalizamos
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# mostramos el resultado normalizado en  un dataframe
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

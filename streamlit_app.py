import streamlit
import requests
import pandas
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Helthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show = my_fruit_list.loc[fruit_selected]

# Display the table on the page.
streamlit.dataframe(fruit_to_show)


#create the repeatable code block (called a function)
def get_fruityvoce_data(this_fruit_choice):
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      return streamlit.dataframe(fruityvice_normalized)
   
   
# New Section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
      streamlit.error("Please select a fruit to get information.")
   else:
      back_from_function = get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)
      

      
#streamlit.write('The user entered ', fruit_choice)



#don't run anything past here while we troubleshoot
streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_row)

#Allow the end user to add a fruit to the list

   

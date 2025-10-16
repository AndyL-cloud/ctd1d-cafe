import streamlit as st

## hzq code
## ----------------------------------------------------------------------------------------------------------------------------------------

coffee = {'Name' : 'Coffee',
          'Image' : '''https://images.pexels.com/photos/312418/pexels-photo-312418.jpeg?cs=srgb&dl=pexels-chevanon-312418.jpg&fm=jpg'''
           Price : 3,
          'Type' : ['Mocha', 'Latte', 'Cappuccino']
         }

frjuice = {'Name' : 'Fruit Juice',
          Price : 2,
          'Type' : ['Apple', 'Lemon', 'Watermelon']
          }

cake = {'Name' : 'Cake',
          Price : 6,
          'Type' : ['Chocolate', 'Vanilla', 'Cheese']
       }

## ----------------------------------------------------------------------------------------------------------------------------------------

st.set_page_config(page_title="CTD1D Café", page_icon="☕", layout="centered")

st.title("☕ CTD1D Café — Team Streamlit App")
st.write("Welcome to our collaborative Streamlit project!")
st.write("Each teammate can add a page inside the `pages/` folder to build new features.")
st.write("MEOW")
st.write("test")

st.image(coffee['Image'])

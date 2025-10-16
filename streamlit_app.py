import streamlit as st

## hzq code
## ----------------------------------------------------------------------------------------------------------------------------------------

coffee = {'Name' : 'Coffee',
          'Image' : 'https://images.pexels.com/photos/312418/pexels-photo-312418.jpeg?cs=srgb&dl=pexels-chevanon-312418.jpg&fm=jpg',
          'Price' : 3,
          'Type' : ['Mocha', 'Latte', 'Cappuccino']
         }

frjuice = {'Name' : 'Fruit Juice',
           'Image' : 'https://media.istockphoto.com/id/915657126/photo/orange-juice-glass-jar-shot-on-rustic-wooden-table.jpg?s=612x612&w=0&k=20&c=rlj0FwRDQOAV_j8-MUQntzIj8fZegbMewj22nNXxiYc=', 
          'Price' : 2,
          'Type' : ['Apple', 'Lemon', 'Watermelon']
          }

cake = {'Name' : 'Cake',
        'Image' : 'https://static.vecteezy.com/system/resources/previews/001/738/638/large_2x/chocolate-cake-slice-free-photo.jpg', 
        'Price' : 6,
        'Type' : ['Chocolate', 'Vanilla', 'Cheese']
       }

## ----------------------------------------------------------------------------------------------------------------------------------------

st.set_page_config(page_title="CTD1D Café", page_icon="☕", layout="centered")

st.title("☕ CTD1D Café — Team Streamlit App")


st.write("Welcome! What would you like to order?")

col1, col2 = st.columns(2)

with col1:
    st.header("Coffee")
    st.image(coffee['Image'], use_column_width=True)

with col2:
    st.header("Fruit Juice")
    st.image(frjuice['Image'], use_column_width=True)

## st.image(coffee['Image'])
## st.image(frjuice['Image'])
## st.image(cake['Image'])


## ----------------------------------------------------------------------------------------------------------------------------------------

##test test
st.title("Search demo")

query = st.text_input("Search", placeholder="Type something…").strip().lower()

data = ["Sourdough Loaf", "Croissant", "Muffin", "Iced Latte"]
results = [x for x in data if query in x.lower()] if query else data

st.subheader("Results")
for item in results:
    st.write("•", item)

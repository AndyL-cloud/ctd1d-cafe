import streamlit as st

page = 1

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
##-----------------------------------------------------------------------------------------------------------------------------------------test

## ----------------------------------------------------------------------------------------------------------------------------------------

if page == 1:
          
          st.set_page_config(page_title="CTD1D Café", page_icon="☕", layout="centered")

          st.title("☕ CTD1D Café — Team Streamlit App")

          st.write("Welcome! What would you like to order?")

          col1, col2, col3 = st.columns(3)

          with col1:
              st.image(coffee['Image'], use_container_width=True)
              if st.button("Coffee", use_container_width=True):
                  st.write("You clicked Button 1!")
                  page = 2

          with col2:
              st.image(frjuice['Image'], use_container_width=True)
              if st.button("Fruit Juice", use_container_width=True):
                  st.write("You clicked Button 1!")
                  page = 2
                        
          with col3:
              st.image(cake['Image'], use_container_width=True)
              if st.button("Cake", use_container_width=True):
                  st.write("You clicked Button 1!")
                  page = 2
                        
          st.title("Search demo")

          query = st.text_input("Search", placeholder="Type something…").strip().lower()

          data = ["Sourdough Loaf", "Croissant", "Muffin", "Iced Latte"]
          results = [x for x in data if query in x.lower()] if query else data

          st.subheader("Results")
          for item in results:
              st.write("•", item)
          
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

if page == 2:
          st.title('Welcome to page 2!')

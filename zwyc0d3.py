import streamlit as st

#This function is to find the searched product in our dictionary
def search_products(product):
  numbers = []
  special_characters = []
  letters = []
  
  #This is to ensure that the user input does not contain any excess spaces
  product = product.lower().strip()

  #This loop is to sort the user input into separate lists accordingly. 
  for i in product:
    if(i.isdigit()):
      numbers.append(i)
    elif(i.isalpha()):
      letters.append(i)
    else:
      special_characters.append()

  combined_letters = ''.join(letters)

  #This loop is to find the separated letter list in our dictionary of products. 
if "cart" not in st.session_state:
    # store as {item_name: qty}
    st.session_state.cart = {}

def add_to_cart(name: str, qty: int = 1):
    st.session_state.cart[name] = st.session_state.cart.get(name, 0) + int(qty)

def remove_from_cart(name: str):
    st.session_state.cart.pop(name, None)

def cart_subtotal() -> float:
    return round(sum(menu[item] * qty for item, qty in st.session_state.cart.items()), 2)
  
  
      


  
    

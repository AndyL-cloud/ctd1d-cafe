import streamlit as st
#This function is to find the searched product in our dictionary
def search_products(product):
  numbers = []
  special_characters = []
  letters = []
  #This is to ensure that the user input does not contain any excess spaces
  product = product.lower().strip()
  for i in product:
    if(i.isdigit()):
      numbers.append(i)
    elif(i.isalpha()):
      letters.append(i)
    else:
      special_characters.append()
  
  
      

def order(category, sub_category, qty):
  type_of_product = 
  
    

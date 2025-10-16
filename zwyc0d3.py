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
  
  
  
  
      

def order(category, sub_category, qty):
  type_of_product = 
  
    

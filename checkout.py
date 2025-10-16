import pandas as pd
import streamlit as st

#dictionary for the thingies
coffee = {'Name' : 'Coffee', 'Price' : 3,'Type' : ['Mocha', 'Latte', 'Cappuccino']}
frjuice = {'Name' : 'Fruit Juice', 'Price' : 2, 'Type' : ['Apple', 'Lemon', 'Watermelon']}
cake = {'Name' : 'Cake', 'Price' : 6, 'Type' : ['Chocolate', 'Vanilla', 'Cheese']}

menu = [coffee, frjuice, cake]

#just for the prices individually bruh
def find_price(item_name):
    for category in menu:
        if item_name in category['Type']:
            return category['Price']

#actual main command that you use to pull
def receipt(full_list):
    #creates new list that willo be used to combine allat
    idlist = []
    quantitylist = []
    pricelist = []
    subtotal = []
    
    #seperates the full_list into 4 seperate columns: id, qty, price, sub
    for individual_items, individual_qty in full_list:
        price = find_price(individual_items)
        idlist.append(individual_items)
        quantitylist.append(individual_qty)
        pricelist.append(price)
        subtotal.append(individual_qty*price)
    
    #panda that into something pandable
    fullframe = pd.DataFrame({'Item':idlist, 'Quantity':quantitylist, 'Price per Item($)':pricelist, 'Subtotal($)':subtotal})
    
    #return allat work 
    return fullframe
        
   
    
full_list = [(coffee['Type'][0], 2), (cake['Type'][1],3)]
st.write(receipt(full_list))
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
# ---------- HELPERS (plain functions per lessons) ----------
def add_to_cart(name, qty=1):
    """Increase qty for an item in the cart."""
    current = st.session_state.cart.get(name, 0)
    st.session_state.cart[name] = current + int(qty)

def remove_from_cart(name):
    """Remove an item entirely from the cart."""
    if name in st.session_state.cart:
        del st.session_state.cart[name]

def cart_subtotal():
    """Compute subtotal from dicts (loops)."""
    total = 0.0
    for item, qty in st.session_state.cart.items():
        price = menu[item]
        total += price * qty
    return round(total, 2)
# ---------- CART DISPLAY ----------
st.header("🛒 Your Cart")
cart = st.session_state.cart

if not cart:
    st.info("Your cart is empty. Add some delicious items from the menu above.")
else:
    c1, c2, c3, c4, c5 = st.columns([4, 2, 2, 2, 2])
    c1.markdown("**Item**")
    c2.markdown("**Price**")
    c3.markdown("**Qty**")
    c4.markdown("**Line Total**")
    c5.markdown("")

    to_remove = []
    for item, qty in cart.items():
        price = menu[item]
        line_total = price * qty
        c1, c2, c3, c4, c5 = st.columns([4, 2, 2, 2, 2])
        c1.write(item)
        c2.write(f"${price:.2f}")
        new_qty = c3.number_input("Qty", min_value=0, max_value=99, value=int(qty), key=f"edit_{item}")
        c4.write(f"${line_total:.2f}")
        if c5.button("Remove", key=f"rm_{item}"):
            to_remove.append(item)
        if new_qty != qty:
            if new_qty == 0:
                to_remove.append(item)
            else:
                st.session_state.cart[item] = int(new_qty)

    for item in to_remove:
        remove_from_cart(item)

    st.markdown("---")
    st.subheader(f"Subtotal: ${cart_subtotal():.2f}")

    if st.button("Place Order (Mock)"):
        st.success("✅ Order placed successfully! (Mock checkout)")
        st.session_state.cart = {}
  
  
      


  
    

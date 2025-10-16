#setup and menu-define the food items, price and images
import streamlit as st
from datetime import datetime
coffee = {'Name':'Coffee','Price':3,'Type':['Mocha','Latte','Cappuccino']}
frjuice = {'Name':'Fruit Juice','Price':2,'Type':['Apple','Lemon','Watermelon']}
cake = {'Name':'Cake','Price':6,'Type':['Chocolate','Vanilla','Cheese']}

#cart
cart=st.session_state.setdefauly('cart',{})

st.title("☕ CTD1D Café Ordering System")
cat=st.selectbox("Category",["coffee","juice","cake"])
item={'coffee':coffee, 'juice':frjuice, 'cake':cake}[cat]
typ=st.selectbox("Variant", item['Type'])
qty=st.number_input("Quantity", 1,20,1)

if st.button("Add to cart"):
  key=(cat, item['Name'], typ)
  cart[key]=cart.get(key,0)+qty
  st.success(f"Added {qty} × {typ} {item['Name']}")

# -------- TIME & DISCOUNT CONTROLS --------
use_sim = st.checkbox("Simulate Time", True)
hour = st.slider("Hour (0–23)", 0, 23, 9)
band = "morning" if hour < 12 else "afternoon" if hour < 19 else "night"
st.info(f"Time Band: **{band}** – discounts vary by time of day!")

# -------- PRICING ENGINE --------
def has_combo(c):
    return any(k[0]=="coffee" for k in c) and any(k[0]=="cake" for k in c)
combo = has_combo(cart)
pct = {"morning":0.2, "afternoon":0.2, "night":0.3}[band]

rows = []
subtotal = disc = total = 0
for (cat,name,var),q in cart.items():
    base = {'coffee':3,'juice':2,'cake':6}[cat]
    line = base * q
    if q >= 3: line *= 0.9  # bulk discount
    pct_line = 0
    if band == "night": pct_line = pct
    elif band == "afternoon" and cat == "juice": pct_line = pct
    elif band == "morning" and combo and cat in {"coffee","cake"}: pct_line = pct
    d = line * pct_line
    after = line - d
    rows.append((f"{name} – {var}", q, base, line, d, after))
    subtotal += line; disc += d; total += after

# -------- DISPLAY CART --------
st.subheader("🧾 Cart Summary")
if rows:
    st.table({"Item":[r[0] for r in rows],
              "Qty":[r[1] for r in rows],
              "Unit":[r[2] for r in rows],
              "Subtotal":[r[3] for r in rows],
              "Discount":[r[4] for r in rows],
              "Total":[r[5] for r in rows]})
    st.metric("Subtotal", f"${subtotal:.2f}")
    st.metric("Discount", f"-${disc:.2f}")
    st.metric("Grand Total", f"${total:.2f}")
else:
    st.info("Cart is empty.")

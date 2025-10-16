streamlit run app.py

import streamlit as st

# --- App Title ---
st.title("☕️ Café Corner")

st.write("""
Welcome to Café Corner!
Choose your items below and place your order.
""")

# --- Menu Data ---
menu = {
    "Espresso": 2.50,
    "Latte": 3.50,
    "Cappuccino": 3.00,
    "Tea": 2.00,
    "Croissant": 2.75,
    "Muffin": 2.25,
}

# --- Order Selection ---
st.header("Menu")
order = {}
for item, price in menu.items():
    qty = st.number_input(
        label=f"{item} (${price:.2f})",
        min_value=0,
        max_value=10,
        value=0,
        step=1,
        key=item
    )
    if qty:
        order[item] = qty

# --- Display Order Summary ---
if order:
    st.header("Your Order")
    total = 0.0
    for item, qty in order.items():
        cost = menu[item] * qty
        total += cost
        st.write(f"{item} × {qty} = ${cost:.2f}")
    st.markdown(f"**Total: ${total:.2f}**")

    # --- Place Order Button ---
    if st.button("Place Order"):
        st.success("🎉 Your order has been placed!")
        st.balloons()
else:
    st.info("Select at least one item to see your order summary.")

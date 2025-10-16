import streamlit as st
from pathlib import Path

# --- your menu dict (already have this) ---
menu = {
    "Espresso": 2.50,
    "Latte": 3.50,
    "Cappuccino": 3.00,
    "Tea": 2.00,
    "Croissant": 2.75,
    "Muffin": 2.25,
}

# ---------- init state ----------
if "cart" not in st.session_state:
    # store as {item_name: qty}
    st.session_state.cart = {}

# ---------- tiny helpers ----------
def add_to_cart(name: str, qty: int = 1):
    st.session_state.cart[name] = st.session_state.cart.get(name, 0) + int(qty)

def remove_from_cart(name: str):
    st.session_state.cart.pop(name, None)

def cart_subtotal() -> float:
    return round(sum(menu[item] * qty for item, qty in st.session_state.cart.items()), 2)

def icon_for(name: str) -> str:
    # fallback emojis; replace with image files if you have them
    mapping = {
        "Espresso": "☕",
        "Latte": "🥛",
        "Cappuccino": "🍶",
        "Tea": "🫖",
        "Croissant": "🥐",
        "Muffin": "🧁",
    }
    return mapping.get(name, "🍞")

# ---------- layout ----------
st.title("Order Menu")

# If you already have real image icons, uncomment and point to your folder:
# ICON_DIR = Path("icons")  # e.g., icons/Croissant.png, icons/Espresso.png

cols = st.columns(3)
for idx, (name, price) in enumerate(menu.items()):
    with cols[idx % 3]:
        # show emoji or an image
        st.markdown(f"### {icon_for(name)} {name}")
        # If using files instead of emojis:
        # img_path = ICON_DIR / f"{name}.png"
        # if img_path.exists():
        #     st.image(str(img_path), use_container_width=True)

        st.caption(f"${price:.2f}")
        qty = st.number_input(
            "Qty", min_value=1, max_value=20, value=1, step=1, key=f"qty_{name}"
        )
        if st.button(f"Add to cart", key=f"add_{name}"):
            add_to_cart(name, qty)
            st.toast(f"Added {qty} × {name}", icon="✅")

st.divider()

# ---------- cart panel ----------
st.header("🛒 Your Cart")
cart = st.session_state.cart

if not cart:
    st.info("Your cart is empty — add something from the menu above.")
else:
    # header row
    c1, c2, c3, c4, c5 = st.columns([4, 2, 2, 2, 2])
    c1.markdown("**Item**")
    c2.markdown("**Price**")
    c3.markdown("**Qty**")
    c4.markdown("**Line**")
    c5.markdown("")

    # editable rows
    to_delete = []
    for item, qty in cart.items():
        price = menu[item]
        line_total = price * qty
        c1, c2, c3, c4, c5 = st.columns([4, 2, 2, 2, 2])
        c1.write(item)
        c2.write(f"${price:.2f}")
        new_qty = c3.number_input(
            f"qty_{item}", min_value=0, max_value=99, value=int(qty), key=f"edit_{item}"
        )
        c4.write(f"${line_total:.2f}")
        if c5.button("Remove", key=f"rm_{item}"):
            to_delete.append(item)
        # apply qty changes live
        if new_qty != qty:
            if new_qty == 0:
                to_delete.append(item)
            else:
                st.session_state.cart[item] = int(new_qty)

    for item in to_delete:
        remove_from_cart(item)

    st.markdown("---")
    left, right = st.columns([3, 2])
    with left:
        if st.button("🧹 Clear cart"):
            st.session_state.cart = {}
            st.toast("Cart cleared", icon="🗑️")
    with right:
        st.subheader(f"Subtotal: ${cart_subtotal():.2f}")
        if st.button("Place order (mock)"):
            st.success("✅ Order placed! (mock checkout)")
            # optionally clear cart after placing
            # st.session_state.cart = {}

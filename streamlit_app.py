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
# ----------------- 3) TIME TOGGLE: 9am → 9pm in 3-hour slots ------------------
st.subheader("⏰ Choose time of day (shop hours 9am–9pm)")
SLOTS = ["09:00–11:59", "12:00–14:59", "15:00–17:59", "18:00–20:59"]
slot = st.radio("Time slot", SLOTS, index=0, horizontal=True)

def slot_to_band(s: str) -> str:
    """Map slot → pricing band."""
    idx = SLOTS.index(s)
    if idx == 0:          # 09:00–11:59
        return "morning"
    if idx in (1, 2):     # 12:00–17:59
        return "afternoon"
    return "evening"      # 18:00–20:59 (we cap at 9pm)

band = slot_to_band(slot)
st.caption(
    f"Active band: **{band}**  • Rules — "
    "Morning: 20% off Coffee+Cake (combo) • "
    "Afternoon: 20% off Fruit Juice • "
    "Evening: 30% off everything"
)

# ----------------- 4) DISCOUNT ENGINE (no cart needed) ------------------------
def has_combo(order_dict) -> bool:
    """True if at least one coffee AND one cake are ordered."""
    has_coffee = any(CATEGORY.get(i) == "coffee" and q > 0 for i, q in order_dict.items())
    has_cake   = any(CATEGORY.get(i) == "cake"   and q > 0 for i, q in order_dict.items())
    return has_coffee and has_cake

def line_total_with_discounts(item: str, qty: int, band: str, combo_active: bool):
    """
    Calculate per-line pricing.
    Returns (line_before_time, time_discount_amount, line_after_time).
    """
    unit = menu[item]
    # Optional batch/integers example: buy ≥3 of same item → 10% off BEFORE time discount
    line = unit * qty
    if qty >= 3:
        line *= 0.90

    cat = CATEGORY.get(item, "other")
    pct = 0.0
    if band == "evening":
        pct = 0.30
    elif band == "afternoon" and cat == "juice":
        pct = 0.20
    elif band == "morning" and combo_active and cat in {"coffee", "cake"}:
        pct = 0.20

    disc = round(line * pct, 2)
    after = round(line - disc, 2)
    return round(line, 2), disc, after

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

if page == 2:
          st.title('Welcome to page 2!')
'''
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
'''

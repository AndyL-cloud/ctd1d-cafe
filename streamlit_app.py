import streamlit as st

page = 1

## hzq code
## ----------------------------------------------------------------------------------------------------------------------------------------

menu = {
    "Mocha": 15.00,
    "Latte": 17.00,
    "Cappuccino": 16.50,
    "Tea": 1.50,
    "Apple Juice": 2.00,
    "Lemon Juice": 2.25,
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


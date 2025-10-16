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
# ===== ORDER & CART (ADD THIS RIGHT AFTER THE 3-COLUMN SECTION) =====
# Keep your existing coffee / frjuice / cake dicts above.

# Shared cart
cart = st.session_state.setdefault("cart", {})  # key = (cat, name, variant) -> qty

st.subheader("🛍️ Add to Cart")

# 1) Pick category -> variant -> qty
cat_label = st.selectbox("Category", ["coffee", "juice", "cake"])
# map label to the dict you already have
cat_map = {"coffee": coffee, "juice": frjuice, "cake": cake}
item = cat_map[cat_label]

variant = st.selectbox("Variant", item["Type"])
qty = st.number_input("Quantity", 1, 50, 1)

if st.button("Add to cart"):
    key = (cat_label, item["Name"], variant)
    cart[key] = cart.get(key, 0) + qty
    st.success(f"Added {qty} × {variant} {item['Name']}")

st.divider()

# 2) Time-based discounts (simulate hour to demo)
st.subheader("⏰ Time & Discounts")
use_sim = st.checkbox("Simulate time", True)
hour = st.slider("Hour (0–23)", 0, 23, 9)
band = "morning" if hour < 12 else "afternoon" if hour < 19 else "night"
st.info(f"Time Band: **{band}** — Morning: coffee+cake combo -20%, Afternoon: juices -20%, Night: all -30%")

# 3) Pricing engine
def has_combo(c):  # coffee + cake present?
    has_coffee = any(k[0] == "coffee" for k in c)
    has_cake   = any(k[0] == "cake"   for k in c)
    return has_coffee and has_cake

combo = has_combo(cart)
pct = {"morning": 0.20, "afternoon": 0.20, "night": 0.30}[band]

rows = []
subtotal = disc = total = 0.0
for (cat_key, name, var), q in cart.items():
    base = {"coffee": 3, "juice": 2, "cake": 6}[cat_key]  # from your dicts
    line = base * q
    if q >= 3:  # simple bulk: ≥3 same variant -> 10% off line BEFORE time discount
        line *= 0.90

    pct_line = 0.0
    if band == "night":
        pct_line = pct
    elif band == "afternoon" and cat_key == "juice":
        pct_line = pct
    elif band == "morning" and combo and cat_key in {"coffee", "cake"}:
        pct_line = pct

    d = line * pct_line
    after = line - d
    rows.append((f"{name} — {var}", int(q), base, round(line, 2), round(d, 2), round(after, 2)))
    subtotal += line
    disc += d
    total += after

# 4) Show receipt
st.subheader("🧾 Cart Summary")
if rows:
    st.table({
        "Item":      [r[0] for r in rows],
        "Qty":       [r[1] for r in rows],
        "Unit":      [r[2] for r in rows],
        "Subtotal":  [r[3] for r in rows],
        "Discount":  [r[4] for r in rows],
        "Total":     [r[5] for r in rows],
    })
    c1, c2, c3 = st.columns(3)
    c1.metric("Subtotal", f"${subtotal:.2f}")
    c2.metric("Discount", f"-${disc:.2f}")
    c3.metric("Grand Total", f"${total:.2f}")
else:
    st.info("Cart is empty — add items above.")

if st.button("🧹 Clear cart"):
    cart.clear()
    st.rerun()
# ===== END OF INSERT =====

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

##test test
          st.title("Search demo")

          query = st.text_input("Search", placeholder="Type something…").strip().lower()

          data = ["Sourdough Loaf", "Croissant", "Muffin", "Iced Latte"]
          results = [x for x in data if query in x.lower()] if query else data

          st.subheader("Results")
          for item in results:
              st.write("•", item)

if page == 2:
          st.title('Welcome to page 2!')

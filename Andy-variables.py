import streamlit as st
from utils.pricing import get_time_band

st.title("Discounts-Controls")

if "enable_time_rules" not in st.session_state:
  st.session_state.enable_time_rules=True
if "enable_combo_rule" not in st.session_state:
  st.session_state.enable_combo_rule=True
if "sim_hour" not in st.session_state:
  st.session_state.sim_hour=9
if "use_sim" not in st.session_state:
  st.session_state.use_sim= True

st.checkbox("Enable time-based discounts", value=st.session_state.enable_time_rules,
            key="enable_time_rules")
st.checkbox("Enable Coffee+Cake combo(morning)", value=st.session_state.enable_combo_rule,
            key="enable_combo_rule")

st.subheader("simulate time (for demo)")
st.slider("Hour (0-23)",0,23, value=st.session_state.use_sim, key"sim_hour")

tb=get_time_band(st.session_state.sim_hour if st.session_state.use_sim else None)
st.info(f"current time band: **{tb}**)
st.markdown("""
- **Morning (<12:00)**: 20% off **coffee & cake** **only if** both are in the cart (combo).  
- **Afternoon (12:00–18:59)**: 20% off **fruit juice**.  
- **Night (≥19:00)**: 30% off **everything**.  
- **Bulk**: Buy ≥3 of the same variant → extra 10% off that line (before time discount).
""")

def has_combo(cart)
has_coffee=any(k[0]=="coffee" for k in cart)
has_cake=any(k[0]=="cake" for k in cart)
return has_coffee and has_cake

discount=o
if "cart" in st.session_state and has_combo(st.session_state.cart):
  discount=0.1
  

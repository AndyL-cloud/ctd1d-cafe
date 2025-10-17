# ========== 3) TIME TOGGLE (9am → 9pm in 3-hour slots) ==========
st.subheader("⏰ Choose time of day (shop hours 9am–9pm)")
SLOTS = ["09:00–11:59", "12:00–14:59", "15:00–17:59", "18:00–20:59"]
slot = st.radio("Time slot", SLOTS, index=0, horizontal=True)

def slot_to_band(s: str) -> str:
    """Turn a slot into a time band name."""
    idx = SLOTS.index(s)
    if idx == 0:            # 09–11
        return "morning"
    if idx in (1, 2):       # 12–17
        return "afternoon"
    return "evening"        # 18–20 (we close by 21:00)

band = slot_to_band(slot)
st.caption(
    f"Active band: **{band}**  • Rules — "
    "Morning: 20% off Coffee+Cake (combo) • "
    "Afternoon: 20% off Fruit Juice • "
    "Evening: 30% off everything • "
    "Bulk: ≥3 of the same item = extra 10% off that line (before time discount)"
)

# ========== 4) DISCOUNT HELPERS (very small + readable) ==========
def has_combo(order_dict) -> bool:
    """True if at least one coffee AND one cake are ordered."""
    has_coffee = any(CATEGORY[i] == "coffee" for i, q in order_dict.items() if q > 0)
    has_cake   = any(CATEGORY[i] == "cake"   for i, q in order_dict.items() if q > 0)
    return has_coffee and has_cake

def line_total(item: str, qty: int, band: str, combo: bool):
    """
    Return (line_before_time, time_discount_amount, line_after_time)
    Steps:
      1) Base = price * qty
      2) If qty >= 3 → bulk 10% off
      3) Apply time-based % by band
    """
    unit = MENU[item]
    line = unit * qty

    # bulk rule (functions + integers)
    if qty >= 3:
        line *= 0.90  # 10% off before time discounts

    # time-based rules
    pct = 0.0
    cat = CATEGORY[item]
    if band == "evening":
        pct = 0.30                           # 30% off everything
    elif band == "afternoon" and cat == "juice":
        pct = 0.20                           # 20% off juices
    elif band == "morning" and combo and cat in {"coffee", "cake"}:
        pct = 0.20                           # combo 20% (coffee + cake both present)

    time_disc = round(line * pct, 2)
    after = round(line - time_disc, 2)
    return round(line, 2), time_disc, after

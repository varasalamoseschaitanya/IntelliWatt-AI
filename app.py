import streamlit as st
import pandas as pd
import random
import time
import numpy as np
from sklearn.linear_model import LinearRegression

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="IntelliWatt AI",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

body {
    background-color: #030726;
}

.main {
    background-color: #030726;
    color: white;
}

h1, h2, h3, h4, h5, h6 {
    color: white;
}

.metric-box {
    background-color: #081136;
    padding: 15px;
    border-radius: 15px;
    text-align: center;
    border: 1px solid #1e2a5a;
}

.metric-title {
    font-size: 18px;
    color: #d1d5db;
}

.metric-value {
    font-size: 42px;
    font-weight: bold;
    color: white;
}

.graph-box {
    background-color: #081136;
    padding: 20px;
    border-radius: 20px;
    border: 1px solid #1e2a5a;
}

.feed-box {
    background-color: #081136;
    padding: 20px;
    border-radius: 25px;
    border: 1px solid #1e2a5a;
    height: 520px;
    overflow-y: auto;
}

.feed-item {
    background-color: #16354F;
    padding: 14px;
    margin-bottom: 12px;
    border-radius: 12px;
    border-left: 5px solid #00FFD1;
    font-size: 16px;
    color: white;
}

.status-box {
    padding: 15px;
    border-radius: 10px;
    color: white;
    text-align: center;
    font-weight: bold;
    min-height: 60px;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: 0.4s;
}

.green-box {
    background-color: #14532d;
}

.red-box {
    background-color: #7f1d1d;
}

.active-button {
    opacity: 1;
    animation:
        activeFloat 2s ease-in-out infinite,
        activeGlow 2s ease-in-out infinite;
}

.inactive-button {
    opacity: 0.30;
    animation: none;
    box-shadow: none;
}

@keyframes activeFloat {
    0% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-5px);
    }

    100% {
        transform: translateY(0px);
    }
}

@keyframes activeGlow {
    0% {
        box-shadow: 0 0 8px rgba(255,255,255,0.15);
    }

    50% {
        box-shadow:
            0 0 18px rgba(0,229,255,0.45),
            0 0 28px rgba(0,229,255,0.25);
    }

    100% {
        box-shadow: 0 0 8px rgba(255,255,255,0.15);
    }
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------

top1, top2 = st.columns([8, 2])

with top1:
    st.markdown(
        "<h1 style='color:#39FF14;'>IntelliWatt <span style='color:#ff4d4d;'>AI</span></h1>",
        unsafe_allow_html=True
    )

with top2:
    environment = st.selectbox(
        "",
        ["Home", "Hostel", "Office", "Factory"]
    )

# ---------------- DEVICE PANEL ----------------

st.markdown("## Device Simulation Panel")

d1, d2, d3, d4 = st.columns(4)

with d1:
    fan = st.toggle("Fan")
    tv = st.toggle("TV")

with d2:
    fridge = st.toggle("Fridge")
    washing_machine = st.toggle("Washing Machine")

with d3:
    microwave = st.toggle("Microwave")
    ac = st.toggle("AC")

with d4:
    heater = st.toggle("Heater")
    water_motor = st.toggle("Water Motor")

# ---------------- POWER CALCULATION ----------------

power = 0
overload_devices = []

if fan:
    power += 75

if tv:
    power += 120

if fridge:
    power += 250

if washing_machine:
    power += 1000
    overload_devices.append("WASHING MACHINE")

if microwave:
    power += 1200
    overload_devices.append("MICROWAVE")

if ac:
    power += 1500
    overload_devices.append("AC")

if heater:
    power += 2000
    overload_devices.append("HEATER")

if water_motor:
    power += 1500
    overload_devices.append("WATER MOTOR")

if power > 0:
    power += random.randint(10, 50)
else:
    power = 0

overload_device = ", ".join(overload_devices) if overload_devices else "NONE"

# ---------------- OVERLOAD LIMIT ----------------

OVERLOAD_LIMIT = 3000

# ---------------- SESSION STORAGE ----------------

if "power_data" not in st.session_state:
    st.session_state.power_data = []

if "feed_data" not in st.session_state:
    st.session_state.feed_data = []

st.session_state.power_data.append(power)
st.session_state.power_data = st.session_state.power_data[-30:]

power_data = st.session_state.power_data

# ---------------- AI PREDICTION ----------------

if len(power_data) >= 2:
    x = np.array(range(len(power_data))).reshape(-1, 1)
    y = np.array(power_data)

    model = LinearRegression()
    model.fit(x, y)

    future = np.array([[len(power_data) + 1]])
    prediction = model.predict(future)[0]
    prediction = max(0, prediction)
else:
    prediction = power

# ---------------- COST CALCULATION ----------------

cost_per_unit = 6
total_cost = sum(power_data) / 1000 * cost_per_unit / 3600

# ---------------- OVERLOAD EVENTS ----------------

overload_count = len([p for p in power_data if p > OVERLOAD_LIMIT])

# ---------------- SMART LOAD STATUS ----------------

if power < 1000:
    status = "SAFE"
    status_color = "#22c55e"

elif power < 2200:
    status = "NORMAL"
    status_color = "#3b82f6"

elif power < 2800:
    status = "HIGH LOAD"
    status_color = "#facc15"

elif power < 3000:
    status = "CRITICAL"
    status_color = "#f97316"

else:
    status = "OVERLOAD"
    status_color = "#ef4444"

# ---------------- METRICS ----------------

m1, m2, m3, m4, m5 = st.columns(5)

with m1:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-title">Current Usage</div>
        <div class="metric-value">{power} W</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-title">Predicted Usage</div>
        <div class="metric-value">{prediction:.0f} W</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-title">Estimated Cost</div>
        <div class="metric-value">₹ {total_cost:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-title">Overload Events</div>
        <div class="metric-value">{overload_count}</div>
    </div>
    """, unsafe_allow_html=True)

with m5:
    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-title">Load Status</div>
        <div class="metric-value" style="color:{status_color}; font-size:28px;">
            {status}
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------------- MAIN AREA ----------------

left, right = st.columns([3, 2])

# ---------------- GRAPH ----------------

with left:
    st.markdown(
        "<h1 style='color:#00E5FF;'>Live Power Graph</h1>",
        unsafe_allow_html=True
    )

    st.markdown('<div class="graph-box">', unsafe_allow_html=True)

    chart_data = pd.DataFrame(
        power_data,
        columns=["Power"]
    )

    st.line_chart(chart_data)

    st.markdown('</div>', unsafe_allow_html=True)

    s1, s2 = st.columns(2)

    with s1:
        green_class = "active-button" if power <= OVERLOAD_LIMIT else "inactive-button"

        st.markdown(
            f"""
            <div class="status-box green-box {green_class}">
                ✅ SYSTEM OPERATING NORMALLY
            </div>
            """,
            unsafe_allow_html=True
        )

    with s2:
        red_class = "active-button" if power > OVERLOAD_LIMIT else "inactive-button"

        red_text = (
            f"⚠ OVERLOAD DETECTED : {overload_device}"
            if power > OVERLOAD_LIMIT
            else
            "⚠ NO OVERLOAD"
        )

        st.markdown(
            f"""
            <div class="status-box red-box {red_class}">
                {red_text}
            </div>
            """,
            unsafe_allow_html=True
        )

# ---------------- LIVE FEED ----------------

with right:
    st.markdown(
        "<h1 style='color:#00E5FF;'>Live Activity Feed</h1>",
        unsafe_allow_html=True
    )

    feed = f"""
    <div class="feed-item">
        ⚡ Current : {power}W <br><br>
        🎯 Prediction : {prediction:.2f}W <br><br>
        💰 Cost : ₹{total_cost:.2f} <br><br>
        🔥 Environment : {environment}
    </div>
    """

    st.session_state.feed_data.insert(0, feed)
    st.session_state.feed_data = st.session_state.feed_data[:20]

    final_feed = "".join(st.session_state.feed_data)

    st.markdown(
        f"""
        <div class="feed-box">
            {final_feed}
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------- AUTO REFRESH ----------------

time.sleep(1)
st.rerun()

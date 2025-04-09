
import streamlit as st
import pandas as pd

# Sample vehicle data
vehicles = pd.DataFrame([
    {"Make": "Toyota", "Model": "Camry", "Year": 2024, "Trim": "XLE", "Color": "Silver", "Dealer": "Sunrise Toyota"},
    {"Make": "Toyota", "Model": "RAV4", "Year": 2024, "Trim": "XSE Hybrid", "Color": "Blue", "Dealer": "Metro Toyota"},
    {"Make": "Toyota", "Model": "Highlander", "Year": 2024, "Trim": "Limited", "Color": "White", "Dealer": "Evergreen Toyota"},
    {"Make": "Toyota", "Model": "Corolla", "Year": 2024, "Trim": "SE", "Color": "Red", "Dealer": "City Toyota"},
    {"Make": "Toyota", "Model": "Tacoma", "Year": 2024, "Trim": "TRD Off-Road", "Color": "Gray", "Dealer": "Westside Toyota"},
])

# Dealer data
dealers = {
    "Sunrise Toyota": {"City": "San Diego", "Perks": ["At-Home Delivery", "Lifetime Powertrain Warranty"], "Review": "Friendly service and smooth online process."},
    "Metro Toyota": {"City": "Los Angeles", "Perks": ["At-Home Delivery"], "Review": "No-pressure experience and tech-savvy team."},
    "Evergreen Toyota": {"City": "San Jose", "Perks": ["Lifetime Powertrain Warranty"], "Review": "Great selection and long-term support."},
    "City Toyota": {"City": "San Francisco", "Perks": [], "Review": "Efficient buying process, tight parking."},
    "Westside Toyota": {"City": "Oakland", "Perks": ["At-Home Delivery", "Lifetime Powertrain Warranty"], "Review": "Transparent pricing and easy to work with."},
}

# Splash
st.title("🚗 Kabang")
st.subheader("Smarter Car Shopping Starts Here")
st.markdown("Search new cars. Compare dealer perks. Get trade-in estimates — all in one place.")
st.divider()

# Search
st.header("🔍 Search New Vehicles")
make = st.selectbox("Make", ["Toyota"])
model = st.selectbox("Model", vehicles["Model"].unique())
year = st.selectbox("Year", vehicles["Year"].unique())

results = vehicles[(vehicles["Make"] == make) & (vehicles["Model"] == model) & (vehicles["Year"] == year)]

st.subheader("Results:")
for _, row in results.iterrows():
    d = dealers.get(row["Dealer"], {})
    st.markdown(f"**{row['Year']} {row['Make']} {row['Model']} {row['Trim']}**")
    st.markdown(f"Dealer: {row['Dealer']} – {d.get('City', '')}")
    st.markdown(f"Color: {row['Color']}")
    if d.get("Perks"):
        st.markdown("Perks: " + ", ".join(d["Perks"]))
    st.markdown(f"_"{d.get('Review', '')}"_")
    st.markdown("---")

# Trade-in
st.header("💸 Trade-In Estimator")
col1, col2 = st.columns(2)
with col1:
    t_year = st.selectbox("Vehicle Year", range(2005, 2025)[::-1])
    t_make = st.text_input("Make")
    t_model = st.text_input("Model")
with col2:
    mileage = st.number_input("Mileage", min_value=0, max_value=300000, step=5000)
    condition = st.selectbox("Condition", ["Excellent", "Good", "Fair", "Poor"])

if st.button("Estimate Trade-In Value"):
    if mileage and t_make and t_model:
        estimate = max(1000, 20000 - (mileage // 1000 * 150))
        st.success(f"Estimated Trade-In Value: ${estimate:,} - ${estimate + 2000:,}")
    else:
        st.warning("Enter all trade-in info for an estimate.")

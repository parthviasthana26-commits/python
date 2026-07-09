import streamlit as st
import pandas as pd

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Black Friday Sales Explorer",
    page_icon="🛍️",
    layout="wide"
)

# ---------------- LOAD DATA ----------------
df = pd.read_csv("BlackFriday.csv")

# ---------------- TITLE ----------------
st.title("🛍️ Black Friday Sales Explorer")
st.markdown("### Analyze Customer Purchase Behaviour")

# ---------------- SIDEBAR ----------------
st.sidebar.header("🔍 Filters")

gender = st.sidebar.selectbox(
    "Select Gender",
    df["Gender"].unique()
)

age_options = ["All"] + sorted(df["Age"].unique().tolist())

age = st.sidebar.selectbox(
    "Select Age Group",
    age_options
)

# ---------------- FILTER DATA ----------------
filtered = df[df["Gender"] == gender]

if age != "All":
    filtered = filtered[filtered["Age"] == age]

# ---------------- METRICS ----------------
st.subheader("📊 Sales Summary")

col1, col2, col3 = st.columns(3)

col1.metric("👥 Customers", len(filtered))
col2.metric("💰 Total Purchase", f"₹ {int(filtered['Purchase'].sum()):,}")
col3.metric("📈 Avg Purchase", f"₹ {filtered['Purchase'].mean():.2f}")

col4, col5 = st.columns(2)

col4.metric("🔥 Max Purchase", f"₹ {filtered['Purchase'].max()}")
col5.metric("📉 Min Purchase", f"₹ {filtered['Purchase'].min()}")

st.divider()

# ---------------- PURCHASE CHART ----------------
st.subheader("📈 Purchase Distribution")
st.bar_chart(filtered["Purchase"].head(20))

# ---------------- AGE ANALYSIS ----------------
st.subheader("👥 Customers by Age")
st.bar_chart(filtered["Age"].value_counts())

# ---------------- CITY ANALYSIS ----------------
st.subheader("🏙️ City Category")
st.bar_chart(filtered["City_Category"].value_counts())

# ---------------- OCCUPATION ----------------
st.subheader("💼 Occupation Distribution")
st.bar_chart(filtered["Occupation"].value_counts())

# ---------------- SEARCH USER ----------------
st.subheader("🔎 Search Customer")

user = st.text_input("Enter User ID")

if user:
    result = df[df["User_ID"].astype(str) == user]

    if len(result) > 0:
        st.success("Customer Found ✅")
        st.dataframe(result)
    else:
        st.error("No Customer Found")

# ---------------- DOWNLOAD ----------------
csv = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Data",
    data=csv,
    file_name="Filtered_BlackFriday_Data.csv",
    mime="text/csv"
)

# ---------------- RECORDS ----------------
st.info(f"📌 Total Filtered Records: {len(filtered)}")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<center><h4>👩‍💻 Developed by Parthvi Asthana</h4></center>",
    unsafe_allow_html=True
)
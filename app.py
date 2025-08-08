# app.py
import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# Load Data
# =========================
@st.cache_data
def load_data():
    df = pd.read_csv("vehicle_data_clean_timeseries.csv", parse_dates=["date"])
    return df

df = load_data()

# =========================
# Sidebar Filters
# =========================
st.sidebar.header("Filters")

# Date Range Filter
min_date = df["date"].min()
max_date = df["date"].max()
date_range = st.sidebar.date_input("Select Date Range", [min_date, max_date])

# Category Filter
categories = df["category"].unique()
selected_categories = st.sidebar.multiselect(
    "Select Vehicle Categories", categories, default=categories
)

# Manufacturer Filter
manufacturers = df["manufacturer"].unique()
selected_manufacturers = st.sidebar.multiselect(
    "Select Manufacturers", selected_manufacturers if 'selected_manufacturers' in locals() else manufacturers, default=manufacturers
)

# =========================
# Filter Data
# =========================
filtered_df = df[
    (df["date"] >= pd.to_datetime(date_range[0])) &
    (df["date"] <= pd.to_datetime(date_range[1])) &
    (df["category"].isin(selected_categories)) &
    (df["manufacturer"].isin(selected_manufacturers))
]

# =========================
# Growth Calculations
# =========================
def calculate_growth(data, period):
    data = data.copy()
    data = data.sort_values("date")
    data["prev_registrations"] = data["registrations"].shift(period)
    data["growth_%"] = ((data["registrations"] - data["prev_registrations"]) / data["prev_registrations"]) * 100
    return data

# YoY & QoQ for selected data
category_monthly = filtered_df.groupby(["date", "category"])["registrations"].sum().reset_index()
category_yoy = calculate_growth(category_monthly, 12)
category_qoq = calculate_growth(category_monthly, 3)

# =========================
# KPI Metrics
# =========================
st.title("🚗 Vehicle Registration Dashboard")
st.markdown("Investor-focused insights on vehicle registrations from Vahan data.")

total_reg = filtered_df["registrations"].sum()
yoy_growth = category_yoy["growth_%"].mean()
qoq_growth = category_qoq["growth_%"].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Registrations", f"{total_reg:,}")
col2.metric("Avg YoY Growth", f"{yoy_growth:.2f}%" if pd.notna(yoy_growth) else "N/A")
col3.metric("Avg QoQ Growth", f"{qoq_growth:.2f}%" if pd.notna(qoq_growth) else "N/A")

# =========================
# Charts
# =========================
# Trend Chart
fig_trend = px.line(filtered_df, x="date", y="registrations", color="category", title="Registration Trends Over Time")
st.plotly_chart(fig_trend, use_container_width=True)

# YoY Growth Chart
fig_yoy = px.bar(category_yoy, x="date", y="growth_%", color="category", title="Year-over-Year Growth %")
st.plotly_chart(fig_yoy, use_container_width=True)

# QoQ Growth Chart
fig_qoq = px.bar(category_qoq, x="date", y="growth_%", color="category", title="Quarter-over-Quarter Growth %")
st.plotly_chart(fig_qoq, use_container_width=True)

# =========================
# Investor Insight
# =========================
fastest_growing = filtered_df.groupby("manufacturer")["registrations"].sum().idxmax()
st.subheader("💡 Investor Insight")
st.write(f"The top-performing manufacturer in the selected range is **{fastest_growing}** based on total registrations.")

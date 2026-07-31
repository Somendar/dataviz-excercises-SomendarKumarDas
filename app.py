import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="Olist E-Commerce Dashboard",
    page_icon="🛒",
    layout="wide"
)

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\Somendar Das\Desktop\Ecom-DV\master_dataset.csv")

    df["order_purchase_timestamp"] = pd.to_datetime(df["order_purchase_timestamp"])

    return df

master_df = load_data()

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------
st.sidebar.title("Filters")

years = sorted(master_df["order_year"].dropna().unique())
selected_year = st.sidebar.multiselect(
    "Select Year",
    years,
    default=years
)

states = sorted(master_df["customer_state"].dropna().unique())
selected_states = st.sidebar.multiselect(
    "Select State",
    states,
    default=states
)

categories = sorted(master_df["product_category_name_english"].dropna().unique())
selected_categories = st.sidebar.multiselect(
    "Product Category",
    categories,
    default=categories
)

filtered_df = master_df[
    (master_df["order_year"].isin(selected_year)) &
    (master_df["customer_state"].isin(selected_states)) &
    (master_df["product_category_name_english"].isin(selected_categories))
]

# ---------------------------------------------------
# Dashboard Title
# ---------------------------------------------------
st.title("🛒 Olist E-Commerce Business Dashboard")
st.markdown("Interactive Business Intelligence Dashboard")

# ---------------------------------------------------
# KPI Cards
# ---------------------------------------------------
total_revenue = filtered_df["price"].sum()
total_orders = filtered_df["order_id"].nunique()
total_customers = filtered_df["customer_unique_id"].nunique()
avg_review = filtered_df["review_score"].mean()
avg_delivery = filtered_df["delivery_days"].mean()

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("💰 Revenue", f"${total_revenue:,.0f}")
col2.metric("📦 Orders", total_orders)
col3.metric("👥 Customers", total_customers)
col4.metric("⭐ Avg Review", f"{avg_review:.2f}")
col5.metric("🚚 Avg Delivery", f"{avg_delivery:.1f} Days")

st.divider()

# ---------------------------------------------------
# Monthly Orders
# ---------------------------------------------------
monthly_orders = (
    filtered_df.groupby(["order_year","order_month"])["order_id"]
    .nunique()
    .reset_index(name="Orders")
)

month_order = [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]

monthly_orders["order_month"] = pd.Categorical(
    monthly_orders["order_month"],
    categories=month_order,
    ordered=True
)

monthly_orders = monthly_orders.sort_values(
    ["order_year","order_month"]
)

fig = px.line(
    monthly_orders,
    x="order_month",
    y="Orders",
    color="order_year",
    markers=True,
    title="Monthly Order Trend"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# Revenue by State
# ---------------------------------------------------
col1, col2 = st.columns(2)

with col1:

    state_sales = (
        filtered_df.groupby("customer_state")["price"]
        .sum()
        .reset_index()
        .sort_values("price", ascending=False)
    )

    fig = px.bar(
        state_sales,
        x="customer_state",
        y="price",
        title="Revenue by State"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    category_sales = (
        filtered_df.groupby("product_category_name_english")["price"]
        .sum()
        .reset_index()
        .sort_values("price", ascending=False)
        .head(10)
    )

    fig = px.bar(
        category_sales,
        x="price",
        y="product_category_name_english",
        orientation="h",
        title="Top Product Categories"
    )

    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# Payment & Reviews
# ---------------------------------------------------
col1, col2 = st.columns(2)

with col1:

    payment = (
        filtered_df["payment_type"]
        .value_counts()
        .reset_index()
    )

    payment.columns = ["Payment Type","Count"]

    fig = px.pie(
        payment,
        names="Payment Type",
        values="Count",
        title="Payment Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    review = (
        filtered_df["review_score"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    review.columns = ["Review Score","Count"]

    fig = px.bar(
        review,
        x="Review Score",
        y="Count",
        color="Review Score",
        title="Review Score Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# Purchase Hour & Delivery
# ---------------------------------------------------
col1, col2 = st.columns(2)

with col1:

    hour = (
        filtered_df.groupby("purchase_hour")["order_id"]
        .nunique()
        .reset_index(name="Orders")
    )

    fig = px.line(
        hour,
        x="purchase_hour",
        y="Orders",
        markers=True,
        title="Orders by Purchase Hour"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    delivery = (
        filtered_df.groupby("late_delivery")["review_score"]
        .mean()
        .reset_index()
    )

    fig = px.bar(
        delivery,
        x="late_delivery",
        y="review_score",
        title="Average Review by Delivery Status"
    )

    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------
# Top Sellers
# ---------------------------------------------------
seller_sales = (
    filtered_df.groupby("seller_id")["price"]
    .sum()
    .reset_index()
    .sort_values("price", ascending=False)
    .head(10)
)

fig = px.bar(
    seller_sales,
    x="seller_id",
    y="price",
    title="Top 10 Sellers by Revenue"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

st.success("Dashboard Developed using Streamlit & Plotly")
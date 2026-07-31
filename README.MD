# 🛒 Olist E-Commerce Analytics Dashboard

##  Project Overview

This project presents an end-to-end data analytics solution using the Brazilian Olist E-Commerce dataset. The objective is to analyze customer behavior, sales performance, product trends, payment methods, delivery efficiency, and customer satisfaction through interactive visualizations and a Streamlit dashboard.

The project follows the complete data analytics workflow from data understanding and preprocessing to business intelligence and dashboard development.

---

##  Objectives

- Analyze sales performance across different time periods.
- Identify top-performing product categories.
- Understand customer purchasing behavior.
- Evaluate delivery performance and customer satisfaction.
- Analyze payment preferences.
- Build an interactive dashboard for business decision-making.

---

##  Dataset

**Dataset:** Brazilian Olist E-Commerce Dataset

The dataset contains information about:

- Customers
- Orders
- Order Items
- Products
- Sellers
- Payments
- Reviews
- Geolocation
- Product Category Translation

---

##  Technologies Used

- Python
- Pandas
- NumPy
- Plotly
- Streamlit
- Jupyter Notebook
- VS Code

---

##  Project Workflow

### 1. Data Understanding
- Explored all dataset tables
- Studied relationships between tables
- Identified primary and foreign keys

### 2. Data Cleaning
- Converted date columns
- Handled missing values
- Validated relationships
- Created master analytical dataset

### 3. Feature Engineering
Created business-ready features including:
- Order Year
- Order Month
- Purchase Hour
- Delivery Days
- Delivery Delay
- Late Delivery Flag
- Total Item Value

### 4. Exploratory Data Analysis (EDA)

Business questions answered include:

- Monthly order trends
- Top revenue-generating product categories
- Revenue by customer state
- Payment method distribution
- Customer review distribution
- Orders by weekday
- Orders by purchase hour
- Delivery performance
- Impact of late delivery on customer reviews
- Top-performing sellers

### 5. Dashboard Development

Built an interactive Streamlit dashboard featuring:

- KPI Cards
- Sidebar Filters
- Monthly Sales Trend
- Revenue by State
- Product Category Analysis
- Payment Distribution
- Customer Review Analysis
- Purchase Hour Analysis
- Delivery Performance
- Top Sellers

---

##  Key Business Insights

- Customer orders increased significantly over time.
- Health & Beauty is the highest revenue-generating product category.
- São Paulo contributes the largest share of revenue.
- Credit Card is the most preferred payment method.
- Most customers provide positive reviews (4–5 stars).
- Orders are primarily placed during weekdays and daytime hours.
- Late deliveries significantly reduce customer satisfaction.
- A small group of sellers contributes a large share of marketplace revenue.

---

##  Business Recommendations

- Increase investment in high-performing product categories.
- Expand marketing campaigns in high-revenue states.
- Improve delivery performance to enhance customer satisfaction.
- Strengthen partnerships with top-performing sellers.
- Optimize inventory planning during peak shopping periods.

---

##  Project Structure

```
Ecom-DV/
│
├── app.py
├── Ecommerce_Analytics.ipynb
├── master_dataset.csv
├── requirements.txt
├── README.md
│
├── data/
│   └── raw/
│
└── assets/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Ecom-DV.git
```

Navigate to the project folder:

```bash
cd Ecom-DV
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit dashboard:

```bash
streamlit run app.py
```

---

##  Dashboard Preview

The dashboard provides interactive filtering by:

- Year
- State
- Product Category

It includes:

- Business KPIs
- Interactive Plotly Charts
- Revenue Analysis
- Customer Insights
- Delivery Performance
- Seller Performance

---

## 👨 Author

**Somendar Kumar Das**



---

##  License

This project was developed for academic purposes as part of the Data Visualization course.
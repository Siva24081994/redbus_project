import streamlit as st
import pandas as pd
import mysql.connector

# MySQL connection
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Red_bus_project"
    )

# Function to load data from the MySQL database
def load_data():
    conn = create_connection()
    query = "SELECT * FROM Redbus_routes"
    return pd.read_sql(query, conn)

# Load data
data = load_data()

# Streamlit application
st.markdown(
    "<h1 style='color: red; font-size: 48px; font-weight: bold;'>Redbus</h1>", 
    unsafe_allow_html=True
)


# Route filter (initial filter)
route_name = st.sidebar.selectbox("Select Route", options=data['route_name'].unique())

# Filter the data based on the selected route
filtered_data_by_route = data[data['route_name'] == route_name]



# Optional Bus name filter (only shows buses for the selected route, but can be skipped)
busname = st.sidebar.selectbox(
    "Bus Name (optional)", 
    options=["All"] + list(filtered_data_by_route['busname'].unique()), 
    index=0
)

# Optional Bus type filter (only shows bus types for the selected route and bus, can be skipped)
bustype = st.sidebar.selectbox(
    "Bus Type (optional)", 
    options=["All"] + list(filtered_data_by_route['bustype'].unique()), 
    index=0
)

# Price filter
price_range = st.sidebar.slider("Price Range", min_value=0, max_value=int(filtered_data_by_route['price'].max()), value=(0, int(filtered_data_by_route['price'].max())))

# Star rating slider
star_rating_range = st.sidebar.slider(
    "Star Rating Range",
    min_value=0.0,
    max_value=5.0,
    value=(0.0, 5.0),
    step=0.1
)

# Seat availability slider
seat_availability_range = st.sidebar.slider(
    "Seats Available",
    min_value=0,
    max_value=int(filtered_data_by_route['seats_available'].max()),
    value=(0, int(filtered_data_by_route['seats_available'].max()))
)

# Apply filters based on selected route, and optionally selected bus name, bus type, price, star rating, and seat availability
filtered_data = filtered_data_by_route.copy()

if busname != "All":
    filtered_data = filtered_data[filtered_data['busname'] == busname]  # Filter by bus name if selected

if bustype != "All":
    filtered_data = filtered_data[filtered_data['bustype'] == bustype]  # Filter by bus type if selected

# Filter by price range, star rating, and seat availability
filtered_data = filtered_data[
    (filtered_data['price'] >= price_range[0]) & (filtered_data['price'] <= price_range[1])
]
filtered_data = filtered_data[
    (filtered_data['star_rating'] >= star_rating_range[0]) & (filtered_data['star_rating'] <= star_rating_range[1])
]
filtered_data = filtered_data[
    (filtered_data['seats_available'] >= seat_availability_range[0]) & (filtered_data['seats_available'] <= seat_availability_range[1])
]

# Display filtered data
st.subheader(f"Bus Details for Route: {route_name}")
st.write(filtered_data)
# Add a video (you can use a YouTube link or local file)
st.video("https://youtu.be/eyAAUGhvZu8?si=U5PiwQkDpirTJaHO")  # Replace with actual Redbus video link

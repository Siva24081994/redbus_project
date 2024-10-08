Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit

Project Overview
This project, titled "Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit", focuses on automating the process of web scraping Redbus data, storing it in a structured SQL database, and building an interactive application using Streamlit. The application enables users to filter and explore bus routes, schedules, prices, seat availability, and more. By using Python, Selenium, SQL, and Streamlit, this project enhances the transportation domain's data-driven decision-making processes.

Table of Contents
Skills Takeaway
Domain
Problem Statement
Business Use Cases
Approach
Database Schema
Python Code Overview
Data Scraping with Selenium
SQL Database Interaction
Streamlit Application
Results
Project Evaluation Metrics
References

1. Skills Takeaway
By working on this project, you will develop the following skills:
Web Scraping using Selenium
Python programming
SQL Database Interaction
Streamlit for building interactive web applications
Data Filtering and Analysis

2. Domain
Domain: Transportation
The transportation industry can benefit from automated data scraping, analysis, and visualization for improving operational efficiency and strategic planning.

3. Problem Statement
The Redbus Data Scraping and Filtering with Streamlit Application aims to automate the extraction, storage, and analysis of bus travel data from the Redbus website. The scraped data includes information like bus routes, schedules, prices, seat availability, etc. The application allows users to filter and analyze this data, providing valuable insights for businesses and travelers.
Challenges Solved:
Automating data extraction with Selenium.
Storing scraped data in an SQL database.
Allowing users to interactively filter and analyze data via Streamlit.

4. Business Use Cases
This solution can be applied in various business scenarios:
Travel Aggregators: Providing real-time bus schedules and seat availability for customers.
Market Analysis: Understanding travel patterns for market research.
Customer Service: Offering personalized travel recommendations based on data insights.
Competitor Analysis: Comparing pricing and service levels with competitors.

5. Approach
Data Scraping:
Selenium is used to scrape Redbus data, including routes, schedules, prices, and seat availability.
Data Storage:
The scraped data is stored in an SQL database named Red_bus_project, in the table redbus_routes.
Streamlit Application:
A Streamlit application is developed to visualize and filter the scraped data.
Filters include options for route, bus type, price range, star rating, and seat availability.
Data Analysis:
The application retrieves data using SQL queries based on user inputs, allowing for dynamic filtering and data exploration.

6. Database Schema
Database Name: Red_bus_project
Table Name: redbus_routes
The table redbus_routes stores all the bus details scraped from Redbus. The table schema is as follows:
Column Name
Data Type
Description
id
INT
Primary Key (Auto-increment)
route_name
TEXT
The name of the bus route
route_link
TEXT
URL link for route details
busname
TEXT
The name of the bus
bustype
TEXT
The type of bus (Sleeper/Seater/AC/Non-AC)
departing_time
TIME
The time the bus departs
duration
TEXT
Duration of the journey
reaching_time
TIME
The time the bus reaches the destination
star_rating
FLOAT
The star rating given by passengers
price
DECIMAL
The ticket price
seats_available
INT
The number of seats available

SQL Script to Create the Database and Table:
CREATE DATABASE IF NOT EXISTS Red_bus_project;

USE Red_bus_project;

CREATE TABLE IF NOT EXISTS redbus_routes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    route_name TEXT NOT NULL,
    route_link TEXT,
    busname TEXT NOT NULL,
    bustype TEXT NOT NULL,
    departing_time TIME,
    duration TEXT NOT NULL,
    reaching_time TIME,
    star_rating FLOAT,
    price DECIMAL(10, 2) NOT NULL,
    seats_available INT NOT NULL
);


7. Python Code Overview
Data Scraping with Selenium
The following code demonstrates scraping data using Selenium:
python
Copy code
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up WebDriver (ChromeDriver in this case)
driver = webdriver.Chrome()

# Open Redbus Website
driver.get("https://www.redbus.in/")

# Code to navigate and scrape relevant data from the website

# Close the browser
driver.quit()

This scraped data includes:
Route name and link
Bus name, type, and availability
Departing and reaching time
Star rating and price
SQL Database Interaction
After scraping the data, it is stored in the redbus_routes table in the Red_bus_project database:
import mysql.connector

# Establish connection to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Red_bus_project"
)

# SQL Insert Query
insert_query = """
INSERT INTO redbus_routes(route_name, route_link, busname, bustype, departing_time, duration, reaching_time, star_rating, price, seats_available)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Example of inserting data
mycursor = mydb.cursor()
mycursor.execute(insert_query, (route_name, route_link, bus_name, bus_type, depart_time, duration, reach_time, star_rating, price, seats_available))
mydb.commit()

# Close connection
mycursor.close()
mydb.close()

Streamlit Application
The Streamlit app allows users to interactively filter the bus data based on parameters like route, price, and availability.

import streamlit as st
import pandas as pd
import mysql.connector

# Streamlit Filters and UI
route = st.selectbox("Select Route", ["Route 1", "Route 2", "Route 3"])
price_range = st.slider("Price Range", 100, 5000)

# Fetch filtered data from SQL database
def fetch_data(route, price_range):
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="Red_bus_project")
    query = f"SELECT * FROM redbus_routes WHERE route_name = '{route}' AND price <= {price_range}"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Display data
filtered_data = fetch_data(route, price_range)
st.write(filtered_data)


8. Results
The project aims to achieve the following:
Successfully scrape data from Redbus for at least 10 Government State Bus Transport routes.
Store the data in an SQL database.
Develop an interactive Streamlit application for users to filter and explore the bus data.

9. Project Evaluation Metrics
The project will be evaluated based on the following criteria:
Data Scraping Accuracy: Completeness and correctness of the scraped data.
Database Design: Effective and efficient database schema.
Application Usability: User experience and ease of use of the Streamlit application.
Filter Functionality: Effectiveness and responsiveness of data filters.
Code Quality: Adherence to coding standards and best practices.

10. References
Streamlit Documentation: Streamlit Docs
Selenium Documentation: Selenium Docs
How to Establish SQL Connection: Guide
Project FAQs: RedBus_FAQs
Live Evaluation Session Booking: Booking Link



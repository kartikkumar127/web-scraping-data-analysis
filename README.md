# Web-Scraping-And-Data-Analysis
An end-to-end data engineering and analytics project that demonstrates web scraping, data cleaning, interactive visualization using Streamlit, and business insights using Power BI.

## Project Overview

This project scrapes book data from a live website, cleans and transforms the data using Python, provides an interactive Streamlit web application, and visualizes insights through a Power BI dashboard.

The project simulates a real-world data pipeline used by data analysts and data engineers.

## Tech Stack

Python (Requests, BeautifulSoup, Pandas)

Streamlit (Web Application)

Power BI (Dashboard & KPIs)

CSV (Data Storage)


## Project Structure

web-scraping-data-analysis/

 scraper.py # Web scraping with pagination & error handling
 
 clean_data.py # Data cleaning & transformation
 
 app.py # Streamlit web application
 
 books_raw.csv # Raw scraped data
 
 books_cleaned.csv # Cleaned dataset for analysis
 
 requirements.txt # Project dependencies
 
 README.md # Project documentation


## Features

## Web Scraping

Scrapes multiple pages using pagination

Extracts book title, price, rating, and availability

Includes error handling and timeout protection

## Data Cleaning

Converts price to numeric format

Converts rating text to numeric values

Removes extra spaces and inconsistencies

## Streamlit Application

Select number of pages to scrape

One-click scraping & cleaning

Interactive data preview

Download cleaned CSV

## Power BI Dashboard

KPI Cards (Total Books, Avg Price, Avg Rating)

Rating-wise distribution

Price analysis

Interactive tables

## How to Run the Project
step 1 Install Dependencies

>>pip install -r requirements.txt

step 2 Run Web Scraper

>>python scraper.py

step 3 Clean the Data

>>python clean_data.py

step 4 Run Streamlit App

>>streamlit run app.py

step 5 Power BI Dashboard Setup

 1. Open Power BI Desktop

 2. Load books_cleaned.csv

 3. Create the following visuals:

KPI Cards (Total Books, Avg Price, Avg Rating)

Bar Chart: Count of Books by Rating

Line/Column Chart: Avg Price by Rating

Table: Title, Price, Rating

## Sample KPIs

Total Books Scraped

Average Book Price

Average Rating

Rating Distribution

## Business Problem

Many businesses rely on online data (prices, reviews, products, trends), but this data is:

Scattered across multiple websites

Not available in structured formats

Time-consuming to collect manually

Manual data collection leads to delayed insights, outdated reports, and missed opportunities.

## Solution

This project automates web data extraction and analysis by:

Scraping data from websites automatically

Cleaning and structuring raw web data

Performing analysis and generating insights

Preparing data for dashboards and reporting tools

## Use Cases
 E-Commerce & Retail

> Track product prices

> Monitor competitor offerings

> Analyze discounts and availability

 Customer Experience Teams

> Collect and analyze online reviews

> Identify customer sentiment and trends

 Data Analysts

> Build datasets for analysis

> Automate recurring data collection

> Feed clean data into Power BI / SQL

 Market Research

> Track trends across regions

> Compare brands and pricing over time

## Business Impact

Saves hours of manual data collection

Enables real-time market insights

Improves competitive decision-making

Scalable for large datasets

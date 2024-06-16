#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 16:37:55 2024

@author: rohandaram
"""

import sqlite3

# The following is where I stored my database, but you can mention the path of where you
# want to store the database.
connection = sqlite3.connect('/Users/rohandaram/UNF-Tools/Databases/SQL_Lab.db');

# Creating a cursor that will be used throughout the program to execute SQL statements
cursor = connection.cursor()

# Start of SQL queries to create tables
customers_table = """ CREATE TABLE IF NOT EXISTS Customers (
        customer_id INTEGER PRIMARY KEY,
        customer_name TEXT,
        customer_age INTEGER
    ); """
cursor.execute(customers_table)

orders_table = """ CREATE TABLE IF NOT EXISTS Orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        shippement_id INTEGER,
        quantity INTEGER,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    ); """
cursor.execute(orders_table)

products_table = """ CREATE TABLE IF NOT EXISTS Products (
        product_id INTEGER PRIMARY KEY,
        product_name TEXT,
        product_category TEXT
    ); """
cursor.execute(products_table)

sales_table = """ CREATE TABLE IF NOT EXISTS Sales (
        sales_id INTEGER,
        product_id INTEGER,
        sales_person_name TEXT,
        sales_amount INTEGER,
        PRIMARY KEY (sales_id, sales_person_name),
        FOREIGN KEY (product_id) REFERENCES products(product_id)
    ); """
cursor.execute(sales_table)
# End of SQL queries to create tables

# Statements for adding records to the Customers table
sqlStatement = """ INSERT INTO Customers (customer_id, customer_name, customer_age)
        VALUES (100, 'John Svendson', 35) """
cursor.execute(sqlStatement)

sqlStatement = """ INSERT INTO Customers (customer_id, customer_name, customer_age)
        VALUES (200, 'Stephen Adams', 25) """
cursor.execute(sqlStatement)

sqlStatement = """ INSERT INTO Customers (customer_id, customer_name, customer_age)
        VALUES (300, 'Kari Pettersen', 40) """
cursor.execute(sqlStatement)

sqlStatement = """ INSERT INTO Customers (customer_id, customer_name, customer_age)
        VALUES (400, 'James McClure', 30) """
cursor.execute(sqlStatement)

# Statements for adding records to the Orders table
sqlStatement = """ INSERT INTO Orders (order_id, customer_id, shippement_id, quantity)
        VALUES (1000, 100, 5000, 100) """
cursor.execute(sqlStatement)

sqlStatement = """ INSERT INTO Orders (order_id, customer_id, shippement_id, quantity)
        VALUES (1001, 400, 5050, 30) """
cursor.execute(sqlStatement)

sqlStatement = """ INSERT INTO Orders (order_id, customer_id, shippement_id, quantity)
        VALUES (1002, 100, 5100, 20) """
cursor.execute(sqlStatement)

sqlStatement = """ INSERT INTO Orders (order_id, customer_id, shippement_id, quantity)
        VALUES (1003, 200, 5500, 50) """
cursor.execute(sqlStatement)

sqlStatement = """ INSERT INTO Orders (order_id, customer_id, shippement_id, quantity)
        VALUES (1004, 200, 5350, 10) """
cursor.execute(sqlStatement)

sqlStatement = """ INSERT INTO Orders (order_id, customer_id, shippement_id, quantity)
        VALUES (1005, 300, 5450, 200) """
cursor.execute(sqlStatement)

# Statements for adding records to the Products table
sqlStatement = """ INSERT INTO Products (product_id, product_name, product_category)
        VALUES (12, 'Bike ABC', 'Road Bike') """
cursor.execute(sqlStatement)

sqlStatement = """ INSERT INTO Products (product_id, product_name, product_category)
        VALUES (13, 'Bike DEF', 'Mountain Bike') """
cursor.execute(sqlStatement)

sqlStatement = """ INSERT INTO Products (product_id, product_name, product_category)
        VALUES (14, 'Bike GHI', 'Road Bike') """
cursor.execute(sqlStatement)

sqlStatement = """ INSERT INTO Products (product_id, product_name, product_category)
        VALUES (15, 'Bike JKL', 'Touring Bike') """
cursor.execute(sqlStatement)

# Statements for adding records to the Sales table
sqlStatement = """ INSERT INTO sales (sales_id, sales_person_name, product_id, Sales_amount)
        VALUES (10000, 'Joe Brown', 12, 1000) """
cursor.execute(sqlStatement)

sqlStatement = """ INSERT INTO sales (sales_id, sales_person_name, product_id, Sales_amount)
        VALUES (10001, 'Bill Johnson', 12, 5000) """
cursor.execute(sqlStatement)

sqlStatement = """ INSERT INTO sales (sales_id, sales_person_name, product_id, Sales_amount)
        VALUES (10002, 'Joe Brown', 13, 10000) """
cursor.execute(sqlStatement)

sqlStatement = """ INSERT INTO sales (sales_id, sales_person_name, product_id, Sales_amount)
        VALUES (10003, 'Bill Johnson', 15, 3000) """
cursor.execute(sqlStatement)

print("SQL DB created and records inserted")

# Finding customers with age greater than 30

sqlQuery = """ SELECT * FROM Customers WHERE customer_age > 30; """
cursor.execute(sqlQuery)
records = cursor.fetchall() # Gets all the records that meet the criteria of the SQL query

print("Customers that hava an age greater than 30 are: ")
for record in records:
    print(record) # Prints each of the record

print()

# Select statement that returns the following properties when condition in met

sqlQuery = """ SELECT Customers.customer_name, Orders.order_id, Orders.quantity
        FROM customers
        JOIN orders ON Customers.customer_id = Orders.customer_id """
cursor.execute(sqlQuery)
records = cursor.fetchall() # Gets all the records that meet the criteria of the SQL query

print("The records that fulfill the objective of the SELECT statement are: ")
for record in records:
    print(record) # Prints each of the record

print()

# Statement that returns the records that are distinct from the product category

sqlQuery = """ SELECT DISTINCT product_category FROM Products; """
cursor.execute(sqlQuery)
records = cursor.fetchall() # Gets all the records that meet the criteria of the SQL query

print("Distinct list of product categories from the product table are: ")
for record in records:
    print(record) # Prints each of the record

print()

# Statement that returns the records with the matching product id

sqlQuery = """ SELECT Sales.sales_person_name, Products.product_name, Sales.sales_amount
        FROM Sales
        JOIN Products ON Sales.product_id = Products.product_id
        WHERE Products.product_id = 12 """
cursor.execute(sqlQuery)
records = cursor.fetchall() # Gets all the records that meet the criteria of the SQL query

print("The records that fulfill the objective of the SELECT statement are: ")
for record in records:
    print(record) # Prints each of the record

print()

# Statement that updates the name of one of the record in the Sales table

sqlQuery = """ UPDATE Sales
        SET sales_person_name = 'Sophie Thomas'
        WHERE sales_id = 10000 """
cursor.execute(sqlQuery) # This query updates the current records

# Selects the updated records from the Sales table
sqlQuery = """ SELECT * FROM Sales """
cursor.execute(sqlQuery) # This query selects the records after they have been updated. 
records = cursor.fetchall() # Gets all the records of the SELECT statement.

print("The records of the updated table are: ")
for record in records:
    print(record) # Prints each of the record

# After finishing using the database, the changes are committed and the connection is closed
connection.commit()
connection.close()

print()

# API

import requests

# This method will take API resource and query parameter
print("Question 9")
def queryAPI(apiResource, queryParameter):
    response = requests.get(apiResource, params=queryParameter)
    
    # Prints the status code of the response
    print("Status Code: ")
    print(response.status_code)
    print()
    
    # Prints the header
    print("Headers: ")
    print(response.headers)
    print()
    
    # Prints the information from the server in key value pairs
    print("Response Information: ")
    print(response.json())
    print()
    
# Calling the method with the one of the query options from the Lab 
queryAPI('https://api.datamuse.com/words', {"sl" : "jirraf"})

print()

# Scraping information using the BeautifulSoup package

# Program that used to BeautifulSoup to go to https://news.google.com and
# prints out all of the headlines on the page.

import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.google.com")

# Parses the HTML content on the webpage
soup = BeautifulSoup(response.content, "html.parser")

# Finds all the headlines that are under the <a> HTML tag and stores it in the variable
headlines = soup.findAll('a')

# Prints out all the headlines under the <a> HTML tag
print("The Google News headlines are: ")
for headline in headlines: 
    # This statement formats the headlines to make it more readable before they are printed
    print(headline.text.strip())

# End of Program 

# This method will find and return a list of the headlines that match the provided keywords
def find_headline_by_keyword(headingsList, *keywords):
    response = requests.get("https://news.google.com")
    soup = BeautifulSoup(response.content, "html.parser")
    
    matchingHeadlines = []
    formattedHeadlinesList = []
    for heading in headingsList:
        headlines = soup.findAll(heading)
        for headline in headlines: 
            # Formats and adds each headline to a List
            headlineFormatted = headline.text.strip()
            formattedHeadlinesList.append(headlineFormatted)
    
    for headline in formattedHeadlinesList:
        
        # Checks for matching keywords while the formatted headlines are iterated through
        if all(keyword.lower() in headline.lower() for keyword in keywords):
        
           # Adds the headlines that match the keywords to the matchingHeadlines List 
           matchingHeadlines.append(headline)
    
    # Returns the List containing the matching headlines
    return matchingHeadlines

print()

print("List of the headlines under the corresponding heading that include the keywords: ")
for specificHeadline in find_headline_by_keyword(['a'], "Blizzard", "California"):
    
    # Prints each headline that is stored in the List.
    print(specificHeadline)

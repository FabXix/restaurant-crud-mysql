# Restaurant CRUD System (MySQL + Python)

## Description

This project is a basic restaurant database management system built with Python and MySQL. It allows managing cooks, dishes, and ingredients, as well as their relationships, using CRUD operations and SQL queries.

## Features

- Bulk insertion of data from CSV files (`cook`, `dish`, `ingredient`, `dish_ingredient`)
- Ability to drop specific tables or all tables
- Queries to explore relationships between entities:
  - Ingredients used by all cooks
  - Dishes by cook or all cooks
  - Cook responsible for a specific dish
  - Count of cooks that use specific ingredients

## Database Structure

The system uses the following entities:

- Cook: stores cook information (name, RFC)
- Dish: stores dishes with price and reference to a cook
- Ingredient: stores ingredient information and cost
- Dish_Ingredient: junction table representing a many-to-many relationship between dishes and ingredients

## Technologies Used

- Python
- MySQL
- mysql-connector-python
- CSV files for data loading
- Modular SQL queries (queries.py)

## System Design

The system initializes the database using `init_db`, loads data from CSV files, and provides an interactive console menu to perform operations.

SQL queries are separated into a dedicated module to keep the project organized and maintainable.

## Objective

The goal of this project is to practice relational database design, many-to-many relationships, data loading from external files, and executing SQL queries through Python.

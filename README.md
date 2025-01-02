# Tarifario Searcher

## Project Overview

This project extracts pricing data from the website [tarifario.org](https://tarifario.org) and provides an interactive search tool for users to find rates based on categories, subcategories, and concepts. The system processes this data into a structured format and allows users to interactively search for pricing information and manage a virtual cart.

### Components:

1. **Data Extraction and Processing (Tarifario_data.py):**
   - The first script scrapes pricing data from [tarifario.org](https://tarifario.org).
   - It fetches tables from the site, processes the information, and saves it as a CSV file (`tarifario_data.csv`).
   - The columns include the categories, subcategories, and the rates for three clients (Client A, Client B, and Client C).

2. **Interactive Search Tool (Tarifario_searcher.py):**
   - The second script uses Tkinter to create a GUI for users to search the pricing information.
   - Users can select a category, subcategory, and concept from dropdown menus.
   - Once the selection is made, the corresponding pricing information for each client is displayed.
   - Users can add items to their cart, and the cart is updated with the selected items, displaying the total amounts for each client.

### Features:
- **Dynamic Dropdowns:** Category, subcategory, and concept options update based on the previous selections.
- **Search Functionality:** Once the user selects a category, subcategory, and concept, the script fetches the pricing data for that specific combination.
- **Cart System:** Allows users to add selected items to their cart, and the cart is displayed with the corresponding totals for each client.
- **Data Source:** Pricing data is extracted and processed from the publicly available tables on [tarifario.org](https://tarifario.org).

## How to Use:
1. **Run Script 1** to scrape and save the data:
   - This will create a CSV file (`tarifario_data.csv`) containing the pricing information.
2. **Run Script 2** to launch the interactive GUI:
   - Choose the category, subcategory, and concept, and the script will show the corresponding prices for the selected clients.
   - Add items to the cart and view the total prices for each client.

## Dependencies:
- `requests`: for fetching data from the website.
- `pandas`: for processing and storing the data.
- `tkinter`: for creating the graphical user interface.

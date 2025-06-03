# 📊 Soul Foods Sales Visualizer

This project was completed as part of the **Quantium Software Engineering Job Simulation** on the Forage platform.

It involves building an interactive dashboard using **Dash** and **Plotly** to analyze the sales of **Pink Morsels** before and after a price change on **January 15, 2021**.

---

## 🎯 Objective

The purpose of this simulation was to:
- Clean and analyze real-world business data
- Answer a key business question:  
  > **"Were sales higher before or after the Pink Morsel price increase?"**
- Build a professional-grade dashboard for business stakeholders

---

## ✅ Tasks Completed

This project involved the following tasks:

1. **Data Cleaning**
   - Removed unnecessary rows
   - Handled missing values and formatting
   - Converted columns like `sales` from string to numeric values

2. **Data Merging**
   - Combined multiple CSV files (`data0.csv`, `data1.csv`, `data2.csv`) into a single cleaned dataset

3. **Feature Engineering**
   - Created a `Sales` column from `quantity × unit price`
   - Dropped intermediate columns after processing

4. **Interactive Visualization**
   - Created a line chart of sales over time
   - Added a vertical line marker for the price change on Jan 15, 2021

5. **Dash Application**
   - Built a web dashboard with:
     - 📈 Line chart of total daily sales
     - 🔘 Radio buttons to filter by region (`north`, `east`, `south`, `west`, `all`)
     - 🎨 Custom CSS styling

---

## 🗂️ Project Structure
quantium-starter-repo/
├── app.py # Dash application
├── Formated_Output.csv # Cleaned and combined dataset
└── README.md # Project documentation


---

## 🚀 Running the App

### Prerequisites

Install required Python libraries:

```bash
pip install dash pandas plotly


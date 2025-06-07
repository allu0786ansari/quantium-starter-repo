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

## ✅ Tasks Completed For Software Engineering Job Simulation On Forage

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

```bash
quantium-starter-repo/
├── app.py                 # Main Dash app
├── Formated_Output.csv    # Cleaned and merged dataset
├── README.md              # Project documentation

---

## 🚀 How to Run

### 1. Install Dependencies

Make sure your Python environment is active, then install required packages:

\```bash
pip install dash pandas plotly
\```

### 2. Run the App

\```bash
python app.py
\```

---

## 🛠 Technologies Used

- **Python 3.10+**
- **Dash** – Interactive Python web framework
- **Plotly** – Beautiful interactive plots
- **Pandas** – Data manipulation and transformation
- **HTML & CSS** – Basic styling for layout and readability
- **unit testing using pytest and selenium** - Basic implementation for testing the application 

---

## 🧠 Learnings

- Cleaned and transformed real-world sales data using pandas
- Merged multiple CSVs with consistent formatting
- Created line charts with custom annotations using Plotly
- Built an interactive web dashboard with Dash and callbacks
- Implemented filtering with Dash components (radio buttons)
- Styled the UI to be clean, minimal, and user-friendly

---

## 📷 Screenshot





## 🙌 Acknowledgements

- **Quantium** – for providing the business problem and dataset  
- **Forage** – for offering the Software Engineering Job Simulation  
- **Plotly & Dash Teams** – for making data visualization intuitive and interactive  


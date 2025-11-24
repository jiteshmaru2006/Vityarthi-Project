### ## Project Title
**Sales Metrics & Profitability Calculator**

### ## Overview of the Project
The **Sales Metrics & Profitability Calculator** is a versatile financial utility designed to automate the calculation of essential business metrics, including Cost, Revenue, Profit, Markup, and Gross Margin. By accepting any valid combination of two input variables, the system mathematically infers the remaining financial data points, providing an instant and comprehensive snapshot of a product's pricing structure.  This tool serves as a critical asset for business owners, pricing analysts, and students, eliminating manual calculation errors and strictly defining the often-confused mathematical relationship between markup percentages and gross margin ratios.

### ## Features
The application features a **multi-directional calculation engine** capable of deriving a complete financial profile from any pair of five supported parameters (Cost, Revenue, Profit, Markup, or Gross Margin). It intelligently handles percentage inputs, automatically normalizing Markup and Gross Margin values for calculation while distinguishing between cost-based and revenue-based profitability. The system utilizes a robust logic structure to handle seven distinct input combinations and concludes with a **formatted summary display**, presenting all five key metrics rounded to two decimal places for clear, actionable insights.

### ## Technologies and Tools Used
The project is built exclusively using **Python 3.x**, leveraging its standard library to ensure lightweight execution and cross-platform compatibility without the need for external dependencies. The core logic relies on Python's **fundamental arithmetic operators** and conditional control flow (`if-elif-else`) to manage the algebraic relationships between financial variables. The user interface is implemented via the **Command Line Interface (CLI)**, utilizing standard input/output streams and dictionary data structures to facilitate dynamic user interaction and data mapping.

### ## Steps to Install and Run
To execute this project, ensure you have **Python 3** installed on your machine, then save the provided code into a file named `sales_calculator.py`. Open your system’s terminal or command prompt, navigate to the directory where the file is saved using the `cd` command, and run the script by typing `python sales_calculator.py`. Once the program initializes, the console will list the available fields; simply type the names of the two parameters you wish to provide (e.g., "cost" and "revenue") followed by their numerical values when prompted to generate the full report.

### ## Instructions for Testing
To test the application's accuracy, run the script and select a standard pricing scenario, such as entering **"cost"** with a value of `100` and **"markup"** with a value of `50`; the system should correctly calculate a **Revenue** of `150` and a **Profit** of `50`. Verify the distinction between margin and markup by running a second test using **"revenue"** of `100` and **"grossMargin"** of `20`; the result should output a **Profit** of `20` and a **Cost** of `80`, confirming that the algorithm correctly applies the margin against total revenue rather than cost.

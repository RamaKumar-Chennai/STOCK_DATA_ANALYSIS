# STOCK_DATA_ANALYSIS

Project Title	Data-Driven Stock Analysis: Organizing, Cleaning, and Visualizing Market Trends
Skills take away From This Project	Pandas, Python, Power BI, Streamlit, SQL,Statistics ,Data Organizing, Cleaning, and Visualizing.
Domain	Finance / Data Analytics
Problem Statement:
The Stock Performance Dashboard aims to provide a comprehensive visualization and analysis of the Nifty 50 stocks' performance over the past year. The project will analyze daily stock data, including open, close, high, low, and volume values. Clean and process the data, generate key performance insights, and visualize the top-performing stocks in terms of price changes, as well as average stock metrics. The solution will offer interactive dashboards using Streamlit and Power BI to help Investors, analysts, and enthusiasts make informed decisions based on the stock performance trends.

Business Use Cases:
1.	Stock Performance Ranking: Identify the top 10 best-performing stocks (green stocks) and the top 10 worst-performing stocks (red stocks) over the past year.
2.	Market Overview: Provide an overall market summary with average stock performance and insights into the percentage of green vs red stocks.
3.	Investment Insights: Help investors quickly identify which stocks showed consistent growth and which ones had significant declines.
4.	Decision Support: Provide insights on average prices, volatility, and overall stock behavior, useful for both retail and institutional traders.
________________________________________

Approach:
Data Extraction and Transformation:
•	Data is provided in YAML format, organized by months.
•	Within each month's folder, there are date-wise data entries.
•	I extracted this data from the YAML file and transformed it into a CSV format, organized by symbols 
•	This resulted in 50 CSV files after the extraction process, one for each symbol or data category

Once I run my streamlit program, the STREAMLIT DASHBOAD presents the stock data sorted out by the TICKER(COMPANY)
The STOCK DASHBOARD presents the following options:
"Yearly Returns", 
"Volatality",
"Cumulative Returns",
"Sector-wise Performance",
"Correlation Heatmap",
"Monthly Gainers and Losers"

YEARLY RETURNS:

o	Top 10 Green Stocks: Sort the stocks based on their yearly return and select the top 10.
o	Top 10 Loss Stocks: Sort the stocks based on their yearly return and select the bottom 10.
o	Market Summary:
	The overall number of green vs. red stocks is calculated.
	The average price and the average Volume across all stocks is calculated
     Visualization:
     Bar charts with the stock ticker on the x-axis and Top 10 Green Stocks AND   Top 10                  Loss Stocks on the y-axis are drawn


Volatility Analysis:
•	Objective:The volatility of each stock over the past year is visualized by calculating the standard deviation of daily returns.
•	Reason: Volatility gives insight into how much the price fluctuates, which is valuable for risk assessment. Higher volatility often indicates more risk, while lower volatility indicates a more stable stock.
Visualization:
•	Top 10 Most Volatile Stocks: A bar chart with the stock ticker on the x-axis and volatility (standard deviation) on the y-axisis is drawn.


Cumulative Return Over Time:
•	Objective: The cumulative return of each stock from the beginning of the year to the end is calculated.
•	Reason: The cumulative return is an important metric to visualize overall performance and growth over time. This helps users compare how different stocks performed relative to each other.
•	.
Visualization:
•	Cumulative Return for Top 5 Performing Stocks: A line chart displaying cumulative returns for each stock over the year (increasing trend indicates positive performance) is drawn.

Sector-wise Performance:
•	Objective:It  provides a breakdown of stock performance by sector (sector data shared as csv).
•	Reason: Investors and analysts often look at sector performance to gauge market sentiment in specific industries (e.g., IT, Financials, Energy, etc.).

   Visualization:
•	Average Yearly Return by Sector: A bar chart where each bar represents a sector and its height indicates the average yearly return for stocks within that sector is drawn


 Stock Price Correlation:
•	Objective: Visualize the correlation between the stock prices of different companies.
•	Reason: This analysis is valuable to understand if certain stocks tend to move in tandem (e.g., correlated with market trends or sector performance).
  Visualization:
•	Stock Price Correlation Heatmap: A heatmap to show the correlation between the closing prices of various stocks. Darker colors represent higher correlations.




 Top 5 Gainers and Losers (Month-wise):
•	Objective: Provides monthly breakdowns of the top-performing and worst-performing stocks.
•	Reason: This analysis will allow users to observe more granular trends and understand which stocks are gaining or losing momentum on a monthly basis.
Visualization:
•	Top 5 Gainers and Losers by Month:  A set of 12 bar charts for each month showing the top 5 gainers and losers based on percentage return is created.



________________________________________
Results:
•	A fully functional dashboard showing the top-performing and worst-performing stocks over the last year.
•	Insights on the overall market with clear indicators of stock performance trends.
•	Interactive visualizations Streamlit to make the data easily accessible for users.

________________________________________
Technical Tags:
•	Languages: Python
•	Database: MySQL/PostgreSQL
•	Visualization Tools: Streamlit, Power BI
•	Libraries: Pandas, Matplotlib, SQLAlchemy
________________________________________
Project Deliverables:
1.	SQL Database: Contains clean and processed data.
2.	Python Scripts: For data cleaning, analysis, and database interaction.
3.	Streamlit Application: Interactive dashboard for real-time analysis.
________________________________________


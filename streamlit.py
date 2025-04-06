import streamlit as st
import pandas as pd
from ticker_grouping import  grouping
from ticker_grouping import  yearly_returns
from ticker_grouping import  volatality
from ticker_grouping import  cum_returns
from ticker_grouping import correlation
from ticker_grouping import top5_gainers_losers
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Stock Analysis Dashboard")


# Sidebar for navigation
st.sidebar.title("Navigation")
options = [" ","Yearly Returns", "Volatality","Cumulative Returns","Sector-wise Performance","Correlation Heatmap","Monthly Gainers and Losers"]
choice = st.sidebar.selectbox("Select Option", options)


combined_df=grouping()

st.write(combined_df)

top_10_green_stocks,top_10_red_stocks,green_stocks_count,red_stocks_count,aver_price,aver_vol,merge_df_yearly_returns,YEARLY_RETURNS,Ticker,sector_average_yearly_returns_st = yearly_returns(combined_df)

# IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD
import sqlalchemy
import pymysql
from sqlalchemy import create_engine
import pandas as pd


# DEFINE THE DATABASE CREDENTIALS


#engine = db.create_engine("mysql+mysqlconnector://username:password@hostname:port/dbname")
#engine = create_engine('mysql+pymysql://USERNAME:PASSWORD@HOST:PORT/DBNAME')
user = 'root'
password = 'root'
host = 'localhost'
port = "3306"
database = 'practice'

# PYTHON FUNCTION TO CONNECT TO THE MYSQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
def get_connection():
    return create_engine(
        url="mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
)
    )
 
 
if __name__ == '__main__':
 
    try:
       
        # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
        engine = get_connection()
        print(
            f"Connection to the {host} for user {user} created successfully.")
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

combined_df.to_sql("stock_data",con=engine,if_exists='replace')




#volatality,top_5_stocks_st_,top5_gainers,top5_losers
#top_10_green_stocks,top_10_red_stocks,vol_df



if choice=="Yearly Returns" :
  

   
  #STREAMLIT WRITE 
  st.write("\n\nTOP 10 GREEN STOCKS\n\n")
  
  st.write(top_10_green_stocks)

  st.write("\n\nTOP 10 RED STOCKS\n\n")
  st.write(top_10_red_stocks)
  st.write("GREEN STOCKS: ")
  st.write(green_stocks_count) 
  st.write(" RED STOCKS : ")
  st.write(red_stocks_count)
  st.write("AVERAGE PRICE: ")
  st.write(aver_price)
  st.write("AVERAGE VOLUME: ")
  st.write(aver_vol)
  top_10_green_stocks.to_sql("top_10_green_stocks",con=engine,if_exists='replace')
  top_10_red_stocks.to_sql("top_10_red_stocks",con=engine,if_exists='replace')
  # Create a bar plot
  print("TOP TEN GREEN STOCKS OF TICKER AND YEARLY RETURNS")
  print(top_10_green_stocks[['Ticker','YEARLY_RETURNS']])
  fig, ax = plt.subplots(figsize=(12, 6))
  ax.bar(top_10_green_stocks['Ticker'],top_10_green_stocks['YEARLY_RETURNS'])
  

  # Add titles and labels
  ax.set_title('TOP 10 GREEN STOCKS')
  ax.set_xlabel('TICKER')
  ax.set_ylabel('TOP 10 GREEN STOCKS')

  # Display the plot in Streamlit
  st.pyplot(fig)

  fig, ax = plt.subplots(figsize=(12, 6))
  ax.bar(top_10_red_stocks['Ticker'],top_10_red_stocks['YEARLY_RETURNS'])
  

  # Add titles and labels
  ax.set_title('TOP 10 RED STOCKS')
  ax.set_xlabel('TICKER')
  ax.set_ylabel('TOP 10 RED STOCKS')

  # Display the plot in Streamlit
  st.pyplot(fig)


elif choice=="Volatality":
  vol_df,Ticker,Volatality=volatality(combined_df)
  print("type of volatality is",type(Volatality))
  print("type of ticker is",type(Ticker))
  
  st.write("TOP 10 MOST VOLATILE STOCKS")
  st.write(vol_df)
  fig,ax=plt.subplots(figsize=(12, 6))
  ax.bar(Ticker,Volatality)
  ax.set_title("TOP 10 MOST VOLATILE STOCKS")
  ax.set_xlabel("Ticker")
  ax.set_ylabel("Volatality")
  st.pyplot(fig)
  plt.tight_layout()
  vol_df.to_sql("top_10_volatile_stocks",con=engine,if_exists='replace')
  
  

  
  
elif choice=="Cumulative Returns":
 top_5_stocks_st,Ticker, Cum_returns=cum_returns(combined_df)
 st.write("TOP 5 STOCKS")
 st.write(top_5_stocks_st)
 

 # Create a bar plot
 fig, ax = plt.subplots()
 ax.bar(Ticker, Cum_returns)
 

 # Add titles and labels
 ax.set_title('TOP 5 STOCKS')
 ax.set_xlabel('TICKER')
 ax.set_ylabel('CUMULATIVE RETURNS')

 # Display the plot in Streamlit
 st.pyplot(fig)

 # Add some interactive elements
 st.write("This is a simple bar plot created using Streamlit and Matplotlib.")
 top_5_stocks_st.to_sql("top_5_stocks_cum_returns",con=engine,if_exists='replace')

elif choice=="Sector-wise Performance":
  st.write("SECTOR WISE PERFORMANCE IS ")
  st.write(sector_average_yearly_returns_st)
 # merge_df_yearly_returns,YEARLY_RETURNS,Ticker 
  fig, ax = plt.subplots(figsize=(15, 9))
  ax.bar(sector_average_yearly_returns_st['sector'], sector_average_yearly_returns_st['YEARLY_RETURNS'])
 #ax.bar(top_5_stocks_st['Ticker'].tolist(),top_5_stocks_st['Cum_returns'].tolist())

 # Add titles and labels
  ax.set_title('Sector-wise Performance')
  ax.set_xlabel('SECTOR')
  ax.set_ylabel('YEARLY RETURNS')

 # Display the plot in Streamlit
  st.pyplot(fig)
elif choice=="Correlation Heatmap":
  corr_matrix=correlation(combined_df)
  st.write("CORRELATION MATRIX")
  st.write(corr_matrix)
  

  fig, ax = plt.subplots(figsize=(18, 18))
  sns.heatmap(corr_matrix, ax=ax)
  st.write(fig)

elif choice=="Monthly Gainers and Losers":
  monthly_returns_merge,month_df,year_df=top5_gainers_losers(combined_df)
 
  
  #PLOT TOP 5 GAINERS AND LOSERS IN A MONTH
  import seaborn as sns
  import matplotlib.pyplot as plt
  def plot_top5_gainers_losers(month,year):
  
   monthly_data=monthly_returns_merge[(monthly_returns_merge['month']==month ) & ( monthly_returns_merge['year']==year)]
   
  
  
   top5_gainers=monthly_data.nlargest(5,['monthly_returns'])
   top5_losers=monthly_data.nsmallest(5,['monthly_returns'])
   print("top5_gainers for month",month)
   print(top5_gainers)
   print("top5_losers for month",month)
   print(top5_losers)
   top5_gainers.to_sql(f"top5_gainers{month}-{year}",con=engine,if_exists='replace')
   top5_losers.to_sql(f"top5_losers{month}-{year}",con=engine,if_exists='replace')
  
  
   fig, axes = plt.subplots(1, 2, figsize=(12, 6))
   sns.barplot(data=top5_gainers,x='Ticker',y='monthly_returns',ax=axes[0])
   axes[0].set_title(f'Top 5 Gainers - Month {month},Year{year}')
   axes[0].set_xticklabels(axes[0].get_xticklabels(), rotation=45, ha='right')
   

   
   sns.barplot(data=top5_losers,x='Ticker',y='monthly_returns',ax=axes[1])
   axes[1].set_title(f'Top 5 Losers - Month {month},Year{year}')
   axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=45, ha='right')
   
   st.write(fig)
   
  
  
 
  year=2023
  for month in range(10,13):

    plot_top5_gainers_losers(month,year)



  year=2024
  for month in range(1,12):

    plot_top5_gainers_losers(month,year)





def grouping():

  from conversion import  conversion
  import os
  import yaml
  import streamlit as st
  import matplotlib.pyplot as plt

  import csv
  import re
  import pandas as pd
  df,os_make_dir=conversion()
  print("the make directory is ",os_make_dir)
  print("the columns are")
  print(df.columns)


  df['date'] = pd.to_datetime(df['date'], errors='coerce')



  df.to_csv(os_make_dir+'\\total_output.csv', index=False)

  for  ticker,group in df.groupby(['Ticker']):
     ticker=str(ticker)
     
     ticker=re.sub(r"[^\w-]","", ticker)
                   
     
     file_name=os_make_dir+"\\"+ticker+".csv"
    
     group.to_csv(file_name, index=False)

  combined_df = pd.DataFrame(index=None)


  for file in os.listdir(os_make_dir):
    if file.endswith(".csv"):
        file_path = os.path.join(os_make_dir, file)
        stock_data = pd.read_csv(file_path)
        combined_df = pd.concat([combined_df, stock_data], ignore_index=True)

  print(combined_df)
  
  print("groping program and csv file splittign ends here")
  
  return combined_df
  
  

#Calculating DAILY RETURNS

def volatality(combined_df):
 combined_df['Daily_returns']=(combined_df['close']-combined_df['open'])/(combined_df['open'])
 print("after daily  returns column is added")
 print("after adding daily returns col,the comboned df is")
 print(combined_df)

#1. CALCULATING VOLATALITY
 volatality=combined_df.groupby('Ticker')['Daily_returns'].std().nlargest(10)
 
 print("\n\nTop 10 most volatile stocks:\n\n")
 print(volatality)
 volatality_df=volatality.reset_index()
 print("volatality df columns are ")
 print(volatality_df.columns)
 volatality_df.columns =['Ticker','Volatality']
 print("the volatality df is ")
 print(volatality_df)
 
 return(volatality_df,volatality_df['Ticker'],volatality_df['Volatality'])


#Calculating CUMULATIVE RETURNS
def cum_returns(combined_df):
  import matplotlib.pyplot as plt
  combined_df['Daily_returns']=(combined_df['close']-combined_df['open'])/(combined_df['open'])
  combined_df['Cum_returns']=combined_df.groupby('Ticker')['Daily_returns'].cumsum()
  print("after adding cum returns col,combined_df is ")
  print(combined_df)

  top_5_stocks=combined_df.groupby('Ticker')['Cum_returns'].max().nlargest(5).index
  top_5_stocks_st=combined_df.groupby('Ticker')['Cum_returns'].max().nlargest(5)


  
  top_5_stocks_st_df = top_5_stocks_st.reset_index()
  print("the converted data frame is")
  print(top_5_stocks_st_df)
  
  return(top_5_stocks_st_df,top_5_stocks_st_df['Ticker'],top_5_stocks_st_df['Cum_returns'])
   


#CALCULATING YEARLY RETURNS

def yearly_returns(combined_df):
  import matplotlib.pyplot as plt
  import pandas as pd 
  first_row_groupby_open=pd.DataFrame(index=None)
  last_row_groupby_close=pd.DataFrame(index=None)
  merge_df_yearly_returns=pd.DataFrame(index=None)  
  print("the open price value for each stock is ")

  
  first_row_groupby_open=combined_df.groupby('Ticker').head(1)[['Ticker','open']]

  print("the close price value for each stock is ")

  print(combined_df.groupby('Ticker').tail(1)[['Ticker','close']])
  last_row_groupby_close=combined_df.groupby('Ticker').tail(1)[['Ticker','close']]
 

  merge_df_yearly_returns=pd.merge(first_row_groupby_open,last_row_groupby_close,on='Ticker',how='inner')
  print("the merged dataset is")
  print(merge_df_yearly_returns)
  merge_df_yearly_returns['YEARLY_RETURNS']=((merge_df_yearly_returns['close']-merge_df_yearly_returns['open'])/merge_df_yearly_returns['open'])*100
  print("merge_df is")
  print(merge_df_yearly_returns)
  print("merge_df_yearly_returns.columns is ")
  print(merge_df_yearly_returns.columns)
  print("combined_df.columns ")
  print(combined_df.columns)

  
  print("\n\nTOP 10 GREEN STOCKS\n\n")
  top_10_green_stocks=merge_df_yearly_returns.nlargest(10,columns='YEARLY_RETURNS')
  print(top_10_green_stocks[['Ticker','YEARLY_RETURNS']])

  

  print("\n\nTOP 10 RED STOCKS\n\n")

  top_10_red_stocks=merge_df_yearly_returns.nsmallest(10,columns='YEARLY_RETURNS')

  print(top_10_red_stocks[['Ticker','YEARLY_RETURNS']])



  green_stocks_count=((merge_df_yearly_returns['YEARLY_RETURNS']>0).sum())

  red_stocks_count=((merge_df_yearly_returns['YEARLY_RETURNS']<=0).sum())


  print(f"GREEN STOCKS: {green_stocks_count} \n RED STOCKS : {red_stocks_count}")

  print("AVERAGE PRICE: ",combined_df['close'].mean())
  print("AVERAGE VOLUME: ",combined_df['volume'].mean())




  #Calculating  Sector yearly returns
  #Read the sector data csv file
 

  sector_path="C:\\Users\\Rama Kumar\\Downloads\\Sector_data - Sheet1.csv"
  sector_data=pd.read_csv(sector_path)
  #print the se ctor dataframe
  print(sector_data)
  #Merge the sector data with the original dataframe 
  merged_sector_data=pd.merge(combined_df,sector_data[['COMPANY','sector']],left_on='Ticker',right_on='COMPANY',how='left')
  print("The MERGED SECTOR DATA ")
  print(merged_sector_data)

  #Finding the null values in MERGED_SECTOR_DATA
  print("the null values in merged sector data are ")
  print(merged_sector_data.isnull().sum())

  #Filling the null values
  merged_sector_data['COMPANY']=merged_sector_data['COMPANY'].fillna('MISCELLANEOUS')
  merged_sector_data['sector']=merged_sector_data['sector'].fillna('MISCELLANEOUS')
  ##To check if the null values in MERGED_SECTOR_DATA are filled correctly
  print(merged_sector_data.isnull().sum())
  #Merge the yearly returns and sector dataframes
  merged_sector_data_yearly_returns=pd.merge(merged_sector_data,merge_df_yearly_returns[['YEARLY_RETURNS','Ticker']],on='Ticker',how='inner')
  print("The MERGED SECTOR DATA WITH YEARLY RETURNS")
  print(merged_sector_data_yearly_returns)

  #Evaluate the sector wise performance 
  sector_average_yearly_returns=merged_sector_data_yearly_returns.groupby('sector')['YEARLY_RETURNS'].mean()
  print("The average yearly returs for each sector is")
  print(sector_average_yearly_returns)
  
  
  sector_average_yearly_returns_st=sector_average_yearly_returns.reset_index()
  
  print("sector_average_yearly_returns_st is",sector_average_yearly_returns_st)
  
  return (top_10_green_stocks[['Ticker','YEARLY_RETURNS']],top_10_red_stocks[['Ticker','YEARLY_RETURNS']],green_stocks_count,red_stocks_count,combined_df['close'].mean(),combined_df['volume'].mean(),merge_df_yearly_returns,merge_df_yearly_returns['YEARLY_RETURNS'],merge_df_yearly_returns['Ticker'],sector_average_yearly_returns_st)

  



 
 
 

# 4. Stock Price Correlation:
def correlation(combined_df):
 import pandas as pd
 pivot_table=pd.pivot_table(combined_df,index='date',columns='Ticker',values='close')

 print("\n PIVOT TABLE\n")
 print(pivot_table)

 close_pivot=pivot_table.pct_change()
 print("DAILY CLOSE PRICE")
 print(close_pivot)

 close_pivot=close_pivot.dropna()
 print("AFTER DROPPING NULL VALUES")
 print(close_pivot)

 #CORELATION MATRIX
 corr_matrix=close_pivot.corr()
 print("CORRELATION MATRIX")
 print(corr_matrix)

 

 return(corr_matrix)



#5. Top 5 Gainers and Losers (Month-wise):
def top5_gainers_losers(combined_df):
 import pandas as pd
 combined_df['date']=pd.to_datetime(combined_df['date'])
 combined_df['month']=combined_df['date'].dt.month
 combined_df['year']=combined_df['date'].dt.year


 print("combined df after adding month column")
 print(combined_df)
 monthly_returns=pd.DataFrame()
 #STOCK DATA WITH FIRST OPEN PRICE IN A MONTH
 monthly_returns=combined_df.groupby(['Ticker','year','month']).head(1)[['Ticker','open','year','month']]

 print("Monthly returns with ticker and first open for a month")
 print(monthly_returns)

 #STOCK DATA WITH LAST CLOSE PRICE IN A MONTH
 monthly_returns1=combined_df.groupby(['Ticker','year','month']).tail(1)[['Ticker','close','year','month']]


 print("monthly returns with ticker and last close for a month")
 print(monthly_returns1)


 print("Stock data with first open price and last close price in a month")
 monthly_returns_merge=pd.merge(monthly_returns,monthly_returns1,on=['Ticker','year','month'],how='left')
 print(monthly_returns_merge)
 monthly_returns_merge['monthly_returns']=monthly_returns_merge['close']-monthly_returns_merge['open']
 print(monthly_returns_merge,monthly_returns_merge['month'],monthly_returns_merge['year'])
 return(monthly_returns_merge,monthly_returns_merge['month'],monthly_returns_merge['year'])


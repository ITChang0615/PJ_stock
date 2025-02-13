	#-------------------------------------------------------------------------------------------------------------------------------------------
	
	  
    stock_data['_成交金額'] =stock_data['成交金額']* stock_data['Price_Change'].apply(lambda x: 1 if x > 0 else -1)
	
    # Calculate and clean up trading volume metrics
    stock_data['短交易量'] = (stock_data['_成交金額'] - stock_data['Volume_MA_short']) / stock_data['Volume_MA_short']
    stock_data['遠交易量'] = (stock_data['Volume_MA_short'] - stock_data['Volume_MA_long']) / stock_data['Volume_MA_long']
    
    #stock_data['短交易量'] =stock_data['短交易量']* stock_data['Price_Change'].apply(lambda x: 1 if x > 0 else -1)
    
	stock_data['短交易量'] = (stock_data['短交易量'] * 10).fillna('0').astype(int)
    stock_data['短交易量'] = stock_data['短交易量'].rolling(window=10).sum()
	
    stock_data['遠交易量'] = (stock_data['遠交易量'] * 100).fillna('0').astype(int)
	
	stock_data['短增'] = stock_data['短交易量'] > stock_data['遠交易量']

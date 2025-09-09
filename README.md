
	量能: 成交股數/一年內最大量  (%)
	
	# 計算成交量震盪指標
	Volume_Oscillator : (Volume_MA_short-Volume_MA_long)/Volume_MA_long (%)
	-------------------------------------------------------------------
	【MA5_% / 均價_%】
	
	MA5_%=(收盤價-MA_short)/ MA_short					|>-1 <0
	均價_%=(MA_short-MA_long)/ MA_long				|>0
	
	check 	
	https://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_6442.tw_20250509|tse_6757.tw_20250509|tse_1101.tw_20250509|
	
-------------------------------------------------------------------------------
20250909
	app.jsonData=app.jsonData_
	app.jsonData=app.jsonData.filter(x => x.分類標籤_)
	app.jsonData=app.jsonData.filter(x => x.分類標籤.split("【")[1]?.split("】")[0]!='e')
	app.jsonData=app.jsonData.filter(x => (x.highlight_date=='2025-09-05'|x.highlight_date=='2025-09-08'))
	
	app.sync_realtime()
	
	app.sync_data()

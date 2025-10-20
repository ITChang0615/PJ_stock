
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




MACD

|*                                            * 
|    *                                     *    
| c     *                               *   b
|         *                           *         
|------------------------------------ > 均
|              *                *    
|              e *            *  d   
|                  *        *       
|                    *    *         


app.jsonData=app.jsonData_.filter(x=> x['總價差']>0 && x['MA5_%'] >0 && x['均價_%']<0 && x['均價long_%']>0 )

app.jsonData=app.jsonData_.filter(x=>x.highlight_date>'2025-10-14'&& parseFloat(x['highlight_%'])<7 && parseFloat(x['%K'])>parseFloat(x['%D'])&& x.量能avg>10 )

app.jsonData=app.jsonData_.filter(x=> parseFloat(x['MACD_minus'])>0.1 && parseFloat(x['%K'])<50 && parseFloat(x['%K'])>parseFloat(x['%D']) )

app.jsonData=app.jsonData_.filter(x=> parseFloat(x['rt_price'])>3 )
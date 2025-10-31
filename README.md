
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





CooLWEBSITE





		 
##################################################################################################################

---
app.jsonData=app.jsonData_.filter(x=>parseFloat(x.now_price)>parseFloat(x.highlight_enddate收盤價_1) && parseFloat(x.now_price)>parseFloat(x.highlight_enddate收盤價_2) 
																&& x.LevelArea>-90 && x['MACD-SL']>-1 && x.量能>10 &&x.Type1!='生技醫療業'&& x['%D']<x['%K']*1.1 )

---
app.jsonData=app.jsonData_.filter(x=>parseFloat(x.now_price)>parseFloat(x.highlight_enddate收盤價_1) && parseFloat(x.now_price)>parseFloat(x.highlight_enddate收盤價_2) 
																&& x.LevelArea>-90 && x['MACD-SL']>0)



var alist=['8299', '8086', '8016', '7751', '7749', '7712', '6937', '6695', '6515', '6488', '6271', '6239', '6223', '6138', '5487', '5347', '5285', '3707', '3556', '3532', '3530', '3260', '3227', '3016', '3014', '2434', '2329']
 app.jsonData=app.jsonData_.filter(x=>alist.includes(x.stock_number))


app.jsonData=app.jsonData_.filter(x=>parseFloat(x.淨值倍率)>1  && x['成交股數'] >1000  && x['均價long_%']>0 && x['highlight_%_2']<0  && x['%K'] > x['%D'] *1.1 && x['MACD'] > x['MACD-SL'] *1.1)


##################################################################################################################
##################################################################################################################


app.jsonData=app.jsonData_.filter(x=>x.highlight_enddate=='2025-10-29' && x['highlight_%_1']==0 && x['highlight_%_2']<=0)

app.jsonData=app.jsonData_.filter(x=>x.Type1=='電子零組件業')


app.jsonData=app.jsonData_.filter(x=>x.diff_quote>3)

app.jsonData=app.jsonData_.filter(x=>x['highlight_%_1']>0  &&x['highlight_%_2']>0)

app.jsonData=app.jsonData.filter(x =>  x.Full_Summary.includes('建議關注買點'))

app.jsonData=app.jsonData.filter(x => x['均價long_%']>0)

app.jsonData=app.jsonData.filter(x=>(x.datalist.filter(y=>y['VPC_MA_%']>10).length)<1)

app.jsonData=app.jsonData_.filter(x =>   x['MACD-SL'] > 0 &&   x['MACD'] > x['MACD-SL'] && x['均價long_%']>0 )

 x['%K'] > x['%D']


	 
app.jsonData_.map(x => x['%K'] =x['%K'] -x['%D'] )
	 
app.jsonData=app.jsonData_.filter(x=> x['%K'] > 0  x.LevelArea>-40 )
app.jsonData=app.jsonData_.filter(x=> x['%K'] > 0  && x.LevelArea>-40  && x.LevelArea<80 )


app.jsonData=app.jsonData_.filter(x=>(x.datalist.filter(y=>y['均價long_%']<0).length)>1 && (x.datalist.filter(y=>y['均價long_%']>0).length)>1 && x['均價long_%']>0 && x.highlight_date!='0' )

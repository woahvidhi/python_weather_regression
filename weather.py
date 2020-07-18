from matplotlib import pyplot as plt
from pandas import*
from tkinter import*

#extraction of data

data = pandas.read_csv('data.csv')
date = data['Date'].tolist()
data_temp = data['Temperature'].tolist()
data_humid = data['Humidity'].tolist()
data_ws = data['Wind Speed'].tolist()
data_dp = data['Dew Point'].tolist()
data_prs = data['Pressure'].tolist()

#analysis of data
week_temp=[]
week_humid=[]
week_ws=[]
week_dp=[]
week_prs=[]
week = []
count = 1
for i in range(0,len(data_temp)-3,6):

	sum_t, sum_h, sum_w, sum_d, sum_p = 0,0,0,0,0
	week.append(str(count))
	for j in range(0,7):
		sum_t += data_temp[i+j]
		sum_h += data_humid[i+j]
		sum_w += data_ws[i+j]
		sum_d += data_dp[i+j]
		sum_p += data_prs[i+j]	
	week_temp.append(sum_t//7)
	week_humid.append(sum_h//7)
	week_ws.append(sum_w//7)
	week_dp.append(sum_d//7)
	week_prs.append(sum_p//7)
	count+=1

#to find max and min
sort_t = sorted(data_temp)
sort_h = sorted(data_humid)
sort_w= sorted(data_ws)
sort_d = sorted(data_dp)
sort_p = sorted(data_prs)
	
min = [sort_t[0], sort_h[0], sort_w[0],sort_d[0],sort_p[0]]
max = [sort_t[-1], sort_h[-1], sort_w[-1],sort_d[-1],sort_p[-1]]	


# button

def f1(n):
	if n==1:
		temp.deiconify()
	elif n==2:
		humid.deiconify()
	elif n==3:
		ws.deiconify()
	elif n==4:
		dp.deiconify()
	else:
		prs.deiconify()
	root.withdraw()
def f2(n):
	root.deiconify()
	if n==1:
		temp.withdraw()
	elif n==2:
		humid.withdraw()
	elif n==3:
		ws.withdraw()
	elif n==4:
		dp.withdraw()
	else:
		prs.withdraw()
def f3(n):
	if n == 1:
		plt.plot(week,week_temp, linewidth=1, marker='o', markersize=1)
		plt.title('TEMPERATURE')
		plt.ylabel('FAHRENHEIT')
	elif n == 2:
		plt.plot(week,week_humid, linewidth=1, marker='o', markersize=1)
		plt.title('HUMIDITY')
		plt.ylabel('GRAMS PER CUBIC METER')
	elif n == 3:
		plt.plot(week,week_ws, linewidth=1, marker='o', markersize=1)
		plt.title('WIND SPEED')
		plt.ylabel('MPH')
	elif n == 4:
		plt.plot(week,week_dp, linewidth=1, marker='o', markersize=1)
		plt.title('DEW POINT')
		plt.ylabel('FAHRENHEIT')
	else:
		plt.plot(week,week_prs, linewidth=1, marker='o', markersize=1)
		plt.title('PRESSURE')
		plt.ylabel('PASCALS')
	
	plt.xlabel("WEEK -->")
	plt.grid()
	plt.show()


# main

root = Tk()
root.title("Weather")
root.geometry("500x500+450+150")

lblTitle = Label(root,text='Weather Forcast')
btnTemp = Button(root, text = 'TEMPERATURE',width = 15, command = lambda:f1(1))
btnHumid = Button(root, text = 'HUMIDITY',width = 15, command = lambda:f1(2))
btnWs = Button(root, text = 'WIND SPEED',width = 15, command = lambda:f1(3))
btnDp = Button(root, text = 'DEW POINT',width = 15, command = lambda:f1(4))
btnPrs = Button(root, text = 'PRESSURE',width = 15, command = lambda:f1(5))

lblTitle.pack(pady=10)
btnTemp.pack(pady=10)
btnHumid.pack(pady=10)
btnWs.pack(pady=10)
btnDp.pack(pady=10)
btnPrs.pack(pady=10)

# temperature
temp = Toplevel(root)
temp.title('TEMPERATURE')
temp.geometry("500x500+450+150") 
temp.withdraw()

btnTempGraph = Button(temp, text = 'GRAPH',width = 10, command = lambda:f3(1))
btnTempGraph.pack(pady=20)
lblTempMax = Label(temp,text='MAX = '+str(max[0]))
lblTempMax.pack(pady=20)
lblTempMin = Label(temp,text='MIN = '+str(min[0]))
lblTempMin.pack(pady=20)
btnTempBack = Button(temp, text = 'BACK',width = 10, command = lambda:f2(1))
btnTempBack.pack(pady=10)

# humidity
humid = Toplevel(root)
humid.title('HUMIDITY')
humid.geometry("500x500+450+150")
humid.withdraw()

btnHumidGraph = Button(humid, text = 'GRAPH',width = 10, command = lambda:f3(2))
btnHumidGraph.pack(pady=20)
lblHumidMax = Label(humid,text='MAX = '+str(max[1]))
lblHumidMax.pack(pady=20)
lblHumidMin = Label(humid,text='MIN = '+str(min[1]))
lblHumidMin.pack(pady=20)
btnHumidBack = Button(humid, text = 'BACK',width = 10, command = lambda:f2(2))
btnHumidBack.pack(pady=10)

# wind speed
ws = Toplevel(root)
ws.title('WIND SPEED')
ws.geometry("500x500+450+150")
ws.withdraw()

btnWsGraph = Button(ws, text = 'GRAPH',width = 10, command = lambda:f3(3))
btnWsGraph.pack(pady=20)
lblWsMax = Label(ws,text='MAX = '+str(max[2]))
lblWsMax.pack(pady=20)
lblWsMin = Label(ws,text='MIN = '+str(min[2]))
lblWsMin.pack(pady=20)
btnWsBack = Button(ws, text = 'BACK',width = 10, command = lambda:f2(3))
btnWsBack.pack(pady=10)

# dew point
dp = Toplevel(root)
dp.title('DEW POINT')
dp.geometry("500x500+450+150")
dp.withdraw()

btnDpgraph = Button(dp, text = 'GRAPH',width = 10, command = lambda:f3(4))
btnDpgraph.pack(pady=20)
lblDpMax = Label(dp,text='MAX = '+str(max[3]))
lblDpMax.pack(pady=20)
lbDpMin = Label(dp,text='MIN = '+str(min[3]))
lbDpMin.pack(pady=20)
btnDpBack = Button(dp, text = 'BACK',width = 10, command = lambda:f2(4))
btnDpBack.pack(pady=10)

# pressure
prs = Toplevel(root)
prs.title('PRESSURE')
prs.geometry("500x500+450+150")
prs.withdraw()

btnPrsGraph = Button(prs, text = 'GRAPH',width = 10, command = lambda:f3(5))
btnPrsGraph.pack(pady=20)
lblPrsMax = Label(prs,text='MAX = '+str(max[4]))
lblPrsMax.pack(pady=20)
lblPrsMin = Label(prs,text='MIN = '+str(min[4]))
lblPrsMin.pack(pady=20)
btnPrsBack = Button(prs, text = 'BACK',width = 10, command = lambda:f2(5))
btnPrsBack.pack(pady=10)


root.mainloop()

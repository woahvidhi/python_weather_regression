from matplotlib import pyplot as plt
from pandas import*

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

while True:
	n = int(input("1.Temperature, 2.Humid, 3.Wind Speed, 4.Dew Point, 5.Pressure and 6.Exit: "))
	if n == 1:
		plt.plot(week,week_temp, linewidth=1, marker='o', markersize=1)
		plt.title('TEMPERATURE')
		plt.ylabel('FAHRENHEIT')
		plt.xlabel("WEEK -->")
		plt.grid()
		plt.show()

	elif n == 2:
		plt.plot(week,week_humid, linewidth=1, marker='o', markersize=1)
		plt.title('HUMIDITY')
		plt.ylabel('GRAMS PER CUBIC METER')
		plt.xlabel("WEEK -->")
		plt.grid()
		plt.show()

	elif n == 3:
		plt.plot(week,week_ws, linewidth=1, marker='o', markersize=1)
		plt.title('WIND SPEED')
		plt.ylabel('MPH')
		plt.xlabel("WEEK -->")
		plt.grid()
		plt.show()

	elif n == 4:
		plt.plot(week,week_dp, linewidth=1, marker='o', markersize=1)
		plt.title('DEW POINT')
		plt.ylabel('FAHRENHEIT')
		plt.xlabel("WEEK -->")
		plt.grid()
		plt.show()

	elif n== 5:
		plt.plot(week,week_prs, linewidth=1, marker='o', markersize=1)
		plt.title('PRESSURE')
		plt.ylabel('PASCALS')
		plt.xlabel("WEEK -->")
		plt.grid()
		plt.show()

	elif n==6:
		break
	else:
		print('Invalid option')
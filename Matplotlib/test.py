import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mplfinance.original_flavor import candlestick_ohlc
from matplotlib import style
import matplotlib.animation as animation

import csv
import random
import numpy as np
import urllib.request
import datetime as dt

style.use('fivethirtyeight')

fig = plt.figure()

def create_plots():

    xs = []

    ys = []

    for i in range(10):

        x = i

        y = random.randrange(10)

        xs.append(x)

        ys.append(y)

    return xs , ys

ax1 = fig.add_subplot(221)

ax2 = fig.add_subplot(222)

ax3 = fig.add_subplot(212)

x,y = create_plots()

ax1.plot(x,y)

x,y = create_plots()

ax2.plot(x,y)

x,y = create_plots()

ax3.plot(x,y)

plt.show()


# style.use('fivethirtyeight')

# ========================================= Información en tiempo real

# fig = plt.figure()

# ax1 = fig.add_subplot(1,1,1)

# def animate(i):

#     graph_data = open('example.txt', 'r').read()

#     lines = graph_data.split('\n')

#     xs = []

#     ys = []

#     for line in lines :

#         if len(line) > 1:

#             x, y = line.split(',')

#             xs.append(x)

#             ys.append(y)

#     ax1.clear()

#     ax1.plot(xs, ys)

# ani = animation.FuncAnimation(fig, animate, interval=1000)

# plt.show()

# =================================== Obtener datos desde internet

# def bytespdate2num(fmt, encoding='utf-8'):

#     def bytesconverter(b):
        
#         s = b.decode(encoding)

#         return (mdates.datestr2num(s))
    
#     return bytesconverter

# def graph_data():

#     fig = plt.figure()

#     ax1 = plt.subplot2grid((1,1), (0,0))

#     stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'

#     source_code = urllib.request.urlopen(stock_price_url).read().decode()

#     stock_data = []

#     split_source = source_code.split('\n')

#     for line in split_source:

#         if "Date" not in line:

#             stock_data.append(line)

#     Date, Open, High, Low, Close, Adjusted_close, Volume = np.loadtxt(
        
#         stock_data, 
        
#         delimiter=',', 
        
#         unpack=True,

#         converters={0: bytespdate2num('%Y%m%d')}
#         )
    
#     x = 0

#     y = len(Date)

#     ohlc = []

#     while x < y:

#         append_me = Date[x], Open[x], High[x], Low[x], Close[x], Volume[x]

#         ohlc.append(append_me)

#         x+=1

#     # candlestick_ohlc(ax1, ohlc, width=0.4, colorup='g', colordown='r')

#     ax1.plot(Date, Close)

#     ax1.plot(Date, Open)


#     for label in ax1.xaxis.get_ticklabels():

#         label.set_rotation(45)

#     ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

#     # ax1.xaxis.set_major_locator(mticker.MaxNLocator(5))

#     ax1.grid(True)
    
    # ============================= Modificaciones estéticas 
    
    # ax1.plot_date(Date, Close, '-', label="Price")

    # ax1.plot([], [], linewidth=5, label='Gain', color='g', alpha=0.5)

    # ax1.plot([], [], linewidth=5, label='Loss', color='r', alpha=0.5)

    # ax1.axhline(Close[0], color='k', linewidth=5)

    # ax1.fill_between(Date, Close, Close[0], where=(Close > Close[0]), facecolor='g', alpha=0.5)

    # ax1.fill_between(Date, Close, Close[0], where=(Close < Close[0]), facecolor='r', alpha=0.5)


    # for label in ax1.xaxis.get_ticklabels():

    #     label.set_rotation(45)

    # ax1.grid(True)# , color='g', linestyle='-')

    # # ax1.xaxis.label.set_color('c')

    # # ax1.yaxis.label.set_color('r')

    # # ax1.set_yticks([0,25,50,75])

    # ax1.spines['left'].set_color('c')

    # ax1.spines['right'].set_visible(False)

    # ax1.spines['top'].set_visible(False)

    # ax1.spines['left'].set_linewidth(5)

    # ax1.tick_params(axis='x', colors='#f06215')

#     plt.xlabel('Date')

#     plt.ylabel('Price')

#     plt.title('TSLA')

#     plt.legend()

#     plt.subplots_adjust(left=0.09, bottom=0.18, right=0.94, top=0.95, wspace=0.2, hspace=0)

#     plt.show()

# graph_data()
    
# ================================== Obtener datos desde archivos

# Parte 1!!!!!!!!!!!!!!!!!!!!!!!!

# x = []

# y = []

# with open('example.txt', 'r') as csvfile:

#     plots = csv.reader(csvfile, delimiter=',')

#     for row in plots: 

#         x.append(int(row[0]))

#         y.append(int(row[1]))

# plt.plot(x,y, label='Loaded from file!')


# Parte 2!!!!!!!!!!!!!!!!!!!!!!!!

# x, y = np.loadtxt('example.txt', delimiter=',', unpack=True)

# plt.plot(x,y, label='Loaded from file! 2')

# =================================== Gráfico circular

# days = [1,2,3,4,5]

# sleeping = [7,8,6,11,7]

# eating = [2,3,4,3,2]

# working = [7,8,7,2,2]

# playing = [8,5,6,7,13]

# slices = [7,2,2,13]

# activities = [ 'sleeping', 'eating', 'working', 'playing'] 

# colors = ['c','m','r','y']

# plt.pie(
    
#     slices, 
    
#     labels=activities, 
    
#     colors=colors, 
    
#     startangle=90, 
    
#     shadow=True, 
    
#     explode=(0,0.1,0,0),
    
#     autopct='%1.1f%%'
#     )
# ==================================== Gráfico de área

# days = [1,2,3,4,5]

# sleeping = [7,8,6,11,7]

# eating = [2,3,4,3,2]

# working = [7,8,7,2,2]

# playing = [8,5,6,7,13]

# plt.plot([],[], color='m', label='Sleeping', linewidth=5)
# plt.plot([],[], color='c', label='Eating', linewidth=5)
# plt.plot([],[], color='r', label='Working', linewidth=5)
# plt.plot([],[], color='k', label='Playing', linewidth=5)


# plt.stackplot(days, sleeping, eating, working, playing, colors=['m','c','r','k'])

# ====================================== Gráfico de dispersión

# x = [1,2,3,4,5,6,7,8]

# y = [5,8,3,5,8,4,2,6]

# plt.scatter(x,y, label='skitscart', color='k', marker='*')

# ====================================== Histograma

# edad_poblacion = [22,55,62,45,21,76,43,21,54,11,76,32,76,43,32,21,54,45,65,73,32,33,54,22,73,63,3,7]

# bins = [0,10,20,30,40,50,60,70,80,90,100,110,120]

# plt.hist(edad_poblacion, bins, histtype='bar', rwidth=0.8)

# ========================================== Gráfico de barras 

# x = [2,4,6,8,10]
# y = [6,7,8,2,4]

# x2 = [1,3,5,7,9]
# y2 = [7,8,2,4,2] 

# plt.bar(x,y, label='Barras', color='red')

# plt.bar(x2,y2, label='Barras 2')

# =========================================== Gráfico

# x = [2,4,6]
# y = [6,7,8]

# plt.plot(x,y,label='línea') 

# plt.xlabel('x')

# plt.ylabel('y')

# plt.title('Gráfico mamalón\nChequea esto')

# plt.legend()

# plt.show()

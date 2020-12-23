from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
import mpld3

from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

frame_len = 10000
fig = plt.figure(figsize=(9,6))

def animate(i):
    data = pd.read_csv('sentiment.csv')
    y1 = data['Trump']
    y2 = data['Biden']
    
    if len(y1)<=frame_len:
        plt.cla()
        plt.plot(y1, label = 'Donald Trump')
        plt.plot(y2, label = 'Joe Biden')
    else:
        plt.cla()
        plt.plot(y1[-frame_len], label='Donald Trump')
        plt.plot(y2[-frame_len], label='Joe Biden')
        
    plt.legend(loc='upper left')
    plt.title("Twitter Sentiment Analysis")
    plt.xlabel('Total Tweet', fontsize=14)
    plt.ylabel('Total Sentiment Value', fontsize=14)
    plt.tight_layout()

while(True):    
    ani = FuncAnimation(plt.gcf(), animate, interval=100)
    html_str = mpld3.fig_to_html(fig)
    Html_file= open("index.html","w")
    Html_file.write(html_str)
    Html_file.close()    
        #plt.show()
    mpld3.show()

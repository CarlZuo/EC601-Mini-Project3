import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json('./myResultsTweet.json', lines=True, encoding='utf-8')

df_choose = df[['id', 'Name', 'Text']]


def draw_chart(num_list, title):  # draw chart
    name_list = [1,2,3,4,5,6,7,8,9,10] # name of x axis
    plt.bar(range(len(name_list)), num_list, color='rgb', tick_label=name_list)
    plt.xlabel("name")
    plt.ylabel("text")
    plt.title(title)
    plt.show()

draw_chart(number_temp, title)
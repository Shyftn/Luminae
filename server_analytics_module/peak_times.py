import sqlite3
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime

def calculate_and_plot_activity(command):
    ## Establish a connection to the SQLite database that stores server activity data
    conn = sqlite3.connect('server_activity.db')

    ## Define a SQL query to fetch all timestamps from the activity data
    query = 'SELECT timestamp FROM activity'

    ## Execute the SQL query
    cur = conn.cursor()
    cur.execute(query)

    ## Fetch all timestamps and extract the hour or day from each timestamp based on command
    if command == 'daily':
        timestamps = [row[0].hour for row in cur.fetchall()]
        xlabel = 'Hour of the Day (24-hour format)'
        title = 'Daily Server Activity'
    elif command == 'monthly':
        timestamps = [row[0].day for row in cur.fetchall()]
        xlabel = 'Day of the Month'
        title = 'Monthly Server Activity'
    
    ## Count the occurrences of each hour or day using the Counter class from the collections module
    count = Counter(timestamps)

    ## The hour or day with the most occurrences is the peak time
    peak_time = count.most_common(1)[0][0]
    print(f'Peak {command} activity time: {peak_time}')

    ## Sort the hours or days
    sorted_times = sorted(count.items())
    times = [time for time, _ in sorted_times]
    activity = [count[time] for time in times]

    ## Plot the hours or days on the x-axis and activity count on the y-axis
    plt.plot(times, activity)

    ## Set the title and labels for the plot
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel('Number of Messages')

    ## Show the plot
    plt.show()

def setup(bot):
    bot.add_command(commands.Command(lambda: calculate_and_plot_activity('daily'), name='peak_times'))
    bot.add_command(commands.Command(lambda: calculate_and_plot_activity('monthly'), name='SAM'))

import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/nome_weather_2022_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get dates and high temps from this file
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[6])
        dates.append(current_date)
        highs.append(high)

# Plot high temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Format plot
plt.title('Daily high temperatures, 2022', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperatures (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
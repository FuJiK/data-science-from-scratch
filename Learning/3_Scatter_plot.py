from matplotlib import pyplot as plt
friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = [chr(i) for i in range(65, 65+9)]
plt.scatter(friends,minutes)
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
            xy = (friend_count, minute_count),
            xytext = (5, -5),
            textcoords = 'offset points')
plt.title("Daily Minutes VS. Number of Friends")

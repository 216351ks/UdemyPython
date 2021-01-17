def color(colors, n):
    return colors[:n]
colors = ["red", "orange", "green", "violet", "blue", "yellow"]

for x in range(1, len(colors) + 1):
    print(color(colors, x))
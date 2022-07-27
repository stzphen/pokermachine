import tkinter as tk
from rangeCharts import *

def drawChart(canvas, rangeChart):
    cardlist = ["A", "K", "Q", "J", "T", 9, 8, 7, 6, 5, 4, 3, 2]
    grid = []
    index = 0
    for i in range(13):
        for j in range(13):
            jeff = cardlist[i]
            steve = cardlist[j]
            if i < j:
                grid.append(str(jeff) + str(steve))
                grid[13 * i + j] += "o"
            elif i > j:
                grid.append(str(steve) + str(jeff))
                grid[13 * i + j] += "s"
            elif i == j:
                grid.append(str(jeff) + str(steve))
    for x in range(13):
        for y in range(13):
            if rangeChart.exists(grid[index]) == 1:
                color = "blue"
            else:
                color = "yellow"
            canvas.create_rectangle(50*x, 50*y, 50*(x+1), 50*(y+1), fill = color)
            canvas.create_text(25 + 50*x, 50 *y + 25, text = grid[index])
            index += 1

root = tk.Tk()
canvas = tk.Canvas(root, width = 650, height = 650)
rc = RangeChart()
drawChart(canvas, rc)
canvas.pack()
root.mainloop()

#test
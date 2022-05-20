import matplotlib.pyplot as plt
from csvLoader import CsvLoader
from interpolator import Interpolator

titles = ["Gdańsk Spacerniak", "Kanion Kolorado", "Mount Everest"]
sources = ["SpacerniakGdansk.csv", "WielkiKanionKolorado.csv", "MountEverest.csv"]
distances = []
heights = []

for source in sources:
    distance, height = CsvLoader.csvLoad(source)
    distances.append(distance)
    heights.append(height)

numbersOfNodes = [4, 6, 8, 16, 24]

for i in range(0, len(sources)):
    for numberOfNodes in numbersOfNodes:
        xp = []
        yp = []
        lagrange = []
        splines = []

        for j in range(0, len(distances[i])):
            if j % int(len(distances[i]) / numberOfNodes) == 0:
                xp.append(distances[i][j])
                yp.append(heights[i][j])
        xs = Interpolator.prepSplines(xp, yp)
        for x in distances[i]:
            lagrange.append(Interpolator.lagrange(xp, yp, x))
            splines.append(Interpolator.splines(xp, yp, xs, x))

        plt.plot(distances[i], heights[i], color='blue', linewidth=1)
        plt.plot(distances[i], lagrange, color='red', linewidth=2)
        plt.scatter(xp, yp, color='red')
        plt.title((titles[i] + " (" + str(numberOfNodes) + " nodes) " + "Lagrange method"))
        plt.xlabel('distance [m]')
        plt.ylabel('height [m]')
        plt.yscale('log')
        plt.savefig((titles[i] + "(" + str(numberOfNodes) + "nodes)" + "Lagrange method" + ".png"))
        plt.show()

        plt.plot(distances[i], heights[i], color='blue', linewidth=1)
        plt.plot(distances[i], splines, color='red', linewidth=2)
        plt.scatter(xp, yp, color='red')
        plt.title((titles[i] + " (" + str(numberOfNodes) + " nodes) " + "Splines method"))
        plt.xlabel('distance [m]')
        plt.ylabel('height [m]')
        plt.yscale('log')
        plt.savefig((titles[i] + "(" + str(numberOfNodes) + "nodes)" + "Splines method" + ".png"))
        plt.show()







from csvLoader import CsvLoader
from interpolator import Interpolator

distance, height = CsvLoader.csvLoad("MountEverest.csv")
xp = [1, 3, 5]
yp = [6, -2, 4]
Interpolator.splines(xp, yp, 0)

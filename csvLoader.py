import pandas as pd


class CsvLoader:

    @staticmethod
    def csvLoad(path):
        csvData = pd.read_csv(path)
        distance = csvData.Dystans
        height = csvData.Wysokosc
        return distance, height

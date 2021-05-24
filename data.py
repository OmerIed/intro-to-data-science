import pandas


class Data:
    def __init__(self, path):
        """
                :param path: path of the csv file
                initiating data object, loading the data from the csv file and casting it to dictionary
        """
        df = pandas.read_csv(path)
        self.data = df.to_dict(orient="list")

    def create_samples(self):
        pass

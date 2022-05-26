import math
import numpy as np

# import biblioteki zewnętrznej Hive
from Hive import Utilities
from Hive import Hive


def evaluator(vector, a=1, b=100):
    vector = np.array(vector)

    return (a - vector[0]) ** 2 + b * (vector[1] - vector[0] ** 2) ** 2


def run():
    ndim = int(2)
    model = Hive.BeeHive(lower=[0] * ndim,
                         upper=[10] * ndim,
                         fun=evaluator,
                         numb_bees=10,
                         max_itrs=50, )

    cost = model.run()

    Utilities.ConvergencePlot(cost)

    print("Fitness Value ABC: {0}".format(model.best))


if __name__ == "__main__":
    run()

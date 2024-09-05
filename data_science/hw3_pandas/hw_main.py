import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]

if __name__ == "__main__":
    iris_df = pd.read_csv(url, header=None, names=column_names)
    petal_length_col = iris_df["petal_length"]

    avg_sepal_length = iris_df.groupby("class")["sepal_length"].mean()
    max_setosa_petal_width = iris_df[iris_df["class"] == "Iris-setosa"]["petal_width"].max()
    petal_length_frequency = petal_length_col.value_counts().sort_index()

    petal_length_hist = petal_length_col.hist(bins=30)
    plt.title("Distribution of Petal Length for All Iris Species")
    plt.xlabel("Petal Length")
    plt.ylabel("Frequency")
    plt.xticks(np.arange(0, petal_length_col.max(), 0.5))
    plt.yticks(np.arange(0, petal_length_frequency.max() * 2, 1))

    versicolor_df = iris_df[iris_df["class"] == "Iris-versicolor"].copy()
    long_petal_irises = iris_df[iris_df["petal_length"] > 5]

    avg_petal_width = iris_df.groupby("class")["petal_width"].mean()
    min_sepal_length = iris_df.groupby("class")["sepal_length"].min()

    iris_df["avg_petal_length"] = iris_df["petal_length"].mean()
    iris_df["avg_petal_length_by_class"] = iris_df.groupby("class")["petal_length"].transform("mean")

    large_petal_length_classes_count = iris_df.query(f"petal_length > {iris_df['petal_length'].mean()}")[
        ["class", "avg_petal_length", "avg_petal_length_by_class"]].value_counts()

    # Task 1
    print(f'\nAverage sepal length by class\n{avg_sepal_length}')
    print(f'\nMax setosa petal width: {max_setosa_petal_width}')
    print(f'\nPetal length frequency\n{petal_length_frequency}')

    # Task 2
    print(f'\nVersicolor iris data:\n{versicolor_df}')
    print(f'\nIrises with petal length > 5\n{long_petal_irises}')

    # Task 3
    print(f'\nAverage petal width by class\n{avg_petal_width}')
    print(f'\nMin sepal length by class\n{min_sepal_length}')
    print(f'\nIrises with petal length > average by classes:\n{large_petal_length_classes_count}')

    plt.show()

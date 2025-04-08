# This is a sample Python script.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    # read the data
    data = pd.read_csv("C:\\Users\\user\\Downloads\\countries.csv")
    # info and head of data
    print(data.info())
    print(data.head())


    # Data Processing

    # basics maths
    print(data.describe())
    # check null values
    print(data.isnull().sum())
    # checking duplicated va
    print(data.duplicated().sum())
    # drop null values
    data.dropna(inplace=True)
    # check data points are drop or not
    print(data.info())
    # outliers
    data_copy = data.copy()
    for col in data_copy.select_dtypes(include=np.number):
        # iqr method
        q1 = data_copy[col].quantile(0.25)  # 25%
        q3 = data_copy[col].quantile(0.75)  # 75%

        iqr = q3 - q1
        # calculat upper and lower bounds
        lower_bound = q1 - 1.5*iqr
        upper_bound = q3 + 1.5*iqr

        # outlier free data
        data_copy = data_copy[(data_copy[col] >= lower_bound) & (data_copy[col] <= upper_bound)]

    print(data_copy.info())
    print(data_copy.head())
    # creating columns range
    A = np.array(['Total Ecological Footprint', 'Cropland', 'Grazing Land','Forest Land','Fishing Water'])
    B = np.array(['Urban Land','Total Biocapacity'])
    union = np.union1d(A, B)  # union of two array
    for col in union:
        num = [-3, 2, 3, 100]
        label = ['low(sustainable)', 'medium(okay)', 'high(unsustainable)']
        data_copy[col+"_range"] = pd.cut(x=data_copy[col], bins=num, labels=label)
    # checking change
    print(data_copy.info())

    # Data Visualization

    # making graphs
    for col in union:
        new_col = col + "_range"
        plt.figure(figsize=(14, 7))
        sns.countplot(data=data_copy, x=new_col)
        plt.yscale('log') # x axis into log
        plt.title(f"Distribution of {new_col} basics of 2016")
        plt.show()

    # graph of region
    plt.figure(figsize=(20, 5))
    # count the region and collect it
    reg = data_copy["Region"].value_counts().reset_index()
    reg.columns = ['Region', 'count']
    sns.barplot(data=reg, x="Region", y="count")
    plt.xlabel("Region")
    plt.ylabel("count")
    plt.title("Distribution of Region  basics of 2016")
    plt.show()

    # top10  population  basics countries
    plt.figure(figsize=(8, 6))
    # Distribution population across each country
    df = data_copy.groupby(['Country', 'Population (millions)']).size().reset_index(name='count')
    top10 = df.nlargest(10, 'count')  # topo 10 values
    sns.lineplot(data=top10, x='Country', y='count', hue='Population (millions)', marker='o')
    plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

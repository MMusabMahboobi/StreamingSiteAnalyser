import pandas as pd
import matplotlib.pyplot as plt

# load data
df = pd.read_csv("StreamingSite.csv")

# print data
print("DATASET")
print(df)
print("\n")

# count movies vs TV shows
print("TYPES")
type_counts = df["type"].value_counts()
print(type_counts)
print("\n")

# print most common release year
print("MOST TITLES RELEASED IN:")
print(df["release_year"].mode()[0])

# show release years
df["release_year"].plot(kind = "hist", edgecolor="black")
plt.title("Number of Titles Released in Each Year Range")
plt.xlabel("Release Year Ranges")
plt.ylabel("Number of Titles")

plt.show()


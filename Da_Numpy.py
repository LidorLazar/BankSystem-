import pandas as pd
from collections import Counter


with open('c:/Users/97252/Desktop/diamonds.csv', 'r') as diamond_file:
    diamonds = pd.read_csv(diamond_file)

print(f"max price for diamond is: {max(diamonds['price'])}")
print(f"Average price per diamond is: {diamonds['price'].mean()}")
print(f"how many Ideal diamond there are: {Counter(diamonds['cut'])['Ideal']}")
colors = Counter(diamonds['color']).keys()
print(f"There are {len(colors)} colors: {', '.join(colors)}")
print("the median carat of premium type diamonds is")
print(Counter(diamonds['cut']).get('Premium'))
print(f"Average carat for each cut: {diamonds['carat'].mean()}")

print(Counter(diamonds['cut']).get('Premium'))
print(diamonds.groupby(by=['cut']).median())
print(diamonds.groupby(by=['cut', 'carat']).median())
print(diamonds.pivot_table('carat','cut', aggfunc='median'))
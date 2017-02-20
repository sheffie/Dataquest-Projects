from read import load_data

data = load_data()

d = data["url"].value_counts()

print(d[0:100])






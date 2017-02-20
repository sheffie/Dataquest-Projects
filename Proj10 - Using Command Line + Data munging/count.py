from read import load_data
import collections

data = load_data()
headlines_combined = ""
for i in range(len(data)):
	headlines_combined += str(data["headline"][i]) + " "

headlines_combined = headlines_combined.lower().split(" ")
cnt = collections.Counter()

for word in headlines_combined:
    cnt[word] += 1

print(cnt.most_common(100))

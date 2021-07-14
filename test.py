asset_file = open("output.txt")
game_dictionary = []
for line in asset_file:
    x = line.split("?")
    game_dictionary.append(x)

anomalies = []

for i in range(len(game_dictionary)):
    if len(game_dictionary[i]) != 2:
        anomalies.append(i)
        print(i)

print(anomalies)

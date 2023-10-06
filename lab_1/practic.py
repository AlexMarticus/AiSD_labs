planet = [[1, 1, 0, 0, 0], [1, 0, 1, 0, 0], [0, 1, 1, 0, 0],
          [0, 0, 0, 0, 1], [0, 0, 0, 1, 0]]
city={i+1:[] for i in range (len(planet))}
for i in range(len(planet)):
    city[i+1].append(i+1)
    for j in range(len(planet)):
        if planet[i][j]==1:city[i+1].append(j+1)
for i in city:
    for j in city[i]:
        city[i]=city[i]+city[j]
    city[i]=list(set(city[i]))


print(f'В самой большой стране города:{max(city.values(), key=len)}')

connections = []
def train_connections(origin, destinations, region):
    new_dict = {}
    connections.append(new_dict)
    new_dict.update({"origin": origin})
    new_dict.update({"destinations": destinations})
    new_dict.update({"region": region})

train_connections("Wroclaw",["Katowice", "Opole", "Jelenia Gora"], "dolnyslask")
print(connections)
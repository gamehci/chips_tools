import json

with open("test_data.json", "r") as json_file:
    game_library = json.load(json_file)
    games = game_library["games"]
   # for i in range(len(games)):
    #    print(i, games[i])

    for key in game_library:
        print(game_library[key])
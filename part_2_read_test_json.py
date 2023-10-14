import json
import cc_classes

json_file_name = "data/test_data.json"


#in class
with open("data/test_data.json", "r") as json_file:
    game_library = json.load(json_file)
    games = game_library["games"]

    for key in game_library:
        print(game_library[key])


import cc_dat_utils
import cc_classes
import json


def load_json_level_pack(json_file):
    """Load level pack from a JSON file into a CCLevelPack object"""
    with open(json_file, 'r') as f:
        data = json.load(f)

    #now, data should be a dictionary
    return data

    level_pack = cc_classes.CCLevelPack()

    print(level_data)
    level.level_number = level_data.get("level_number", 0)

    # Convert JSON data to CCLevel objects
    for level_data in data["level1"]:
        level = cc_classes.CCLevel()
        level.level_number = level_data.get("level_number", 0)
        level.time = level_data.get("time", 0)
        level.num_chips = level_data.get("num_chips", 0)
        level.upper_layer = level_data.get("upper_layer", [0] * 1024)
        level.lower_layer = level_data.get("lower_layer", [0] * 1024)
        # Add other fields as needed
        # For now, assuming no optional fields. If they exist, a similar conversion must be done.
        level_pack.levels.append(level)

    return level_pack


# Load the JSON level pack
level_pack = load_json_level_pack("alicia_level.json")

# Convert to DAT and save
cc_dat_utils.write_cc_level_pack_to_dat(level_pack, "alicia_level.dat")

print(cc_dat)

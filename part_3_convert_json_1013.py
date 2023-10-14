import json
import cc_dat_utils
import cc_classes

# Load JSON file
with open("alicia_level.json", "r") as json_file:
    level_pack_data = json.load(json_file)

# Convert JSON to CCLevel object
print(level_pack_data)

# Create an in-memory CC level pack (initially empty)
level_pack = cc_classes.CCLevelPack()

# Extract level1 data from the loaded JSON
level1_data = level_pack_data["level1"]

# Create a new CCLevel object for level1
level1 = cc_classes.CCLevel()
level1.level_number = level1_data["level_number"]
level1.time = level1_data["time"]
level1.num_chips = level1_data["num_chips"]
level1.upper_layer = level1_data["upper_layer"]
level1.lower_layer = level1_data["lower_layer"]

# Append the Encoded Password Field to the optional fields of level1
#level1.optional_fields = level1_data["optional_fields"]

password_field = cc_classes.CCEncodedPasswordField(level1_data["optional_fields"]["password"])
level1.optional_fields.append(password_field)

#monster_field = cc_classes.CCMonsterMovementField(level1_data["optional_fields"]["monsters"])
#level1.optional_fields.append(monster_field)

hint_field = cc_classes.CCMapHintField(level1_data["optional_fields"]["hint"])
level1.optional_fields.append(hint_field)

#loop, * = unpacking
for trap_config in level1_data["optional_fields"]["traps"]:
    #bx, by, tx, ty = trap_config (*이 있을땐 이 부분이 필요없음)
    trap1 = cc_classes.CCTrapControl(*trap_config)
    level1.optional_fields.append(cc_classes.CCTrapControlsField([trap1]))

# Append the constructed level to the level pack
level_pack.levels.append(level1)

# Save the CCLevelPack object to a DAT file
cc_dat_utils.write_cc_level_pack_to_dat(level_pack, "alicia_level.dat")

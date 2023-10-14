import json
import cc_classes
import cc_dat_utils

def json_to_dat(json_file, dat_file):
    with open("alicia_old_deprecate.json", "r") as json_reader:
        data = json.load(json_reader)

    level_pack = cc_classes.CCLevelPack()
    for level in data["levels"]:
        level_pack.levels.append(cc_dat_utils.write_cc_level_pack_to_dat(level))

    with open(dat_file, "wb") as dat_writer:
        dat_writer.write(b"\xAC\xAA\x02\x00")
        dat_writer.write(len(level_pack.levels).to_bytes(2, byteorder="big"))
        for level in level_pack.levels:
            dat_writer.write(level.to_dat())

if __name__ == "__main__":
    json_file = "alicia_old_deprecate.json"
    dat_file = "alicia_level.dat"
    json_to_dat(json_file, dat_file)

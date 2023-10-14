
import json
import cc_dat_utils
import cc_classes



# load JSON file
with open("alicia_level.json", "r") as json_file:
    level_pack_data = json.load(json_file)

#convert JSON --> CCLevel object
print(level_pack_data)

#make me in memory cc level pack (empty) 빈 레벨이지만 파이썬 메모리에 존재함.
# create an in-memory CC level pack (empty)
level_pack = cc_classes.CCLevelPack()

#create a new level
level1 = cc_classes.CCLevel()

#extract data for level1 from json
level1_data = level_pack_data["level1"]

#assign properties to level1
level1.level_number = level1_data["level_number"]
level1.time = level1_data["time"]
level1.num_chips = level1_data["num_chips"]
level1.upper_layer = level1_data["upper_layer"]
level1.lower_layer = level1_data["lower_layer"]
#IT WORKED!! NO ERRORS

#


level_pack.levels.append(level1)


#이 빈 레벨 컨테이너를 만들어라 ^ cclevel() << 어프렌티스 = 컨스트럭터 새 오브젝트를 리턴함.


#save the CCLevel object to a DAT file
cc_dat_utils.write_cc_level_pack_to_dat(level_pack, "alicia_level.dat")
#이건 레벨팩이 있으니 여기에 써라.
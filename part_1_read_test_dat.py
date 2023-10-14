
import cc_dat_utils


#Part 1
input_dat_file = "alicia_test.dat"


#Use cc_dat_utils.make_cc_level_pack_from_dat() to load the file specified by input_dat_file
#print the resulting data

level = cc_dat_utils.make_cc_level_pack_from_dat("alicia_test.dat")
print(level)
level.levels[0].time = 111

cc_dat_utils.write_cc_level_pack_to_dat(level, "alicia_test.dat")
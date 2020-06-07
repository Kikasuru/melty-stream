# Taken from https://github.com/pluot-mb/CCCaster/blob/master/netplay/Constants.hpp

# Character Select Data
CC_P1_SELECTOR_MODE_ADDR        = 0x74D8EC
CC_P1_CHARA_SELECTOR_ADDR       = 0x74D8F8
CC_P1_CHARACTER_ADDR            = 0x74D8FC
CC_P1_MOON_SELECTOR_ADDR        = 0x74D900
CC_P1_COLOR_SELECTOR_ADDR       = 0x74D904

CC_P2_SELECTOR_MODE_ADDR        = 0x74D910
CC_P2_CHARA_SELECTOR_ADDR       = 0x74D91C
CC_P2_CHARACTER_ADDR            = 0x74D920
CC_P2_MOON_SELECTOR_ADDR        = 0x74D924
CC_P2_COLOR_SELECTOR_ADDR       = 0x74D928

CC_STAGE_SELECTOR_ADDR          = 0x74FD98

# Total size of a single player structure.
# Note: there are FOUR player structs in memory, due to the puppet characters.
CC_PLR_STRUCT_SIZE              = 0xAFC

CC_P1_HEAT_ADDR                 = 0x555214
CC_P2_HEAT_ADDR                 = CC_P1_HEAT_ADDR + CC_PLR_STRUCT_SIZE

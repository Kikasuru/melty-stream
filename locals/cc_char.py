def getCharName(char):
    chars = {
        0x00: "sion",
        0x01: "arc",
        0x02: "ciel",
        0x03: "akiha",
        0x04: "maids",
        0x05: "hisui",
        0x06: "kohak",
        0x07: "tohno",
        0x08: "miyak",
        0x09: "wara",
        0x0A: "nero",
        0x0B: "vsion",
        0x0C: "warc",
        0x0D: "vkiha",
        0x0E: "mech",
        0x0F: "nanay",
        0x11: "sacch",
        0x12: "len",
        0x13: "pciel",
        0x14: "neco",
        0x16: "aoko",
        0x17: "wlen",
        0x19: "nac",
        0x1C: "kouma",
        0x1D: "skiha",
        0x1E: "ries",
        0x1F: "roa",
        0x21: "ryoug",
        0x22: "nmech",
        0x23: "kmech",
        0x33: "hime"
    }
    return chars.get(char, None)

# cake->binary->cake vUnicode
# reddust9

zero_emojis = ["🙂", "👎"] # add emoji codes that represent binary 0s here
one_emojis = ["🙃", "👍"] # add emoji codes that represent binary 1s here
translate_back_index = 1


def bin_to_emoji(emojis: str):
    binStr = ""

    for emoji in emojis:
        if emoji in zero_emojis:
            binStr += "0"
            translate_back_index = zero_emojis.index(emoji)
        elif emoji in one_emojis:
            binStr += "1"
            translate_back_index = one_emojis.index(emoji)
        else:
            print("Unrecognized emoji:", emoji)
            binStr += "0"
            
    print("Binary:", binStr)
    deci = int(binStr, 2)
    deci += 1

    newBin = format(deci, "b")
    if len(newBin) < 8:
        rev = newBin[::-1]
        rev += "0" * (8 - len(newBin))
        newBin = rev[::-1]

    outStr = ""
    for bit in newBin:
        if bit == "0":
            outStr += zero_emojis[translate_back_index]
        elif bit == "1":
            outStr += one_emojis[translate_back_index]
        else:
            outStr += ":question:"

    return outStr
            

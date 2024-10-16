from base64 import b64decode
import itertools

flag_start = "TVlSQ1RG"
flag_end = "0="

flag_parts = []
flag_parts.append("Q0")
flag_parts.append("VE")
flag_parts.append("eX")
flag_parts.append("tf")
flag_parts.append("Jp")
flag_parts.append("Fz")
flag_parts.append("X0")
flag_parts.append("e1")
flag_parts.append("xF")

def get_flag():
    times = 0
    permutations = itertools.permutations(flag_parts)
    for i in permutations:
        try:
            strong = b64decode(flag_start+"".join(i)+flag_end).decode("utf-8")
            if strong[-1] == "}" and strong[0:7] == "MYRCTF{":
                times += 1
                print(strong)
        except:
            pass
    return

get_flag()
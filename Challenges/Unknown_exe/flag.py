from base64 import b64decode
from webbrowser import open

print("The flag is in pices :(")
print("I only remember that a famous person was on it.")
def get_flag():
    flag_parts = []
    flag_parts.append("lS")
    flag_parts.append("Q0")
    flag_parts.append("VE")
    flag_parts.append("eX")
    flag_parts.append("Q1")
    flag_parts.append("tf")
    flag_parts.append("Jp")
    flag_parts.append("Fz")
    flag_parts.append("X0")
    flag_parts.append("0=")
    flag_parts.append("e1")
    flag_parts.append("xF")
    flag_parts.append("TV")
    flag_parts.append("RG")
    
    print(b64decode("".join(flag_parts)))

def get_nothing():
    open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

get_nothing()
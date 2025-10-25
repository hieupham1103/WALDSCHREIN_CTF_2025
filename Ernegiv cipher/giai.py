enc = "JLQHQWWSFEVWPYDAGHUHTNJNLGGSJFJPDGVKPFB"
key = "NEVERGONNAGIVEYOUUPNEVERGONNALETYOUDOWN"

def d(ch): return ord(ch) - 65        
def c(i): return chr(i + 65)             

pt = "".join(c((d(e) - d(k) - 1) % 26) for e, k in zip(enc, key))
print(pt)

# VGUCYPHER{DONTTELLMETOREVERSEITEVERAGAIN}
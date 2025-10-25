KEY = 0x36
def le(hexstr):
    return int(hexstr, 16).to_bytes(len(hexstr)//2, 'little')

chunks = [
    "58575e4269584350",
    "51585f405a594569",
    "4b425f69",               
]

data = b"".join(le(h) for h in chunks)
print("chunk hex:", data.hex())
print("decoded:", bytes(b ^ KEY for b in data).decode('ascii', 'replace'))


chunks = [
    "535e464f55435140",  # movabs #1
    "51585f5b57584d44",  # movabs #2
    "69020069",          # movl
    "50",                # movb
]

data = b"".join(le(h) for h in chunks)
print("chunk hex:", data.hex())
print("decoded:", bytes(b ^ KEY for b in data).decode('ascii', 'replace'))


chunks = [
    "4558595f42555843",
    "694f574169455f69",
    "5344595b",      
    "69",         
]

data = b"".join(le(h) for h in chunks)
print("chunk hex:", data.hex())
print("decoded:", bytes(b ^ KEY for b in data).decode('ascii', 'replace'))
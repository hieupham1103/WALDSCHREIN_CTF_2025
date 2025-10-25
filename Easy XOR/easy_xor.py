hex_s = "38 29 26 3b 2a 3e 26 36 2a 28 36 7e 21 69 3d 77 11 62 6d 0c 20 7e 24 07 3e 37 11 65 6b 66 79 11 35 2a 62 7d 20 37 25"
ct = bytes(int(b, 16) for b in hex_s.split())
key = b"NNSXS"

pt = bytes(c ^ key[i % len(key)] for i, c in enumerate(ct))
print(pt.decode())  

# vgucypher{x0r1n9_15_n0w_my_6357_fr13nd}

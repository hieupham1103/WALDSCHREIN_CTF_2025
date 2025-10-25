import struct
import zlib

# Read the PNG file
with open('reachforthatsky.png', 'rb') as f:
    data = f.read()

# Read IHDR chunk
ihdr_length = struct.unpack('>I', data[8:12])[0]
ihdr_type = data[12:16]
ihdr_data = data[16:16+ihdr_length]

# Parse IHDR
width = struct.unpack('>I', ihdr_data[0:4])[0]
height = struct.unpack('>I', ihdr_data[4:8])[0]

print(f"Current dimensions: {width} x {height}")

# Get stored CRC
stored_crc = struct.unpack('>I', data[16+ihdr_length:20+ihdr_length])[0]
print(f"Stored CRC: {hex(stored_crc)}")

print("\nSearching for correct height (keeping width constant)...")
for h in range(1, 4096):
    test_data = struct.pack('>II', width, h) + ihdr_data[8:]
    test_crc = zlib.crc32(ihdr_type + test_data)
    if test_crc == stored_crc:
        print(f"FOUND! Width: {width}, Height: {h}")
        print(f"CRC matches: {hex(test_crc)}")
        
        # Create corrected PNG
        corrected = data[:16] + test_data + data[16+ihdr_length:]
        with open('fixed.png', 'wb') as out:
            out.write(corrected)
        print("Fixed image saved as 'fixed.png'")
        break
print("\nSearching for correct width (keeping height constant)...")
for w in range(1, 4096):
    test_data = struct.pack('>II', w, height) + ihdr_data[8:]
    test_crc = zlib.crc32(ihdr_type + test_data)
    if test_crc == stored_crc:
        print(f"FOUND! Width: {w}, Height: {height}")
        print(f"CRC matches: {hex(test_crc)}")
        
        corrected = data[:16] + test_data + data[16+ihdr_length:]
        with open('fixed.png', 'wb') as out:
            out.write(corrected)
        print("Fixed image saved as 'fixed.png'")
        break

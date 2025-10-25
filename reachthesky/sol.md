PNG files consist of chunks, with the IHDR (Image Header) chunk containing critical image metadata:
- Width (4 bytes)
- Height (4 bytes) 
- Bit depth (1 byte)
- Color type (1 byte)
- Compression method (1 byte)
- Filter method (1 byte)
- Interlace method (1 byte)

Each chunk has a CRC-32 checksum to verify data integrity.

When examining `reachforthatsky.png`, we found:
- Current dimensions: 1536 x 512 pixels
- The stored CRC in the IHDR chunk doesn't match the calculated CRC for these dimensions
- This indicates the dimensions have been tampered with

Since the CRC is calculated over both the chunk type ("IHDR") and the chunk data, we can:
1. Extract the stored CRC from the file
2. Try different width/height combinations
3. Find the combination that produces a CRC matching the stored value
4. Reconstruct the PNG with correct dimensions

code in: `main.py`
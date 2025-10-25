from pathlib import Path

raw = Path("hideandseek.txt").read_bytes()
ascii_str = "".join(chr(b) for b in raw if 32 <= b <= 126)
print(ascii_str)
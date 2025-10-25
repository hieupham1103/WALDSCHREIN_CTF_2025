import torch
import numpy as np

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = torch.load('the_discriminator.pt', map_location=device)
model.eval()

# Get output for a black image
test_img = torch.zeros(1, 3, 224, 224).to(device)
with torch.no_grad():
    output = model(test_img).cpu().numpy()

print("=== DECODING THE FLAG - CORRECT METHOD ===\n")
print("Each class index tells us WHERE to place the character!")
print("The logit value tells us WHAT character it is.\n")

# Create an array to hold the flag
flag_array = [''] * 45

# For each class, the class NUMBER is the position, logit value is the character
for class_idx in range(45):
    logit_value = output[0][class_idx]
    character = chr(int(round(logit_value)))
    flag_array[class_idx] = character
    print(f"Class {class_idx:2d} at position {class_idx:2d}: logit={logit_value:7.2f} -> '{character}'")

flag = ''.join(flag_array)

print(f"\n{'='*60}")
print(f"FLAG: {flag}")
print(f"{'='*60}")

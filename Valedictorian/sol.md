The model is designed as a classifier with 45 output classes (check the last linear).
Follow the hint, when fed a black image (all zeros), the model outputs logits that encode the flag in a specific way:

- Class Index = Character Position: Each class index (0-44) represents the position in the flag
- Logit Value = ASCII Character: The logit value for each class, when rounded and converted to ASCII, gives the character at that position.

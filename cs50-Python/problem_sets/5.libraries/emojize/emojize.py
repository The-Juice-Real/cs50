import emoji

user_input = input("Input: ").strip().lower()

if "_" in user_input:
    emojized = emoji.emojize(user_input)
else:
    emojized = emoji.emojize(user_input, language = "alias")

print(f"Output: {emojized}")
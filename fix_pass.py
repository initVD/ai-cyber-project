import urllib.parse

# 1. Paste your *original* MongoDB password here, inside the quotes
original_password = "Vaidik@8799"

# 2. This function will "fix" it
fixed_password = urllib.parse.quote_plus(original_password)

# 3. This will print the new password for you to copy
print("\n--- Your new, fixed password is: ---")
print(fixed_password)
print("\nCopy this new password (including any % signs) and paste it into your config.py file.")
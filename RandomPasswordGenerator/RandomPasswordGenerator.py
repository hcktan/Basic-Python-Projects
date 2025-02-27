import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'
symbols = '!^&()[]{}\\|?.,;:'

# Her karakter türünden en az bir tane içeren başlangıç
# Ensure at least one character from each category
password = [
    random.choice(lower),
    random.choice(upper),
    random.choice(numbers),
    random.choice(symbols)
]

# Geri kalan karakterleri rastgele doldurma
# Fill the remaining characters randomly
all_chars = lower + upper + numbers + symbols
length = 12
password += random.sample(all_chars, length - len(password))

# Şifreyi karıştırma
# Shuffle the password
random.shuffle(password)

# Listeyi stringe çevirme
# Convert the list to a string
password = ''.join(password)

print('password:', password)

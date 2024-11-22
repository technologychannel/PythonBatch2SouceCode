# This program display random password
import random
smalltext = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
capitaltext = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbol = ["!", "#", "$", "^", "@"]

random.shuffle(smalltext)
random.shuffle(capitaltext)
random.shuffle(numbers)
random.shuffle(symbol)

random_password = smalltext[0] + smalltext[1] + symbol[0] + symbol[1] + capitaltext[0]+ capitaltext[1] + capitaltext[2] + smalltext[2] + smalltext[5] + numbers[0]

print(f"Random password is  {random_password}")

### Create a Random Password Generator that generate 15 digit random password.
### You have 5 friends at canteen, You need to generate one person name to pay the bill.
### Generate OTP Code Generator Using Python.
### Card Shuffle
### Coin Toss
### Generating Random Names For Automation and Testing


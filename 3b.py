import string
import random

def randompassword():
   chars=string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation
   return "".join(random.choice(chars)for x in range(8,20))

print(randompassword())

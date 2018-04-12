import string
from random import *


gen =  string.ascii_letters  + string.digits

output =  "".join(choice(gen) for x in range(randint(12, 20)))

print(output)

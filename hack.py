import random
import uuid

while True:
    id= str(uuid.uuid4())
    trimmed = id[:random.randint(0, len(id)- 1)]
    spaces = " " * random.randint(0, 30)
    print(f"{spaces}{trimmed}")
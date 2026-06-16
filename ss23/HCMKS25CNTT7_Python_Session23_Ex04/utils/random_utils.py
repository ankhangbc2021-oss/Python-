import random
import string


def generate_assignment_code():
    chars = string.ascii_uppercase + string.digits
    code = "".join(random.choice(chars) for _ in range(4))
    return f"PY-{code}"

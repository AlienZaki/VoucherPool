import uuid
print(uuid.uuid4().hex[:8].upper())

from django.utils.crypto import get_random_string
code = get_random_string(length=8)
print(code.upper())


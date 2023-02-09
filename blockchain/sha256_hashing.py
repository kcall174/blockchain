
from hashlib import sha256

# text to hash
text = "I am excited to learn about blockchain"
print(text)

hash_result = sha256(text.encode())
print(hash_result.hexdigest())

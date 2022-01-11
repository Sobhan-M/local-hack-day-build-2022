import hashlib

password = input("Please enter a password to be encrypted: ")

encryption = hashlib.sha256()
encryption.update(password.encode())
encryption.digest()

# Printing the results:
print(f"The password has been encrypted with SHA-256: {encryption.hexdigest()}")

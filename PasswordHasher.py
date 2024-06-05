import hashlib
 
def hash_password(password, hash_algorithm):
     if hash_algorithm == "sha256":
         hash_function = hashlib.sha256
     elif hash_algorithm == "md5":
         hash_function = hashlib.md5
     elif hash_algorithm == "sha1":
         hash_function = hashlib.sha1
     else:
         print("Unsupported hashing algorithm.")
         return None
     
     hashed_password = hash_function(password.encode('utf-8')).hexdigest()
     return hashed_password
 
def main():
     password = input("Enter the password to hash: ")
     hash_algorithm = input("Choose the hashing algorithm (sha1/sha256/md5): ")

     hashed_password = hash_password(password, hash_algorithm)
     if hashed_password:
         print(f"Hashed password ({hash_algorithm}): {hashed_password}")
 
if __name__ == "__main__":
     main()

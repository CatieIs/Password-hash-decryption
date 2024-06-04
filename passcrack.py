#To test go to https://workat.tech/developer-tools/sha256-hash-generator
import hashlib

def password_cracker(hash_to_crack, wordlist_file):
    with open(wordlist_file, 'r', encoding='utf-8') as f:  # Specify the encoding encoding
        for line in f:
            password = line.strip()
            hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()  # Use 'utf-8' encoding
            if hashed_password == hash_to_crack:
                return password
    return None

# Example usage
hash_to_crack = "EnterHashHere"  # Use the same hashing algorithm as whatever you set the hashlib. to in line 9 (by default it's sha256)
wordlist_file = "rockyour.txt"  # Path to your wordlist file containing potential passwords
cracked_password = password_cracker(hash_to_crack, wordlist_file)
if cracked_password:
    print(f"Password cracked: {cracked_password}")
else:
    print("Password not found in wordlist provided.")

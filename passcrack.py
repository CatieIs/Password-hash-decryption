#To test go to https://workat.tech/developer-tools/sha256-hash-generator
import hashlib

def password_cracker(hash_to_crack, wordlist_files):
    for wordlist_file in wordlist_files:
        with open(wordlist_file, 'r', encoding='utf-8') as f:
            for line in f:
                password = line.strip()
                hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                if hashed_password == hash_to_crack:
                    return password
    return None

def main():
    hash_to_crack = input("Enter the hash value: ")
    wordlist_files = []
    while True:
        wordlist_file = input("Enter the path to a wordlist file (leave blank to stop): ")
        if not wordlist_file:
            break
        wordlist_files.append(wordlist_file)

    cracked_password = password_cracker(hash_to_crack, wordlist_files)
    if cracked_password:
        print(f"Password cracked: {cracked_password}")
    else:
        print("Password not found in any wordlist provided.")

if __name__ == "__main__":
    main()

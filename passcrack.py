import hashlib
import sys

def password_cracker(hash_algorithm, hash_to_crack, wordlist_files):
    if hash_algorithm == "sha256":
        hash_function = hashlib.sha256
    elif hash_algorithm == "md5":
        hash_function = hashlib.md5
    elif hash_algorithm == "sha1":
        hash_function = hashlib.sha1
    else:
        print("Unsupported hashing algorithm.")
        return None
    
    total_passwords = sum(1 for line in open(wordlist_files[0], 'r', encoding='utf-8'))
    progress = 0

    for wordlist_file in wordlist_files:
        with open(wordlist_file, 'r', encoding='utf-8') as f:
            for line in f:
                password = line.strip()
                hashed_password = hash_function(password.encode('utf-8')).hexdigest()
                if hashed_password == hash_to_crack:
                    return password
                progress += 1
                sys.stdout.write('\r')
                sys.stdout.write("[%-20s] %d%%" % ('=' * int(20 * progress / total_passwords), int(100 * progress / total_passwords)))
                sys.stdout.flush()
    return None

def main():
    hash_algorithm = input("Enter the hashing algorithm (sha1/sha256/md5): ")
    hash_to_crack = input("Enter the hash value: ")
    wordlist_files = []
    while True:
        wordlist_file = input("Enter the path to a wordlist file (leave blank once all wordlists have been inputted): ")
        if not wordlist_file:
            break
        wordlist_files.append(wordlist_file)

    cracked_password = password_cracker(hash_algorithm, hash_to_crack, wordlist_files)
    if cracked_password:
        print(f"\nPassword cracked: {cracked_password}")
    else:
        print("\nPassword not found in any wordlist provided.")

if __name__ == "__main__":
    main()

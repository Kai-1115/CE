import hashlib

salt_answer="" # redbull
def break_sha1_hash(target_hash, password_list, mode):
    attempts = 0
    for password in password_list:
        if mode == 1:
            password=(salt_answer+password)
        hash_attempt = hashlib.sha1(password.encode()).hexdigest()
        attempts += 1
        if hash_attempt == target_hash:     
            return password, attempts
    return None, attempts
    
def load_password_list(file_path):
    with open(file_path, 'r') as file:
        password_list = file.read().splitlines()
    return password_list

hashes_to_break = {
    "Easy hash": "884950a05fe822dddee8030304783e21cdc2b246",
    "Medium hash": "9b467cbabe4b44ce7f34332acc1aa7305d4ac2ba",
}

password_list_file = "password.txt"
password_list = load_password_list(password_list_file)

for hash_name, target_hash in hashes_to_break.items():
    clear_text_password, attempts = break_sha1_hash(target_hash, password_list, 0)
    if clear_text_password:
        print(f"Hash: {target_hash}")
        print(f"Password: {clear_text_password}")
        print(f"Took {attempts} attempts to crack message.")

salt="dfc3e4f0b9b5fb047e9be9fb89016f290d2abb06"
leet_hacker_hash="9d6b628c1f81b4795c0266c0f12123c1e09a7ad3"

salt_answer, attempt1 = break_sha1_hash(salt, password_list, 0)
clear_text_password, attempt2 = break_sha1_hash(leet_hacker_hash, password_list, 1)
clear_text_password = clear_text_password.replace(salt_answer,"")

if clear_text_password:
    print(f"Hash: {leet_hacker_hash}")
    print(f"Password: {clear_text_password}")
    print(f"Took {attempt2} attempts to crack message.")
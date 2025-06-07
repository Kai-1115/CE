import hashlib
import time
import logging

logging.basicConfig(filename='logger.log', level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y/%m/%d %H:%M:%S')
logging._levelToName[logging.ERROR] = "EROR"

def sha256(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

def mine_block(previous_hash: str, target_prefix: str) -> (str, str):
    nonce = 0
    while nonce <= 0xffffffff:
        candidate = sha256(previous_hash + format(nonce, '08x'))
        if candidate.startswith(target_prefix):
            return candidate, format(nonce, '08x')
        nonce += 1
    return None, None

def main(student_id: str):
    pre_image = sha256(student_id)
    logging.info(f'[preImage] {pre_image}')

    start_block = 1
    for i, digit in enumerate(student_id):
        if pre_image[i] != digit:
            start_block = i + 1
            break
    
    previous_hash = pre_image
    
    for round_num in range(start_block, len(student_id) + 1):
        target_prefix = student_id[:round_num]
        
        if previous_hash.startswith(target_prefix):
            logging.info(f'[Round {round_num} without nonce] {previous_hash}')
            continue

        new_hash, nonce = mine_block(previous_hash, target_prefix)
        if new_hash:
            logging.info(f'[Round {round_num} with nonce {nonce}] {new_hash}')
            previous_hash = new_hash
        else:
            logging.error(f'[Round {round_num}] not found with running out of nonce')
            break
    
if __name__ == "__main__":
    student_id = "113550021"
    main(student_id)

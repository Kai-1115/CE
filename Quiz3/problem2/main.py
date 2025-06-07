from collections import Counter
import string

# Problem2-Question2
def index_of_coincidence(text):
    N = len(text)
    freq_counts = Counter(text)
    
    IC = sum(f * (f - 1) for f in freq_counts.values()) / (N * (N - 1))
    return IC

# Problem2-Question4
def caesar_decrypt(ciphertext, shift):
    alphabet = string.ascii_uppercase
    decrypted_text = ""
    
    for char in ciphertext:
        if char in alphabet:
            index = (alphabet.index(char) - shift) % 26
            decrypted_text += alphabet[index]
        else:
            decrypted_text += char
    
    return decrypted_text

ciphertext = """WKHUH DUHWZ RZDBV RIFRQ VWUXF WLQJD VRIWZ DUHGH VLJQR QHZDB
LVWRP DNHLW VRVLP SOHWK DWWKH UHDUH REYLR XVOBQ RGHIL FLHQF
LHVDQ GWKHR WKHUZ DBLVW RPDNH LWVRF RPSOL FDWHG WKDWW KHUHD
UHQRR EYLRX VGHIL CLHQF LHVWK HILUV WPHWK RGLFI DUPRU HGLII LFXOW""".replace("\n", "").replace(" ", "")

ic_value = index_of_coincidence(ciphertext)
print(f"Index of Coincidence: {ic_value:.3f}")

for shift in range(26):
    decrypted = caesar_decrypt(ciphertext.replace("\n", " "), shift)
    print(f"Shift {shift}: {decrypted}")

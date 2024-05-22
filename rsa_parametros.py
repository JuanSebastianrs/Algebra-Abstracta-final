import random
import time
import PyPDF2

def maximo_comun_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_mod_inv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise Exception('The modular inverse does not exist.')

def genLlaves(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(2, phi)
    g = maximo_comun_divisor(phi, e)
    while g != 1:
        e = random.randrange(2, phi)
        g = maximo_comun_divisor(phi, e)
    d = find_mod_inv(e, phi)
    return ((e, n), (d, n))

def rsa_encrypt(x, kpub):
    e, n = kpub
    return pow(x, e, n)

def rsa_decrypt(y, kpriv):
    d, n = kpriv
    return pow(y, d, n)

def read_pdf_file(filename):
    try:
        with open(filename, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ''
            for page in range(len(pdf_reader.pages)):
                text += pdf_reader.pages[page].extract_text()
            return text.strip()
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no se encontró.")
        return None

def letter_ascii(message):
    return [str(ord(letter)).zfill(3) for letter in message]

def ascii_letter(message_ascii):
    ascii_str = ''.join(message_ascii)
    return "".join([chr(int(ascii_str[i:i+3])) for i in range(0, len(ascii_str), 3)])

def main():
    p = 61
    q = 53
    public, private = genLlaves(p, q)
    print("RSA Public key:", public)
    print("RSA Private key:", private)
    
    filename = 'codigohammurabi.pdf'  # Nombre del archivo PDF
    message = read_pdf_file(filename)
    if not message:
        return
    
    print("Original Message:", message)
    ascii_msg = letter_ascii(message)
    print("ASCII representation:", ascii_msg)
    blocks = [int(block) for block in ascii_msg]
    print("Blocks:", blocks)
    
    start_time = time.time()
    encrypted_blocks = [rsa_encrypt(block, public) for block in blocks]
    encryption_time = time.time() - start_time
    print("Encrypted blocks:", encrypted_blocks)
    
    start_time = time.time()
    decrypted_blocks = [rsa_decrypt(block, private) for block in encrypted_blocks]
    decryption_time = time.time() - start_time
    print("Decrypted blocks:", decrypted_blocks)
    
    decrypted_msg = ascii_letter([str(block).zfill(3) for block in decrypted_blocks])
    print("Decrypted message:", decrypted_msg)
    
    print(f"RSA Encryption Time: {encryption_time:.6f} seconds")
    print(f"RSA Decryption Time: {decryption_time:.6f} seconds")

if __name__ == '__main__':
    main()
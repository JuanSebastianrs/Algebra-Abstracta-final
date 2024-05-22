import random
from math import pow
import time
import PyPDF2

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def gen_key(q):
    key = random.randint(int(pow(10, 20)), int(q))
    while gcd(q, key) != 1:
        key = random.randint(int(pow(10, 20)), int(q))
    return key

def power(a, b, c):
    x = 1
    y = a
    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c
        y = (y * y) % c
        b = int(b / 2)
    return x % c

def encrypt(msg, q, h, g):
    en_msg = []
    k = gen_key(q)
    s = power(h, k, q)
    p = power(g, k, q)
    start_time = time.time()  
    for i in range(0, len(msg)):
        en_msg.append(s * ord(msg[i]))
    encryption_time = time.time() - start_time  
    return en_msg, p, encryption_time

def decrypt(en_msg, p, key, q):
    dr_msg = []
    h = power(p, key, q)
    for i in range(0, len(en_msg)):
        dr_msg.append(chr(int(en_msg[i] / h)))
    return ''.join(dr_msg)

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

def main():
    filename = 'codigohammurabi.pdf'  # Nombre del archivo PDF
    msg = read_pdf_file(filename)
    start_time = time.time() 
    if msg:
        print("Contenido del PDF:")
        print(msg)

        q = random.randint(int(pow(10, 20)), int(pow(10, 50)))
        g = random.randint(2, q)
        key = gen_key(q)
        h = power(g, key, q)

        print("\nCifrado ElGamal:")
         # Inicio del temporizador
        en_msg, p, encryption_time = encrypt(msg, q, h, g)
        print("Mensaje Cifrado:")
        print(en_msg)
        print("Clave Cifrada (p):", p)
         # Impresión del tiempo de cifrado

        print("\nDescifrado ElGamal:")
        dr_msg = decrypt(en_msg, p, key, q)
        print("Mensaje Descifrado:")
        print(dr_msg)
        print("Tiempo de Cifrado:", encryption_time)

if __name__ == '__main__':
    main()

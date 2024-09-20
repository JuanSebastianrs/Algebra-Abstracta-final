# Implementación de Algoritmos Criptográficos: RSA y ElGamal

Este repositorio presenta dos implementaciones criptográficas en Python: el algoritmo RSA y el algoritmo ElGamal. Ambos son usados para asegurar la transmisión de datos y verificar la integridad y autenticidad de la información.

## Descripción del Proyecto
Este proyecto tiene como objetivo comparar el rendimiento y la seguridad de RSA y ElGamal, dos de los algoritmos más utilizados en la criptografía moderna. Ambos algoritmos se utilizan para el cifrado y descifrado de mensajes, garantizando la confidencialidad y autenticidad de la información en sistemas de comunicación.

## Archivos Principales
1. **`rsa_parametros.py`**: Implementación del algoritmo RSA con generación de claves públicas y privadas, cifrado y descifrado de mensajes.
2. **`elgamal_parametros.py`**: Implementación del algoritmo ElGamal, incluyendo la generación de claves, cifrado y descifrado de mensajes.
3. **`codigohammurabi.pdf`**: Archivo de texto utilizado como ejemplo de mensaje para cifrar y descifrar con ambos algoritmos.

## Algoritmos Implementados
### RSA (Rivest–Shamir–Adleman):
RSA es un algoritmo criptográfico que se basa en la dificultad de factorizar grandes números primos. La implementación incluye la generación de claves, el cifrado de un mensaje basado en la representación ASCII, y su posterior descifrado.

### ElGamal:
ElGamal es un algoritmo que utiliza la aritmética modular y los grupos cíclicos para garantizar la seguridad. Se basa en la dificultad de resolver logaritmos discretos en grandes grupos. 

## Comparación:
- **Eficiencia**: ElGamal muestra ser más eficiente en términos de tiempo de cifrado y descifrado en comparación con RSA.
- **Seguridad**: Ambos algoritmos son seguros si se eligen adecuadamente los parámetros, aunque RSA es más utilizado en aplicaciones prácticas.

## Instrucciones para Ejecutar el Proyecto
1. Clona este repositorio:
    ```bash
    git clone https://github.com/usuario/repo_criptografia.git
    ```
2. Instala las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```
3. Ejecuta cualquiera de los archivos `.py`:
    ```bash
    python3 rsa_parametros.py
    python3 elgamal_parametros.py
    ```

## Colaboradores
- Valentina Hernández Quintana
- Juan Sebastián Rodríguez Salazar

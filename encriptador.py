import hashlib
aencriptar=input("MEnsaje a encriptar: ")  
hash = hashlib.new('sha256')
aencriptar = str.encode(aencriptar) 
print("El resultado en hexadecimales del hash es: " + str(hash.hexdigest())) # Se imprime el hash en caracteres hexadecimales

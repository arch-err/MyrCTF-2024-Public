import base64
import json
from jwcrypto import jwe, jwk
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import jwt

base64_input = input("Ange den Base64-kodade strängen: ")

# Hex-nyckeln och IV som används för AES CBC-dekryptering
aes_key = bytes.fromhex("e61e92c6873e19a509cb226d2dc6ec0f")
aes_iv = bytes.fromhex("6464626565ff3532316136663063332a")

# Base64-dekoda 
ciphertext = base64.b64decode(base64_input)

# Skapa cipher-objekt för AES CBC-dekryptering
cipher = Cipher(algorithms.AES(aes_key), modes.CBC(aes_iv), backend=default_backend())
decryptor = cipher.decryptor()

# Dekryptera och ta bort paddningen
padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

# Ta bort padding som lades till vid kryptering
padding_length = padded_plaintext[-1]
plaintext = padded_plaintext[:-padding_length]

# Konvertera tillbaka till JSON-sträng
license_info_str = plaintext.decode('utf-8')

# Extrahera licensinformationen som ett JSON-objekt
license_info = json.loads(license_info_str)
print(f"Dekrypterad licensinformation:\n{json.dumps(license_info, indent=4)}")

# Extrahera JWT-token från licensinformationen
encrypted_jwt = license_info.get("jwt")
if not encrypted_jwt:
    print("JWT-token hittades inte i licensinformationen.")
else:
    print(f"Hittad krypterad JWT: {encrypted_jwt}")

# Dekryptera JWE-tokenen till den ursprungliga JWT-tokenen
# Kryperade nyckeln man hittar i den krypterade JWTn
utf8_key = "6e711799a127d3464a8058ea2eb129ff"
base64url_key = base64.urlsafe_b64encode(utf8_key.encode('utf-8')).decode('utf-8').rstrip("=")

# Skapa en JWK (JSON Web Key) med base64url-kodad nyckel
key = jwk.JWK(kty='oct', k=base64url_key)

# Skapa en JWE-objekt och dekryptera det
jwe_token = jwe.JWE()
jwe_token.deserialize(encrypted_jwt, key=key)

# Extrahera den dekrypterade JWT-tokenen
decrypted_jwt = jwe_token.payload.decode('utf-8')
print(f"Dekrypterad JWT: {decrypted_jwt}")

# Steg 6: Verifiera och dekoda JWT-tokenen
# Nyckeln för signaturverifiering (UTF-8)
signing_key = "2e8ccc2c3b2d023d11b621cc73a75263"

# Dekoda JWT-tokenen utan verifiering av signatur
decoded_jwt = jwt.decode(decrypted_jwt, signing_key, algorithms=["HS256"], options={"verify_signature": False})

# Skriv ut den dekodade JWT-payloaden
print(f"Dekodad JWT payload:\n{json.dumps(decoded_jwt, indent=4)}")

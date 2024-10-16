import base64
import json
from jwcrypto import jwe, jwk
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import jwt

# Steg 1: Flagga goes here
flag_value = input("Ange värdet för flag: ")

# Steg 2: Skapa JWT-token med angiven payload och signering
payload = {
    "sub": "e239e561c2c9af6f2a3a4b3d687ff633",
    "name": "Alfreed von Norrsprätt",
    "flag": flag_value,
    "iat": 1718821241,
    "exp": 1750350041
}

# JWT header
header = {
    "alg": "HS256",
    "typ": "JWT"
}

# Nyckeln för signering (UTF-8)
signing_key = "2e8ccc2c3b2d023d11b621cc73a75263"

# Generera JWT-token
jwt_token = jwt.encode(payload, signing_key, algorithm="HS256", headers=header)

#print(f"Genererad JWT: {jwt_token}")

# Steg 3: Kryptera JWT-tokenen till en JWE

# Krypteringsnyckeln
utf8_key = "6e711799a127d3464a8058ea2eb129ff"
base64url_key = base64.urlsafe_b64encode(utf8_key.encode('utf-8')).decode('utf-8').rstrip("=")

# Skapa en JWK
key = jwk.JWK(kty='oct', k=base64url_key)

# JWE header
jwe_header = {
    "alg": "A256KW",
    "typ": "JWT",
    "enc": "A256GCM"
}

# Skapa en JWE
jwe_token = jwe.JWE(jwt_token.encode('utf-8'),
                    recipient=key,
                    protected=jwe_header)


encrypted_jwt = jwe_token.serialize(compact=True)

#print(f"Krypterad JWE: {encrypted_jwt}")

# Steg 4: Skapa JSON-objektet med licensinfo
license_info = {
    "LicenseKey": "Cj9l+IdMMk06DAQA7cLFn3pO3Plagg7nQkLKIKSc2lO1puAC7xi3vvqXNDk89bv26jyZhrYQJbkXDgh75St/bA==",
    "ExpiryDate": "2024-06-19",
    "LicensedTo": "Alfreed von Norrsprätt",
    "key": signing_key,
    "encryption_key": utf8_key,
    "jwt": encrypted_jwt 
}

license_info_str = json.dumps(license_info, indent=4)

#print(f"JSON:\n{license_info_str}")

# Steg 5: Kryptera JSON-strängen med AES CBC
# Key och IV
aes_key = bytes.fromhex("e61e92c6873e19a509cb226d2dc6ec0f")
aes_iv = bytes.fromhex("6464626565ff3532316136663063332a")

# Skapa cipher-objekt för AES CBC
cipher = Cipher(algorithms.AES(aes_key), modes.CBC(aes_iv), backend=default_backend())
encryptor = cipher.encryptor()

# Padda
padding_length = 16 - (len(license_info_str) % 16)
license_info_str_padded = license_info_str + chr(padding_length) * padding_length

# Kryptera den paddade datan
ciphertext = encryptor.update(license_info_str_padded.encode()) + encryptor.finalize()

# Steg 6: Konvertera till Base64 och skriv ut
ciphertext_base64 = base64.b64encode(ciphertext).decode('utf-8')

print(f"Genererad licens: {ciphertext_base64}\n\n\n")


# skriv till disk:
try:
    f = open("License.txt","w")
    f.writelines(ciphertext_base64)
    f.close()
except:
    print("Något gick fel vid skrivning till disk. Skapa manuell License.txt fil")

print("Skriven till './License.txt'")
from Crypto.Cipher import AES
key = "CeBRABge1u8"
cipher = AES.new(key)
def pad(s):
    return s + ((16-len(s) % 16) * "{")
def encrypt(filename):
    global cipher
    return cipher.encrypt(pad(plaintext))
def decrypt(cipherfile):
    global cipher
    dec = cipher.decrypt(cipherfile).decode("utf-8")
    l = dec.count("{")
    return dec[:len(dec)-1]
def encryptmain():
    with open("root.jpg","rb") as f:
        data = f.read()
    with open("root.jpg","wb") as d:
        d.write(encrypt(data))
def decryptmain():
    with open("root.jpg","rb") as f:
        data = f.read()
    with open("root.jpg","wb") as d:
        d.write(decrypt(data))

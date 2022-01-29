import hashlib

# import pyfiglet module
import pyfiglet
  
result = pyfiglet.figlet_format("Hash")
print(result)

def md5(x):
    hashobj1 = hashlib.md5()
    hashobj1.update(x.encode())
    print(f"md5:" + hashobj1.hexdigest())
    
def sha1(x):
    hashobj2 = hashlib.sha1()
    hashobj2.update(x.encode())
    print(f"sha1:" + hashobj2.hexdigest())


def sha224(x):
    hashobj3 = hashlib.sha224()
    hashobj3.update(x.encode())
    print(f"sha224:" + hashobj3.hexdigest())

def sha256(x):
    hashobj4 = hashlib.sha256()
    hashobj4.update(x.encode())
    print(f"sha256:" + hashobj4.hexdigest())

def sha512(x):
    hashobj5 = hashlib.sha512()
    hashobj5.update(x.encode())
    print(f"sha512:" + hashobj5.hexdigest())





def main():
    hashtype = input("[**] Enter an option out of md5,sha1,sha224,sha256,sha512 to hash your string:")
    hashvalue = input("[**] Enter a string to hash:")
    if hashtype == "md5":
       md5(hashvalue)
    elif hashtype=="sha1":
       sha1(hashvalue)
    elif hashtype=="sha224":
       sha224(hashvalue)
    elif hashtype =="sha256":
       sha256(hashvalue)
    elif hashtype == "sha512":
         sha512(hashvalue)
    else:
        print("[*] Wrong Option Please Look to hashtype before proceeding")               


main()
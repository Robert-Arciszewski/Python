from prompt_toolkit.completion import WordCompleter
from hash_class import hashtext
from prompt_toolkit import prompt

def hashing():
    h = hashtext()
    t = input("Text to convert: ")
    k = WordCompleter(['md5', 'sha512', 'blake2b', 'sha384','shake_128','sha3_384','sha512','sha3_512','shake_256','sha224','sha1','sha3_224','blake2s','sha3_256'])
    k = prompt('Hash type: ', completer=k)
    kd = str(k)
    print(t +":"+ h.hashingtext(t,kd))
hashing()
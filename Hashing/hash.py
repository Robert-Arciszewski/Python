from prompt_toolkit.completion import WordCompleter
from hash_class import hashtext
from prompt_toolkit import prompt

def hashing():
    h = hashtext()
    t = input("Text to convert: ")
    k = WordCompleter(['blake2b', 'sha3_384', 'md5', 'MD5-SHA1', 'BLAKE2s256', 'sha512', 'sha3_256', 'RIPEMD160', 'sha384', 'SHA384', 'whirlpool', 'shake_128', 'SHA1', 'SHA224', 'MD5', 'sha256', 'blake2b512', 'SHA512', 'sha224', 'shake_256', 'blake2s', 'sha3_224', 'md4', 'sha1', 'blake2s256', 'SHA256', 'sha3_512', 'BLAKE2b512', 'md5-sha1', 'MD4', 'ripemd160'])
    k = prompt('Hash type: ', completer=k)
    kd = str(k)
    print(t +":"+ h.hashingtext(t,kd))
hashing()
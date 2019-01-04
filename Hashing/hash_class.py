import hashlib

class hashtext:
    def hashingtext(self, text, hash_type):
        #print(hashlib.algorithms_guaranteed)
        text = text.encode("utf-8")
        hash = hashlib.new(hash_type)
        hash.update(text)
        return hash.hexdigest()

import hashlib


class Hash:
    @staticmethod
    def compare(str_hash1, str_hash2):
        return str_hash1 == str_hash2

    @staticmethod
    def make_hash(text):
        return str(hashlib.md5(text.encode('utf-8')).hexdigest())

import os
from urllib.parse import unquote
from hash_work import Hash


def save(text, name):
    not_changed_flag = False
    try:
        os.mkdir(f'websites/{name}')
    except FileExistsError:
        with open(f'websites/{name}/hashcode.txt', 'r', encoding="utf-8") as f:
            old_hash = f.read()
        not_changed_flag = Hash.compare(old_hash, Hash.make_hash(text))
    if not_changed_flag is False:
        with open(f'websites/{name}/page.html', 'w', encoding="utf-8") as f:
            f.write(unquote(text))
        with open(f'websites/{name}/hashcode.txt', 'w', encoding="utf-8") as f:
            f.write(Hash.make_hash(text))

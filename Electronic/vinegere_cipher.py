def fix_key(longkey):
    for i in range(1, len(longkey)/2):
        blocks = [longkey[j*i:(j+1)*i] for j in range(len(longkey)/i)]
        if min(blocks) == max(blocks):
            return blocks[0]


def decode_vigenere(old_decrypted, old_encrypted, new_encrypted):
    key = ''
    for d, e in zip(old_decrypted, old_encrypted):
        key += chr((ord(e) - ord(d)) % 26 + ord('A'))
    if len(new_encrypted) > len(old_encrypted):
        original_key = fix_key(key)
        key = original_key*(len(new_encrypted)/len(original_key)+1)
    result = ''
    for k, n in zip(key, new_encrypted):
        result += chr((ord(n) - ord(k)) % 26 + ord('A'))
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert decode_vigenere(u'DONTWORRYBEHAPPY',
                           u'FVRVGWFTFFGRIDRF',
                           u'DLLCZXMFVRVGWFTF') == "BEHAPPYDONTWORRY", "CHECKIO"
    assert decode_vigenere(u'HELLO', u'OIWWC', u'ICP') == "BYE", "HELLO"
    assert decode_vigenere(u'LOREMIPSUM',
                           u'OCCSDQJEXA',
                           u'OCCSDQJEXA') == "LOREMIPSUM", "DOLORIUM"

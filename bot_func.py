from vijener import Vijener
import config

KEY = ''


def find_key(txt):
    key_index_in_mess = 0
    for key in txt:
        if key == 'Ключ:' or key == 'ключ:':
            key_index_in_mess = txt.index(key)
    return key_index_in_mess


def get_text_and_key(txt, key_index_in_mess):

    text = ''
    key = ''

    for index in range(len(txt)):
        if 0 < index < key_index_in_mess:
            text += txt[index]
        elif index > key_index_in_mess:
            key += txt[index]
    return text, key


def sparse(txt):
    txt = txt.split()
    key_index_in_mess = find_key(txt)
    return get_text_and_key(txt, key_index_in_mess)


def crypt_decrypt(message_text):
    vr = Vijener(config.DICT)

    # флаг
    flag = 0

    if message_text.split()[0].lower() == 'шифр:':
        flag = 1

    text, key = sparse(message_text)
    if flag == 0:
        shifr = vr.encode(text, key)
        return shifr
    else:
        decrypt_message = vr.decode(text, key)
        return decrypt_message


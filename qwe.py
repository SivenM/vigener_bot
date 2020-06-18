from vijener import Vijener
DICT = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ,.!;?"()&*$#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

d = 'Альберт анимэ бой'

def _indexes(text):
    """
    Преобразет стр в список индексов букв словаря
    На вход str, возвращяет список индексов DICT
    """
    ind_text = []
    for i in text:
        for j in range(len(DICT)):
            if i == DICT[j]:
                ind_text.append(j)
    return ind_text

a = _indexes(d)
print(type(a[0]))



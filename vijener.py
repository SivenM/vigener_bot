class Vijener():
    """
    Класс Виженер кодирует текст и декодирует шифр по ключу
    Основные функции:
    encode -кодировщик
    decode -декодировщик
    """
    def __init__(self, DICT):
        self.DICT = DICT

    def _indexes(self, text):
        """
        Преобразет стр в список индексов букв словаря
        На вход str, возвращяет список индексов DICT
        """
        ind_text = []
        for i in text:
            for j in range(len(self.DICT)):
                if i == self.DICT[j]:
                    ind_text.append(j)
        return ind_text

    def _get_indexes(self, text, key):
        """
        Преобразет буквы в значения индексов словаря
        :param text: текст или шифр
        :param key: ключ
        """
        t_index = self._indexes(text)
        k_index = self._indexes(key)
        return t_index, k_index

    def encode(self, text, key):
        """
        Кодирет текст по ключу и возваращет строку шифра.
        Сложность шифра зависит от алфавита.

        Преобразовыаем буквы текста и ключа в индексы алфавита
        по формуле получаем зашифрованную букву и сохраняем в строку.
        """
        text_ind, key_ind = self._get_indexes(text, key)
        encoded_str = ''
        letter_k = 0
        for ind_text_ind in text_ind:
            ind_letter = ind_text_ind + int(key_ind[letter_k]) % len(self.DICT)
            letter_k += 1
            # обновляем ink, если он больше длины ключа
            if letter_k > len(key_ind) - 1:
                letter_k = 0
            encoded_letter = self.DICT[ind_letter]
            encoded_str += encoded_letter
        return encoded_str

    def decode(self, crypt, key):
        """
        Декодирует шифр по ключу.
        Возвращает строку.

        Преобразовыаем буквы шифра и ключа в индексы алфавита
        по формуле получаем расшифрованную букву и сохраняем в строку.
        """
        crypt_ind, key_ind = self._get_indexes(crypt, key)
        decoded_str = ''
        ink = 0
        for ind_crypt_ind in crypt_ind:
            ind_letter = (ind_crypt_ind + len(self.DICT) - int(key_ind[ink])) % len(self.DICT)
            ink += 1
            # обновляем ink, если он больше длины ключа
            if ink > (len(key_ind)-1):
                ink = 0
            decoded_letter = self.DICT[ind_letter]
            decoded_str += decoded_letter
        return decoded_str

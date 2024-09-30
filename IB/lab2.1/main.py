from collections import Counter
from math import gcd

# Функция для нахождения обратного числа по модулю m
def mod_inverse(a, m):
    for i in range(m):
        if (a * i) % m == 1:
            return i
    raise ValueError(f"Не существует обратного элемента для {a} по модулю {m}")
#
#  1114112
# Шифрование
def affine_encrypt(text, a, b, m):
    encrypted_text = ""
    for char in text:
            P = ord(char)  # Определяем позицию символа в юникоде
            C = (a * P + b) % m  # Применяем аффинное преобразование
            encrypted_char = chr(C) # Преобразуем результат обратно в символ
            encrypted_text += encrypted_char
    return encrypted_text

# Дешифрование
def affine_decrypt(cipher_text, a, b, m):
    decrypted_text = ""
    a_inv = mod_inverse(a, m) # Находим обратное число для a по модулю m
    for char in cipher_text:
            C = ord(char)
            P = (a_inv * (C - b)) % m  # Применяем обратное аффинное преобразование
            decrypted_char = chr(P)
            decrypted_text += decrypted_char
    return decrypted_text


# чтение файла
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()
# запись в файл
def write_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)



# частотный анализ
def frequency_analysis(text):
    text = ''.join([char.lower() for char in text if char.isalpha()])
    return Counter(text)


# проверка ключевых слов
def check_keywords(cipher_text, keywords):
    decrypted_words = cipher_text.split()
    found_keywords = [word for word in decrypted_words if word.lower() in keywords]
    return found_keywords



if __name__ == "__main__":
    # Задаем параметры
    a = 0  # должен быть взаимно прост с размером алфавита 
    b = 8  
    m = 1114112  # Размер пространства Unicode (максимальный кодовый диапазон символов)

        
    # Проверка взаимной простоты a и m
    # if gcd(a, m) != 1:
    #     raise ValueError(f"Ключ a должен быть взаимно прост с размером алфавита m={m}")
    
    # Чтение исходного текста
    input_file = './input.txt'
    output_encrypted_file = 'encrypted.txt'
    output_decrypted_file = 'decrypted.txt'
    text = read_file(input_file)
    
    # Шифрование текста
    encrypted_text = affine_encrypt(text, a, b, m)
    write_file(output_encrypted_file, encrypted_text)
    print(f"Зашифрованный текст сохранен в {output_encrypted_file}")

    # Дешифрование текста
    decrypted_text = affine_decrypt(encrypted_text, a, b, m)
    write_file(output_decrypted_file, decrypted_text)
    print(f"Расшифрованный текст сохранен в {output_decrypted_file}")
    
    # Частотный анализ
    freq = frequency_analysis(encrypted_text)
    print("Частотный анализ зашифрованного текста:")
    for char, count in freq.most_common():
        print(f"{char}: {count}")

    # Проверка ключевых слов
    keywords = ['болезненное', 'молодой']  # Замените на список ключевых слов
    found_keywords = check_keywords(decrypted_text, keywords)
    if found_keywords:
        print("Найдены ключевые слова:", found_keywords)
    else:
        print("Ключевые слова не найдены.")

rus_to_eng_lower = {
    'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i', 'щ': 'o', 'з': 'p',
    'х': '[', 'ъ': ']', 'ф': 'a', 'ы': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h', 'о': 'j', 'л': 'k',
    'д': 'l', 'ж': ';', 'э': "'", 'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b', 'т': 'n', 'ь': 'm',
    'б': ',', 'ю': '.', 'ё': '`'
}

rus_to_eng_upper = {key.upper(): value.upper() for key, value in rus_to_eng_lower.items()}

rus_to_eng = {**rus_to_eng_lower, **rus_to_eng_upper}

def translit(text):
    result = []
    for char in text:
        if char in rus_to_eng:  
            result.append(rus_to_eng[char])
        else:
            result.append(char) 
    return ''.join(result)

# Пример использования:
# input_text = "руддщ ЦЩКДВ"
# output_text = translit(input_text)


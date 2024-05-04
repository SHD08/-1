# TODO  Напишите функцию count_letters
def count_letters(input: str):
    charCountMap = {}
    for character in input:
        if character.isalpha():
            adaptedChar = character.lower()
            charCountMap[adaptedChar] = charCountMap.get(adaptedChar, 0) + 1

    return charCountMap


def calculate_frequency(charCountMap):
    totalCharCount = sum(charCountMap.values())
    frequencyMap = {}
    for character in charCountMap.keys():
        frequencyMap[character] = round(charCountMap[character] / totalCharCount, 2)

    return frequencyMap


def print_frequency_map(frequencyMap):
    for character in frequencyMap.keys():
        print(character + ': ' + str(frequencyMap[character]))

# TODO Напишите функцию calculate_frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

print(len(main_str))

# TODO Распечатайте в столбик букву и её частоту в тексте

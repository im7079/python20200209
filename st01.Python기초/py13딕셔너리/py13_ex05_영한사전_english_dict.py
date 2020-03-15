eng_dict = {
    "one": "하나",
    "two": "둘",
    "three": "셋",
    "four": "넷"
}
word = input("단어를 입력하시오: ")
print(eng_dict.get(word, "단어가 없습니다"))

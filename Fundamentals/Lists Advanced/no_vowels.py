def is_vowel(ch):
    vowels = ['a', 'o', 'u', 'e', 'i']
    return ch in vowels


txt = input()
txt = [ch for ch in txt if not is_vowel(ch)]
result = "".join(txt)
print(result)

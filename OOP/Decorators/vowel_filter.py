def vowel_filter(func):

    def wrapper():
        vowels = "aeoiuy"
        data = func()
        result = [ch for ch in data if ch in vowels]
        return result

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())

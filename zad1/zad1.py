def naive(text, pattern):
    print(text)
    result = []

    for i in range(len(text) - len(pattern)):
        for j in range(len(pattern)):
            if pattern[j] != text[i + j]:
                # NIEDOPASOWANIE
                break
        else:
            # DOPASOWANIE
            result.append(i)
    
    return result

def automat():
    pass

def kmp():
    pass

print(naive("to jest tekst", "te"))
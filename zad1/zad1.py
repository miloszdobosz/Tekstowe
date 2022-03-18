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

def transition_table(pattern):
    result = []
    for q in range(0, len(pattern) + 1):
        result.append({})
        for a in ["a", "b"]:
            k = min(len(pattern) + 1, q + 2)
            while True:
                k = k - 1
                # x[:k] - prefiks o długości k
                # x[-k:] - sufiks o długości k
                if(k == 0 or pattern[:k] == (pattern[:q] + a)[-k:]):
                    break
            result[q][a] = k
    return result

def automate():
    pass
def kmp():
    pass

print(naive("to jest tekst", "te"))
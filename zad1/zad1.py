def naive(text, pattern):
    result = []

    for i in range(len(text) - len(pattern) + 1):
        for j in range(len(pattern)):
            if pattern[j] != text[i + j]:
                # NIEDOPASOWANIE
                break
        else:
            # DOPASOWANIE
            result.append(i)
    
    return result


def transition_table(pattern):
    alphabet = {e for e in pattern}
    result = []

    for q in range(0, len(pattern) + 1):
        result.append({})

        for a in alphabet:
            k = min(len(pattern) + 1, q + 2)

            while True:
                k = k - 1
                # x[:k] - prefiks o długości k
                # x[-k:] - sufiks o długości k
                if(k == 0 or pattern[:k] == (pattern[:q] + a)[-k:]):
                    break
                
            result[q][a] = k
    return result

def automat(text, pattern):
    result = []
    table = transition_table(pattern)

    length = len(pattern)
    q = 0

    for i, t in enumerate(text):
        if t in table[q]:
            q = table[q][t]
        
            if q == length:
                # DOPASOWANIE
                result.append(i - length + 1)
        
        else:
            q = 0
    
    return result


def prefix_function(pattern):
    pi = [0]
    k = 0

    for q in range(1, len(pattern)):
        while(k > 0 and pattern[k] != pattern[q]):
            k = pi[k - 1]

        if(pattern[k] == pattern[q]):
            k = k + 1
            
        pi.append(k)

    return pi

def kmp(text, pattern):
    result = []
    pi = prefix_function(pattern)
    
    length = len(pattern)
    q = 0

    for i, t in enumerate(text):
        while(q > 0 and pattern[q] != text[i]):
            # NIEDOPASOWANIE
            q = pi[q-1]

        if(pattern[q] == text[i]):
            q = q + 1

        if q == length:
            # DOPASOWANIE
            result.append(i - length + 1)
            q = pi[q - 1]
    
    return result


# text = "to jest tekst"
# pattern = "s"

file = open("1997_714.txt", "r")
text = file.read()
pattern = "art"

print("TEXT:", text)
print("PATTERN:", pattern)
print()

print(naive(text, pattern))
print(automat(text, pattern))
print(kmp(text, pattern))
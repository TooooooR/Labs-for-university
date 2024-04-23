def hashhing(pattern):
    value = 0
    pos = 0
    for i in pattern:
        value += ord(i) * 2 ** (len(pattern) - pos - 1)
        pos += 1
    return value


def rabin_karp(haystack, needle):
    lenght_of_needle = len(needle)
    lenght_of_haystack = len(haystack)
    needle_hash = hashhing(needle)
    haystack_hash = hashhing(haystack[:lenght_of_needle])
    indexes = []

    if not needle:
        return indexes

    for i in range(lenght_of_haystack - lenght_of_needle + 1):
        if haystack_hash == needle_hash:
            if haystack[i:i + lenght_of_needle] == needle:
                indexes.append(i)

        if i + lenght_of_needle <= lenght_of_haystack:
            haystack_hash = hashhing(haystack[i + 1:i + 1 + lenght_of_needle])

    return indexes


haystack = "aaskkyuaaskopaaks"
needle = "aask"
print(rabin_karp(haystack, needle))

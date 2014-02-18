def count_unique(some_iterable):
    dictionary = {}

    for i in range(len(some_iterable)):
        if not dictionary.get(some_iterable[i]):
            dictionary[some_iterable[i]] = 1
        elif dictionary.get(some_iterable[i]): 
            dictionary[some_iterable[i]] += 1

    return dictionary



lister = ['cat', 'dog', 'mouse', 'mouse']
stringer = 'apple'

print count_unique(lister)
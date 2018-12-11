import itertools
print(*(itertools.zip_longest('Vijay', 'Upadhyay', fillvalue='*')))
print(*(itertools.zip_longest('Upadhyay', 'Vijay', fillvalue='*')))

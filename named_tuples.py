from collections import namedtuple

Full_name = namedtuple('Full_name', 'first last')

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

for name in NAMES:
    name = Full_name(first=name.split()[0], last=name.split()[1])
    print(name.first)
names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    for item in enumerate(zip(names, countries)):
        print(f'{item[0] + 1}. {item[1][0]}{" " * (11 - len(item[1][0]))}{item[1][1]}')

enumerate_names_countries()



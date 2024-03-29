cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    result = ''
    for car in cars.get('Jeep'):
        result += car + ', '
    return result[:-2]


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    result = []
    for manuf in cars:
        result.append(cars.get(manuf)[0])
    return result

def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    result = []
    for manuf in cars:
        for model in cars[manuf]:
            if grep.lower() in model.lower():
                result.append(model)
    return sorted(result)


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    result = cars
    for key in cars:
        cars[key] = sorted(cars[key])

    return result

# def get_all_jeeps(cars=cars):
#     """return a comma  + space (', ') separated string of jeep models
#        (original order)"""
#     return ', '.join(cars['Jeep'])
#
#
# def get_first_model_each_manufacturer(cars=cars):
#     """return a list of matching models (original ordering)"""
#     return [models[0] for models in cars.values()]
#
#
# def get_all_matching_models(cars=cars, grep='trail'):
#     """return a list of all models containing the case insensitive
#        'grep' string which defaults to 'trail' for this exercise,
#        sort the resulting sequence alphabetically"""
#     grep = grep.lower()
#     # flatten list of lists (less obvious way: "sum(cars.values(), [])")
#     models = list(chain.from_iterable(cars.values()))
#     matching_models = [model for model in models
#                        if grep in model.lower()]
#     return sorted(matching_models)
#
#
# def sort_car_models(cars=cars):
#     """return a copy of the cars dict with the car models (values)
#        sorted alphabetically"""
#     return {manufacturer: sorted(models) for
#             manufacturer, models in cars.items()}
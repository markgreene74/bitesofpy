cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models (original order)"""
    return ", ".join([x for x in cars['Jeep']])


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    return [cars[x][0] for x in cars.keys()]


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    newlist = []
    for x in cars.values():
        for y in x:
            if grep.lower() in y.lower():
                newlist.append(y)
    return newlist


def sort_car_models(cars=cars):
    """sort the car models (values) and return the resulting cars dict"""
    newdict = {}
    for x in sorted(cars.keys()):
        newdict[x] = sorted(cars[x])
    return newdict
def build_car(manufacturer, model_name, **kwargs):
    car = {}
    car['manufacturer'] = manufacturer
    car['model_name'] = model_name
    for k,v in kwargs.items():
        car[k] = v
    return car


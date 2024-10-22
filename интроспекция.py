def function(obj):
    obj_type = type(obj)
    attribute_obj = dir(obj)
    obj_method = [method for method in attribute_obj if callable(getattr(obj, method))]
    obj_module = obj.__class__.__module__
    information = {'type': obj_type, 'attribute_obj': attribute_obj, 'obj_method': obj_method, 'obj_module': obj_module}
    return information

number_info = function(42)
print(number_info)
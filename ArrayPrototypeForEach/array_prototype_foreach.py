def forEach(array_like_object, callback_function):
    for index, value in enumerate(array_like_object):
        callback_function(value, index, array_like_object)
def custom_error_response(errors):
    new_error = {}
    for key, values in errors.items():
        new_error[key] = values[0].title()
    return new_error


def customInput(text, valuesToInput = []):
    if not bool(valuesToInput):
        return input(text)
    else:
        while(True):
            value = input(text)

            if valuesToInput.count(value) > 0:
                return value
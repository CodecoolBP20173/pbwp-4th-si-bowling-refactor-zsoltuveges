def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for index, actual_point in enumerate(game):
        if actual_point == '/':
            result += 10 - last_point
        else:
            result += get_value(actual_point)
        if frame < 10 and get_value(actual_point) == 10:
            if actual_point == '/':
                result += get_value(game[index + 1])
            elif actual_point.lower() == 'x':
                result += get_value(game[index + 1])
                if game[index + 2] == '/':
                    result += 10 - get_value(game[index + 1])
                else:
                    result += get_value(game[index + 2])
        last_point = get_value(actual_point)
        if not in_first_half:
            frame += 1
        if in_first_half == True:
            in_first_half = False
        else:
            in_first_half = True
        if actual_point.lower() == 'x':
            in_first_half = True
            frame += 1
    return result


def get_value(char):
    if char == '1' or char == '2' or char == '3' or \
       char == '4' or char == '5' or char == '6' or \
       char == '7' or char == '8' or char == '9':
        return int(char)
    elif char.lower() == 'x':
        return 10
    elif char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()

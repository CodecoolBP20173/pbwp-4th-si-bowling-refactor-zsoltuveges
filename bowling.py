def score(game):
    frame = 1
    result = 0
    in_first_half = True
    last_point = 0
    for index, actual_point in enumerate(game):
        result += calculate_frame_result(index, actual_point, frame, game, last_point)
        last_point = get_value(actual_point)
        in_first_half, frame = checking_first_half(in_first_half, actual_point, frame)
    return result


def get_value(char):
    try:
        if char.lower() == 'x':
            return 10
        elif char == '/':
            return 10
        elif char == '-':
            return 0
        elif int(char) in range(1, 10):
            return int(char)
    except:
        raise ValueError()


def calculate_frame_result(index, actual_point, frame, game, last_point):
    actual_result = 0
    if actual_point == '/':
        actual_result += 10 - last_point
    else:
        actual_result += get_value(actual_point)
    if frame < 10 and get_value(actual_point) == 10:
        if actual_point == '/':
            actual_result += get_value(game[index + 1])
        elif actual_point.lower() == 'x':
            actual_result += get_value(game[index + 1])
            if game[index + 2] == '/':
                actual_result += 10 - get_value(game[index + 1])
            else:
                actual_result += get_value(game[index + 2])
    return actual_result


def checking_first_half(in_first_half, actual_point, frame):
    if not in_first_half:
        frame += 1
    if in_first_half is True:
        in_first_half = False
    else:
        in_first_half = True
    if actual_point.lower() == 'x':
        in_first_half = True
        frame += 1
    return in_first_half, frame
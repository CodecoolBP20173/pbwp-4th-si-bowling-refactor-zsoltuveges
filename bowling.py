def score(game):
    frame = 1
    result = 0
    in_first_half = True
    last_point = 0
    MAX_POINT = 10
    MAX_FRAME = 10
    STRIKE = "x"
    SPARE = "/"
    MISS = "-"
    for index, actual_point in enumerate(game):
        result += calculate_frame_result(index, actual_point, frame, game, last_point, MAX_POINT, MAX_FRAME, STRIKE, SPARE, MISS)
        last_point = get_value(actual_point, MAX_POINT, STRIKE, SPARE, MISS)
        in_first_half, frame = checking_first_half(in_first_half, actual_point, frame, STRIKE)
    return result


def get_value(char, MAX_POINT, STRIKE, SPARE, MISS):
    try:
        if char.lower() == STRIKE:
            return MAX_POINT
        elif char == SPARE:
            return MAX_POINT
        elif char == MISS:
            return 0
        elif int(char) in range(1, 10):
            return int(char)
    except:
        raise ValueError()


def calculate_frame_result(index, actual_point, frame, game, last_point, MAX_POINT, MAX_FRAME, STRIKE, SPARE, MISS):
    actual_result = 0
    if actual_point == SPARE:
        actual_result += MAX_POINT - last_point
    else:
        actual_result += get_value(actual_point, MAX_POINT, STRIKE, SPARE, MISS)
    if frame < MAX_FRAME and get_value(actual_point, MAX_POINT, STRIKE, SPARE, MISS) == MAX_POINT:
        if actual_point == SPARE:
            actual_result += get_value(game[index + 1], MAX_POINT, STRIKE, SPARE, MISS)
        elif actual_point.lower() == STRIKE:
            actual_result += get_value(game[index + 1], MAX_POINT, STRIKE, SPARE, MISS)
            if game[index + 2] == SPARE:
                actual_result += MAX_POINT - get_value(game[index + 1], MAX_POINT, STRIKE, SPARE, MISS)
            else:
                actual_result += get_value(game[index + 2], MAX_POINT, STRIKE, SPARE, MISS)
    return actual_result


def checking_first_half(in_first_half, actual_point, frame, STRIKE):
    if not in_first_half:
        frame += 1
    if in_first_half is True:
        in_first_half = False
    else:
        in_first_half = True
    if actual_point.lower() == STRIKE:
        in_first_half = True
        frame += 1
    return in_first_half, frame
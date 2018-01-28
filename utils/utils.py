# utils.py by bllli (under Python3.6)


def get_value_in_choices(choices: tuple, key: int) -> str or None:
    """通过key获取choices中对应的value"""
    try:
        for choice in choices:
            if key == choice[0]:
                return choice[1]
    except IndexError:
        pass
    raise ValueError('')

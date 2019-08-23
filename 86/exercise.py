def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    converted = []
    for item in rgb:
        if 0 < item <= 255:
            converted.append(hex(item).split('0x')[1].upper())
        elif item == 0:
            converted.append('00')
        else:
            raise ValueError('Out of range')
    return f"#{''.join(converted)}"

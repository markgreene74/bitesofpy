import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
color_values_module = os.path.join('/tmp', 'color_values.py')
urllib.request.urlretrieve('https://bit.ly/2MSuu4z',
                           color_values_module)
sys.path.append('/tmp')

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.color = color
        self.rgb = COLOR_NAMES.get(color.upper())

    @classmethod
    def hex2rgb(cls, color_hex):
        """Class method that converts a hex value into an rgb one"""
        color_hex = color_hex.replace("#", "")
        try:
            color_rgb = tuple(int(color_hex[i : i + 2], 16) for i in (0, 2, 4))
        except ValueError:
            raise ValueError("Not hexadecimal")
        return color_rgb

    @classmethod
    def rgb2hex(cls, color_rgb):
        """Class method that converts an rgb value into a hex one"""
        if isinstance(color_rgb, tuple) and all([i in range(256) for i in color_rgb]):
            r, g, b = color_rgb
            return "#{:02x}{:02x}{:02x}".format(r, g, b)
        else:
            raise ValueError("Not rgb")

    def __repr__(self):
        """Returns the repl of the object"""
        return f"{self.__class__.__name__}('{self.color}')"

    def __str__(self):
        """Returns the string value of the color object"""
        return str(self.rgb) if self.rgb else "Unknown"

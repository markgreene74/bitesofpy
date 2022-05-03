from collections import namedtuple, defaultdict
import re

social_platforms = """Twitter
  Min: 1
  Max: 15
  Can contain: a-z A-Z 0-9 _

Facebook
  Min: 5
  Max: 50
  Can contain: a-z A-Z 0-9 .

Reddit
  Min: 3
  Max: 20
  Can contain: a-z A-Z 0-9 _ -
"""

# note range is of type range and regex is a re.compile object
Validator = namedtuple("Validator", "range regex")


def parse_social_platforms_string():
    """Convert the social_platforms string above into a dict where
    keys = social platformsname and values = validator namedtuples"""
    data = defaultdict(Validator)
    for i in social_platforms.split("\n\n"):
        # try, just in case there is any surprise
        try:
            platform = re.search(r"^([\w]+)\n", i).group(1)
            min, max = re.findall(r":\s(\d+)\n", i)
            re_string = re.search(r"contain:\s(.*)$", i).group(1)
        except AttributeError:
            print("Something is wrong")
            platform = "None"
            min = 1
            max = 2
            re_string = "a-zA-Z"
        # make some magic here
        min, max = int(min), int(max)
        re_string = re_string.replace(" ", "")
        pattern = re.compile(r"^[{0}]+$".format(re_string))
        # and finally add to the dictionary
        data[platform] = Validator(range(min, max), pattern)
    return data


def validate_username(platform, username):
    """Receives platforms(Twitter, Facebook or Reddit) and username string,
    raise a ValueError if the wrong platform is passed in,
    return True/False if username is valid for entered platform"""
    all_validators = parse_social_platforms_string()
    if platform in all_validators.keys():
        validator = all_validators[platform]
    else:
        raise ValueError("Wrong platform")

    if bool(re.match(validator.regex, username)) and len(username) in validator.range:
        return True
    else:
        return False

# https://codechalleng.es/bites/141/
from enum import Enum
from datetime import datetime
from collections import Counter
from itertools import takewhile


class DateFormat(Enum):
    DDMMYY = 0  # dd/mm/yy
    MMDDYY = 1  # mm/dd/yy
    YYMMDD = 2  # yy/mm/dd
    NONPARSABLE = -999

    @classmethod
    def get_d_parse_formats(cls, val=None):
        """ Arg:
        val(int | None) enum member value
        Returns:
        1. for val=None a list of explicit format strings 
            for all supported date formats in this enum
        2. for val=n an explicit format string for a given enum member value
        """
        d_parse_formats = ["%d/%m/%y", "%m/%d/%y", "%y/%m/%d"]
        if val is None:
            return d_parse_formats
        if 0 <= val <= len(d_parse_formats):
            return d_parse_formats[val]
        raise ValueError


class InfDateFmtError(Exception):
    """custom exception when it is not possible to infer a date format
    e.g. too many NONPARSABLE or a tie """

    pass


def _maybe_DateFormats(date_str):
    """ Args:
    date_str (str) string representing a date in unknown format
    Returns:
    a list of enum members, where each member represents
    a possible date format for the input date_str
    """
    d_parse_formats = DateFormat.get_d_parse_formats()
    maybe_formats = []
    for idx, d_parse_fmt in enumerate(d_parse_formats):
        try:
            _parsed_date = datetime.strptime(
                date_str, d_parse_fmt
            )  # pylint: disable=W0612
            maybe_formats.append(DateFormat(idx))
        except ValueError:
            pass
    if len(maybe_formats) == 0:
        maybe_formats.append(DateFormat.NONPARSABLE)
    return maybe_formats


def get_dates(dates):
    """ Args:
    dates (list) list of date strings
    where each list item represents a date in unknown format
    Returns:
    list of date strings, where each list item represents
    a date in yyyy-mm-dd format. Date format of input date strings is
    inferred based on the most prevalent format in the dates list.
    Alowed/supported date formats are defined in a DF enum class.
    """
    # complete this method
    d_parse_formats = DateFormat.get_d_parse_formats()
    result = Counter()
    new_dates = []
    # parse all the dates to gather the date format
    for adate in dates:
        result.update(_maybe_DateFormats(adate))
    # get the counter of most_common(1) and find if there are
    # other entries with the same counter
    max_c = result.most_common(1)[0][1]
    if len(list(takewhile(lambda x: x[1] == max_c, result.most_common()))) > 1:
        raise InfDateFmtError
    # if the most_common is NONPARSABLE raise InfDateFmtError
    # otherwise decide which conversion string will be used
    if result.most_common(1)[0][0] == DateFormat.NONPARSABLE:
        raise InfDateFmtError
    else:
        date_convrs_str = d_parse_formats[result.most_common(1)[0][0].value]
    # parse dates using the conversion string and store the results
    # in a list of new_dates
    for adate in dates:
        try:
            _adate_str = str(datetime.strptime(adate, date_convrs_str).date())
        except (ValueError, TypeError):
            _adate_str = "Invalid"
        new_dates.append(_adate_str)
    return new_dates

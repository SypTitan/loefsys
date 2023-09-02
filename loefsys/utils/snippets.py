from collections import namedtuple
import datetime


def dict2obj(d, name="Object"):
    return namedtuple(name, d.keys())(*d.values())


def overlaps(check, others, can_equal=True):
    """Check for overlapping date ranges.
    This works by checking the maximum of the two `since` times, and the minimum of
    the two `until` times. Because there are no infinite dates, the value date_max
    is created for when the `until` value is None; this signifies a timespan that
    has not ended yet and is the maximum possible date in Python's datetime.
    The ranges overlap when the maximum start time is smaller than the minimum
    end time, as can be seen in this example of two integer ranges:
    check: . . . .[4]. . . . 9
    other: . . 2 . .[5]. . . .
    check: . . . .[4]. . . . 9
    other: . . 2 . . . . . . . [date_max]
    And when non overlapping:
    check: . . . . . .[6] . . 9
    other: . . 2 . .[5]. . . .
    4 < 5 == True so these intervals overlap, while 6 < 5 == False so these intervals
    don't overlap
    The can_equal argument is used for boards, where the end date can't be the same
    as the start date.
    >>> overlaps( \
    dict2obj({ \
        'pk': 1 \
        , 'since': datetime.date(2018, 12, 1) \
        , 'until': datetime.date(2019, 1, 1) \
    }) \
    , [dict2obj({ \
    'pk': 2 \
    , 'since': datetime.date(2019, 1, 1) \
    , 'until': datetime.date(2019, 1, 31) \
    })])
    False
    >>> overlaps( \
    dict2obj({ \
        'pk': 1 \
        , 'since': datetime.date(2018, 12, 1) \
        , 'until': datetime.date(2019, 1, 1) \
    }) \
    , [dict2obj({ \
    'pk': 2 \
    , 'since': datetime.date(2019, 1, 1) \
    , 'until': datetime.date(2019, 1, 31) \
    })], False)
    True
    >>> overlaps( \
    dict2obj({ \
        'pk': 1 \
        , 'since': datetime.date(2018, 12, 1) \
        , 'until': datetime.date(2019, 1, 2) \
    }) \
    , [dict2obj({ \
    'pk': 2 \
    , 'since': datetime.date(2019, 1, 1) \
    , 'until': datetime.date(2019, 1, 31) \
    })])
    True
    """
    date_max = datetime.date(datetime.MAXYEAR, 12, 31)
    for other in others:
        if check.pk == other.pk:
            # No checks for the object we're validating
            continue

        max_start = max(check.since, other.since)
        min_end = min(check.until or date_max, other.until or date_max)

        if max_start == min_end and not can_equal:
            return True
        if max_start < min_end:
            return True

    return False

loefsys.utils.snippets
======================

.. py:module:: loefsys.utils.snippets


Functions
---------

.. autoapisummary::

   loefsys.utils.snippets.dict2obj
   loefsys.utils.snippets.overlaps


Module Contents
---------------

.. py:function:: dict2obj(d: dict, name: str = 'Object')

   Convert a dictionary into a custom object.

   This utility function converts any raw dictionary into a Name

   :param d: the dict to be converted.
   :type d: dict
   :param name: the type of the NamedTuple.
   :type name: str

   :returns: A NamedTuple


.. py:function:: overlaps(check, others, can_equal=True)

   Check for overlapping date ranges.

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
   >>> overlaps(     dict2obj({         'pk': 1         , 'since': datetime.date(2018, 12, 1)         , 'until': datetime.date(2019, 1, 1)     })     , [dict2obj({     'pk': 2     , 'since': datetime.date(2019, 1, 1)     , 'until': datetime.date(2019, 1, 31)     })])
   False
   >>> overlaps(     dict2obj({         'pk': 1         , 'since': datetime.date(2018, 12, 1)         , 'until': datetime.date(2019, 1, 1)     })     , [dict2obj({     'pk': 2     , 'since': datetime.date(2019, 1, 1)     , 'until': datetime.date(2019, 1, 31)     })], False)
   True
   >>> overlaps(     dict2obj({         'pk': 1         , 'since': datetime.date(2018, 12, 1)         , 'until': datetime.date(2019, 1, 2)     })     , [dict2obj({     'pk': 2     , 'since': datetime.date(2019, 1, 1)     , 'until': datetime.date(2019, 1, 31)     })])
   True



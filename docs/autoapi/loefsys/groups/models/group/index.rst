loefsys.groups.models.group
===========================

.. py:module:: loefsys.groups.models.group


Classes
-------

.. autoapisummary::

   loefsys.groups.models.group.ActiveMemberGroupManager
   loefsys.groups.models.group.Group


Module Contents
---------------

.. py:class:: ActiveMemberGroupManager

   Bases: :py:obj:`django.db.models.Manager`


   Returns active objects only sorted by the localized name.


   .. py:method:: get_queryset()


.. py:class:: Group(*args, **kwargs)

   Bases: :py:obj:`django.db.models.Model`


   Describes a group of members (Users with Membership object).


   .. py:class:: GroupTypes(*args, **kwds)

      Bases: :py:obj:`django.db.models.IntegerChoices`


      Class for creating enumerated integer choices.


      .. py:attribute:: BOARD


      .. py:attribute:: COMMITTEE


      .. py:attribute:: SOCIETY


      .. py:attribute:: FRATERNITY


      .. py:attribute:: YEARCLUB



   .. py:attribute:: group_type


   .. py:attribute:: name


   .. py:attribute:: description


   .. py:attribute:: members


   .. py:attribute:: active


   .. py:attribute:: contact_email


   .. py:attribute:: display_members


   .. py:attribute:: since


   .. py:attribute:: until


   .. py:property:: size


   .. py:method:: __str__()

      Return str(self).




loefsys.groups.models
=====================

.. py:module:: loefsys.groups.models


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/loefsys/groups/models/board/index
   /autoapi/loefsys/groups/models/committee/index
   /autoapi/loefsys/groups/models/fraternity/index
   /autoapi/loefsys/groups/models/group/index
   /autoapi/loefsys/groups/models/group_membership/index
   /autoapi/loefsys/groups/models/year_club/index


Classes
-------

.. autoapisummary::

   loefsys.groups.models.Board
   loefsys.groups.models.Committee
   loefsys.groups.models.Fraternity
   loefsys.groups.models.Group
   loefsys.groups.models.GroupMembership
   loefsys.groups.models.YearClub


Package Contents
----------------

.. py:class:: Board(*args, **kwargs)

   Bases: :py:obj:`loefsys.groups.models.group.Group`


   Describes a group of members (Users with Membership object).


   .. py:attribute:: year


.. py:class:: Committee(*args, **kwargs)

   Bases: :py:obj:`loefsys.groups.models.group.Group`


   Describes a group of members (Users with Membership object).


   .. py:attribute:: mandatory


.. py:class:: Fraternity(*args, **kwargs)

   Bases: :py:obj:`loefsys.groups.models.group.Group`


   Describes a group of members (Users with Membership object).


   .. py:attribute:: GENDER_CHOICES
      :value: (('MIXED', 'Mixed'), ('FEMALE', 'Female'), ('MALE', 'Male'))



   .. py:attribute:: gender_requirement


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



.. py:class:: GroupMembership(*args, **kwargs)

   Bases: :py:obj:`django.db.models.Model`


   Describes a group membership.


   .. py:attribute:: objects


   .. py:attribute:: active_objects


   .. py:attribute:: user


   .. py:attribute:: group


   .. py:attribute:: chair


   .. py:attribute:: role


   .. py:attribute:: since


   .. py:attribute:: until


   .. py:attribute:: note


   .. py:method:: __str__()

      Return str(self).



.. py:class:: YearClub(*args, **kwargs)

   Bases: :py:obj:`loefsys.groups.models.group.Group`


   Describes a group of members (Users with Membership object).


   .. py:attribute:: year



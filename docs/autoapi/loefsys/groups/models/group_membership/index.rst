loefsys.groups.models.group_membership
======================================

.. py:module:: loefsys.groups.models.group_membership


Classes
-------

.. autoapisummary::

   loefsys.groups.models.group_membership.ActiveMembershipManager
   loefsys.groups.models.group_membership.GroupMembership


Module Contents
---------------

.. py:class:: ActiveMembershipManager

   Bases: :py:obj:`django.db.models.Manager`


   Custom manager that gets the currently active membergroup memberships.


   .. py:method:: get_queryset()


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




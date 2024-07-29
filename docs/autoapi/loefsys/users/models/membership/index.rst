loefsys.users.models.membership
===============================

.. py:module:: loefsys.users.models.membership


Classes
-------

.. autoapisummary::

   loefsys.users.models.membership.MembershipTypes
   loefsys.users.models.membership.Membership


Module Contents
---------------

.. py:class:: MembershipTypes(*args, **kwds)

   Bases: :py:obj:`django.db.models.TextChoices`


   Class for creating enumerated string choices.


   .. py:attribute:: ACTIVE


   .. py:attribute:: PASSIVE


   .. py:attribute:: ALUMNUS


.. py:class:: Membership(*args, **kwargs)

   Bases: :py:obj:`django.db.models.Model`


   Make subclasses preserve the alters_data attribute on overridden methods.


   .. py:attribute:: user


   .. py:attribute:: membership_type


   .. py:attribute:: since


   .. py:attribute:: until


   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



   .. py:method:: is_active()


   .. py:method:: __str__()

      Return str(self).




loefsys.users.models
====================

.. py:module:: loefsys.users.models


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/loefsys/users/models/contacts/index
   /autoapi/loefsys/users/models/membership/index
   /autoapi/loefsys/users/models/user/index


Classes
-------

.. autoapisummary::

   loefsys.users.models.Contacts
   loefsys.users.models.Membership
   loefsys.users.models.User


Package Contents
----------------

.. py:class:: Contacts(*args, **kwargs)

   Bases: :py:obj:`django.db.models.Model`


   Make subclasses preserve the alters_data attribute on overridden methods.


   .. py:attribute:: user


   .. py:attribute:: first_name


   .. py:attribute:: last_name


   .. py:attribute:: institution


   .. py:attribute:: programme


   .. py:attribute:: student_number


   .. py:attribute:: RSC_number


   .. py:attribute:: member_since


   .. py:attribute:: member_until


   .. py:attribute:: alumni_since


   .. py:attribute:: payment_method


   .. py:attribute:: remark


   .. py:attribute:: address_street


   .. py:attribute:: address_street2


   .. py:attribute:: address_postal_code


   .. py:attribute:: address_city


   .. py:attribute:: address_country


   .. py:attribute:: phone_number


   .. py:attribute:: IBAN


   .. py:attribute:: birthday


   .. py:attribute:: gender


   .. py:attribute:: receive_newsletter


   .. py:attribute:: show_birthday


   .. py:attribute:: profile_description


   .. py:attribute:: initials


   .. py:attribute:: nickname


   .. py:attribute:: display_name_preference


   .. py:property:: is_member


   .. py:method:: __str__()

      Return str(self).



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



.. py:class:: User(*args, **kwargs)

   Bases: :py:obj:`django.contrib.auth.models.AbstractBaseUser`, :py:obj:`django.contrib.auth.models.PermissionsMixin`


   Make subclasses preserve the alters_data attribute on overridden methods.


   .. py:attribute:: email


   .. py:attribute:: is_staff


   .. py:attribute:: is_active


   .. py:attribute:: USERNAME_FIELD
      :value: 'email'



   .. py:attribute:: REQUIRED_FIELDS
      :value: []



   .. py:attribute:: objects


   .. py:attribute:: membership_set
      :type:  django.db.models.QuerySet[loefsys.users.models.membership.Membership]


   .. py:method:: __str__()

      Return str(self).




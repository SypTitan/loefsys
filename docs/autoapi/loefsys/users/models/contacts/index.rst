loefsys.users.models.contacts
=============================

.. py:module:: loefsys.users.models.contacts


Classes
-------

.. autoapisummary::

   loefsys.users.models.contacts.PaymentMethods
   loefsys.users.models.contacts.Genders
   loefsys.users.models.contacts.Contacts


Module Contents
---------------

.. py:class:: PaymentMethods(*args, **kwds)

   Bases: :py:obj:`django.db.models.TextChoices`


   Class for creating enumerated string choices.


   .. py:attribute:: COLLECTION


.. py:class:: Genders(*args, **kwds)

   Bases: :py:obj:`django.db.models.TextChoices`


   Class for creating enumerated string choices.


   .. py:attribute:: MALE


   .. py:attribute:: FEMALE


   .. py:attribute:: OTHER


   .. py:attribute:: UNSPECIFIED


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




loefsys.reservations.models.reservable
======================================

.. py:module:: loefsys.reservations.models.reservable


Classes
-------

.. autoapisummary::

   loefsys.reservations.models.reservable.ReservableType
   loefsys.reservations.models.reservable.Reservable


Module Contents
---------------

.. py:class:: ReservableType(*args, **kwargs)

   Bases: :py:obj:`django.db.models.Model`


   Describes a type of material that can be reserved.


   .. py:class:: Reservables(*args, **kwds)

      Bases: :py:obj:`django.db.models.IntegerChoices`


      Class for creating enumerated integer choices.


      .. py:attribute:: BOAT


      .. py:attribute:: ROOM


      .. py:attribute:: MATERIAL



   .. py:attribute:: type_of_reservable


   .. py:attribute:: name


   .. py:attribute:: description


   .. py:method:: __str__()

      Return str(self).



.. py:class:: Reservable(*args, **kwargs)

   Bases: :py:obj:`django.db.models.Model`


   Make subclasses preserve the alters_data attribute on overridden methods.


   .. py:attribute:: LOCATION_CHOICES
      :value: (('BOARDROOM', 'Boardroom'), ('BASTION', 'Bastion'), ('KRAAIJ', 'Kraaij'))



   .. py:attribute:: location


   .. py:attribute:: reservable


   .. py:attribute:: reservable_type


   .. py:attribute:: description


   .. py:attribute:: member_price


   .. py:attribute:: alumni_price


   .. py:attribute:: external_price


   .. py:method:: __str__()

      Return str(self).




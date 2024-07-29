loefsys.events.models.event_registation
=======================================

.. py:module:: loefsys.events.models.event_registation


Classes
-------

.. autoapisummary::

   loefsys.events.models.event_registation.EventRegistration


Functions
---------

.. autoapisummary::

   loefsys.events.models.event_registation.registration_user_choices_limit


Module Contents
---------------

.. py:function:: registration_user_choices_limit(event)

   Define queryset filters to only include current members.


.. py:class:: EventRegistration(*args, **kwargs)

   Bases: :py:obj:`django.db.models.Model`


   Make subclasses preserve the alters_data attribute on overridden methods.


   .. py:attribute:: event


   .. py:attribute:: user


   .. py:class:: Meta

      .. py:attribute:: unique_together
         :value: ('event', 'user')




   .. py:attribute:: guest_form


   .. py:attribute:: date


   .. py:attribute:: date_cancelled


   .. py:attribute:: present


   .. py:attribute:: paid


   .. py:property:: fine


   .. py:property:: costs


   .. py:property:: contact


   .. py:method:: __str__()

      Return str(self).




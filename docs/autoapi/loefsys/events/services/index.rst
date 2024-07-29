loefsys.events.services
=======================

.. py:module:: loefsys.events.services


Functions
---------

.. autoapisummary::

   loefsys.events.services.is_user_registered
   loefsys.events.services.user_registration_pending
   loefsys.events.services.is_user_present
   loefsys.events.services.is_organiser
   loefsys.events.services.create_registration


Module Contents
---------------

.. py:function:: is_user_registered(user, event)

   Return if the user is registered for the specified event.

   :param user: the user
   :param event: the event
   :return: None if registration is not required or no member else True/False


.. py:function:: user_registration_pending(user, event)

   Return if the user is in the queue, but not yet registered for, the specific event.

   :param user: the user
   :param event: the event
   :return: None if registration is not required or no member else True/False


.. py:function:: is_user_present(user, event)

.. py:function:: is_organiser(member, event)

.. py:function:: create_registration(user, event)

   Create a new user registration for an event.

   :param user: the user
   :param event: the event
   :return: Return the registration if successful



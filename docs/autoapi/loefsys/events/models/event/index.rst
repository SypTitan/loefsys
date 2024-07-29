loefsys.events.models.event
===========================

.. py:module:: loefsys.events.models.event


Classes
-------

.. autoapisummary::

   loefsys.events.models.event.Event


Module Contents
---------------

.. py:class:: Event(*args, **kwargs)

   Bases: :py:obj:`django.db.models.Model`


   Model for an event.

   TODO @Mark expand on this.


   .. py:attribute:: NO_REGISTRATION_MESSAGE
      :type:  ClassVar[str]

      Default text for an event without registration required.


   .. py:class:: EventCategories(*args, **kwds)

      Bases: :py:obj:`django.db.models.IntegerChoices`


      Categories for an event.

      Events can be filtered based on their category. This enum is used for the
      filtering.


      .. py:attribute:: OTHER

         Used when other categories aren't appropriate.


      .. py:attribute:: ALUMNI

         Used for events for ex-members of the association.


      .. py:attribute:: LEISURE

         Used for entertainment events.

         Examples are 'borrels', parties, game activites, and more.


      .. py:attribute:: ASSOCIATION

         Used for events related to the board.

         Examples are general meetings, or the fries table moment.


      .. py:attribute:: SAILING

         Used for events directly involving sailing.


      .. py:attribute:: COMPETITION

         Used for events specifically for sailing competetions.

         Examples are NESTOR, regatta's, and more.



   .. py:attribute:: title
      :type:  str

      The title to display for the event.


   .. py:attribute:: organiser_groups
      :type:  list[loefsys.groups.models.Group]

      A list of the groups organising this event.


   .. py:attribute:: organiser_contacts
      :type:  list[django.conf.settings.AUTH_USER_MODEL]

      list[:setting:`django:AUTH_USER_MODEL`]:
      A list of the contacts involved in organising this event.

      :type: organiser_contacts


   .. py:attribute:: is_open_event
      :type:  bool

      Determine whether this event is open for non-members.


   .. py:attribute:: start

      The start date and time of the event.


   .. py:attribute:: end

      The end date and time of the event.


   .. py:attribute:: category

      The category of the event.

      See :class:`loefsys.events.models.Event.EventCategories`.


   .. py:attribute:: registration_start


   .. py:attribute:: registration_end


   .. py:attribute:: cancel_deadline


   .. py:attribute:: send_cancel_email


   .. py:attribute:: optional_registrations


   .. py:attribute:: location


   .. py:attribute:: map_location


   .. py:attribute:: price


   .. py:attribute:: fine


   .. py:attribute:: max_participants


   .. py:attribute:: no_registration_message


   .. py:attribute:: published


   .. py:property:: active_registrations
      Queryset with all non-cancelled registrations.


   .. py:property:: participants
      Return the active participants.


   .. py:property:: queue
      Return the waiting queue.


   .. py:property:: registration_required


   .. py:property:: can_cancel_for_free


   .. py:property:: reached_participants_limit
      Is this event up to capacity?.


   .. py:property:: registration_closed


   .. py:method:: clean()

      Hook for doing any extra model-wide validation after clean() has been
      called on every field by self.clean_fields. Any ValidationError raised
      by this method will not be associated with a particular field; it will
      have a special-case association with the field defined by NON_FIELD_ERRORS.



   .. py:method:: get_absolute_url()


   .. py:method:: __str__()

      Return str(self).




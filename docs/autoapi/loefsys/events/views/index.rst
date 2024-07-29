loefsys.events.views
====================

.. py:module:: loefsys.events.views


Classes
-------

.. autoapisummary::

   loefsys.events.views.EventListView
   loefsys.events.views.EventDetailView
   loefsys.events.views.EventRegisterView
   loefsys.events.views.EventGuestContactCreateView


Module Contents
---------------

.. py:class:: EventListView(**kwargs)

   Bases: :py:obj:`django.views.generic.ListView`


   Render some list of objects, set by `self.model` or `self.queryset`.
   `self.queryset` can actually be any iterable of items, not just a queryset.


   .. py:attribute:: template_name
      :value: 'events/index.html'



   .. py:attribute:: context_object_name
      :value: 'events'



   .. py:method:: get_queryset()

      Return the list of items for this view.

      The return value must be an iterable and may be an instance of
      `QuerySet` in which case `QuerySet` specific behavior will be enabled.



.. py:class:: EventDetailView(**kwargs)

   Bases: :py:obj:`django.views.generic.DetailView`


   View that renders a member's profile.


   .. py:attribute:: model


   .. py:attribute:: queryset


   .. py:attribute:: template_name
      :value: 'events/event.html'



   .. py:attribute:: context_object_name
      :value: 'event'



   .. py:method:: get_context_data(**kwargs)

      Insert the single object into the context dict.



.. py:class:: EventRegisterView(**kwargs)

   Bases: :py:obj:`django.views.View`


   Define a view that allows the user to register for an event using a POST request.

   The user should be authenticated.


   .. py:method:: get(request, *args, **kwargs)


   .. py:method:: post(request, *args, **kwargs)


.. py:class:: EventGuestContactCreateView(**kwargs)

   Bases: :py:obj:`django.contrib.auth.mixins.LoginRequiredMixin`, :py:obj:`django.views.generic.edit.CreateView`


   Verify that the current user is authenticated.


   .. py:attribute:: form_class


   .. py:attribute:: exclude
      :value: ['user']



   .. py:method:: form_valid(form)

      If the form is valid, save the associated model.




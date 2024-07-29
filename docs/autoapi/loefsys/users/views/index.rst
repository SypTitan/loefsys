loefsys.users.views
===================

.. py:module:: loefsys.users.views


Classes
-------

.. autoapisummary::

   loefsys.users.views.ProfileListView
   loefsys.users.views.ProfileDetailView


Module Contents
---------------

.. py:class:: ProfileListView(**kwargs)

   Bases: :py:obj:`django.views.generic.ListView`


   Render some list of objects, set by `self.model` or `self.queryset`.
   `self.queryset` can actually be any iterable of items, not just a queryset.


   .. py:attribute:: template_name
      :value: 'users/index.html'



   .. py:attribute:: context_object_name
      :value: 'users'



.. py:class:: ProfileDetailView(**kwargs)

   Bases: :py:obj:`django.views.generic.DetailView`


   View that renders a member's profile.


   .. py:attribute:: model


   .. py:attribute:: template_name
      :value: 'users/profile.html'



   .. py:method:: setup(request, *args, **kwargs) -> None

      Initialize attributes shared by all view methods.




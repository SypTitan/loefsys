loefsys.events.admin
====================

.. py:module:: loefsys.events.admin


Classes
-------

.. autoapisummary::

   loefsys.events.admin.RegistrationInline
   loefsys.events.admin.EventAdmin


Module Contents
---------------

.. py:class:: RegistrationInline(parent_model, admin_site)

   Bases: :py:obj:`django.contrib.admin.TabularInline`


   Options for inline editing of ``model`` instances.

   Provide ``fk_name`` to specify the attribute name of the ``ForeignKey``
   from ``model`` to its parent. This is required if ``model`` has more than
   one ``ForeignKey`` to its parent.


   .. py:attribute:: model


   .. py:attribute:: extra
      :value: 0



   .. py:method:: has_delete_permission(request)

      Return True if the given request has permission to delete the given
      Django model instance, the default implementation doesn't examine the
      `obj` parameter.

      Can be overridden by the user in subclasses. In such case it should
      return True if the given request has permission to delete the `obj`
      model instance. If `obj` is None, this should return True if the given
      request has permission to delete *any* object of the given type.



.. py:class:: EventAdmin(model, admin_site)

   Bases: :py:obj:`django.contrib.admin.ModelAdmin`


   Encapsulate all admin options and functionality for a given model.


   .. py:attribute:: list_display
      :value: ['title', 'start']



   .. py:attribute:: inlines



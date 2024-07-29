loefsys.groups.admin
====================

.. py:module:: loefsys.groups.admin


Classes
-------

.. autoapisummary::

   loefsys.groups.admin.MemberGroupMembershipInline
   loefsys.groups.admin.MemberGroupMembershipAdmin
   loefsys.groups.admin.BoardInline
   loefsys.groups.admin.BoardAdmin


Module Contents
---------------

.. py:class:: MemberGroupMembershipInline(parent_model, admin_site)

   Bases: :py:obj:`django.contrib.admin.TabularInline`


   Options for inline editing of ``model`` instances.

   Provide ``fk_name`` to specify the attribute name of the ``ForeignKey``
   from ``model`` to its parent. This is required if ``model`` has more than
   one ``ForeignKey`` to its parent.


   .. py:attribute:: model


   .. py:attribute:: verbose_name
      :value: 'membership'



   .. py:attribute:: verbose_name_plural
      :value: 'memberships'



   .. py:attribute:: extra
      :value: 0



   .. py:method:: has_delete_permission(request, obj=None)

      Return True if the given request has permission to delete the given
      Django model instance, the default implementation doesn't examine the
      `obj` parameter.

      Can be overridden by the user in subclasses. In such case it should
      return True if the given request has permission to delete the `obj`
      model instance. If `obj` is None, this should return True if the given
      request has permission to delete *any* object of the given type.



.. py:class:: MemberGroupMembershipAdmin(model, admin_site)

   Bases: :py:obj:`django.contrib.admin.ModelAdmin`


   Encapsulate all admin options and functionality for a given model.


   .. py:attribute:: inlines


.. py:class:: BoardInline(parent_model, admin_site)

   Bases: :py:obj:`django.contrib.admin.TabularInline`


   Options for inline editing of ``model`` instances.

   Provide ``fk_name`` to specify the attribute name of the ``ForeignKey``
   from ``model`` to its parent. This is required if ``model`` has more than
   one ``ForeignKey`` to its parent.


   .. py:attribute:: model


   .. py:attribute:: verbose_name
      :value: 'Board'



   .. py:attribute:: verbose_name_plural
      :value: 'Boards'



   .. py:method:: has_delete_permission(request, obj=None)

      Return True if the given request has permission to delete the given
      Django model instance, the default implementation doesn't examine the
      `obj` parameter.

      Can be overridden by the user in subclasses. In such case it should
      return True if the given request has permission to delete the `obj`
      model instance. If `obj` is None, this should return True if the given
      request has permission to delete *any* object of the given type.



.. py:class:: BoardAdmin(model, admin_site)

   Bases: :py:obj:`django.contrib.admin.ModelAdmin`


   Encapsulate all admin options and functionality for a given model.


   .. py:attribute:: inlines



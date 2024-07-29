loefsys.users.adapters
======================

.. py:module:: loefsys.users.adapters


Classes
-------

.. autoapisummary::

   loefsys.users.adapters.AccountAdapter
   loefsys.users.adapters.SocialAccountAdapter


Module Contents
---------------

.. py:class:: AccountAdapter

   Bases: :py:obj:`allauth.account.adapter.DefaultAccountAdapter`


   .. py:method:: is_open_for_signup(request: django.http.HttpRequest)


.. py:class:: SocialAccountAdapter

   Bases: :py:obj:`allauth.socialaccount.adapter.DefaultSocialAccountAdapter`


   .. py:method:: is_open_for_signup(request: django.http.HttpRequest, sociallogin: Any)



loefsys.users.tests
===================

.. py:module:: loefsys.users.tests


Classes
-------

.. autoapisummary::

   loefsys.users.tests.UsersManagersTests


Module Contents
---------------

.. py:class:: UsersManagersTests(methodName='runTest')

   Bases: :py:obj:`django.test.TestCase`


   Similar to TransactionTestCase, but use `transaction.atomic()` to achieve
   test isolation.

   In most situations, TestCase should be preferred to TransactionTestCase as
   it allows faster execution. However, there are some situations where using
   TransactionTestCase might be necessary (e.g. testing some transactional
   behavior).

   On database backends with no transaction support, TestCase behaves as
   TransactionTestCase.


   .. py:method:: test_create_user()


   .. py:method:: test_create_superuser()



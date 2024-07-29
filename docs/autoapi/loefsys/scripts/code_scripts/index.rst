loefsys.scripts.code_scripts
============================

.. py:module:: loefsys.scripts.code_scripts

.. autoapi-nested-parse::

   Submodule containing scripts related to the repository code.

   With the available scripts, linting, formatting, and typechecking is easily available.



Functions
---------

.. autoapisummary::

   loefsys.scripts.code_scripts.lint
   loefsys.scripts.code_scripts.format
   loefsys.scripts.code_scripts.typecheck


Module Contents
---------------

.. py:function:: lint() -> None

   Apply linting to the project code.

   See `Ruff linter <https://docs.astral.sh/ruff/linter/>`_ for more details.


.. py:function:: format() -> None

   Apply formatting to the project code.

   See `Ruff formatter <https://docs.astral.sh/ruff/formatter/>`_ for more details.


.. py:function:: typecheck() -> None

   Perform typechecking analysis on the project code.

   See :doc:`mypy <mypy:index>` for more details



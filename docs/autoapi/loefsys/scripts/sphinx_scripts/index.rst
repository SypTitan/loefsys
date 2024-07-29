loefsys.scripts.sphinx_scripts
==============================

.. py:module:: loefsys.scripts.sphinx_scripts

.. autoapi-nested-parse::

   Submodule containing scripts related to Sphinx docs generation.

   The available scripts allow generation of the API docs and building of the docs.



Functions
---------

.. autoapisummary::

   loefsys.scripts.sphinx_scripts.makedocs
   loefsys.scripts.sphinx_scripts.genapidocs


Module Contents
---------------

.. py:function:: makedocs() -> None

   Generate HTML documentation for the project.

   See :doc:`sphinx:man/sphinx-build` for more details.


.. py:function:: genapidocs() -> None

   Generate API documentation from the docstrings.

   See :doc:`sphinx:man/sphinx-apidoc` for more details.



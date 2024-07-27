How to Write Docstring Documentation
====================================

In principle, all code in the repository needs to be sufficiently tested and documented. This section covers how to write proper documentation.

For the style of docstrings, the Google style is used. Therefore, refer to the `Google Style Guide <https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings>`_ when writing docstrings.

Examples
--------

Module Example
^^^^^^^^^^^^^^
Reference for writing docstrings of a module can be found `here <https://github.com/google/styleguide/blob/gh-pages/pyguide.md#382-modules>`_.

.. code-block:: python

    """Write a short, one-line summary here.

    After a blank line, continue with a more elaborate description. Optionally include
    exported classes and functions and/or usage examples.

    Typical usage example:

        foo = ClassFoo()
        bar = foo.FunctionBar()
    """

Function Example
-------
Reference for writing docstrings of a function can be found `here <https://github.com/google/styleguide/blob/gh-pages/pyguide.md#383-functions-and-methods>`_.

.. code-block:: python

    def foo(bar: str, baz: int) -> str:
        """Write a short, one-line summary here

        If necessary, write a somewhat more extensive summary here. This can be as long
        as necessary.

        Args:
            bar (str): This is the description of parameter `bar`.
            baz (int): This is the description of parameter `baz`.

        Returns:
            str: Description of the return value.
        """
        return "Hello world!"

Class Example
-------------
Reference for writing docstrings of a class can be found `here <https://github.com/google/styleguide/blob/gh-pages/pyguide.md#384-classes>`_.

.. code-block:: python

    class Foo:
        """Again, write a short, one-line summary of the class

        Follow with longer class information.

        Attributes:
            bar (int): This is the description of parameter `bar`.
        """

        bar: int

        def __init__(self):
            """Initialize the Foo instance.

            Can't be bothered to write more.
            """
            self.bar = 0

# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
"""Arraylias Exception classes"""


class ArrayliasError(Exception):
    """BaseClass for Arraylias errors"""

    def __init__(self, *msg):
        """Set the error message."""
        super().__init__(*msg)
        self.msg = " ".join(msg)

    def __str__(self):
        """Return the message."""
        return repr(self.msg)


class AliasError(ArrayliasError):
    """Class for Arraylias dispatch errors"""


class LibraryError(ArrayliasError):
    """Class for Arraylias missing array library errors"""

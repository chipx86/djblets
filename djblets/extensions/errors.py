#
# errors.py -- Extension errors.
#
# Copyright (c) 2010-2011  Beanbag, Inc.
# Copyright (c) 2008-2010  Christian Hammond
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from __future__ import unicode_literals

from django.utils.translation import ugettext as _


class EnablingExtensionError(Exception):
    """An extension could not be enabled."""

    def __init__(self, message, load_error=None, needs_reload=False):
        """Initialize the error.

        Args:
            message (unicode):
                The detailed error message.

            load_error (unicode, optional):
                An exception from the attempt to enable the extension, or
                other useful information to display to the user to help
                diagnose the problem.

            needs_reload (bool, optional):
                Whether fixing this error requires reloading the extension.
        """
        super(EnablingExtensionError, self).__init__(message)

        self.load_error = load_error
        self.needs_reload = needs_reload


class DisablingExtensionError(Exception):
    """An extension could not be disabled."""
    pass


class InstallExtensionError(Exception):
    """An extension could not be installed."""
    def __init__(self, message, load_error=None):
        self.message = message
        self.load_error = load_error


class InstallExtensionMediaError(InstallExtensionError):
    """An error indicating that extension media files could not be installed.
    """


class InvalidExtensionError(Exception):
    """An extension does not exist."""
    def __init__(self, extension_id):
        super(InvalidExtensionError, self).__init__()
        self.message = _("Cannot find extension with id %s") % extension_id

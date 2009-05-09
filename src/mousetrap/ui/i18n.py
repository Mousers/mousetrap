# -*- coding: utf-8 -*-

# mouseTrap
#
# Copyright 2008 Flavio Percoco Premoli
#
# This file is part of mouseTrap.
#
# mouseTrap is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# mouseTrap is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with mouseTrap.  If not, see <http://www.gnu.org/licenses/>.

"""
Provides i18n support for mouseTrap using the gettext module.  Tells
gettext where to find localized strings and creates an alias, _, that
maps to the gettext.gettext function.  This function will accept a
string and return a localized string for that string.
"""

import os       # to get localdir path
import gettext  # to get gettext (i18n) support

# Alias gettext.gettext to _ and gettext.ngettext to ngettext
#
_ = gettext.gettext
ngettext = gettext.ngettext


# Tell gettext where to find localized strings.
#
localedir = os.path.join ("@prefix@", "@DATADIRNAME@", "locale")
gettext.bindtextdomain ("@GETTEXT_PACKAGE@", localedir)
gettext.textdomain("mousetrap")

#import debug

########################################################################
#                                                                      #
# Utility methods to facilitate easier translation                     #
#                                                                      #
########################################################################
#
# def _(txt):
#     return txt

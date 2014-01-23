# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2014 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Interfaces for the the help viewlets pages."""
from zope.interface.interface import Interface
from zope.viewlet.interfaces import IViewletManager


class IGSHelp(Interface):
    '''A marker interface for the Help system.'''


class IUserHelp(IViewletManager):
    '''A viewlet manager for user help'''


class IAdminHelp(IViewletManager):
    '''A viewlet manager for administration help'''

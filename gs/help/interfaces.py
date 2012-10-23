# coding=utf-8
"""Interfaces for the the help viewlets pages."""
from zope.interface.interface import Interface
from zope.viewlet.interfaces import IViewletManager

class IGSHelp(Interface):
    '''A marker interface for the Help system.'''

class IUserHelp(IViewletManager):
    '''A viewlet manager for user help'''

class IAdminHelp(IViewletManager):
    '''A viewlet manager for administration help'''

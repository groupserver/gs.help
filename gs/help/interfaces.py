# coding=utf-8
"""Interfaces for the the help viewlets pages."""
from zope.interface import Attribute
from zope.viewlet.interfaces import IViewletManager
from zope.schema import List, Text, Bool, Choice
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary

class IUserHelp(IViewletManager):
    '''A viewlet manager for user help'''

class IAdminHelp(IViewletManager):
    '''A viewlet manager for administration help'''


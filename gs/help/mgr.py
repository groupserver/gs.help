# coding=utf-8
# --=mpj17=-- Yes, this is a nasty hack to get around differences 
# between Zope 2.10 and Zope 2.13.
from zope.viewlet.manager import ViewletManagerBase
try:
    # Try the thing from Zope 2.13
    from zope.viewlet.manager import WeightOrderedViewletManager
except ImportError, e:
    # Fall back for Zope 2.10
    WeightOrderedViewletManager = ViewletManagerBase


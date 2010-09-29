Introduction
============

The help system for GroupServer consists of six pages:

`User Manual`_
  Step-by-step instructions on *how* to carry out tasks in GroupServer.

`User Guide`_
  A friendly guide on how to work in a group. It covers the *why* some
  tasks need to be carried out.

`FAQ`_
  Answers to questions that are often put to the support teams at
  OnlineGroups.Net and the E-Democracy.org Forums.

`Admin Manual`_
  Step-by-step instructions on *how* to carry out administration tasks
  in GroupServer.

`Admin Guide`_
  A friendly guide on how to set up and maintain groups. It covers *why* 
  some administration tasks need to be carried out.

Finally there is a shared Help page that links to the other five pages.

User Manual
-----------

The user manual contains step-by-step instructions on how the normal
users of GroupServer (anyone without group administration privileges)
should carry out tasks using the system.

The manual should be useful for normal-users, but the intended audience
is the *developers* of GroupServer. It allows a discussion of a system
without having to write code. When coding, the manual acts as a guide
as to the functionality that should be written. Finally, the help can
be used as a functional test.

User Guide
----------

FAQ
---

Admin Manual
------------

The administration manual contains ste-by-step instructions on how
GroupServer groups and sites are administrated. It omits any tasks
that require direct access to the filesystem, relational database,
or Zope Management Interface. Developers are the primary audience for
the administration manual, just like the `user manual`_.

Sections are added to the manual using a `viewlet`_. The simplest way
to create a section is to write a staic page snippet (contained within
a ``<div>`` element). This snippet should be in the module that it is
documenting. To add the section to the administration manual add the
following to the ``configure.zcml`` file::

  <browser:viewlet name="start-a-site-help"
    manager="gs.help.interfaces.IAdminHelp"
    template="browser/templates/help.pt"
    permission="zope.Public"
    weight="0" />

* The ``name`` is not used, but is necessary (to turn the underlying
  class into a *named adaptor*). The viewlet has the same name as the
  ID of the top element in the section (a ``<div>``) but with ``-help``
  appended.  This should help us find the ZPT page for the section if
  we are looking at the help page, yet avoid name-clashes

* The ``manager`` attribute determines the help page that the section
  will appear in. In this case help for an administrator is being
  provided so we attach to the ``gs.help.interfaces.IAdminHelp`` manager.

* The ``template`` is the static ZPT page that contains the help text.
  For most help static text will be fine. However, if you want
  to do something fancy you can specify a class, or both a
  class and a template. See the `viewlet`_ documentation.

* The ``permission`` is required; it will probabily always be set to
  ``zope.Public``.

* The ``weight`` is used to sort the sections. The help above is the
  first thing an administrator can do, so it is given a weight of 0.

Admin Guide
-----------

.. Resources

.. _GroupServer.org: http://groupserver.org
.. _viewlet: http://docs.zope.org/zope.viewlet/


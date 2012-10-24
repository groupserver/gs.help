Introduction
============

The help system for GroupServer_ consists of six pages:

#. `User Manual`_
#. `User Guide`_
#. `FAQ`_
#. `Administration Manual`_
#. `Administration Guide`_

Finally there is a shared Help page that links to the other five pages.

User Manual
===========

The user manual contains step-by-step instructions on *how* the normal
users of GroupServer (anyone without group administration privileges)
should carry out tasks using the system. While the manual should be useful
for normal-users, but the intended audience is the *developers* of
GroupServer. It allows a discussion of a system without having to write
code. When coding, the manual acts as a guide as to the functionality that
should be written. Finally, the help can be used as a functional test.

The `help viewlets`_ are provided by products external to ``gs.help``. This
product just provides the manual page that displays all the viewlets. The
instructions should be written in a standard `help style`_ to provide some
consistency.

Help Viewlets
-------------

The contents of the user manual is provided by viewlets_. Each product
provides its own help, and this help is collated by the manual.

The ``ZCML`` declaration for a section of the user manual usually looks
something like this::

  <browser:viewlet 
    name="gs-profile-signup-base-help"
    manager="gs.help.interfaces.IUserHelp"
    class="gs.viewlet.SiteViewlet"
    template="browser/templates/help.pt"
    permission="zope.Public"
    weight="0" />

* The ``name`` is taken from the name of the egg. The ``name`` is not used,
  but is necessary (to turn the underlying class into a *named adaptor*).
* The ``manager`` is always ``gs.help.interfaces.IUserHelp`` .
* The standard ``SiteViewlet`` is usually used as the class, so the 
  ``siteInfo`` can be used to personalise the text.
* The ``permission`` is always ``zope.Public``.

Help Style
----------

The style for the help is taken from `GNOME Documentation Style
Guide`_. Just like the GNOME documentation, the headings, and all
instructions, should be written in the *imperative* form, and the user
should be addressed as "you." The major differences to the GNOME
documentation are as follows:

* GroupServer users *visit* pages (rather than *go to* or *navigate to*).
* GroupServer users *click* links: 
  ``…click <samp class="link">Change Email Settings</samp>.``
* All interface elements *other* than links are explicitly labelled:

  - ``…click the <samp class="button">Add</samp> button.``
  - ``…select the <samp class="radio">privacy</samp> option.``
  - ``…enter your name in the <samp class="entry">Name</samp> entry.``

The contents of the viewlet is typically is made up of a ``<div>`` element;
the ``id`` attribute is set to the egg name, with ``-`` characters
replacing the ``.`` characters. The highest heading in these sections is an
``<h2>`` element. The instructions are provided in an ordered list
``<ol>``. An example of a help document is as follows::

  <div id="gs-profile-signup-base" class="section">
    <h2>Sign Up</h2>
    …
    <ol>
      <li>
        Visit the group that you wish to join.
      </li>
    …
    </ol>
    <p class="note">
      <strong class="label">Note:</strong>
      …
    </p>
  </div><!--gs-profile-signup-base-->

The ``note`` at the end is optional, and is provided to clarify the
instructions (such as particular privacy settings for the group being
necessary).


User Guide
==========

The user-guide provides some over-arching advice on how to use a group,
providing the *why*, rather than the *how* that is provided by the `user
manual`_. Unlike the manual, the complete contents of the guide is provided
by this ``gs.help`` product.

FAQ
===

The Frequently Asked Questions provides short snippets of help for
frequently occurring issues. The contents of the FAQ is provided by this
``gs.help`` product, but it is possible that individual products could
supply FAQ sections in the future.

Administration Manual
=====================

The administration manual contains ste-by-step instructions on *how*
GroupServer groups and sites are administrated. It omits any tasks that
require direct access to the filesystem, relational database, or Zope
Management Interface (ZMI). Developers are the primary audience for the
administration manual, just like the `user manual`_.

Most of the formatting for the administration manual is the same as for the
`help viewlets`_ that are used in the user manual. The following example
shows the ZCML configuration for an entry in the manual::

  <browser:viewlet name="gs-start-a-site-help"
    manager="gs.help.interfaces.IAdminHelp"
    template="browser/templates/help.pt"
    permission="zope.Public"
    weight="1" />

* The ``manager`` is always ``gs.help.interfaces.IAdminHelp``.
* The ``permission`` is always be set to ``zope.Public``.

Administration Guide
====================

A friendly guide on how to set up and maintain groups. It covers *why* some
administration tasks need to be carried out, including the different
*roles*. The entire contents of the administration guide is provided by
this ``gs.help`` egg.

Resources
=========

- Code repository: https://source.iopen.net/groupserver/gs.help
- Questions and comments to http://groupserver.org/groups/develop
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org
.. _viewlets: http://docs.zope.org/zope.viewlet/
.. _GNOME Documentation Style Guide: http://developer.gnome.org/gdp-style-guide/stable/

.. SPDX-License-Identifier: CC-BY-SA-4.0

.. Copyright (C) 2019 embedded brains GmbH
.. Copyright (C) 2019 Sebastian Huber
.. Copyright (C) 2018 Joel Sherill
.. Copyright (C) 2016 Chris Johns <chrisj@rtems.org>

.. index:: community; developers

.. _Contributing:

Contributing
************

How to Contribute?
==================

You can contribute to the RTEMS Project in various ways, for example:

* participation in mailing list discussions, helping other users

* documentation updates, clarifications, consolidation, fixes

* bug fixes, bug report consolidation

* new BSPs

* new device drivers

* new CPU (processor architecture) ports

* improvements in the existing code base (code size, code clarity, test
  coverage, performance optimizations)

* new features

* RTEMS Tools improvements

Most contributions will end up in patches of the RTEMS source code or
documentation sources.  The patch integration into the RTEMS repositories is
done through a
:ref:`patch review process <PatchReviewProcess>`
on the :r:list:`devel`.

Code Formatting and Style Checking
==================

For the core parts of RTEMS, the coding style is defined 
`here <https://docs.rtems.org/branches/master/eng/coding-conventions.html>`_. It 
can get quite tricky most especially for newcommers to get it right when sending 
patches. As a result, the RTEMS Project has put in place a functionality to help 
new commers and existing developers automatically check for style differences in 
their patches. 

This functionality is enabled by using an already written git pre-commit hook 
script found in rtems.git/hooks/pre-commit. Follow these steps to make use of it:

* Firstly, make sure you have  Python 3 installed.
* Install clang-format

.. code-block:: none

   sudo apt install clang-format
   
* Go to rtems.git/.git/hooks/pre-commit.sample and rename pre-commit.sample to 
  pre-commit.
* Copy and paste the contents of rtems.git/hooks/pre-commit to the renamed file 
  (rtems.git/.git/hooks/pre-commit).

At this point, everything is set and you can start contributing to the codebase. 
This will operate in the **default mode** in which upon commiting, the script checks for style differences and if it finds any, it prints out the number of style issues as well as the affected files. Also, the commit aborts. Below is an example of what it should look like...

.. code-block:: none

      Checking for style differences... 

      Files affected: 
    cpukit/score/src/mpci.c
    cpukit/score/src/profilingisrentryexit.c
    cpukit/score/src/schedulercbs.c

     StyleWarning: You have about a total of 7 style issue(s) in the 3 file(s) listed 
     above
     ERROR: Commit aborted due to code format inconsistencies with RTEMS 

There is another mode known as the **nonstrict mode** which does everything in the 
default mode except for the fact that the commit does not abort. This mode is enabled 
by simply making a change to your local git configuration file before commiting:

.. code-block:: none

   git config style.mode "nonstrict"

Furthermore, there is another mode which prints out the style issues but in more detail 
clearly showing what the patch looked like before and and how it is supposed to look like. 
It is enabled just like the ``nonstrict`` mode:

.. code-block:: none

    git config style.verbose "verbose"

In order to bypass the entire pre-commit hook script, add the ``--no-verify`` option 
upon commiting.

Preparing and Sending Patches
=============================

The RTEMS Project uses Git for version control.  Git has a special command to
prepare patches intended for mailing lists:
`git format-patch <https://git-scm.com/docs/git-format-patch>`_.
Create logically connected patches as a patch series ideally accompanied by a
cover letter (``--cover-letter`` option).  You can send patches via email
through a Git command:
`git send-email <https://git-scm.com/docs/git-send-email>`_.

.. _ChecklistForPatches:

Checklist for Patches
=====================

Check the following items before you send a patch to the :r:list:`devel`:

* The author name of the patch is your full name.

* The author email of the patch is your valid email address.

* The licence conditions of the contributed content allow an integration into
  the RTEMS code base.

* If you are the copyright holder of the entire patch content, then please
  contribute it under the
  `BSD-2-Clause <https://git.rtems.org/rtems/tree/LICENSE.BSD-2-Clause>`_
  license.  For documentation use
  `CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0/>`_.

* Make sure you have a pregnant subject which does not exceed 50 characters in
  one line.  Use a "topic: The pregnant subject" style.  A topic could be the
  main component of patch.  Just have a look at existing commit messages.

* The patch has a good commit message.  It should describe the reason for the
  change.  It should list alternative approaches and why they were not chosen.

* The code changes honour the coding style.  At least do your changes in the
  style of the surrounding code.

* The patch contains no spelling mistakes and grammar errors.

* The patch is easy to review.  It changes one thing only and contains no
  unrelated changes.  Format changes should be separated from functional
  changes.

* If the patch corresponds to a ticket, it should have "Close #X." or
  "Update #X." as the last line in the commit message to update status once it
  is committed to the repository.

* The patch builds.  All RTEMS tests link with this patch.

* The patch does not introduce new compiler warnings.

* The patch does not introduce new test failures in existing tests.

Patch Review Process
====================

Patches sent to the :r:list:`devel` undergo a
:ref:`patch review process <PatchReviewProcess>`.
Once a patch series is accepted for integration into the RTEMS code base it is
committed by an
`RTEMS maintainer <https://git.rtems.org/rtems/tree/MAINTAINERS>`_.  The
maintainers are usually quite busy with all sorts of stuff.  If you do not get a
response to a patch series submission to the mailing list after five work days,
please send a reminder.  It helps if you follow the :ref:`ChecklistForPatches`.
An easy to review patch series which meets the quality standards of the RTEMS
Project will be more likely get integrated quickly.

.. _PatchReviewProcess:

.. figure:: ../../images/user/patch-review.*
   :width: 70%
   :alt: RTEMS Patch Review Process
   :figclass: align-center

   RTEMS Patch Review Process.

Why Contribute?
===============

If you are writing a major extension to RTEMS, such as a port
to a new CPU family (processor architecture) or model, a new target board, a
major rewrite of some existing component, or adding some missing functionality,
please keep in mind the importance of keeping other developers informed.
Part of being a good cooperating member of the RTEMS development team is the
responsibility to consider what the other developers need in order
to work effectively.

Nobody likes to do a lot of work and find it was duplicated effort.
So when you work on a major new feature, you should tell
:r:list:`users` what you are working on, and give
occasional reports of how far you have come and how confident
you are that you will finish the job. This way, other developers
(if they are paying attention) will be aware which projects would
duplicate your effort, and can either join up with you, or at
least avoid spending time on something that will be unnecessary
because of your work. If, for whatever reason, you are not in a
position to publicly discuss your work, please at least privately
let an
`RTEMS maintainer <https://git.rtems.org/rtems/tree/MAINTAINERS>`_
know about it so they can look out for duplicated effort or possible
collaborators.

You should also monitor the :r:list:`users` and :r:list:`devel`
to see if someone else mentions working on a similar
project to yours. If that happens, speak up!

If you are thinking of taking a contract to develop changes
under a temporary delayed-release agreement, please negotiate
the agreement so that you can give progress reports before the
release date, even though you cannot release the code itself.
Also please arrange so that, when the agreed-on date comes,
you can release whatever part of the job you succeeded in doing,
even if you have not succeeded in finishing it.
Someone else may be able to finish the job.

Many people have done RTEMS ports or BSPs on their own, to a wide
variety of processors, without much communication with the RTEMS
development team. However, much of this work has been lost over
time, or have proven very hard to integrate. So, what we are asking
is that, to the maximum extent possible, you communicate with us
as early on and as much as possible.

Common Questions and Answers
============================

Here are some questions RTEMS porters may have with our answers to
them. While the focus here is on new ports and BSPs, we believe that
the issues are similar for other RTEMS development efforts including
student efforts to implement new algorithmic optimizations.

    Our engineers understand our target environment better than anyone else, and
    we have a tight schedule. Why should we work with the RTEMS developers, when
    we can get the code out faster by whacking it out on our own?

You understand your target environment better than anyone else.
However, the RTEMS developers understand RTEMS better than anyone
else; furthermore, the RTEMS developers tend to have a wide breadth
of experience across a large number of processors, boards, peripherals,
and application domains. It has been our experience that few problems
encountered in embedded systems development are unique to a particular
processor or application. The vast majority of the time an issue that
arises in one project has also shown up in other projects.

The intimate knowledge of RTEMS internals as well as a wide breadth of
embedded systems knowledge means that there is a good chance that at
least one RTEMS developer has already addressed issues you are likely
to face when doing your port, BSP, or application. The developers can
help guide you towards a workable long term solution, possibly saving
you significant time in your development cycle.

If getting the sources into the official RTEMS distributions is one of
your goals, then engaging other RTEMS developers early will also likely
shorten your development time. By interacting as early as possible you
are more likely to write code which can be easily accepted into the official
sources when you are finished. If you wait until you think you are done
to begin interacting with the RTEMS team, you might find that you did
some things wrong and you may have to rewrite parts of your RTEMS port,
which is a waste of your valuable time.

    Why should we care if our port is integrated into the official RTEMS
    sources? We can distribute it ourselves to whoever is interested.

Yes, the RTEMS licenses allows you to do that. But by doing so, you end up
having to maintain that code yourself; this can be a significant
effort over time as the RTEMS sources change rapidly.

You also lose the advantage of wider exposure by including your port
in the official RTEMS sources maintained by the RTEMS Project.
The wider exposure in the RTEMS developer and tester community will
help keep your work up to date with the current sources. You may even
find that volunteers will run the ever-growing test suite on your port
and fix problems during the development cycle -- sometimes without your
intervention.

It has been our experience that integrated ports tend to ultimately
be of better quality and stay up to date from release to release.

    Why should we communicate up front? We are happy to let the RTEMS developers
    integrate our stuff later.

See above. It will save work for you over both the short and the
long term, and it is the right thing to do.

    Aspects of my target environment that my application exploits are still
    under NDA.

Nevertheless, if the target hardware is built of any commercial parts
that are generally available including, but not limited to, the CPU
or peripherals, then that portion of your work is still of general use.
Similarly, if you have written software that adheres to existing API or
interface standards, then that portion is also of general use.
Our experience is that most embedded applications do utilize a custom
mix of hardware and application, but they are built upon layers of hardware
and software components that are in no way unique to the project.

If you are porting to an unreleased CPU family or model, then just
announcing it is important because other RTEMS users may be planning
to use it and some of them may already be trying to port RTEMS on
their own. Your customers might be happier to know that your port
will eventually be available. Also, there is no requirement that RTEMS
include all features or ports at any particular time, so you are encouraged
to submit discrete pieces of functionality in stages.

Assume that your processor has some new functionality or peripherals.
However that functionality is still covered by NDA, but the basic core
architecture is not. It is still to your advantage to go ahead and work
with the developers early to provide a "base port" for the CPU family.
That base port would only use the publicly available specifications
until such time as the NDA is lifted. Once the NDA is lifted you can
work with the developers to provide the code necessary to take
advantage of the new functionality.

Ultimately, cooperating with the free software community as early as
possible helps you by decreasing your development cycle, decreasing
your long term maintenance costs and may help raise interest in your
processor by having a free compiler implementation available to
anyone who wants to take a look.

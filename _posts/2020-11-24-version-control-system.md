---
published: false
key: '!!str'
title: Version Control System
---
# The Problem

If you happen to go through the following scenario as you are struggling to keep renaming the updated files, then version control system is an
option foryou.

1. index.html
2. index_new.html
3. index_new_v2.htm|
4. index_new_v4.htm|
5. index_new_v2_final.html
6. index_new_v2_really_ﬁnal.html

![bad-version-control.png]({{site.baseurl}}/images/bad-version-control.png)

# Solution

However, when it comes to maintaining a record of changes in documents, structure is required. That's where version control (also known as source or revision control) comes in.

Version control is a system that records the changes made to a file or set of tiles over time in such a way that it is possible to recover specific versions later. If a mistake is made. clevelopers/ designer can turn back the clock and compare earlier versions of the code to help fix the mistake while minimizing disruption to all team members.

Version cintrol system is useful because:

1. You can revert back to specific ‘versions’ of your code.
2. Collaboration on the same work is possible because specific changes and associated contributors are tracked.

Git as the state of the art in version control. One can maintain multiple versions of a file, conduct multiple experiments and yet preserve a clean “latest” version of work. It lets users roll back their changes when needed, and one can even rewrite history when you feel like it.

# Local Version Control System

Many people's version—control method of choice is to copy files into another directory or rename the files. This approach is very common because it is so simple, but it is also incredibly error prone. It is easy to forget which directory you're in and accidentally write to the wrong file or copy over ﬁles you don't mean to.
To deal with this issue, programmers long ago developed local VCSs that had a simple database that kept all the changes to files under revision control.

![version_control_local.png]({{site.baseurl}}/images/version_control_local.png)

One of the more popular VCS tools was a system called RCS, which is still distributed with many computers today. RCS works by keeping patchsets (that is, the differences between files) in a special format on disk; it can then re—create what any file looked like at any point in time by
adding up all the patches.

# Centralized & Distributed Version Control System
Centralized version control systems are based on the idea that there is a single "central" copy of your project somewhere (probably on a server), and programmers will "commit" their changes to this central copy. Centralized version control systems like Subversion (SVN), CVS, Perforce.

Distributed version systems do not necessarily rely on a central sen/er to store all the versions of a project's files. Instead, every developer “clones” a copy of a repository and has the full history of the project on their own hard drive. This copy (or “clone") has all of the metadata of the original. Some distributed version control systems are Git, CVS, Subversion, Mercurial.

![version-control-systems.png]({{site.baseurl}}/images/version-control-systems.png)


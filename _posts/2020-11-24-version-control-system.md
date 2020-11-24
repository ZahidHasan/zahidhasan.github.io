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


Simple Work-flow of Version Control System

1. Pull down any changes other people have made from the central server.
2. Make your changes, and make sure they work properly.
3. Commit your changes to the central sen/er, so other programmers can see them.

# Introduction to Git and Github
Git is a free and open source version control system, originally created by Linus Torvalds in 2005. Unlike older centralized version control systems such as SVN and CVS, Git is distributed: every developer has the full history of their code repository locally.
Github [github.com](github.com) is a service for hosting software repositories managed by the Git version control system.

# Pull Work-flow: Working on your own project
1. Create an empty project on GitHub.
2. Create an empty project in your local hard disk using git.
3. Add the GitHub repo to the local project.
4. Pull] Fetch remote project into local one.
5. Make some changes in the local project.
6. Add changed files to got for tracking (staging).
7. Commit.
8. Push the project into GitHub.

# Clone Work-flow : Working on your own project
1. Create an empty project on github.
2. Clone the project into local hard disk.
3. Make some changes in the project.
4. Add changed files to got for tracking (staging).
5. Commit.
6. Push the project into GitHub.


### Pull vs Clone
**Git pull**: when you do a git pull, it gets all the changes from the remote or central repository and attaches it to your corresponding branch in your local repository.

**Git fetch**: when you do a git fetch, it gets all the changes from the remote repository, stores the changes in a separate branch in your local repositoiy and if you want to reflect those changes in your corresponding branches, use a git merge to do that.
To summarize,

**git pull = git fetch + git merge**

# Fork work-flow: Contributing to other's project

1. Fork the project.
2. Create a topic branch from master .
3. Make some commits to improve the project.
4. Push this branch to your GitHub project.
5. Open a Pull Request on GitHub.
6. Discuss, and optionally continue committing.
7. The project owner merges or closes the Pull Request.

### Fetch, Clone, Fork
`git clone` is basically a combination of:

- `git init` (create the local repository)
- `git remote add` (add the URL to that repository)
- `git -Fetch` (fetch all branches from that URL to your local repository)
- `git checkout` (create all the files ofthe main branch in your working tree)

Therefore. no, you don't have to do a git init , because it is already done by git clone .
Forked repositories are generally "sen/er»side clones" and usually managed and hosted by a 3rd party Git service like Bitbucket and Github.
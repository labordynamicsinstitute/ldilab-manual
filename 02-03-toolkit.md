# Toolkit

In this chapter, we will introduce you to a few of the toolkits that we will use for this project, and that you may find useful for most future data and code work.

## Command line

The shell (command line) is a power tool that allows you to do complex things with just a few keystrokes. You can combine and chain things together. Later in your studies, you may find that it is a fundamental tool used in combination, or even core, to other powerful tools and computing resources (including “high-performance computing” supercomputers). 

For our purpose, there are a few key features that are important:

- it is present on all the computers you will be working on (with the possible exception of the Bash shell on Windows, which we will get to shortly).
- it allows us to show you how things work without paying attention whether you are on a Mac, Linux, or Windows, or if you prefer one or the other fancy windowed program.

We will leverage the excellent lessons provided by the Software Carpentries, somewhat optimized for our purposes. 

> - Go to our [customized shell lesson](https://labordynamicsinstitute.github.io/shell-novice/)
> - See the [full lesson at Carpentries](https://swcarpentry.github.io/shell-novice/)

Note: we will walk you through the basics very quickly, but you will want to try this out later, on your own time, before we get to the Git lesson later.


## Markdown

(based on [this Carpentries tutorial](https://carpentries-incubator.github.io/jekyll-pages-novice/))

Markdown is a lightweight markup language, i.e. **a convention for adding
style information to textual content**.

Having a rather minimalistic syntax, text formatted in Markdown is comparably
readable.
This might be one reason for Markdown having become the language of choice
for formatted user input on websites like, for example:
- [Stack Exchange](https://stackexchange.com/)
- [GitHub](https://github.com/)
- [GitLab](https://about.gitlab.com/).


### Where to Start Writing Markdown?

A lot of tools for rendering Markdown source code exist.
Rendering is the process of generating a nice view of the content
using the style information included in the source text.
Chances are high, your editor can do this. Chances are, many websites use and render it. It is the native way to add formatting on Github, Bitbucket, etc.

In our case, we will use Visual Studio Code to write and preview Markdown. All of our reports will be written in Markdown. This tutorial is written in Markdown!

> - Open up Visual Studio Code, 
> - Add the line `# My Title` 
> - and save as a new file called 'README.md'

Let's add `Some **bold** font` and see what happens when we preview it using the preview button.

> Where is the Preview button? Read the introduction to the [Visual Studio Code: Writing Markdown](https://code.visualstudio.com/docs/languages/markdown) article to find out!

If new sections were added you will also find green vertical bars visually highlighting the new content.



### Writing Markdown

Now that we know about the editing interface and preview tab of our projects `README.md`
we can use it as a text editor and investigate selected Markdown features.

Our `README.md` already contains vanilla text and
two formatting features:
- Heading `# My Title`
- Emphasis using `**bold**`.

Let's learn some more Markdown by adding some formatting and see what happens when we preview it in the preview tab.
Add the following to your `README.md` file.

~~~
# My Title

Repo for learning how to write Markdown

## Learning Markdown

Vanilla text may contain *italics* and **bold words**.

This paragraph is separated from the previous one by a blank line.
Line breaks  
are caused by two trailing spaces at the end of a line.

[Carpentries Webpage](https://carpentries.org/)


### Carpentries Lesson Programs:
- Software Carpentry
- Data Carpentry
- Library Carpentry
~~~

You can see in the preview tab again to see how the formatting renders.


> ### Markdown trailing spaces are meaningful
>
> In the example above there are two spaces at the end of `Line breaks  `.
> These introduce what is called a **hard line break**, causing that paragraph to
> continue in the next line by adding a `<br/>` to the generated HTML.  
>
> If you break the line in a markdown file but don't include the two trailing spaces
> the generated HTML will continue in the same line **without** introducing a `<br/>`.
> This is called a **soft line break**.
>
> In some cases you may find that **soft line breaks** do introduce a `<br/>`.
> This can happen when using different [markdown flavors](#markdown-flavours).
>
> See for instance:
> ~~~
> Soft line
> break
>
> Hard line  
> break
> ~~~


> ### Exercise: Try Out Markdown
> [Online Markdown Tutorial](https://www.markdowntutorial.com/)


### Four reasons you should learn Markdown:

1. Less formatting than HTML
2. Easy to read even with formatting
3. Commonly used for websites and software development
4. We use it in our reports!

## Git

Git is a version control system, which we use extensively in the LDI Replication Lab.

### Why a version control system?

You can review  history of code or text to find out:

- _Which changes were made?_ Identify the lines that have been changed.
- _Who made the changes?_ If multiple people work on a project, who made the particular change. Also tabulate contributions to the project by person.
- _When were the changes made?_
- _Why were changes needed?_ The ability to attach _log messages_ provides a lot of information.

### Key Git Concept:  repository

A _repository = Git project_ is a  collection of files and folders, along with each file's revision history. There are

- _commits_: collections of additions or modifications, a snapshot
- _branches_: versions or variants of the main repository
- _clones_: Each copy of the repository is complete - fully functional
- _staging area_: an area on your computer where files and changes are collected prior to finalizing a _commit_

### Key Git Concept:  Github or Bitbucket?

There are multiple services that host repositories, and that can serve as a central reference point for these repositories.

- You _push_ to another repository - that could be on your buddy's computer, to a central entity (Github, Bitbucket) - however it is defined.
- You _pull_ changes from another repository.
- A _pull_ + _push_ is sometimes referred to as a _sync_ (synchronisation)

### Basic Git Commands

(also see the [Cheatsheet for Git](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet))

- `git clone` creates a local copy of a project that already exists remotely. The clone includes all the project's files, history, and branches.

- `git add` stages a change. Git tracks changes to a working copy, but it's necessary to stage and take a snapshot of the changes to include them in the project’s history. This command performs _staging_, the first part of that two-step process. Any changes that are staged will become a part of the next snapshot and a part of the project's history.

- `git commit` saves the snapshot to the project history and completes the change-tracking process. In short, a commit functions like taking a photo. Anything that's been staged with `git add` will become a part of the snapshot with `git commit`.

+ `git status` shows the status of changes as untracked, modified, or staged.

- ` git pull` updates the local line of development with updates from its remote counterpart. You use this command if a teammate has made commits to a branch on a remote, and they would like to reflect those changes in their local environment. Or you made a commit on your laptop, and now want to continue the work on a remote desktop server.

- `git push` updates the remote repository with any commits made locally to a branch. Think of it as publishing your changes.

### A Tutorial

We will again leverage the excellent lessons provided by the Software Carpentries, somewhat optimized for our purposes. 

> - Go to our [customized Git lesson](https://labordynamicsinstitute.github.io/git-novice/)
> - See the [full lesson at Carpentries](https://swcarpentry.github.io/git-novice/)


### Some additional resources

- [General resources](https://try.github.io/)
- [Git tutorial](https://guides.github.com/introduction/git-handbook/)


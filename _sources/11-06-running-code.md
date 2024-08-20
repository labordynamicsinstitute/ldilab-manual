(running-code-partb)=
# Running Code (Part B)

In this stage, you will run the code, by using the provided data. The `REPLICATION-PartB.md`  is the report!



:::{admonition} Be sure to use the `REPLICATION-PartB.md` for this section!
:class: dropdown

As part of the [automated processing](running-populate-icpsr), the `REPLICATION.md` is split into two parts, `REPLICATION-PartA.md` and `REPLICATION-PartB.md`. Somebody else may be working on Part A at the same time as you are working on Part B. Please be sure to use the correct file for your work.

:::

## Signal that you are working on Part B

To signal that you are starting to run the code, you will now transition the JIRA subtask to "`Code is running`".

![Move to Part B to Code is running](images/jira-in-progress-partb-2.png)


## Principles

Keep a log of what you do, what you find, and what does not work, in the `REPLICATION-PartB.md`, under *Replication Steps*.

- Document if you manually downloaded data from anywhere other than the authors' deposit.
- Document any manual changes you made to the deposit structure (renamed file, created directory).
- If you run into error messages that are not captured by the "log file" (see below), then screenshot, or copy verbatim, into the report.

You should also run code so that it generates an actual "log file". How to do this depends on the software. 

:::{admonition} We have an [entire section of the manual](running-code-general) for this!

Check the software-specific guidelines in the manual's [section on running code](running-code-general), debug the code, and set the code to run.
:::

:::{note}

Sometimes, code can run for a long time. Leave the Jira ticket in `Code is running` to signal that there is activity there. Remember to come back regularly to check on it, and remember to commit all changes immediately (before running code).
:::

:::{admonition} If you appear to be stuck...
:class: warning

then as soon as possible, call on

- your supervisors (Sofia, Lars)
- more senior RAs (pre-approvers) or graduate students
- bring it up in a Monday or Thursday meeting

Do not let yourself be blocked too long!

:::

Once you have run the code, come back here to continue!


### Details

- If code runs for a long time, record in the Jira issue (as a comment) when you started the code. 
- Use the `Computing Environment` to record where (CCSS, BioHPC node, etc.) you started the code.
- It is not unusual for code to run for several days. You can start a new case in the meantime!

## When you run into problems

Before you even write up your [Findings](partc), you may run into problems. In order to clearly document the problem to somebody else on the team who can reference it, state the problem clearly in the Comments of the Jira ticket. Ideally, you will also reference the filename, both by name and by reference to location within the repository, as well as a log file showing the problem. 


:::{admonition} Referencing Logfiles
:class: info dropdown

You should point to the exact line where the problem appears to show up, as follows:

**Step 0**

Before doing anything, 

- `git add` any modified and any added files
- `git commit` with a commit message that identifies the problem
- `git push`

**Step 1**

Navigate to the Bitbucket repository of this case. If you are doing everything right, you should see the files you just committed and pushed, as well as the log files you are creating (if you are not creating log files, review [Stata instructions](running-code-in-stata), [R instructions](running-code-in-r), or other relevant instructions). You should see a `logs` directory:

![Log directory](images/bitbucket-logfiles-1.png)

Navigate to the logfile you want to reference:

![specific logfiles](images/bitbucket-logfiles-2.png)

In general, the error will be in the last lines of the logfile:

![location of error message](images/bitbucket-logfiles-3.png)

Click on the line number (on the left margin). This should highlight a relevant line:

![highlighted row](images/bitbucket-logfiles-4.png)

Now copy the URL, and paste it into the Comment field of Jira:

![line number highlighted](images/bitbucket-logfiles-5.png)

This allows you point the reader/helper to a specific line immediately, making it very clear where you think the error occurs. In some cases, the error might actually happen earlier, and the logfile provides a lot of information, if not always enough, to help debug.

:::

## Wrapping up

Once the code has run, **error-free and creating the intended output** (as far as you can tell), it is time to wrap up this sub-tasks.

- Review again the **Replication steps** section, please include all steps that you took.

```{note}
You, or somebody else, will compare the output to the manuscript in the next step! You may, however, simply check that output exists, regardless of its specific content, before moving forward.
```

![Move to Part B to Code has completed](images/jira-in-progress-partb-3.png)

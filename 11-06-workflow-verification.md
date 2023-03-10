
# Verification

In this stage, you are verifying the code, by using the provided data, or by inspecting the completeness of the source code. The [REPLICATION.md](`r config$url$templmd`REPLICATION.md) is the report.

Keep a log of what you do, what you find, and what does not work, in the `REPLICATION.md`, under *Findings*.
  - For codes using STATA, we provide a template of `config.do` in the repository. It creates log files and saves it in the repository. Instructions for using `config.do` is in [Appendix F](https://labordynamicsinstitute.github.io/replicability-training-curriculum/using-config-do-in-stata.html)

````{tab-set}

```{tab-item} CISER 

- If using Stata,  see [Stata related procedures](stata-related-procedures).
- If using Matlab, open up Matlab. This might take a while.
- If using Python, we suggest in general to use `git bash`, but you may also be able to use the Python shell. Consult with your supervisor, or the CISER helpdesk.

Consult the [Replication Wiki](https://github.com/labordynamicsinstitute/replicability-training/wiki) for some help in debugging:

- [Stata tips](https://github.com/labordynamicsinstitute/replicability-training/wiki/Stata-Tips)
- [Python tips](https://github.com/labordynamicsinstitute/replicability-training/wiki/Python-Tips)
- [R tips](https://github.com/labordynamicsinstitute/replicability-training/wiki/R-tips)

```

```{tab-item} Github Codespaces (CS) 

- If using Stata,  see [Stata related procedures](stata-related-procedures) for how to prepare files. However, you will use the command-line to run Stata.
  - To run Stata, type `stata-mp -b do main.do` (adjust to account for whatever the program or programs are called). You can do this for every one of the programs. 
- To run R, type `Rscript program.R` or `R --vanilla < program.R > program.Rlog 2>&1` (which will always create a log file)
- To run Python code, type `python3 program.py` or whatever the authors specify.
- If you need other versions of Stata, R, Python, etc. (e.g. Stata 16), you may need to choose a different CS environment that allows to run Docker. See [Docker tips](https://github.com/labordynamicsinstitute/replicability-training/wiki/Docker-Tips)

```
````

Do not forget to add files output by the code to the repository (log files, figures -- `eps, png, pdf` -- and tables -- `tex, txt, xlsx, xls`). Typically (but not always), you can type `git add *` to add any allowable files, but careful with large data files, and sometimes code will output `.txt` files, which you have to force-add: `git add -f name.txt`.

You should commit your report with intermediate results as you have them. Do __not__ wait until you have all the results finished. Commit frequently!

> Add (report, modified files)! Commit! Push!

You can now proceed to change the status to `Writing Report`.

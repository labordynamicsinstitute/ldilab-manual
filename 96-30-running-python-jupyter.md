(python-related-procedures)=
# Python-related procedures

In this section, we will show you a few things related specifically to running code reproducibly with Python and Jupyter notebooks. . For more general debugging tips for Python and other computer languages, see [our wiki](https://github.com/labordynamicsinstitute/replicability-training/wiki/Python-Tips).

## Python package installation

Most systems will have the standard Python package installer `pip` already installed, so you should be able to use it.

:::{admonition} If `pip` is not available...
:class: dropdown

Should for some reason `pip` not be installed, you can install `pip` into your user library using the procedures outlined at <https://pip.pypa.io/en/stable/installation/#ensurepip>. In a nutshell, for Linux

```bash
python -m ensurepip --upgrade
```

should work.

:::


## Best practice to reproduce a Python paper (Python environments)

You should create a Python environment that is dedicated to the project. See [Anaconda instructions](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands) as one possible method, [venv](https://docs.python.org/3/library/venv.html) as another one, though others exist.

Here's `venv` version in a nutshell ([full guide](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment))

- Ensure `venv` exists:
```
pip3 install pyenv
```
- Create a new environment
```
python3 -m venv /path/to/new/virtual/environment
```
or if using relative paths
```
python3 -m venv env
```

which will create `/path/to/new/virtual/environment` or (relative to your current working directory) `env`. That directory will now contain all of your project-related Python packages.

To activate:
```
source env/bin/activate
```

On Windows Bash (depends on install)

```
python -m venv env
source env/Scripts/activate
```

To deactivate:
```
deactivate
```


## Making Python code dynamic

In general, Python code should not have hard-coded paths. Python programs are aware of their own location, and other directories should be relative to that. However, some authors may still follow (econ-specific) norms, and hard-code paths. Similar to our approach for [Stata](stata-step4-modifying-paths), [R](base-root-directory-r), and MATLAB, you can use the `rootdir` principle to make the code more portable/dynamic.

In that case, do the following:

Say the author has code like

```python
xlsread('C:\Users\me\submission\AEJMacro\yesterday\data.xlsx')
```


At the top of the program, add the following lines:

```python
import os
rootdir = os.path.realpath(__file__)
```

Then, wherever the hard-coded path appears, replace it with:

```python
xlsread(os.path.join(rootdir,'data.xlsx'))
```

Alternatively, if the author uses a change of working directory, then 

```python
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
```
would change the working directory to the location of the file being run. 

## Installing packages

Sometimes, authors will list the packages they used. There are a few options:

### They provide a `requirements.txt` file

If the authors provide a `requirements.txt` file, you can install all the packages at once. From an appropriate terminal, run:

```bash
pip install -r requirements.txt
```

### They provide a `environment.yml` file

If the authors provide an `environment.yml` file, they used Conda as the Python system manager. From an appropriate terminal, run:

```bash
conda env create -f environment.yml
```

### They provide a list of packages

If the authors provide a list of packages, the easiest way is to create a simple `requirements.txt` file with a text editor (e.g., VS Code), then proceed as with the first option.



### Using Anaconda Package manager

This is known to work on  CISER (CCSS-Classic).

:::{admonition}  This may not be the way it works on CCSS-Cloud. 
:class: dropdown
Needs an update
:::

If using the default "Jupyter" link in the Start Menu, the working directory won't be right. Assuming that you have set your Workspace to `L:\Documents\Workspace`, the following will create a Jupyter Notebook in the right location (thanks to Louis Liu for creating this Howto)

#### Search "anaconda prompt" from the start menu. right click on the app when it appears and pin it to the taskbar.

![Step 1](images/Jupyter_howto_step1.png)

#### Right click on anaconda prompt in the taskbar (looks like a black window, similar to command line or terminal). Right click on "anaconda powershell prompt" in the tasks menu that pops up, and then properties.

![Step 2](images/Jupyter_howto_step2.png)

#### In the properties window, go to the shortcut tab and change the "Start in:" field to U:\Documents\Workspace or whichever directory you keep your bitbucket repos in. Click apply.

![Step 3](images/Jupyter_howto_step3.png)

#### Next, click on the anaconda prompt shortcut in the taskbar. When anaconda prompt opens, enter the command "`Jupyter notebook`"

![Step 4](images/Jupyter_howto_step4.png)

### Conda on BioHPC

If a replication package uses `conda` for package management, rather than `pip`, follow instructions [at BioHPC](https://biohpc.cornell.edu/lab/userguide.aspx?a=software&i=574#c) on how to install `miniconda` in your home directory, then add the line

```bash
source $HOME/miniconda3/bin/activate
```

at an appropriate location in the code (for instance, replacing `module load conda`).


## Running Jupyter Notebooks

### Manually

In order to run Jupyter notebooks, do the following, once you have opened the Jupyter Notebook or Jupyter Lab interface:

- Navigate to the directory where the notebook is located
- Open the notebook
- Clear all the cells: `Cell` -> `All Output` -> `Clear`
- Run all the cells: `Cell` -> `Run All`
- Save the notebook: `File` -> `Save and Checkpoint`

### From the command line

You should also be able to do the following from the command line:

::::{tab-set}

:::{tab-item} Linux/macOS

If you have a LaTeX installation, you can convert the notebook to a PDF using the following commands:

```bash
# requires a latex installation
pip install nbconvert
jupyter nbconvert --to notebook --execute mynotebook.ipynb
jupyter nbconvert --to pdf                mynotebook.ipynb
```

Alternatively, you can convert the notebook to a PDF more closely resembling the HTML view using the following command:

```bash
pip install nbconvert
pip install pyppeteer
jupyter nbconvert --to notebook --execute mynotebook.ipynb
jupyter nbconvert --to webpdf --allow-chromium-download mynotebook.ipynb
```

:::

:::{tab-item} Windows

Not sure yet. Needs augmentation.

:::

::::

## Document the packages YOU used

If you had to iteratively install packages, you should run the following command at the end of your whole process:

```bash
pip freeze > requirements.txt
```

and add that output (the contents of the `requirements.txt` file) to the repository, and to an appendix in the report. Take care to not overwrite author-provided `requirements.txt` files.

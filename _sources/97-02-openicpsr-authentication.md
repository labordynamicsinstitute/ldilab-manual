(openicpsr-authentication)=
# openICPSR Authentication

## First-time 

Go to [https://www.openicpsr.org/openicpsr/](https://www.openicpsr.org/openicpsr/) and in the top-right corner, choose `Login/Create an account`. You will be redirected to the ICPSR account web page.

- You should create an account with your `netid@cornell.edu`
- You can link your account with your Netid via Google student authentication BUT:
- You must still create a separate password for use by the [automation scripts](setup-bash).

:::{warning}

If you run the script and get an error message like the following:

```
Downloading file: icpsr-123456.zip
Traceback (most recent call last):
  File "/workspaces/codespaces-stata-r-skeleton-private/aearep-nnnn/./tools/download_openicpsr-private.py", line 151, in <module>
    with zipfile.ZipFile(outfile) as z:
  File "/usr/lib/python3.10/zipfile.py", line 1269, in __init__
    self._RealGetContents()
  File "/usr/lib/python3.10/zipfile.py", line 1336, in _RealGetContents
    raise BadZipFile("File is not a zip file")
zipfile.BadZipFile: File is not a zip file
```

it means that you have not set up authentication as described below.

:::

## Creating an openICPSR-specific password when you linked your accounts

- Go to [https://www.openicpsr.org/openicpsr/](https://www.openicpsr.org/openicpsr/). 
- If you are logged in (top-right corner shows your name), log out, or open the page in a different browser.
- On the login page, choose the "Sign in with email" option.

![Sign in with email](images/icpsr-new-login.png)

- Use the **same** email you used to create your account (i.e., `netid@cornell.edu`), but choose the "Forgot password" link

![Password request](images/icpsr-new-login-email.png)

- Choose a password that is **NOT** the same as your Cornell NetID password! 

- Now go to the [Bash setup](setup-bash) instructions, and change your password. 

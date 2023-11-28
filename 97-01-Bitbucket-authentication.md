(bitbucket-authentication)=
# Bitbucket Authentication

## Creating an App Password (or PAT)

The long-term solution is to create an [App Password](https://support.atlassian.com/bitbucket-cloud/docs/app-passwords/).

1. Follow the steps to create an App Password. 
2. You want to give it ONLY permissions to `repository read + write`

![Screenshot of permissions](images/Bitbucket-App-password-permissions.png)

Some important points about app passwords:

- You **cannot** view an app password or adjust permissions after you create the app password.
- You **cannot** use them to log in to your Bitbucket account at bitbucket.org.
- You **cannot** use app passwords to manage workspace actions.

## Possible errors

Any user who created a Bitbucket account after Semptember 13, 2021 may encounter the following error when attempting to git clone (or push) using Internet Explorer.
  ![Internet Explorer Error](images/Bitbucket_Error.png)

### Solution

1. Make Firefox (or Edge) your default browswer. 
2. Sign into Bitbucket on your browswer and then attempt the git action once again. You may then receive an error like below:

  ![Second Error](images/Bitbucket_Error2.png)
  
3. Attempt the git action again.

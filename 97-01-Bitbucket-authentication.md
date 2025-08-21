(bitbucket-authentication)=
# Bitbucket Authentication

## Creating an API Token (or PAT)

The long-term solution is to create an [API Token](https://support.atlassian.com/bitbucket-cloud/docs/api-tokens/)[^apppwd]

[^apppwd]: This used to be an [App Password](https://support.atlassian.com/bitbucket-cloud/docs/app-passwords/), but they are being phased out as of 2025.

1. Follow the steps to [create an API Token](https://support.atlassian.com/bitbucket-cloud/docs/create-an-api-token/). You can also try going to [this page](https://id.atlassian.com/manage-profile/security/api-tokens) directly.
2. Click on **Create API token with scopes**.
  - Name it something like "LDI Replication Lab Git".
  - Choose an expiration date that makes sense (minimum end of semester, maximum 1 year)
  -  You want to give it ONLY permissions to `read:repository:bitbucket` and `write:repository:bitbucket`.

Your confirmation screen should look like this:

![Screenshot of API Token creation](images/atlassian-api-final.png)

3. Click **Create**, and copy the long string of characters that appears to your password manager. Use it whereever it says to use a PAT or Bitbucket API token in this manual.

Some important points about API tokens:

- You **cannot** view an API token or adjust permissions after you create it, but you can create a new one (and delete the old one).
- You **cannot** use them to log in to your Bitbucket account at bitbucket.org.

## Possible errors

Any user who created a Bitbucket account after Semptember 13, 2021 may encounter the following error when attempting to git clone (or push) using Internet Explorer.
  ![Internet Explorer Error](images/Bitbucket_Error.png)

### Solution

1. Make Firefox (or Edge) your default browswer. 
2. Sign into Bitbucket on your browswer and then attempt the git action once again. You may then receive an error like below:

  ![Second Error](images/Bitbucket_Error2.png)
  
3. Attempt the git action again.

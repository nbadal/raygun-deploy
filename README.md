<img src="https://user-images.githubusercontent.com/394812/106365554-30c53800-62eb-11eb-89b3-0a9814ccd5ec.jpg" alt="logo" width="120" />

# Raygun Deployment

Docker Container + GitHub Action for notifying Raygun of app deployments

## Inputs
### `apiKey`
**Required**: The API Key of your Raygun Application, found in Application settings.

### `version`
**Required**: The version of your Application that this deployment is releasing. Should be the same as the version string you use in your Raygun error reports.

### `authToken`
**Required**: Auth token generated on your Raygun User Settings Page.

### `ownerName`
_Optional_: The name of the person who is creating this deployment. Ideally should be a Raygun User. Empty by Default.

### `emailAddress`
_Optional_: The email address of the person who is creating this deployment. Ideally should be a Raygun User email address. Empty by Default.

### `comment`
_Optional_: The deployment notes. This will be parsed as Markdown. Empty by Default.

### `scmIdentifier`
_Optional_: The commit that this deployment was built off. For example, a commit hash. Defaults to the action's commit SHA.

### `scmType`
_Optional_: The source control system you are using. Defaults to `'GitHub'`

### `createdAt`
_Optional_: The date and time this deployment was released in ISO 8601 form. Defaults to the current time.

## Outputs
### `deploymentId`
Unique identifier

### `url`
Full URL to the newly created deployment

### `applicationUrl`
Full URL to the application in Raygun

## Example Usage
```yml
on: [push]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - id: raygun
      name: Notify Raygun
      uses: nbadal/raygun-deploy@v1
      with:
        apiKey: ${{ secrets.RAYGUN_API_KEY }}
        authToken: ${{ secrets.RAYGUN_AUTH_TOKEN }}
        version: 1234

    - name: Get deployment outputs
      run: echo "Raygun Deployment Created! ${{ steps.raygun.outputs.url }}"
```

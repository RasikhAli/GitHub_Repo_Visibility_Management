# GitHub Repo Visibility Management

This Python script allows you to manage the visibility of your GitHub repositories. You can list your repositories, change the visibility of individual repositories, or change the visibility of all repositories at once. This script uses the GitHub API for authentication and repository management.
Prerequisites

## Before using this script, make sure you have the following:
    GitHub account.
    Personal access token with the repo scope. You can create one in your GitHub account settings.

## Usage
    1. Clone this repository to your local machine:
        git clone https://github.com/your-username/GitHub_Repo_Visibility_Management.git

    2. Change your working directory to the cloned repository:
        cd GitHub_Repo_Visibility_Management
    
    3. Run the script using Python:
        python repo_visibility.py
    
    4.  Follow the on-screen prompts to interact with the script.

## Features
  1. List Repositories
      Choose option 1 to list all your GitHub repositories. This includes both public and private repositories.
     
  3. Change Visibility of a Repository
      Choose option 2 to change the visibility of an individual repository. You will be prompted to enter the index of the repository you want to modify and whether you want to make it private or public.
     
  5. Change Visibility of All Repositories
      Choose option 3 to change the visibility of all your repositories at once. You will be prompted to make all repositories either private or public.
     
  4. Quit
      Choose option 4 to exit the script.
     
## Notes
    The script uses the GitHub API to fetch and modify repository information, so you need to provide your GitHub username and personal access token when prompted.
    When changing the visibility of all repositories, the script will iterate through each repository and update its visibility. Be cautious when using this option.

## Disclaimer: This script can modify the visibility of your GitHub repositories. Use it with caution, and ensure that you have the necessary permissions to change the visibility of repositories.

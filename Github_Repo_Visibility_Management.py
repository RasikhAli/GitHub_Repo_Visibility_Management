#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# !pip instlal requests


# In[ ]:


import requests

def list_repositories(username, access_token):
    # Define the API endpoint for listing user repositories, including private ones
    url = f"https://api.github.com/user/repos?type=all"

    # Set up headers with the access token for authentication
    headers = {
        "Authorization": f"token {access_token}",
        "Accept": "application/vnd.github.v3+json"  # Specify API version
    }

    # Send a GET request to the GitHub API to list repositories
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        repositories = response.json()

        return repositories
    else:
        print(f"Failed to retrieve repositories. Status code: {response.status_code}")
        return []

def change_repo_visibility(username, access_token, repo_name, make_private):
    # Define the API endpoint for changing repository visibility
    visibility_url = f"https://api.github.com/repos/{username}/{repo_name}"

    # Set up headers with the access token for authentication
    headers = {
        "Authorization": f"token {access_token}",
        "Accept": "application/vnd.github.v3+json"  # Specify API version
    }

    # Define the payload to change visibility
    visibility_payload = {
        "private": make_private
    }

    # Send a PATCH request to change visibility
    visibility_response = requests.patch(visibility_url, headers=headers, json=visibility_payload)

    # Check if the request was successful
    if visibility_response.status_code == 200:
        new_visibility = "Private" if make_private else "Public"
        print(f"Changed visibility of '{repo_name}' to {new_visibility}.")
    else:
        print(f"Failed to change visibility of '{repo_name}'. Status code: {visibility_response.status_code}")

def main():
    print("GitHub Repository Management")
    username = input("Enter your GitHub username: ")
    access_token = input("Enter your GitHub personal access token: ")

    repositories = list_repositories(username, access_token)

    while True:
        print("\nOptions:")
        print("1. List repositories")
        print("2. Change visibility of a repository")
        print("3. Change visibility of all repositories")
        print("4. Quit")
        choice = input("Select an option: ")

        if choice == "1":
            repositories = list_repositories(username, access_token)
            if repositories:
                print("\nYour GitHub repositories:")
                for index, repo in enumerate(repositories):
                    repo_name = repo["name"]
                    repo_visibility = "Public" if not repo["private"] else "Private"
                    print(f"{index + 1}. {repo_name} ({repo_visibility})")
        elif choice == "2":
            repo_index = int(input("\nEnter the index of the repository to change visibility: "))
            make_private = input("Make it private? (yes/no): ").lower() == "yes"
            if repositories and 1 <= repo_index <= len(repositories):
                repo_name = repositories[repo_index - 1]["name"]
                change_repo_visibility(username, access_token, repo_name, make_private)
        elif choice == "3":
            make_private = input("\nMake all repositories private? (yes/no): ").lower() == "yes"
            if repositories:
                for repo in repositories:
                    repo_name = repo["name"]
                    change_repo_visibility(username, access_token, repo_name, make_private)
        elif choice == "4":
            break
        else:
            print("\nInvalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()


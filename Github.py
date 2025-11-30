import requests
import json
owner = "your-username"  
repo = "your-repo"       
url = f"https://api.github.com/repos/{owner}/{repo}/branches"
headers = {
    "Authorization": "token your-github-token"  
}
def get_branches(owner, repo, headers=None):
    response = requests.get(f"https://api.github.com/repos/{owner}/{repo}/branches", headers=headers)
    if response.status_code == 200:
        branches_data = response.json()
        return branches_data
    else:
        print(f"Error fetching branches: {response.status_code}")
        return None
branches_data = get_branches(owner, repo, headers)
if branches_data:
    branch_names = []
    for branch in branches_data:
        branch_name = branch['name']  
        commit_sha = branch['commit']['sha']  
        protected = branch.get('protected', False)  
        branch_names.append({
            'branch_name': branch_name,
            'commit_sha': commit_sha,
            'protected': protected
        })
    print("Branch Information:")
    for branch in branch_names:
        print(f"Branch: {branch['branch_name']}, SHA: {branch['commit_sha']}, Protected: {branch['protected']}")
    filtered_branches = [branch for branch in branch_names if 'feature' in branch['branch_name'].lower()]
    print("\nFiltered Branches (contain 'feature'):")
    for branch in filtered_branches:
        print(f"Branch: {branch['branch_name']}, SHA: {branch['commit_sha']}, Protected: {branch['protected']}")
    sorted_branches = sorted(branch_names, key=lambda x: x['branch_name'])
    print("\nSorted Branches:")
    for branch in sorted_branches:
        print(f"Branch: {branch['branch_name']}, SHA: {branch['commit_sha']}, Protected: {branch['protected']}")
else:
    print("No data available.")
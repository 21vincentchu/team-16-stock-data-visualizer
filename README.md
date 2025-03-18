# Team 16 Stock Data Visualizer

## git commands to reference back to
### tracking changes 
```
git clone [url] #creates copy of a remoate repo on your machine
git status #shows current branch and directory you're in
git add . #adds all new and modified files
git commit -m "insert message here" #records the changes in the repo
git push origin [branch] $uploads your commits to the remote repo. check using git status. EXAMPLE: git push origin main
git pull origin [branch] #downloads any changes from the remote repo. check using git status.EXAMPLE: git pull origin main

```

### make git branch and push to github after you have made some modfication. Do not make a new branch everytime
```
git branch #list the current branches
git checkout -b your-branch-name #create a new branch and switch to it

### pushing your branch to github and updating your branch
git add . #stage your changes
git commit -m "xyz's branch" #commit
git push -u origin [branch name] #push

```
### merging your branch into the main
```
git checkout main #switching to the main branch
git pull origin main #making sure main is up to date
git merge your-branch-name #merge your branch into main
git push origin main #push the merged changes to GitHub

```


## Project setup

1. Steps to clone the repo:
   
    1. Make a working folder on your local machine
    2. open your working folder in IDE
       
   ```
    git clone https://github.com/21vincentchu/team-16-stock-data-visualizer.git
    cd team-16-stock-data-visualizer
   ``` 

3. Create a virtual environment in command line so make sure we are running all the same packages, and same python with the same libraries. Type these commands
   ```
   python3 -m venv venv
   ```

6. Activate the virtual environment:
     ```
   source venv/bin/activate
     ```

8. Install dependencies
    Make sure you are in the root file, cd team-16-stock-data-visualizer 
    ```
   pip install -r requirements.txt
    ```

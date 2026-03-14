# What is a Git Repository?
# A Git repository is a storage location where all the files of a 
# project and their 
# complete history of changes are stored and managed using Git.

# Types of Git Repository

# There are two main types of Git repositories:
# Local Repository – stored on the developer's computer
# Remote Repository – stored on a server like GitHub

# Local Repository

# Developer ke system par stored hoti ha
# Tutotial/

# Remote Repository
# Internet par stored hoti hai.

# Example:
# GitHub
# GitLab
# Bitbucket


# What is git init?
# The git init command 
# is used to create a new Git repository in a project folder.

# Before:
# project folder
# After:
# Git repository

# Command
# git init


# What is git status?
# The git status command shows the 
# current state of the working directory and staging area.

# git status command batata hai:
# kaunse files modified hai
# kaunse files staged hai
# kaunse files commit hone wale hai

# Command
# git status

# What is Working Directory?
# The working directory is the current folder where the 
# developer edits and modifies project files.
# Example:

# project/
#   index.html
#   app.js
#   style.css

# Git Workflow (Basic Concept)
# Working Directory
#         ↓
# Staging Area
#         ↓
# Repository

# What is Staging Area?
# The Staging Area in Git is an intermediate area where changes are 
# prepared before they are permanently saved in the repository.

# 1️ Working Directory → jaha files edit hoti hai
# 2️ Staging Area → commit ke liye files ready hoti hai
# 3️ Repository → permanent history save hoti hai

# What is git add?
# The git add command is used 
# to move changes from the working directory to the staging area.

# Example 
# Add Single File
# git add file1.py

# Add All Files
# git add .

# Hindi Explanation:
# git add file.txt → ek file add karta hai
# git add . → sabhi files add karta hai

# What is git commit?
# The git commit command is used to save the staged 
# changes permanently in the Git repository along with a message.

# Example
# git commit -m "Any Message"

# What is a Commit?
# A commit is a snapshot of the project at a 
# specific point in time.

# Example:
# Commit 1 → Project Created
# Commit 2 → Login Page Added
# Commit 3 → Dashboard Added


# Git Workflow (Most Important Concept)

# Create / Edit File
#         ↓
    # git init
#         ↓
# git add file.py
#         ↓
# Staging Area
#         ↓
# git commit
#         ↓
# Git Repository

# 1️ File create / edit
# 2️ git add se staging area me bheja
# 3️ git commit se repository me save kiya
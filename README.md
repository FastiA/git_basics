mkdir Rudiuk_DK21-mp
cd Rudiuk_DK21-mp/
git init
touch README.md
git status
git add README.md
git commit -m "subtask 1"

git branch first_branch
git checkout first_branch
git status
git add README.md

git checkout master
git status
git add README.md
git commit -m "subtask 3"
git merge first_branch
git status
git add README.md
git status
git commit -m "merge conflict fixed"
git status
git log
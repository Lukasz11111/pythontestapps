

if [ -z "$1" ]
  then
    commit="working progress"
else
commit="$1"
fi

git add .
sudo git commit -m "$commit"
git push
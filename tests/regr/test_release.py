import git
import revdebug as rdb
import os

repo = git.Repo(search_parent_directories=True)
sha = repo.head.object.hexsha
os.environ['REVDEBUG_RELEASE']=sha
print(sha)
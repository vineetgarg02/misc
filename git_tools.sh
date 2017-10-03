git-upstream-fetch() {
	current_branch=$(git status | grep 'On branch'| awk '{print $3}')
	git checkout master; git fetch upstream; git merge upstream/master; git push origin
	git checkout $current_branch
	git merge origin/master
}

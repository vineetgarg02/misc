export JAVA_HOME=$(/usr/libexec/java_home)


export PATH=/Users/vgarg/workspace/apache-maven-3.3.9/bin:$PATH

#show full directory path
PS1='\u@\h:\w\$ '

#set vi mode
set -o vi

#open files in new vim tab instead of vim instances
#alias gvim='gvim -p --remote-tab-silent'

function iterm2_print_user_vars() {
  iterm2_set_user_var work_dir $(PWD)
}


source /Users/vgarg/repos/misc/hive_tools/hive.profile.sh
source /Users/vgarg/repos/misc/git_tools.sh
source /Users/vgarg/scripts/hiveRunQTests.sh
source /Users/vgarg/repos/misc/hive_profile.sh
#export PATH=$PATH:$HOME/.git-radar
#export PS1="$PS1\$(git-radar --bash --fetch)"

test -e "${HOME}/.iterm2_shell_integration.bash" && source "${HOME}/.iterm2_shell_integration.bash"


alias cn105='ssh -v vineet@cn105-10.l42scl.hortonworks.com'

# Setting PATH for Python 3.6
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.6/bin:${PATH}"
export PATH

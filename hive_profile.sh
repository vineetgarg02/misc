alias hiveMakePackageCl='mvn clean package -DskipTests -Pdist'
alias hiveMakePackage='mvn package -DskipTests -Pdist'
alias hiveMakeCl='mvn clean install -DskipTests'
alias hiveMake='mvn install -DskipTests'
alias sshPG='ssh -i ~/Downloads/openstack-keypair.pem.txt root@172.27.52.141'
alias sshHIVE='ssh -i ~/Downloads/openstack-keypair.pem.txt root@172.27.30.12'


hiveBuildAndMovePackage() {
	hiveMakePackageCl

	branchName=$(git branch | grep ^* | awk '{print $2}')
	srcPath=~/workspace/hive_jars/$branchName
	mkdir -p $srcPath
	org.infernus.idea.checkstyle.exception.CheckStylePluginException: <html><b>The Checkstyle rules file could not be parsed.</b><br>SuppressWithNearbyCommentFilter is not allowed as a child in Checker<br>The file has been blacklisted for 60s.</html>cp -rf packaging $srcPath/
}

hiveStartHiveCli() {
	branchName=$(git branch | grep ^* | awk '{print $2}')
	if [ "$1" == "debug" ]
	then
		~/workspace/hive_jars/$branchName/packaging/target/apache-hive-3.0.0-SNAPSHOT-bin/apache-hive-3.0.0-SNAPSHOT-bin/bin/hive --debug
	else
		~/workspace/hive_jars/$branchName/packaging/target/apache-hive-3.0.0-SNAPSHOT-bin/apache-hive-3.0.0-SNAPSHOT-bin/bin/hive
	fi
}

alias makeCleanHiveP='hiveBuildAndMovePackage'

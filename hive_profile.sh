alias hiveMakePackageCl='mvn clean package -DskipTests -Pdist'
alias hiveMakePackage='mvn package -DskipTests -Pdist'
alias hiveMakeCl='mvn clean install -DskipTests'
alias hiveMake='mvn install -DskipTests'
alias sshPG='ssh -i ~/Downloads/openstack-keypair.pem.txt root@172.27.52.141'
alias sshHIVE='ssh -i ~/Downloads/openstack-keypair.pem.txt root@172.27.30.12'


hiveBuildAndMovePackage() {
	if [ "$1" == "clean" ]
	then
		hiveMakePackageCl
	else
		hiveMakePackage
	fi

	branchName=$(git branch | grep ^* | awk '{print $2}')
	srcPath=~/workspace/hive_jars/$branchName
	mkdir -p $srcPath
	cp -rf packaging $srcPath/
}

hiveStartHiveCli() {
	branchName=$(git branch | grep ^* | awk '{print $2}')
	if [ "$1" == "debug" ]
	then
		~/workspace/hive_jars/$branchName/packaging/target/apache-hive-3.1.0-SNAPSHOT-bin/apache-hive-3.1.0-SNAPSHOT-bin/bin/hive --debug
	else
		~/workspace/hive_jars/$branchName/packaging/target/apache-hive-3.1.0-SNAPSHOT-bin/apache-hive-3.1.0-SNAPSHOT-bin/bin/hive
	fi
}

hiveOverrideTestsAll() {
	if [ "$2" == "" ]
	then
		numFiles=10
	else
		numFiles="$2"
	fi
	echo "numFiles:$numFiles"
	echo "cli driver: $3"
	egrep "$3" $1 | perl -pe 's@.*testCliDriver_@@g' | awk '{print $1 ".q"}' | xargs -n $numFiles | perl -pe 's@ @,@g' | xargs -I{} mvn test -Dtest=$3 -Dtest.output.overwrite=true -Dqfile={}
}

alias makeCleanP='hiveBuildAndMovePackage clean'
alias makeP='hiveBuildAndMovePackage'

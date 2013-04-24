#!/bin/bash
master=$1
slave=$2 
dn="dc=cascadeo,dc=com" 
ldap_proto="ldaps" 
#ldap_proto="ldap" 
ldap_port="636" 
#ldap_port="389"
test1=`/usr/bin/ldapsearch -LLL -x -H $ldap_proto://${master}:$ldap_port -b $dn -s base contextCSN` 
if [ $? != 0 ]; then 
	echo "Error in querying LDAP MASTER."
	 exit 1 
fi
test2=`/usr/bin/ldapsearch -LLL -x -H $ldap_proto://${slave}:$ldap_port -b $dn -s base contextCSN` 
if [ $? != 0 ]; then 
	echo "Error in querying LDAP SLAVE." 
	exit 1 
fi
if [ "$test1" == "$test2" ]; then 
	echo -en "LDAP Servers ARE in sync.\n" 
	echo $master: $test1 
	echo $slave: $test2
	exit 0
else
        echo -en "LDAP Servers are _NOT_ in sync\n" 
        echo $master: $test1 
        echo $slave: $test2 
        exit 1
fi

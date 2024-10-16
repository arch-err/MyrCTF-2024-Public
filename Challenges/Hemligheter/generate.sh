#!/bin/bash

NAMESPACE="mp-secrets"
COMPANYDOMAIN="rcerebri.se"

# Arguments <name> <key=value> <key=value> ...
function genSecret () {
    local NAME=$1
    shift 1

    local keyArgs=""
    for key in $@
    do
        keyArgs="$keyArgs --from-literal=$key"
    done

    # kubectl create secret generic $NAME -n $NAMESPACE $keyArgs -o yaml > secret-$NAME.yaml
    kubectl create secret generic $NAME -n $NAMESPACE $keyArgs --dry-run="client" -o yaml > secret-$NAME.yaml
    sed -i '/namespace: .*/d' secret-$NAME.yaml
}

# Arguments <name> <email>
function gitUser () {
    git config user.name "$1"
    git config user.email "$2"
}

# Arguments
function encDir () {
    for secret in $(ls *.yaml)
    do
        sops --encrypt --age $AGERECIPIENT $secret > ${secret%.yaml}.enc.yaml
        rm $secret
    done
}

dir=RC_ClusterSecrets_QA2
rm -rf $dir

# Init
yq '.flag' challenge.yaml > flag.txt
age-keygen -o key.txt
export SOPS_AGE_KEY=$(grep AGE-SECRET-KEY key.txt)
export AGERECIPIENT=$(grep public key.txt | cut -d" " -f4)
mkdir $dir
cd $dir
git init


# Initial Commit
gitUser "Petrus Öberg" "petrus.oberg@$COMPANYDOMAIN"
genSecret xztrace-grafanaAdmin username=admin password=admin
genSecret xztrace-lokiExporter token=token123
git add --all
git commit -m "Initial Commit" --date="Tue Apr 25 11:18:37 2023 +0200"
# genSecret xztrace-grafanaAdmin username=admin-24457 password='3fd$sg7a7!!2^'


# CICD-Tools
gitUser "Petrus Öberg" "petrus.oberg@$COMPANYDOMAIN"
mkdir cicd-tools
cd cicd-tools
rm *.yaml
genSecret scxf-droneci-admin username=admin password=admin
genSecret scxf-droneci-oberg username=admin password=admin
genSecret scxf-droneci-siden username=admin password=admin
genSecret scxf-droneci-magnusson username=admin password=admin
cd ..
git add --all
git commit -m "DroneCI, dummy creds" --date="Wed May 3 14:33:15 2023 +0200"


# JakobTest
gitUser "Jakob Magnusson" "jakob.magnusson@$COMPANYDOMAIN"
mkdir jakobtest
cd jakobtest
rm *.yaml
genSecret gnmic-test-admin username=administrator password=password
genSecret scxf-gnmic-token token=testtoken
cd ..
git add --all
git commit -m "gnmic test" --date="Fri May 5 09:48:06 2023 +0200"


# CICD-Tools - Real
gitUser "Petrus Öberg" "petrus.oberg@$COMPANYDOMAIN"
mkdir cicd-tools
cd cicd-tools
rm *.yaml
genSecret scxf-droneci-admin username=admin password='A2bGVX#4fd8kcFaH&VUB'
genSecret scxf-droneci-oberg username=u55327 password='Ne&X!8w2smhYUZmSCseo'
genSecret scxf-droneci-siden username=u55122 password='Hg&Kv^&dxr#MCxC#WFa4'
genSecret scxf-droneci-magnusson username=u55916 password='GiExF!R3ivEgmCaq%&%R'
encDir
cd ..
git add --all
git commit -m "droneCI, Real Secrets + Age/Sops" --date="Tue May 9 10:21:38 2023 +0200"


# xztrace - Real
gitUser "Petrus Öberg" "petrus.oberg@$COMPANYDOMAIN"
rm *.yaml
genSecret xztrace-grafanaAdmin username=admin-71263 password='Cq@u289q%CNQ%%!B!BMt'
genSecret xztrace-lokiExporter token="640cfe3114cb5dc7543d1ca09da30c9f39d2031c115b198526ea933ef0268ce2"
genSecret xztrace-alloyToken token="e0fa4de9ec5f9f4d66451e8a50a06883589aa15f121661efb5c3ec1922cc6d0a"
encDir
git add --all
git commit -m "xztrace, Real Secrets" --date="Tue May 9 14:37:04 2023 +0200"


# JakobTest - FAIL, UPLOADED AGEKEY
gitUser "Jakob Magnusson" "jakob.magnusson@$COMPANYDOMAIN"
cd jakobtest
rm *.yaml
genSecret gnmic-test-admin username=administrator password="6Px@ycZU%7rCzhZvhi#q"
genSecret scxf-gnmic-token token="79fe3a9399f1dbd568b1800518043a296b6240247513fdbb87fe418081747a8e"
encDir
cd ..
cp ../key.txt ./
gitUser "Jakob Magnusson" "jakob.magnusson@$COMPANYDOMAIN"
git add --all
git commit -m "gnmic real secrets" --date="Wed May 10 16:52:47 2023 +0200"


# JakobTest - Attempt at rolling secrets
gitUser "Jakob Magnusson" "jakob.magnusson@$COMPANYDOMAIN"
cd jakobtest
rm *.yaml
genSecret gnmic-test-admin username=administrator password="xXLi4rrh9aSXVy8hT!#8"
genSecret scxf-gnmic-token token="c16e0cfd040926e06ce129700c578338ac0e7301e206751065337671bcca019d"
encDir
cd ..
rm ./key.txt
git add --all
git commit -m "rolling secrets after possible leak" --date="Wed May 10 17:32:03 2023 +0200"


# CICD-Tools - Rolling Secrets
gitUser "Martin Sidén" "martin.siden@$COMPANYDOMAIN"
cd cicd-tools
rm *.yaml
genSecret scxf-droneci-admin username=admin password='k4eojmM&Ht4#P4K8KZs5'
genSecret scxf-droneci-oberg username=u55327 password='Xgu3oE4w6*AwGu6qc^^p'
genSecret scxf-droneci-siden username=u55122 password='&fLBzgobkn9cZ9fN*hCU'
genSecret scxf-droneci-magnusson username=u55916 password='iWy%U6LaJ3EW$adT!7Zq'
encDir
cd ..
rm *.yaml
genSecret xztrace-grafanaAdmin username=admin-71263 password='YwZ@5ZRbZ7BbC%RYoXy9'
genSecret xztrace-lokiExporter token="26ad7725c4b256905a131a244e8a44926932c2e11850226e6cc89f9d493a56da"
genSecret xztrace-alloyToken token="$(cat ../flag.txt)"                           #  <---  Flag Added
encDir
git add --all
git commit -m "Rolling Secrets" --date="Tue Apr 25 13:37:42 2024 +0200"


cd ..
7z a $dir.7z $dir

# Cleanup
rm flag.txt
rm key.txt
rm -rf $dir

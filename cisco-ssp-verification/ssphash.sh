#!/bin/bash
#### Description: Checks Cisco software image file against Cisco BulkHashFile 
#### running: > ./ssphash.sh cisco-ios-file.name.15.2.2.2.bin
#### 
#### Written by: Denis Borchev - dborchev@gmail.com on 03-2017
if [ -f ./BulkHashFile.tar ]; then
    cp -a BulkHashFile.tar BulkHashFile.tar.bak
fi
# -N doesn't work against these cisco servers, if it did it would be less secure 
# (hopefully that's the reason), but it would save bandwidth
#wget -nv -N https://www.cisco.com/c/dam/en/us/support/web/tools/bulk_hash/BulkHashFile.tar
wget -nv https://www.cisco.com/c/dam/en/us/support/web/tools/bulk_hash/BulkHashFile.tar
tar -xvf BulkHashFile.tar
# ABSOLUTELY no garantee that the file wasn't changed between these calls
# but I failed to implement piping (which would be better but still imperfect), as TAR gives me errors

python cisco_x509_verify_release.py -e BULKHASH-CCO_RELEASE.cer -i BulkHash.tar -s BulkHash.tar.signature -v dgst -sha512
read -p "Was the verification successful at all steps? " -n 1 -r
echo    # that MUST be interactive, but probably can be reliably automated in case you need large batches of images to check
if [[ $REPLY =~ ^[Yy]$ ]]
then
    RED='\033[0;31m'
    NC='\033[0m' # No Color
    GREEN='\033[0;32m'
    GRAY='\033[0;30m'
    WHITE='\033[0;37m'
    tar -xvf BulkHash.tar
    hashfile="$1"
    hashline=$(cat  BulkHash.csv | grep $hashfile )
    hashmd5=$(echo "$hashline" | awk -F $',' 'BEGIN {OFS = FS} {print $2}')
    hashsha512=$(echo "$hashline" | awk -F $',' 'BEGIN {OFS = FS} {print $3}')
    isActive=$(echo "$hashline" | awk -F $',' 'BEGIN {OFS = FS} {print $5}')
    fSize=$(echo "$hashline" | awk -F $',' 'BEGIN {OFS = FS} {print $6}')
    echo Verifying "$file":
    export SSPHASH=$file OK
    if [[$hashsha512 == $(shasum -a 512 $file | awk {'print $1'})]] 
    then echo ${WHITE}SHA512${NC} ${GREEN}OK${NC}: ${GRAY}$hashsha512 ${NC}
    else 
        echo ${WHITE}SHA512${NC} check ${RED}FAILED ${NC}
        echo Computed:      $(shasum -a 512 $file | awk {'print $1'})
        echo Expected:      $hashsha512
        export SSPHASH=$file FAILED
    fi
    fi
    if [[$hashmd5 == $(md5sum $file | awk {'print $1'})]] 
    then echo ${WHITE}MD5${NC} ${GREEN}OK${NC}: ${GRAY}$hashmd5 ${NC}
    else 
        echo ${WHITE}MD5${NC} check ${RED}FAILED ${NC}
        echo Computed:      $(md5sum $file | awk {'print $1'})
        echo Expected:      $hashmd5
        export SSPHASH=$file FAILED
    fi
    if [[$fSize == $( stat --printf="%s" $file )]] 
    then echo ${WHITE}File Size${NC} ${GREEN}OK${NC}: ${GRAY}$fSize bytes${NC}
    else 
        echo ${WHITE}File Size${NC} check ${RED}FAILED ${NC}
        echo Computed:      $(stat --printf="%s" $file) bytes
        echo Expected:      $fSize bytes
    fi
    if [[$isActive == $( echo Active )]] 
    then echo ${WHITE}Deprecation:${NC} ${GREEN}Not deprecated${NC}: ${GRAY}$fSize bytes${NC}
    else 
        echo ${WHITE}Deprecation:${NC} ${RED}Deprecated ${NC}
        echo It is advised against using this file in production.
    fi
fi
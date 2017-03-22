#Cisco Secure Software Publishing - Bulk Hash File verification script

This script:
- fetches the file https://www.cisco.com/c/dam/en/us/support/web/tools/bulk_hash/BulkHashFile.tar
- verifies the signature using the script included in BulkHashFile.tar
- verifies your image against the BulkHash CSV table ising all three methods (MD5, SHA512, filesize)
- checks if your image is marked as deferred

Run:
''ssphash.sh asdm7.2.bin''

## Disclaimer
I don't work for Cisco. My implementation of their method might be insecure and probably is.
You MUST verify the binaries by hand with the tools you trust.

Please follow this link for more details:

https://www.cisco.com/c/en/us/support/web/tools/bulk-hash/index.html


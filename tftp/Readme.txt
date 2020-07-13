##########################################################################
#
# Filename: Readme.txt
#
# Description: 
# TFTP (Trivial File Transfer Protocol) client and server implementation in Python
#
# @authors: Vasanthakumar K
#			
#
##########################################################################

## Features
RFCs supported:
* 1350 - The TFTP Protocol (Revision 2)
* 2347 - TFTP Option Extension
* 2348 - TFTP Blocksize Option
* 7440 - TFTP Windowsize Option

## Requirements
* Python 3.6+

## Usage
Client:
```
client.py -g <filename> <server-hostname> [port]
```
Use `-p` instead of `-g` to upload (`--put`) the file instead of downloading
(`--get`).

Server:
```
server.py [-p <port>] <server-root>
```

There is also `-h` (--help) option available that explains all the options
available, such as block and window size for the client and disabling uploads
for the server.

#!/bin/bash

echo "Enter new Username: "
read username

echo "Enter your new Password: "
read password

adduser "$username"
echo "$password" | passwd "$username"


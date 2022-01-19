#! /bin/bash


case "$1" in
    `echo $1 | grep ello.* ` )
        echo 'This is a Hello';;
    `echo $1 | grep Good bye.*` )
        echo 'This is a good bye';;
    `echo $1 | grep .*` )
        echo 'this is a mistake'
esac

        

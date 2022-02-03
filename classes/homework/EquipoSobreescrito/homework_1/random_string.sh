#! /bin/bash
head /dev/urandom | tr -cd '[:alnum:]' | cut -c -10

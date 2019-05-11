#!/bin/bash

objdump -Mintel -D $1 | sed -n -e "/<${2}>:/, /^$/ p" | egrep --color "call|jmp|jne|je|jg|ja|jl|jb|"

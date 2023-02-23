#!/usr/bin/bash
set -ev

singularity run   -B $(pwd):/project -H /project docker://python:3.8 ./_test.sh

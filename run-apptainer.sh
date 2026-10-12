#!/usr/bin/bash
set -ev

singularity run   -B $(pwd):/project -H /project docker://python:3.13 ./_test.sh

#!/bin/bash
#Options
curl -sI "$1" | grep -i "Allow" | awk '{sub("^Allow: ", ""); print}'

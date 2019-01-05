#!/bin/bash

project_dir=~/projects/UZH-BMINF005-projects
repo_dir=$project_dir/repos
input_file=$project_dir/git-urls.out.csv

cd "$repo_dir" || exit 1

cut -d',' -f2 "$input_file" \
    | xargs -r -P0 -I{} git clone {}

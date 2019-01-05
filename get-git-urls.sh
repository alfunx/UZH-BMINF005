#!/bin/bash

project_dir=~/projects/UZH-BMINF005-projects
repo_dir=$project_dir/repos
output_file=$project_dir/git-urls.out.csv
input_file=$(realpath "$1")

cd "$repo_dir" || exit 1

sed -E '/(,.*){10}/!d' "$input_file" \
    | cut -d',' -f1,5,6 \
    | sed -E -e 's/,.*,$/,,/' -e 's/,[0-9]*$//' \
    > "$output_file"

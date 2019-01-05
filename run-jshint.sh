#!/bin/bash

project_dir=~/projects/UZH-BMINF005-projects
repo_dir=$project_dir/repos
output_file=$project_dir/jshint.out.csv

cd "$repo_dir" || exit 1

_jshint() {
    jshint "$1" \
        | tail -n 1 \
        | sed -E 's/ errors?//'
}

find . -mindepth 1 -maxdepth 1 -type d -print0 \
    | while IFS= read -r -d $'\0' dir; do
        echo "$(basename "$dir"),$(_jshint "$dir")" \
            >> "$output_file" &
    done

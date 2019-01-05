#!/bin/bash

project_dir=~/projects/UZH-BMINF005-projects
repo_dir=$project_dir/repos
output_file=$project_dir/pylint.out.csv

cd "$repo_dir" || exit 1

_pylint() {
    pylint "$dir" \
        | tail -n 2 \
        | head -n 1 \
        | sed -E 's/Your code has been rated at //' \
        | sed -E 's/ .*//'
}

find . -mindepth 1 -maxdepth 1 -type d -print0 \
    | while IFS= read -r -d $'\0' dir; do
        echo "$(basename "$dir"),$(_pylint "$dir")" \
            >> "$output_file" &
    done

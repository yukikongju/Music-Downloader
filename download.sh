#!/bin/bash

file='songs/songs4.txt'

while IFS= read -r line; do
    echo "Downloading $line"
    youtube-dl -x --audio-format mp3 --output "%(uploader)s - %(title)s.%(ext)s" $line
done < "$file"


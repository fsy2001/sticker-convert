#!/bin/zsh

directory_name=$1

if [ ! -d "$directory_name" ]; then
    mkdir "$directory_name"
fi

resolution=$2

for image in original/*.png; do
    if [ -f "$image" ]; then
        base_image=$(basename "$image" .png)
        sips -Z $resolution "$image" -o "$directory_name/${base_image}.png" 
        sips -Z $(($resolution*2)) "$image" -o "$directory_name/${base_image}@2x.png" 
        sips -Z $(($resolution*3)) "$image" -o "$directory_name/${base_image}@3x.png" 
    fi
done

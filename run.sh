#!/bin/bash

docker run -t -e RENDERER_ACCESS_KEY=secret --net=host msokk/electron-render-service &

python3 -m http.server 8000 &

until $( curl -X POST --output /dev/null --silent --fail http://127.0.1.1:3000/pdf?accessKey=secret -d 'a' ); do
    printf '.'
    sleep 1
done

./render.py

curl -o output/pancakes/recipe.pdf "http://127.0.1.1:3000/pdf?accessKey=secret&marginsType=1&url=http://localhost:8000/output/pancakes/recipe.html"

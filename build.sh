python3 -m pip install -r requirements.txt

python3 generate-homepage.py
printf "generate homepage ✅\n\n"

if [ -d "build" ]
then
    cd build
    git pull
    cd ../
else
    git clone https://github.com/Jothin-kumar/build.git
fi
printf "git (build) ✅\n\n"

python3 build/build.py
cp -r build-output to-deploy
printf "build.py ✅\n\n"

python3 build-sa.py
printf "build-sa.py ✅\n\n"

cp favicon.webp to-deploy/favicon.webp
printf "copy favicon ✅\n\n"
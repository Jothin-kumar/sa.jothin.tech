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

cp robots.txt to-deploy/robots.txt
cp sitemap.txt to-deploy/sitemap.txt
cp _redirects to-deploy/_redirects
printf "copy robots.txt, sitemap.txt & _redirects ✅\n\n"
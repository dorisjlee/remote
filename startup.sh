echo "starting up hacker diary"
cd ~/Desktop/PersonalProj/hacker-diary/docs/
jekyll serve --host=0.0.0.0 > /dev/null 2>&1 &
#jekyll serve #--detach -I
echo "starting up web diary"
cd ~/Desktop/PersonalProj/web_diary/
jekyll serve --host=0.0.0.0 > /dev/null 2>&1 &


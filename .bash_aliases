alias grep='grep --color=auto'
alias ls='ls -GFh'
alias subl="/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl"
#At the end of the day, rename work and hack diary files to summarize what was done today
alias workend="cd ~/Desktop/PersonalProj/web_diary/_posts/;open ."
alias hackend="cd ~/Desktop/PersonalProj/hacker-diary/docs/_posts/;open ." 
# Redirect LaTeX file (Broken after LaTeX update) 
alias pdflatex='/usr/local/texlive/2014/bin/universal-darwin/pdflatex'
alias latex='/usr/local/texlive/2014/bin/universal-darwin/latex'
alias bibtex='/usr/local/texlive/2014/bin/universal-darwin/bibtex'
# HackLife Scripts
hack_path="/Users/dorislee/Desktop/PersonalProj/hack-life/scripts/"
#add [%an] for printing also the name of the person who did the commit (removed because mostly work on my own repo anyways)
alias hacklife='cd /Users/dorislee/Desktop/PersonalProj/hack-life/scripts/'
#alias startup='python $hack_path/startup.py &'
alias podomoro='python Desktop/PersonalProj/timer.py 30 &'
# Diary Scripts
#diary_path='/Users/dorislee/Desktop/PersonalProj/diary.noindex/'
#alias diary='python $diary_path/diary.py new '
# Research Diary Scripts
#research_notes_path='/Users/dorislee/Desktop/PersonalProj/research_diary'
#alias note='python $research_notes_path/research_diary.py new'
##alias organize='python $research_notes_path/organize.py'
#alias organize='function _organize(){ python $research_notes_path/organize.py  $1 $2 $3 ;};_organize'
alias bsh='vim ~/.bash_profile;source ~/.bash_profile'
alias lsd='ls -F|grep /'
alias ls='ls -GFh'
alias ..='cd ..'
alias l='ls'
alias rc3='cd /Users/dorislee/Desktop/GSoC2014/workarea-rc3-project/pipeline'
#Git Alias
alias website_update='cd ~/Desktop/PersonalProj/mygithubpage/;git add . ; git commit -m "update"; git push'
alias glog="git log --pretty=format:'%h %ad | %s%d ' --graph --date=short --since='31 days ago'"
alias gs='git status '
alias ga='git add .'
alias gb='git branch '
alias gc='git commit -m'
alias gd='git diff'
alias push='git push'
alias pull='git pull'
alias go='git checkout '
#Remote Machines
#-A enable forwarding of ssh keys to remote machine if the ssh keys are copied over to .ssh/
alias hopper='ssh -A -Y hopper.nersc.gov'
alias edison='ssh -A -Y edison.nersc.gov'
alias cori='ssh -A -Y cori.nersc.gov'
alias carver='ssh -A -Y carver.nersc.gov'
alias ay='ssh dlee@ugastro.berkeley.edu'
alias boss='ssh -Y dorislee@riemann.lbl.gov'
alias cct='ssh  doris@192.168.169.13'
alias amazon='cd Desktop;ssh -i rc3.pem ec2-user@54.191.66.196'
alias bigdog='ssh doris@bigdog.astro.illinois.edu'
alias charon='ssh -X -Y dorislee@charon.astro.princeton.edu'
alias p2='workon py27dev'
alias p3='workon py34dev'
alias pb='ipython notebook'
#alias pbs='ipython notebook --profile=pyspark'
alias pbs='IPYTHON_OPTS="notebook" $SPARK_HOME/bin/pyspark'
alias crowdclass='ssh dorislee0309@ssh.pythonanywhere.com'
alias gz='ssh dorislee@ssh.pythonanywhere.com'
#Mounting virtual disk remotely onto NERSC machines 
alias mount_home="mkdir home;sshfs dorislee@cori.nersc.gov:/global/homes/d/dorislee/ home  -o auto_cache,defer_permissions,noappledouble"
alias unmount_home="diskutil unmount force home/;rm -r home/"
alias mount_proj="mkdir projects;sshfs dorislee@cori.nersc.gov:/project/projectdirs/astro250/doris  projects -o auto_cache,defer_permissions,noappledouble"
alias unmount_proj="diskutil unmount force projects/;rm -r projects/"
alias sf="mkdir projects;sshfs dorislee@cori.nersc.gov:/project/projectdirs/astro250/doris/ projects -o auto_cache,defer_permissions,noappledouble;cd projects/ ;p2;pb"
alias briss="cd /Users/dorislee/Desktop/Doris_Files/Software/briss; java -jar briss-0.9.jar"
alias startup="cd /Users/dorislee/Desktop/remote; bash startup.sh"

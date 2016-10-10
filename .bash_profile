export PS1="\e[0;36m[\W]\$ \e[m"
#export SPARK_HOME=/Users/dorislee/Desktop/BioVis/spark-1.5.2-bin-hadoop2.4/
#export SPARK_HOME=/Users/dorislee/Desktop/LBNL/spark-1.6.1-bin-without-hadoop
export SPARK_HOME=/Users/dorislee/Desktop/LBNL/spark-1.6.1
export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/build:$SPARK_HOME/python/lib/py4j-0.9-src.zip:$PYTHONPATH
#.bash profile for local (Macbook) 
export CLICOLOR=1
export LSCOLORS=GxFxCxDxBxegedabagaced

export PATH=/usr/local/bin:/usr/local/mysql/bin:/usr/local/texlive/2014/bin/universal-darwin/:$PATH

PATH=$PATH:$HOME/Montage_v3.3/bin:$HOME/Desktop/StarFormation/ramses/trunk/ramses/bin:$HOME/Desktop/Princeton_USRP/athena4.2/bin:$HOME/Desktop/Princeton_USRP/athena4.2/
source  /usr/local/scisoft/bin/Setup.bash
# Enabling virtualenvwrapper at startup
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
export VIRTUALENVWRAPPER_SCRIPT=/usr/local/bin/virtualenvwrapper.sh
source /usr/local/bin/virtualenvwrapper_lazy.sh



b LaTe X source directory changed after upgrade to El Captian 
rt EDITOR='subl -w'
export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad

# Show git branch. From http://effectif.com/git/config
__git_ps1 ()
{
    local b="$(git symbolic-ref HEAD 2>/dev/null)";
    if [ -n "$b" ]; then
        printf "(%s)" "${b##refs/heads/}";
    fi
}

# Show local pyenv.
__pyenv ()
{
    local p="$(pyenv local 2>/dev/null)";
    # echo $p
    p="${p##*/}"
    # echo $p
    if [ "$p" == ""  ]; then
        printf "";
    else
        printf "{%s}" "${p}";
    fi
    # printf $p
}

# Command prompt settings
color_prompt=yes;

# Alias definitions are in a separate file.
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi


# added by Anaconda3 2.4.1 installer
export PATH="/Users/dorislee/anaconda/bin:$PATH"

[[ -s "$HOME/.rvm/scripts/rvm" ]] && source "$HOME/.rvm/scripts/rvm" # Load RVM into a shell session *as a function*

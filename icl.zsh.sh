
#===============================================================================
# icl - interactive command library 
#===============================================================================

f_run_icl(){
    icl_OUTPUT=$(icl)
    print -z $icl_OUTPUT
    zle accept-line # no idea if this is the way it's done
}

zle -N w_run_icl f_run_icl # create a widget
bindkey ^t w_run_icl

#===============================================================================
# END  icl - interactive command library END
#===============================================================================
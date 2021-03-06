
#===============================================================================
# icl - interactive command library 
#===============================================================================

f_icl_writecmd () { 
    perl -e 'ioctl STDOUT, 0x5412, $_ for split //, do{ chomp($_ = <>); $_ }' ; 
}

f_run_icl () {
    icl | f_icl_writecmd
}

bind '"\C-t":"f_run_icl\n"'

#===============================================================================
# END  icl - interactive command library END
#===============================================================================


#===============================================================================
# icl - interactive command library 
#===============================================================================

#TODO: check if icl command exists and skip function definition if it doesn't

function f_run_icl
  icl | read foo
  if [ $foo ]
    commandline $foo
  else
    commandline ''
  end
end


#TODO: check if fish 3, and skip if not

# this will only work for fish 3
bind \ct f_run_icl

#===============================================================================
# END  icl - interactive command library END
#===============================================================================
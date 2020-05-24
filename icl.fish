
#===============================================================================
# icl - interactive command library 
#===============================================================================
function f_run_icl
  icl | read foo
  if [ $foo ]
    commandline $foo
  else
    commandline ''
  end
end

# this will only work for fish 3
bind \ct f_run_icl

#===============================================================================
# END  icl - interactive command library END
#===============================================================================
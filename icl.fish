
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

# this will only work for fish 3
if fish --version | grep 'version 3'
  bind \ct f_run_icl
end

# if you run older versions of fish, you have to define the keybind yourself
# inside your fish_user_key_bindings function:

# function fish_user_key_bindings
#   bind \ct f_run_icl
# end

#===============================================================================
# END  icl - interactive command library END
#===============================================================================
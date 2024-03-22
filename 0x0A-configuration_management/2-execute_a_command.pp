# 2-execute_a_command.pp

# Define the exec resource to kill the process
exec { 'killmenow':
  command     => '/usr/bin/pkill killmenow',
  path        => '/usr/bin',
  refreshonly => true,
}

# Notify when the process is killed
notify { 'Process killmenow terminated':
  subscribe => Exec['killmenow'],
}


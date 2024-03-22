exec { 'reinstall_werkzeug':
  command => '/usr/bin/pip3 install --upgrade --force-reinstall Werkzeug',
  path    => ['/usr/bin'],
}


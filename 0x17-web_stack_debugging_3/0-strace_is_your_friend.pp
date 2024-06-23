# fix Apache returning a 500 error

exec {'fix error':
  command => 'sed -i s/phpp/php/g /var/www/htmlwp-settings.php',
  path    => ['/bin', '/usr/bin/', '/usr/local/bin/']
}

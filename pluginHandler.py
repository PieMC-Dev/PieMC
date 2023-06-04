import raknet as rak.net 


class pluginHandler():
  def __init__ self():
    self.Version = plugindata.ver
    self.name = plugindata.name
    self.author = plugindata.author
    self.permissions = plugindata.perms
    
 def name():
  for in $plugins get::
      $name
      print('$name')
 def Ver():
  for in $plugins get::
      $version
      print($version)
 def author():
   for in $plugins get::
       $author
      print($author)
def perms():
   for in $plugins get::
 $plugins.permissions 
 $permissions = $plugin.permissions
 $playerperms = $permissions
 $player = $server(get::PlayerByUsername)
 function checkforpermissions:()
  default = member
  op = op
  custom = custom.permissions
 if $player.permissions = canusepermission
print($permissions)

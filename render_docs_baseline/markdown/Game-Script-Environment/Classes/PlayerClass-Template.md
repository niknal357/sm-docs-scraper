# PlayerClass script template

[Back to PlayerClass](PlayerClass.md)

Copy this starter script and remove anything you do not need.

```lua
Player = class()

-- Server callbacks
-- Docs: PlayerClass.html#server_oncreate
function Player.server_onCreate( self )
end

-- Docs: PlayerClass.html#server_ondestroy
function Player.server_onDestroy( self )
end

-- Docs: PlayerClass.html#server_onrefresh
function Player.server_onRefresh( self )
end

-- Docs: PlayerClass.html#server_onfixedupdate
function Player.server_onFixedUpdate( self, timeStep )
end

-- Docs: PlayerClass.html#server_onreceiveupdate
function Player.server_onReceiveUpdate( self )
end

-- Docs: PlayerClass.html#server_onprojectile
function Player.server_onProjectile(
    self,
    position,
    airTime,
    velocity,
    projectileName,
    shooter,
    damage,
    customData,
    normal,
    uuid,
    mass
)
end

-- Docs: PlayerClass.html#server_onexplosion
function Player.server_onExplosion( self, center, destructionLevel, damage )
end

-- Docs: PlayerClass.html#server_onmelee
function Player.server_onMelee(
    self,
    position,
    attacker,
    damage,
    power,
    direction,
    normal
)
end

-- Docs: PlayerClass.html#server_oncollision
function Player.server_onCollision(
    self,
    other,
    position,
    selfPointVelocity,
    otherPointVelocity,
    normal
)
end

-- Docs: PlayerClass.html#server_oncollisioncrush
function Player.server_onCollisionCrush( self )
end

-- Docs: PlayerClass.html#server_onshaperemoved
function Player.server_onShapeRemoved( self, items )
end

-- Docs: PlayerClass.html#server_oninventorychanges
function Player.server_onInventoryChanges( self, inventory, changes )
end

-- Client callbacks
-- Docs: PlayerClass.html#client_oncreate
function Player.client_onCreate( self )
end

-- Docs: PlayerClass.html#client_ondestroy
function Player.client_onDestroy( self )
end

-- Docs: PlayerClass.html#client_onrefresh
function Player.client_onRefresh( self )
end

-- Docs: PlayerClass.html#client_onfixedupdate
function Player.client_onFixedUpdate( self, timeStep )
end

-- Docs: PlayerClass.html#client_onupdate
function Player.client_onUpdate( self, deltaTime )
end

-- Docs: PlayerClass.html#client_onclientdataupdate
function Player.client_onClientDataUpdate( self, data, channel )
end

-- Docs: PlayerClass.html#client_onlocalplayerchangedworld
function Player.client_onLocalPlayerChangedWorld( self, world )
end

-- Docs: PlayerClass.html#client_oninteract
function Player.client_onInteract( self, character, state )
end

-- Docs: PlayerClass.html#client_oncancel
function Player.client_onCancel( self )
end

-- Docs: PlayerClass.html#client_onskipdialog
function Player.client_onSkipDialog( self )
end

-- Docs: PlayerClass.html#client_onreload
function Player.client_onReload( self )
end
```

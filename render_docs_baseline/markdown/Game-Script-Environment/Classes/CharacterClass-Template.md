# CharacterClass script template

[Back to CharacterClass](CharacterClass.md)

Copy this starter script and remove anything you do not need.

```lua
Character = class()

-- Server callbacks
-- Docs: CharacterClass.html#server_oncreate
function Character.server_onCreate( self )
end

-- Docs: CharacterClass.html#server_ondestroy
function Character.server_onDestroy( self )
end

-- Docs: CharacterClass.html#server_onrefresh
function Character.server_onRefresh( self )
end

-- Docs: CharacterClass.html#server_onfixedupdate
function Character.server_onFixedUpdate( self, timeStep )
end

-- Docs: CharacterClass.html#server_onreceiveupdate
function Character.server_onReceiveUpdate( self )
end

-- Client callbacks
-- Docs: CharacterClass.html#client_oncreate
function Character.client_onCreate( self )
end

-- Docs: CharacterClass.html#client_ondestroy
function Character.client_onDestroy( self )
end

-- Docs: CharacterClass.html#client_onrefresh
function Character.client_onRefresh( self )
end

-- Docs: CharacterClass.html#client_onfixedupdate
function Character.client_onFixedUpdate( self, timeStep )
end

-- Docs: CharacterClass.html#client_onupdate
function Character.client_onUpdate( self, deltaTime )
end

-- Docs: CharacterClass.html#client_onclientdataupdate
function Character.client_onClientDataUpdate( self, data, channel )
end

-- Docs: CharacterClass.html#client_onlocalplayerchangedworld
function Character.client_onLocalPlayerChangedWorld( self, world )
end

-- Docs: CharacterClass.html#client_onprojectile
function Character.client_onProjectile(
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

-- Docs: CharacterClass.html#client_onmelee
function Character.client_onMelee(
    self,
    position,
    attacker,
    damage,
    power,
    direction,
    normal
)
end

-- Docs: CharacterClass.html#client_oncollision
function Character.client_onCollision(
    self,
    other,
    position,
    selfPointVelocity,
    otherPointVelocity,
    normal
)
end

-- Docs: CharacterClass.html#client_ongraphicsloaded
function Character.client_onGraphicsLoaded( self )
end

-- Docs: CharacterClass.html#client_ongraphicsunloaded
function Character.client_onGraphicsUnloaded( self )
end

-- Docs: CharacterClass.html#client_oninteract
function Character.client_onInteract( self, character, state )
end

-- Docs: CharacterClass.html#client_caninteract
function Character.client_canInteract( self, character )
    return true
end

-- Docs: CharacterClass.html#client_onevent
function Character.client_onEvent( self, event )
end
```

# HarvestableClass script template

[Back to HarvestableClass](HarvestableClass.md)

Copy this starter script and remove anything you do not need.

```lua
Harvestable = class()

-- Constants
-- Docs: HarvestableClass.html#poseweightcount
Harvestable.poseWeightCount = 0

-- Server callbacks
-- Docs: HarvestableClass.html#server_oncreate
function Harvestable.server_onCreate( self )
end

-- Docs: HarvestableClass.html#server_ondestroy
function Harvestable.server_onDestroy( self )
end

-- Docs: HarvestableClass.html#server_onrefresh
function Harvestable.server_onRefresh( self )
end

-- Docs: HarvestableClass.html#server_onfixedupdate
function Harvestable.server_onFixedUpdate( self, timeStep )
end

-- Docs: HarvestableClass.html#server_onreceiveupdate
function Harvestable.server_onReceiveUpdate( self )
end

-- Docs: HarvestableClass.html#server_onunload
function Harvestable.server_onUnload( self )
end

-- Docs: HarvestableClass.html#server_oncollision
function Harvestable.server_onCollision(
    self,
    other,
    position,
    selfPointVelocity,
    otherPointVelocity,
    normal
)
end

-- Docs: HarvestableClass.html#server_onprojectile
function Harvestable.server_onProjectile(
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

-- Docs: HarvestableClass.html#server_onexplosion
function Harvestable.server_onExplosion(
    self,
    center,
    destructionLevel,
    damage
)
end

-- Docs: HarvestableClass.html#server_onmelee
function Harvestable.server_onMelee(
    self,
    position,
    attacker,
    damage,
    power,
    direction,
    normal
)
end

-- Docs: HarvestableClass.html#server_onremoved
function Harvestable.server_onRemoved( self, player )
end

-- Docs: HarvestableClass.html#server_canerase
function Harvestable.server_canErase( self )
    return false
end

-- Docs: HarvestableClass.html#server_onignite
function Harvestable.server_onIgnite( self )
end

-- Docs: HarvestableClass.html#server_onfloating
function Harvestable.server_onFloating( self )
end

-- Client callbacks
-- Docs: HarvestableClass.html#client_oncreate
function Harvestable.client_onCreate( self )
end

-- Docs: HarvestableClass.html#client_ondestroy
function Harvestable.client_onDestroy( self )
end

-- Docs: HarvestableClass.html#client_onrefresh
function Harvestable.client_onRefresh( self )
end

-- Docs: HarvestableClass.html#client_onfixedupdate
function Harvestable.client_onFixedUpdate( self, timeStep )
end

-- Docs: HarvestableClass.html#client_onupdate
function Harvestable.client_onUpdate( self, deltaTime )
end

-- Docs: HarvestableClass.html#client_onclientdataupdate
function Harvestable.client_onClientDataUpdate( self, data, channel )
end

-- Docs: HarvestableClass.html#client_onlocalplayerchangedworld
function Harvestable.client_onLocalPlayerChangedWorld( self, world )
end

-- Docs: HarvestableClass.html#client_oncollision
function Harvestable.client_onCollision(
    self,
    other,
    position,
    selfPointVelocity,
    otherPointVelocity,
    normal
)
end

-- Docs: HarvestableClass.html#client_onprojectile
function Harvestable.client_onProjectile(
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

-- Docs: HarvestableClass.html#client_onmelee
function Harvestable.client_onMelee(
    self,
    position,
    attacker,
    damage,
    power,
    direction,
    normal
)
end

-- Docs: HarvestableClass.html#client_canerase
function Harvestable.client_canErase( self )
    return false
end

-- Docs: HarvestableClass.html#client_oninteract
function Harvestable.client_onInteract( self, character, state )
end

-- Docs: HarvestableClass.html#client_caninteract
function Harvestable.client_canInteract( self, character )
    return true
end

-- Docs: HarvestableClass.html#client_onaction
function Harvestable.client_onAction( self, action, state )
end
```

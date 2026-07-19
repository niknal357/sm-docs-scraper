# UnitClass script template

[Back to UnitClass](UnitClass.md)

Copy this starter script and remove anything you do not need.

```lua
Unit = class()

-- Constants
-- Docs: UnitClass.html#issaveobject
Unit.isSaveObject = true

-- Server callbacks
-- Docs: UnitClass.html#server_oncreate
function Unit.server_onCreate( self )
end

-- Docs: UnitClass.html#server_ondestroy
function Unit.server_onDestroy( self )
end

-- Docs: UnitClass.html#server_onrefresh
function Unit.server_onRefresh( self )
end

-- Docs: UnitClass.html#server_onfixedupdate
function Unit.server_onFixedUpdate( self, timeStep )
end

-- Docs: UnitClass.html#server_onreceiveupdate
function Unit.server_onReceiveUpdate( self )
end

-- Docs: UnitClass.html#server_onprojectile
function Unit.server_onProjectile(
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

-- Docs: UnitClass.html#server_onexplosion
function Unit.server_onExplosion( self, center, destructionLevel, damage )
end

-- Docs: UnitClass.html#server_onmelee
function Unit.server_onMelee(
    self,
    position,
    attacker,
    damage,
    power,
    direction,
    normal
)
end

-- Docs: UnitClass.html#server_oncollision
function Unit.server_onCollision(
    self,
    other,
    position,
    selfPointVelocity,
    otherPointVelocity,
    normal
)
end

-- Docs: UnitClass.html#server_oncollisioncrush
function Unit.server_onCollisionCrush( self )
end

-- Docs: UnitClass.html#server_onunitupdate
function Unit.server_onUnitUpdate( self, deltaTime )
end

-- Docs: UnitClass.html#server_oncharacterchangedcolor
function Unit.server_onCharacterChangedColor( self, color )
end

-- Client callbacks
-- Docs: UnitClass.html#client_oncreate
function Unit.client_onCreate( self )
end

-- Docs: UnitClass.html#client_ondestroy
function Unit.client_onDestroy( self )
end

-- Docs: UnitClass.html#client_onrefresh
function Unit.client_onRefresh( self )
end

-- Docs: UnitClass.html#client_onfixedupdate
function Unit.client_onFixedUpdate( self, timeStep )
end

-- Docs: UnitClass.html#client_onupdate
function Unit.client_onUpdate( self, deltaTime )
end

-- Docs: UnitClass.html#client_onclientdataupdate
function Unit.client_onClientDataUpdate( self, data, channel )
end

-- Docs: UnitClass.html#client_onlocalplayerchangedworld
function Unit.client_onLocalPlayerChangedWorld( self, world )
end
```

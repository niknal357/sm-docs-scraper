# ShapeClass script template

[Back to ShapeClass](ShapeClass.md)

Copy this starter script and remove anything you do not need.

```lua
Shape = class()

-- Constants
-- Docs: ShapeClass.html#colorhighlight
Shape.colorHighlight = sm.color.new("#ffffff")
-- Docs: ShapeClass.html#colornormal
Shape.colorNormal = sm.color.new("#808080")
-- Docs: ShapeClass.html#connecticon
Shape.connectIcon = ""
-- Docs: ShapeClass.html#connecticonscale
Shape.connectIconScale = 0.75
-- Docs: ShapeClass.html#connectioninput
Shape.connectionInput = sm.interactable.connectionType.none
-- Docs: ShapeClass.html#connectionoutput
Shape.connectionOutput = sm.interactable.connectionType.none
-- Docs: ShapeClass.html#maxchildcount
Shape.maxChildCount = 0
-- Docs: ShapeClass.html#maxparentcount
Shape.maxParentCount = 0
-- Docs: ShapeClass.html#poseweightcount
Shape.poseWeightCount = 0

-- Server callbacks
-- Docs: ShapeClass.html#server_oncreate
function Shape.server_onCreate( self )
end

-- Docs: ShapeClass.html#server_ondestroy
function Shape.server_onDestroy( self )
end

-- Docs: ShapeClass.html#server_onrefresh
function Shape.server_onRefresh( self )
end

-- Docs: ShapeClass.html#server_onfixedupdate
function Shape.server_onFixedUpdate( self, timeStep )
end

-- Docs: ShapeClass.html#server_onreceiveupdate
function Shape.server_onReceiveUpdate( self )
end

-- Docs: ShapeClass.html#server_onunload
function Shape.server_onUnload( self )
end

-- Docs: ShapeClass.html#server_onprojectile
function Shape.server_onProjectile(
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

-- Docs: ShapeClass.html#server_onsledgehammer
function Shape.server_onSledgehammer( self )
end

-- Docs: ShapeClass.html#server_onmelee
function Shape.server_onMelee(
    self,
    position,
    attacker,
    damage,
    power,
    direction,
    normal
)
end

-- Docs: ShapeClass.html#server_onexplosion
function Shape.server_onExplosion( self, center, destructionLevel, damage )
end

-- Docs: ShapeClass.html#server_oncollision
function Shape.server_onCollision(
    self,
    other,
    position,
    selfPointVelocity,
    otherPointVelocity,
    normal
)
end

-- Docs: ShapeClass.html#server_canerase
function Shape.server_canErase( self )
    return true
end

-- Docs: ShapeClass.html#server_onworldchanged
function Shape.server_onWorldChanged( self )
end

-- Client callbacks
-- Docs: ShapeClass.html#client_oncreate
function Shape.client_onCreate( self )
end

-- Docs: ShapeClass.html#client_ondestroy
function Shape.client_onDestroy( self )
end

-- Docs: ShapeClass.html#client_onrefresh
function Shape.client_onRefresh( self )
end

-- Docs: ShapeClass.html#client_onfixedupdate
function Shape.client_onFixedUpdate( self, timeStep )
end

-- Docs: ShapeClass.html#client_onupdate
function Shape.client_onUpdate( self, deltaTime )
end

-- Docs: ShapeClass.html#client_onclientdataupdate
function Shape.client_onClientDataUpdate( self, data, channel )
end

-- Docs: ShapeClass.html#client_onlocalplayerchangedworld
function Shape.client_onLocalPlayerChangedWorld( self, world )
end

-- Docs: ShapeClass.html#client_oninteract
function Shape.client_onInteract( self, character, state )
end

-- Docs: ShapeClass.html#client_ontinker
function Shape.client_onTinker( self, character, state )
end

-- Docs: ShapeClass.html#client_oninteractthroughjoint
function Shape.client_onInteractThroughJoint( self, character, state, joint )
end

-- Docs: ShapeClass.html#client_onaction
function Shape.client_onAction( self, action, state )
end

-- Docs: ShapeClass.html#client_onprojectile
function Shape.client_onProjectile(
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

-- Docs: ShapeClass.html#client_onmelee
function Shape.client_onMelee(
    self,
    position,
    attacker,
    damage,
    power,
    direction,
    normal
)
end

-- Docs: ShapeClass.html#client_oncollision
function Shape.client_onCollision(
    self,
    other,
    position,
    selfPointVelocity,
    otherPointVelocity,
    normal
)
end

-- Docs: ShapeClass.html#client_canerase
function Shape.client_canErase( self )
    return true
end

-- Docs: ShapeClass.html#client_caninteract
function Shape.client_canInteract( self, character )
    return true
end

-- Docs: ShapeClass.html#client_caninteractthroughjoint
function Shape.client_canInteractThroughJoint( self, character, joint )
    return true
end

-- Docs: ShapeClass.html#client_cantinker
function Shape.client_canTinker( self, character )
    return true
end

-- Docs: ShapeClass.html#client_getavailableparentconnectioncount
function Shape.client_getAvailableParentConnectionCount( self, flags )
    return 0
end

-- Docs: ShapeClass.html#client_getavailablechildconnectioncount
function Shape.client_getAvailableChildConnectionCount( self, flags )
    return 0
end

-- Docs: ShapeClass.html#client_cancarry
function Shape.client_canCarry( self )
    return false
end

-- Docs: ShapeClass.html#client_onchildjointremoved
function Shape.client_onChildJointRemoved( self, joint )
end
```

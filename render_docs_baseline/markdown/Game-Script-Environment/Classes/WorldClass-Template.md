# WorldClass script template

[Back to WorldClass](WorldClass.md)

Copy this starter script and remove anything you do not need.

```lua
World = class()

-- Constants
-- Docs: WorldClass.html#cellmaxx
World.cellMaxX = 0
-- Docs: WorldClass.html#cellmaxy
World.cellMaxY = 0
-- Docs: WorldClass.html#cellminx
World.cellMinX = 0
-- Docs: WorldClass.html#cellminy
World.cellMinY = 0
-- Docs: WorldClass.html#defaultvoxeldensity
World.defaultVoxelDensity = 0
-- Docs: WorldClass.html#defaultvoxelmaterial
World.defaultVoxelMaterial = 0
-- Docs: WorldClass.html#enableassets
World.enableAssets = true
-- Docs: WorldClass.html#enablebuildonassets
World.enableBuildOnAssets = true
-- Docs: WorldClass.html#enablebuildonbodies
World.enableBuildOnBodies = true
-- Docs: WorldClass.html#enablebuildonlift
World.enableBuildOnLift = true
-- Docs: WorldClass.html#enablebuildonsurface
World.enableBuildOnSurface = true
-- Docs: WorldClass.html#enableclutter
World.enableClutter = true
-- Docs: WorldClass.html#enablecreations
World.enableCreations = true
-- Docs: WorldClass.html#enableharvestables
World.enableHarvestables = true
-- Docs: WorldClass.html#enablekinematics
World.enableKinematics = true
-- Docs: WorldClass.html#enablenavmesh
World.enableNavMesh = true
-- Docs: WorldClass.html#enablenodes
World.enableNodes = true
-- Docs: WorldClass.html#enablesurface
World.enableSurface = true
-- Docs: WorldClass.html#enablevoxelterrain
World.enableVoxelTerrain = true
-- Docs: WorldClass.html#groundmaterialset
World.groundMaterialSet = "$GAME_DATA/Terrain/Materials/gnd_standard_materialset.json"
-- Docs: WorldClass.html#hlod
World.hLod = 0
-- Docs: WorldClass.html#horizonwater
World.horizonWater = 0
-- Docs: WorldClass.html#isindoor
World.isIndoor = false
-- Docs: WorldClass.html#isstatic
World.isStatic = false
-- Docs: WorldClass.html#rendermode
World.renderMode = "outdoor"
-- Docs: WorldClass.html#terrainscript
World.terrainScript = ""
-- Docs: WorldClass.html#voxelmaterialset
World.voxelMaterialSet = "$SURVIVAL_DATA/Terrain/Materials/voxel_materialset_drill1.voxelmaterialset"
-- Docs: WorldClass.html#worldborder
World.worldBorder = true

-- Server callbacks
-- Docs: WorldClass.html#server_oncreate
function World.server_onCreate( self )
end

-- Docs: WorldClass.html#server_ondestroy
function World.server_onDestroy( self )
end

-- Docs: WorldClass.html#server_onrefresh
function World.server_onRefresh( self )
end

-- Docs: WorldClass.html#server_onfixedupdate
function World.server_onFixedUpdate( self, timeStep )
end

-- Docs: WorldClass.html#server_onreceiveupdate
function World.server_onReceiveUpdate( self )
end

-- Docs: WorldClass.html#server_onunload
function World.server_onUnload( self )
end

-- Docs: WorldClass.html#server_onterraincreated
function World.server_onTerrainCreated( self )
end

-- Docs: WorldClass.html#server_onterrainloaded
function World.server_onTerrainLoaded( self )
end

-- Docs: WorldClass.html#server_oncellcreated
function World.server_onCellCreated( self, x, y )
end

-- Docs: WorldClass.html#server_oncellloaded
function World.server_onCellLoaded( self, x, y )
end

-- Docs: WorldClass.html#server_oncellunloaded
function World.server_onCellUnloaded( self, x, y )
end

-- Docs: WorldClass.html#server_oninteractablecreated
function World.server_onInteractableCreated( self, interactable )
end

-- Docs: WorldClass.html#server_oninteractabledestroyed
function World.server_onInteractableDestroyed( self, interactable )
end

-- Docs: WorldClass.html#server_onprojectile
function World.server_onProjectile(
    self,
    position,
    airTime,
    velocity,
    projectileName,
    shooter,
    damage,
    customData,
    normal,
    target,
    uuid
)
end

-- Docs: WorldClass.html#server_onexplosion
function World.server_onExplosion( self, center, destructionLevel, damage )
end

-- Docs: WorldClass.html#server_onmelee
function World.server_onMelee(
    self,
    position,
    attacker,
    target,
    damage,
    power,
    direction,
    normal
)
end

-- Docs: WorldClass.html#server_onprojectilefire
function World.server_onProjectileFire(
    self,
    position,
    velocity,
    projectileName,
    shooter,
    uuid
)
end

-- Docs: WorldClass.html#server_oncollision
function World.server_onCollision(
    self,
    objectA,
    objectB,
    position,
    pointVelocityA,
    pointVelocityB,
    normal
)
end

-- Docs: WorldClass.html#server_onvoxeldestruction
function World.server_onVoxelDestruction( self, densityLoss, positions )
end

-- Docs: WorldClass.html#server_onvoxelconstruction
function World.server_onVoxelConstruction( self, densityGain, positions )
end

-- Docs: WorldClass.html#server_onmining
function World.server_onMining( self, spawns )
end

-- Client callbacks
-- Docs: WorldClass.html#client_oncreate
function World.client_onCreate( self )
end

-- Docs: WorldClass.html#client_ondestroy
function World.client_onDestroy( self )
end

-- Docs: WorldClass.html#client_onrefresh
function World.client_onRefresh( self )
end

-- Docs: WorldClass.html#client_onfixedupdate
function World.client_onFixedUpdate( self, timeStep )
end

-- Docs: WorldClass.html#client_onupdate
function World.client_onUpdate( self, deltaTime )
end

-- Docs: WorldClass.html#client_onclientdataupdate
function World.client_onClientDataUpdate( self, data, channel )
end

-- Docs: WorldClass.html#client_onlocalplayerchangedworld
function World.client_onLocalPlayerChangedWorld( self, world )
end

-- Docs: WorldClass.html#client_onterraincreated
function World.client_onTerrainCreated( self )
end

-- Docs: WorldClass.html#client_onterrainloaded
function World.client_onTerrainLoaded( self )
end

-- Docs: WorldClass.html#client_oncellloaded
function World.client_onCellLoaded( self, x, y )
end

-- Docs: WorldClass.html#client_oncellunloaded
function World.client_onCellUnloaded( self, x, y )
end

-- Docs: WorldClass.html#client_oncollision
function World.client_onCollision(
    self,
    objectA,
    objectB,
    position,
    pointVelocityA,
    pointVelocityB,
    normal
)
end

-- Docs: WorldClass.html#client_onprojectile
function World.client_onProjectile(
    self,
    position,
    airTime,
    velocity,
    projectileName,
    shooter,
    damage,
    normal,
    target,
    uuid
)
end
```

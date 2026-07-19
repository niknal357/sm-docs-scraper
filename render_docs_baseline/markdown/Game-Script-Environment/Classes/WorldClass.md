# WorldClass

**Script template:** [View starter script](WorldClass-Template.md)

A script class that is instanced for every [World](../Userdata/World.md) in the game.

When entering a warehouse floor, the player is entering a new world.

Can receive events sent with [sm.event.sendToWorld](../Static-Functions/sm.event.md#sendtoworld).

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](../Userdata/World.md) | The [World](../Userdata/World.md) game object belonging to this class instance. |
| `network` | [Network](../Userdata/Network.md) | A [Network](../Userdata/Network.md) object that can be used to send messages between client and server. |
| `storage` | [Storage](../Userdata/Storage.md) | (Server side only.) A [Storage](../Userdata/Storage.md) object that can be used to store data for the next time loading this object after being unloaded. |
| `data` | any | Parameters from [sm.world.createWorld](../Static-Functions/sm.world.md#createworld). |

## Constants

### cellMaxX {#cellmaxx}

Terrain generation maximum cell position in X axis. (Defaults to 0)

**Returns:**

| Type | Description |
| --- | --- |
| integer |  |

### cellMaxY {#cellmaxy}

Terrain generation maximum cell position in Y axis. (Defaults to 0)

**Returns:**

| Type | Description |
| --- | --- |
| integer |  |

### cellMinX {#cellminx}

Terrain generation minimum cell position in X axis. (Defaults to 0)

**Returns:**

| Type | Description |
| --- | --- |
| integer |  |

### cellMinY {#cellminy}

Terrain generation minimum cell position in Y axis. (Defaults to 0)

**Returns:**

| Type | Description |
| --- | --- |
| integer |  |

### defaultVoxelDensity {#defaultvoxeldensity}

Default value when sampling voxel density. (Defaults to 0)

**Returns:**

| Type | Description |
| --- | --- |
| integer |  |

### defaultVoxelMaterial {#defaultvoxelmaterial}

Default value when sampling voxel material. (Defaults to 0)

**Returns:**

| Type | Description |
| --- | --- |
| integer |  |

### enableAssets {#enableassets}

Enables or disables terrain assets for this world. (Defaults to true)

**Returns:**

| Type | Description |
| --- | --- |
| boolean |  |

### enableBuildOnAssets {#enablebuildonassets}

Enables or disables the ability to build on terrain assets. (Defaults to true)

**Returns:**

| Type | Description |
| --- | --- |
| boolean |  |

### enableBuildOnBodies {#enablebuildonbodies}

Enables or disables the ability to build on bodies. (Defaults to true)

**Returns:**

| Type | Description |
| --- | --- |
| boolean |  |

### enableBuildOnLift {#enablebuildonlift}

Enables or disables the ability to build on lift. (Defaults to true)

**Returns:**

| Type | Description |
| --- | --- |
| boolean |  |

### enableBuildOnSurface {#enablebuildonsurface}

Enables or disables the ability to build on terrain surface. (Defaults to true)

**Returns:**

| Type | Description |
| --- | --- |
| boolean |  |

### enableClutter {#enableclutter}

Enables or disables terrain clutter for this world. (Defaults to true)

**Returns:**

| Type | Description |
| --- | --- |
| boolean |  |

### enableCreations {#enablecreations}

Enables or disables creations for this world. (Defaults to true)

**Returns:**

| Type | Description |
| --- | --- |
| boolean |  |

### enableHarvestables {#enableharvestables}

Enables or disables terrain harvestables for this world. (Defaults to true)

**Returns:**

| Type | Description |
| --- | --- |
| boolean |  |

### enableKinematics {#enablekinematics}

Enables or disables terrain kinematics for this world. (Defaults to true)

**Returns:**

| Type | Description |
| --- | --- |
| boolean |  |

### enableNavMesh {#enablenavmesh}

Enables or disables navigation mesh generation for better AI path finding. (Defaults to true)

**Returns:**

| Type | Description |
| --- | --- |
| boolean |  |

### enableNodes {#enablenodes}

Enables or disables nodes for this world. (Defaults to true)

**Returns:**

| Type | Description |
| --- | --- |
| boolean |  |

### enableSurface {#enablesurface}

Enables or disables terrain surface for this world. (Defaults to true)

**Returns:**

| Type | Description |
| --- | --- |
| boolean |  |

### enableVoxelTerrain {#enablevoxelterrain}

Enables or disables voxel terrain for this world. (Defaults to true)

**Returns:**

| Type | Description |
| --- | --- |
| boolean |  |

### groundMaterialSet {#groundmaterialset}

Sets the ground material set used by the terrain. (Defaults to "$GAME_DATA/Terrain/Materials/gnd_standard_materialset.json")

Full $-path to the material set.

**Returns:**

| Type | Description |
| --- | --- |
| string |  |

### hLod {#hlod}

Enables or disables h lods.

**Returns:**

| Type | Description |
| --- | --- |
| integer |  |

### horizonWater {#horizonwater}

Enables or disables automatically placing water effects at the edge of the world.

**Returns:**

| Type | Description |
| --- | --- |
| integer |  |

### isIndoor {#isindoor}

Enables or disables indoor mode. (Defaults to false)

Indoor worlds have only one terrain cell in (0, 0)

**Returns:**

| Type | Description |
| --- | --- |
| boolean |  |

### isStatic {#isstatic}

Enables or disables static mode. (Defaults to false)

Static worlds are created at load time and doesn't stream in and out.

**Returns:**

| Type | Description |
| --- | --- |
| boolean |  |

### renderMode {#rendermode}

Sets the render mode for this world. (Default "outdoor")

Possible values: "outdoor", "challenge", "warehouse"

**Returns:**

| Type | Description |
| --- | --- |
| string |  |

### terrainScript {#terrainscript}

Sets the script used to generate terrain.

Full $-path to the terrain generation script.

**Returns:**

| Type | Description |
| --- | --- |
| string |  |

### voxelMaterialSet {#voxelmaterialset}

Sets the voxel material set used by the voxel terrain. (Defaults to "$SURVIVAL_DATA/Terrain/Materials/voxel_materialset_drill1.voxelmaterialset")

Full $-path to the material set.

**Returns:**

| Type | Description |
| --- | --- |
| string |  |

### worldBorder {#worldborder}

Adds borders to the world to prevent objects falling through the ground. (Defaults to true)

**Returns:**

| Type | Description |
| --- | --- |
| boolean |  |

## Server + Client

<a id="server_oncreate"></a>
<a id="client_oncreate"></a>
### onCreate {#oncreate}

``` { .lua .api-signature }
WorldClass:server_onCreate(  )
WorldClass:client_onCreate(  )
```

Called when the scripted object is created. This occurs when a new object is built, spawned, or loaded from the save file.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

<a id="server_ondestroy"></a>
<a id="client_ondestroy"></a>
### onDestroy {#ondestroy}

``` { .lua .api-signature }
WorldClass:server_onDestroy(  )
WorldClass:client_onDestroy(  )
```

Called when the scripted object is destroyed.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

<a id="server_onrefresh"></a>
<a id="client_onrefresh"></a>
### onRefresh {#onrefresh}

``` { .lua .api-signature }
WorldClass:server_onRefresh(  )
WorldClass:client_onRefresh(  )
```

Called if the Lua script attached to the object is modified while the game is running.

> **Note:**
> This event requires Scrap Mechanic to be running with the '-dev' flag. This will allow scripts to automatically refresh upon changes.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

<a id="server_onfixedupdate"></a>
<a id="client_onfixedupdate"></a>
### onFixedUpdate {#onfixedupdate}

``` { .lua .api-signature }
WorldClass:server_onFixedUpdate( timeStep )
WorldClass:client_onFixedUpdate( timeStep )
```

Called every game tick &ndash; 40 ticks a second. If the frame rate is lower than 40 fps, this event may be called twice.

During a fixed update, physics and logic between interactables are updated.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `timeStep` | number | The time period of a tick. (Is always 0.025, a 1/40th of a second.) |

<a id="server_onterraincreated"></a>
<a id="client_onterraincreated"></a>
### onTerrainCreated {#onterraincreated}

#### Server

``` { .lua .api-signature }
WorldClass:server_onTerrainCreated(  )
```

Called when a world's terrain is created for the first time on the server.

This callback is triggered during the initial generation of the world terrain.

```lua
 * function World:server_onTerrainCreated()
 *     -- Terrain creation logic here
 * end
```

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

#### Client

``` { .lua .api-signature }
WorldClass:client_onTerrainCreated(  )
```

Called on the client when a world's terrain is created for the first time.

This callback is used for client-side terrain generation tasks.

```lua
 * function World:client_onTerrainCreated()
 *     -- Client-side terrain creation logic
 * end
```

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

<a id="server_onterrainloaded"></a>
<a id="client_onterrainloaded"></a>
### onTerrainLoaded {#onterrainloaded}

#### Server

``` { .lua .api-signature }
WorldClass:server_onTerrainLoaded(  )
```

Called when a world's terrain is loaded (not created) on the server.

This is triggered when existing terrain data is loaded into the world.

```lua
 * function World:server_onTerrainLoaded()
 *     -- Terrain loading logic here
 * end
```

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

#### Client

``` { .lua .api-signature }
WorldClass:client_onTerrainLoaded(  )
```

Called on the client when a world's terrain is loaded (not created).

This function is useful for initializing client-side elements based on the loaded terrain.

```lua
 * function World:client_onTerrainLoaded()
 *     -- Client-side terrain loading logic
 * end
```

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

<a id="server_oncellloaded"></a>
<a id="client_oncellloaded"></a>
### onCellLoaded {#oncellloaded}

#### Server

``` { .lua .api-signature }
WorldClass:server_onCellLoaded( x, y )
```

Called when a world cell is loaded and feature complete, but has been before.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `x` | integer | Cell x position. |
| `y` | integer | Cell y position. |

#### Client

``` { .lua .api-signature }
WorldClass:client_onCellLoaded( x, y )
```

Called when a world cell is considered feature complete for a client (has nodes).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `x` | integer | Cell x position. |
| `y` | integer | Cell y position. |

<a id="server_oncellunloaded"></a>
<a id="client_oncellunloaded"></a>
### onCellUnloaded {#oncellunloaded}

#### Server

``` { .lua .api-signature }
WorldClass:server_onCellUnloaded( x, y )
```

Called when a world cell is no longer feature complete.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `x` | integer | Cell x position. |
| `y` | integer | Cell y position. |

#### Client

``` { .lua .api-signature }
WorldClass:client_onCellUnloaded( x, y )
```

Called when a world cell is no longer considered feature complete for a client (no longer has nodes).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `x` | integer | Cell x position. |
| `y` | integer | Cell y position. |

<a id="server_onprojectile"></a>
<a id="client_onprojectile"></a>
### onProjectile {#onprojectile}

#### Server

``` { .lua .api-signature }
WorldClass:server_onProjectile(
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
```

Called when a projectile hits something in this world.

> **Note:**
> If the shooter is destroyed before the projectile hits, the shooter value will be nil.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position in world space where the projectile hit. |
| `airTime` | number | The time, in seconds, that the projectile spent flying before the hit. |
| `velocity` | [Vec3](../Userdata/Vec3.md) | The velocity of the projectile at impact. |
| `projectileName` | string | The name of the projectile. (Legacy, use uuid instead) |
| `shooter` | [Player](../Userdata/Player.md)/[Unit](../Userdata/Unit.md)/[Shape](../Userdata/Shape.md)/[Harvestable](../Userdata/Harvestable.md)/nil | The shooter. Can be a [Player](../Userdata/Player.md), [Unit](../Userdata/Unit.md), [Shape](../Userdata/Shape.md), [Harvestable](../Userdata/Harvestable.md) or nil if unknown. |
| `damage` | integer | The damage value of the projectile. |
| `customData` | any | A Lua object that can be defined at shoot time using [sm.projectile.customProjectileAttack](../Static-Functions/sm.projectile.md#customprojectileattack) or an other custom version.  |
| `normal` | [Vec3](../Userdata/Vec3.md) | The normal at the point of impact. |
| `target` | [Character](../Userdata/Character.md)/[Shape](../Userdata/Shape.md)/[Harvestable](../Userdata/Harvestable.md)/[Lift](../Userdata/Lift.md)/nil | The hit target. Can be a [Character](../Userdata/Character.md), [Shape](../Userdata/Shape.md), [Harvestable](../Userdata/Harvestable.md), [Lift](../Userdata/Lift.md) or nil if terrain or unknown. |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the projectile. |

#### Client

``` { .lua .api-signature }
WorldClass:client_onProjectile(
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
```

Called when a projectile hits something in this world.

> **Note:**
> If the shooter is destroyed before the projectile hits, the shooter value will be nil.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position in world space where the projectile hit. |
| `airTime` | number | The time, in seconds, that the projectile spent flying before the hit. |
| `velocity` | [Vec3](../Userdata/Vec3.md) | The velocity of the projectile at impact. |
| `projectileName` | string | The name of the projectile. (Legacy, use uuid instead) |
| `shooter` | [Player](../Userdata/Player.md)/[Character](../Userdata/Character.md)/[Shape](../Userdata/Shape.md)/[Harvestable](../Userdata/Harvestable.md)/nil | The shooter. Can be a [Player](../Userdata/Player.md), [Character](../Userdata/Character.md), [Shape](../Userdata/Shape.md), [Harvestable](../Userdata/Harvestable.md) or nil if unknown. |
| `damage` | integer | The damage value of the projectile. |
| `normal` | [Vec3](../Userdata/Vec3.md) | The normal at the point of impact. |
| `target` | [Character](../Userdata/Character.md)/[Shape](../Userdata/Shape.md)/[Harvestable](../Userdata/Harvestable.md)/[Lift](../Userdata/Lift.md)/nil | The hit target. Can be a [Character](../Userdata/Character.md), [Shape](../Userdata/Shape.md), [Harvestable](../Userdata/Harvestable.md), [Lift](../Userdata/Lift.md) or nil if terrain or unknown. |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the projectile. |

<a id="server_oncollision"></a>
<a id="client_oncollision"></a>
### onCollision {#oncollision}

#### Server

``` { .lua .api-signature }
WorldClass:server_onCollision(
    objectA,
    objectB,
    position,
    pointVelocityA,
    pointVelocityB,
    normal
)
```

Called when a collision occurs in this world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `objectA` | [Shape](../Userdata/Shape.md)/[Character](../Userdata/Character.md)/[Harvestable](../Userdata/Harvestable.md)/[Lift](../Userdata/Lift.md)/nil | The first colliding object. Nil if terrain. |
| `objectB` | [Shape](../Userdata/Shape.md)/[Character](../Userdata/Character.md)/[Harvestable](../Userdata/Harvestable.md)/[Lift](../Userdata/Lift.md)/nil | The other colliding object. Nil if terrain. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position in world space where the collision occurred. |
| `pointVelocityA` | [Vec3](../Userdata/Vec3.md) | The velocity that that the first object had at the point of collision. |
| `pointVelocityB` | [Vec3](../Userdata/Vec3.md) | The velocity that that the other object had at the point of collision. |
| `normal` | [Vec3](../Userdata/Vec3.md) | The collision normal from objectA to objectB. |

#### Client

``` { .lua .api-signature }
WorldClass:client_onCollision(
    objectA,
    objectB,
    position,
    pointVelocityA,
    pointVelocityB,
    normal
)
```

Called when a collision occurs in this world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `objectA` | [Shape](../Userdata/Shape.md)/[Character](../Userdata/Character.md)/[Harvestable](../Userdata/Harvestable.md)/[Lift](../Userdata/Lift.md)/nil | One of the colliding objects. Nil if terrain. |
| `objectB` | [Shape](../Userdata/Shape.md)/[Character](../Userdata/Character.md)/[Harvestable](../Userdata/Harvestable.md)/[Lift](../Userdata/Lift.md)/nil | The other colliding object. Nil if terrain. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position in world space where the collision occurred. |
| `pointVelocityA` | [Vec3](../Userdata/Vec3.md) | The velocity that that the first object had at the point of collision. |
| `pointVelocityB` | [Vec3](../Userdata/Vec3.md) | The velocity that that the other object had at the point of collision. |
| `normal` | [Vec3](../Userdata/Vec3.md) | The collision normal from objectA to objectB. |

## Server-only

<a id="server_onreceiveupdate"></a>
### onReceiveUpdate {#onreceiveupdate}

``` { .lua .api-signature }
WorldClass:server_onReceiveUpdate(  )
```

Called occasionally to indicate that some time has passed.

For performance reasons; it recommended to use this instead of [server_onFixedUpdate](#server_onfixedupdate) for updates that do not need to happen frequently.

Use [sm.game.getCurrentTick](../Static-Functions/sm.game.md#getcurrenttick) to calculate the time.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

<a id="server_onunload"></a>
### onUnload {#onunload}

``` { .lua .api-signature }
WorldClass:server_onUnload(  )
```

Called when the [World](../Userdata/World.md) is unloaded from the game on shutdown.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |

<a id="server_oncellcreated"></a>
### onCellCreated {#oncellcreated}

``` { .lua .api-signature }
WorldClass:server_onCellCreated( x, y )
```

Called when a world cell is loaded and feature complete for the first time.

> **Note:**
> [Interactables](../Userdata/Interactable.md) created by terrain scripts should be processed here using [sm.cell.getInteractablesByTag](../Static-Functions/sm.cell.md#getinteractablesbytag) and [sm.cell.getInteractablesByUuid](../Static-Functions/sm.cell.md#getinteractablesbyuuid).
> They are only accessable for 1 tick after being created.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `x` | integer | Cell x position. |
| `y` | integer | Cell y position. |

<a id="server_oninteractablecreated"></a>
### onInteractableCreated {#oninteractablecreated}

``` { .lua .api-signature }
WorldClass:server_onInteractableCreated( interactable )
```

Called when an [Interactable](../Userdata/Interactable.md) [Shape](../Userdata/Shape.md) is built in the world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `interactable` | [Interactable](../Userdata/Interactable.md) | The [Interactable](../Userdata/Interactable.md) of the built [Shape](../Userdata/Shape.md). |

<a id="server_oninteractabledestroyed"></a>
### onInteractableDestroyed {#oninteractabledestroyed}

``` { .lua .api-signature }
WorldClass:server_onInteractableDestroyed( interactable )
```

Called when an [Interactable](../Userdata/Interactable.md) [Shape](../Userdata/Shape.md) is removed from the world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `interactable` | [Interactable](../Userdata/Interactable.md) | The [Interactable](../Userdata/Interactable.md) of the removed [Shape](../Userdata/Shape.md). |

<a id="server_onexplosion"></a>
### onExplosion {#onexplosion}

``` { .lua .api-signature }
WorldClass:server_onExplosion( center, destructionLevel, damage )
```

Called when an explosion occurs in this world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `center` | [Vec3](../Userdata/Vec3.md) | The center of the explosion. |
| `destructionLevel` | integer | The level of destruction done by this explosion. Corresponds to the 'durability' rating of a [Shape](../Userdata/Shape.md). |
| `damage` | integer | The damage value of the explosion. |

<a id="server_onmelee"></a>
### onMelee {#onmelee}

``` { .lua .api-signature }
WorldClass:server_onMelee(
    position,
    attacker,
    target,
    damage,
    power,
    direction,
    normal
)
```

Called when a melee attack hits something in this world.

> **Note:**
> If the attacker is destroyed before the hit lands, the attacker value will be nil.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position in world space where the attack hit. |
| `attacker` | [Player](../Userdata/Player.md)/[Unit](../Userdata/Unit.md)/nil | The attacker. Can be a [Player](../Userdata/Player.md), [Unit](../Userdata/Unit.md) or nil if unknown. |
| `target` | [Character](../Userdata/Character.md)/[Shape](../Userdata/Shape.md)/[Harvestable](../Userdata/Harvestable.md)/[Lift](../Userdata/Lift.md)/nil | The hit target. Can be a [Character](../Userdata/Character.md), [Shape](../Userdata/Shape.md), [Harvestable](../Userdata/Harvestable.md), [Lift](../Userdata/Lift.md) or nil if terrain or unknown. |
| `damage` | integer | The damage value of the melee hit. |
| `power` | number | The physical impact impact of the hit. |
| `direction` | [Vec3](../Userdata/Vec3.md) | The direction that the melee attack was made. |
| `normal` | [Vec3](../Userdata/Vec3.md) | The normal at the point of impact. |

<a id="server_onprojectilefire"></a>
### onProjectileFire {#onprojectilefire}

``` { .lua .api-signature }
WorldClass:server_onProjectileFire(
    position,
    velocity,
    projectileName,
    shooter,
    uuid
)
```

Called when a projectile is fired in this world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `position` | [Vec3](../Userdata/Vec3.md) | The position in world space where projectile was fired from. |
| `velocity` | [Vec3](../Userdata/Vec3.md) | The fire velocity of the projectile. |
| `projectileName` | string | The name of the projectile. (Legacy, use uuid instead) |
| `shooter` | [Player](../Userdata/Player.md)/[Unit](../Userdata/Unit.md)/[Shape](../Userdata/Shape.md)/[Harvestable](../Userdata/Harvestable.md)/nil | The shooter. Can be a [Player](../Userdata/Player.md), [Unit](../Userdata/Unit.md), [Shape](../Userdata/Shape.md), [Harvestable](../Userdata/Harvestable.md) or nil if unknown. |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the projectile. |

<a id="server_onvoxeldestruction"></a>
### onVoxelDestruction {#onvoxeldestruction}

``` { .lua .api-signature }
WorldClass:server_onVoxelDestruction( densityLoss, positions )
```

Called when a cluster of voxels are destroyed by a player or creation

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `densityLoss` | table | A table containing information about density loss for all materials. |
| `positions` | table | A table containing all positions where voxels were lost for each material. |

<a id="server_onvoxelconstruction"></a>
### onVoxelConstruction {#onvoxelconstruction}

``` { .lua .api-signature }
WorldClass:server_onVoxelConstruction( densityGain, positions )
```

Called when a cluster of voxels are added by a player

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `densityGain` | table | A table containing information about density gain for all materials. |
| `positions` | table | A table containing all positions where voxels were added for each material. |

<a id="server_onmining"></a>
### onMining {#onmining}

``` { .lua .api-signature }
WorldClass:server_onMining( spawns )
```

Called when the mining manager has filtered a batch of voxel loot candidates.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `spawns` | table | An array of { position = [Vec3](../Userdata/Vec3.md), spawnId = integer } describing where and what to spawn. |

## Client-only

<a id="client_onupdate"></a>
### onUpdate {#onupdate}

``` { .lua .api-signature }
WorldClass:client_onUpdate( deltaTime )
```

Called every frame.

During a frame update, graphics, animations and effects are updated.

> **Warning:**
> Because of how frequent this event is called, the game's frame rate is greatly affected by the amount of code executed here.
> For any non-graphics related code, consider using [client_onFixedUpdate](#client_onfixedupdate) instead.
> If the event is not in use, consider removing it from the script. (Event callbacks that are not implemented will not be called.)

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `deltaTime` | number | Delta time since the last frame. |

<a id="client_onclientdataupdate"></a>
### onClientDataUpdate {#onclientdataupdate}

``` { .lua .api-signature }
WorldClass:client_onClientDataUpdate( data, channel )
```

Called when the client receives new client data updates from the server set with [Network.setClientData](../Userdata/Network.md#setclientdata).

Data set in this way is persistent and the latest data will automatically be sent to new clients.

The data will arrive after [client_onCreate](#client_oncreate) during the same tick.

Channel 1 will be received before channel 2 if both are updated.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `data` | any | Any lua object set with [Network.setClientData](../Userdata/Network.md#setclientdata) |
| `channel` | integer | Client data channel, 1 or 2. (default: 1) |

<a id="client_onlocalplayerchangedworld"></a>
### onLocalPlayerChangedWorld {#onlocalplayerchangedworld}

``` { .lua .api-signature }
WorldClass:client_onLocalPlayerChangedWorld( world )
```

Called when the client player changes world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `self` | table | The class instance. |
| `world` | [World](../Userdata/World.md) | The entered world. |

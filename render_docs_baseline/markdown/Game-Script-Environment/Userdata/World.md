# World

**Associated namespace:** [sm.world](../Static-Functions/sm.world.md)

**Usage:** Server And Client

**Serializable:** Yes

A userdata object representing a <strong>world</strong> in the game.

**Values:**

- <a id="clientpublicdata"></a>`clientPublicData` [ **table** ] <br>
    - `Get`: (Client-Only) Returns client public data from a world.
    - `Set`: (Client-Only) Sets client public data on a World.

- <a id="id"></a>`id` [ **integer** ] <br>
    - `Get`: Returns the id of a world.

- <a id="indoor"></a>`indoor` [ **boolean** ] <br>
    - `Get`: Returns true if the world is an indoor world.

- <a id="publicdata"></a>`publicData` [ **table** ] <br>
    - `Get`: (Server-Only) Returns public data from a world.
    - `Set`: (Server-Only) Sets public data on a World.

**Operations:**

| Operation | Returns | Description |
| --- | --- | --- |
| <a id="__eq"></a>`World == World` | boolean | Checks if two instances of [World](World.md) refer to the same World. |

## Server + Client

### getCellBounds {#getcellbounds}

``` { .lua .api-signature }
world:getCellBounds(  )
```

Returns the minimum and maximum cell coordinates for the given world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](World.md) | The world. |

**Returns:**

| Type | Description |
| --- | --- |
| integer, integer, integer, integer | The minimum and maximum cell coordinates (minX, maxX, minY, maxY). |

### getDominantMaterialInCapsule {#getdominantmaterialincapsule}

``` { .lua .api-signature }
world:getDominantMaterialInCapsule( position, radius, height )
```

Finds the dominant voxel material inside a capsule volume.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](World.md) | The world to look in. |
| `position` | [Vec3](Vec3.md) | The center position of the capsule. |
| `radius` | number | The radius of the capsule. |
| `height` | number | The height of the cylindrical part of the capsule (Z-axis aligned, excluding hemispherical caps). |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The dominant material index value. (returns nil if no voxel was found) |
| integer | The highest single-voxel density of the dominant material. |
| [Vec3](Vec3.md) | The weighted average world position of the dominant material (biased toward dense, nearby voxels) |

### getDominantMaterialInSphere {#getdominantmaterialinsphere}

``` { .lua .api-signature }
world:getDominantMaterialInSphere( position, radius )
```

Finds the dominant voxel material inside a sphere volume.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](World.md) | The world to look in. |
| `position` | [Vec3](Vec3.md) | The center position of the sphere. |
| `radius` | number | The radius of the sphere. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The dominant material index value. (returns nil if no voxel was found) |
| integer | The highest single-voxel density of the dominant material. |
| [Vec3](Vec3.md) | The weighted average world position of the dominant material (biased toward dense, nearby voxels). |

### getId {#getid}

``` { .lua .api-signature }
world:getId(  )
```

Returns the id of a world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](World.md) | The world. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The world's id. |

### getVoxelMaterialFromWorldPosition {#getvoxelmaterialfromworldposition}

``` { .lua .api-signature }
world:getVoxelMaterialFromWorldPosition( worldPosition )
```

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](World.md) | The world to look in. |
| `worldPosition` | [Vec3](Vec3.md) | The position of the voxel chunk in the world. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The material index value. (returns nil if no voxel was at point) |
| integer | The density value. (returns nil if no voxel was at point) |

### getWeightedVoxelDensityInWorldPoint {#getweightedvoxeldensityinworldpoint}

``` { .lua .api-signature }
world:getWeightedVoxelDensityInWorldPoint( point )
```

Get weighted voxel density in world point.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](World.md) | The world to look in. |
| `point` | [Vec3](Vec3.md) | The world space point to check density in. |

**Returns:**

| Type | Description |
| --- | --- |
| number | Weighted density. (returns 0 if world doesn't have voxels) |
| [Vec3](Vec3.md) | Weighted direction of voxel influence. |

### getZoneId {#getzoneid}

``` { .lua .api-signature }
world:getZoneId( position )
```

Returns the zone id from a position.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](World.md) | The world. |
| `position` | [Vec3](Vec3.md) | The position. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The Zone id. (nil if position is invalid) |

### isCellInBounds {#iscellinbounds}

``` { .lua .api-signature }
world:isCellInBounds( x, y )
```

Checks if the given cell coordinates are within the bounds of the world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](World.md) | The world. |
| `x` | integer | The X coordinate of the cell. |
| `y` | integer | The Y coordinate of the cell. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if the cell is within the bounds of the world, false otherwise. |

### isIndoor {#isindoor}

``` { .lua .api-signature }
world:isIndoor(  )
```

Returns true if the world is an indoor world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](World.md) | The world. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if indoor. |

### isVoxelTerrainPointClear {#isvoxelterrainpointclear}

``` { .lua .api-signature }
world:isVoxelTerrainPointClear( referencePosition, testPosition )
```

Tests if a world position is free from voxel terrain coverage.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](World.md) | The world. |
| `referencePosition` | [Vec3](Vec3.md) | The reference position (e.g. character position). |
| `testPosition` | [Vec3](Vec3.md) | The position to test for voxel coverage (e.g. shape center). |

**Returns:**

| Type | Description |
| --- | --- |
| bool | True if the position is clear of voxel terrain, false if covered. |

### loadCellWithHandle {#loadcellwithhandle}

``` { .lua .api-signature }
world:loadCellWithHandle( x, y, callback?, params?, ref? )
```

Load a cell. The cell will stay loaded until the cell is released with [LoadCellHandle](LoadCellHandle.md).release()

or when the [LoadCellHandle](LoadCellHandle.md) is garbage collected

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](World.md) | The world. |
| `x` | integer | Cell X position. |
| `y` | integer | Cell Y Position. |
| `callback` *(optional)* | string | Lua function to call when cell is loaded. Callback parameters are ( world, x, y, params ) |
| `params` *(optional)* | any | Parameter object passed to the callback. |
| `ref` *(optional)* | ref | Script ref to callback object. |

**Returns:**

| Type | Description |
| --- | --- |
| [LoadCellHandle](LoadCellHandle.md) | Handle to releasing cell. |

### reloadCell {#reloadcell}

``` { .lua .api-signature }
world:reloadCell( x, y, callback?, ref?, params? )
```

Reload a cell. Callback result values: 0 means cell isnt active and wont be reloaded, 1 means success

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](World.md) | The world. |
| `x` | integer | Cell X position. |
| `y` | integer | Cell Y Position. |
| `callback` *(optional)* | string | Lua function to call when cell is reloaded. Callback parameters are ( world, x, y, result ) (Optional) |
| `ref` *(optional)* | ref | Script ref to callback object. (Optional) |
| `params` *(optional)* | any | Parameter passed to the callback. (Optional) |

### setTerrainScriptData {#setterrainscriptdata}

``` { .lua .api-signature }
world:setTerrainScriptData( data )
```

Set data to pass on to the terrain generation script. If no data is set the terrain generation script receives the same data as the world script.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](World.md) | The world. |
| `data` | any | Any data, available to the terrain generation script as parameter 6 in the create callback. |

## Server-only

### clearLightColorOverride {#clearlightcoloroverride}

``` { .lua .api-signature }
world:clearLightColorOverride(  )
```

Clears the override light color on all light controllers in the world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](World.md) | The world. |

### destroy {#destroy}

``` { .lua .api-signature }
world:destroy(  )
```

Destroys the given world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](World.md) | The world that should be removed. |

### isCellLoadedServer {#iscellloadedserver}

``` { .lua .api-signature }
world:isCellLoadedServer( cellX, cellY )
```

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](World.md) | The world to look in. |
| `cellX` | integer | The cell X value. |
| `cellY` | integer | The cell Y value. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | If the cell is loaded or not. |

### loadCell {#loadcell}

``` { .lua .api-signature }
world:loadCell( x, y, player, callback?, params?, ref? )
```

Load a cell for player. The cell will stay loaded until the player steps into the cell.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](World.md) | The world. |
| `x` | integer | Cell X position. |
| `y` | integer | Cell Y Position. |
| `player` | [Player](Player.md) | A player to load for, can be nil. |
| `callback` *(optional)* | string | Lua function to call when cell is loaded. Callback parameters are ( world, x, y, player, params ) |
| `params` *(optional)* | any | Parameter object passed to the callback. |
| `ref` *(optional)* | ref | Script ref to callback object. |

### loadNavMeshWithHandle {#loadnavmeshwithhandle}

``` { .lua .api-signature }
world:loadNavMeshWithHandle( x, y, callback?, params?, ref? )
```

Load a cell and nav mesh. The cell will stay loaded until the cell is released with [LoadCellHandle](LoadCellHandle.md).release()

or when the [LoadCellHandle](LoadCellHandle.md) is garbage collected

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](World.md) | The world. |
| `x` | integer | Cell X position. |
| `y` | integer | Cell Y Position. |
| `callback` *(optional)* | string | Lua function to call when cell nav mesh is created. Callback parameters are ( world, x, y, params ) |
| `params` *(optional)* | any | Parameter object passed to the callback. |
| `ref` *(optional)* | ref | Script ref to callback object. |

**Returns:**

| Type | Description |
| --- | --- |
| [LoadCellHandle](LoadCellHandle.md) | Handle to releasing cell. |

### setLightColorOverride {#setlightcoloroverride}

``` { .lua .api-signature }
world:setLightColorOverride( color )
```

Sets the override light color on all light controllers in the world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](World.md) | The world. |
| `color` | [Color](Color.md) | The override color. |

### setMiningConfig {#setminingconfig}

``` { .lua .api-signature }
world:setMiningConfig( config )
```

Configures the mining loot population. Matched candidates are sent to the

world script via the server_onMining callback whenever voxels are removed.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](World.md) | The world. |
| `config` | table | Spawn rules keyed by voxel material index (1-8). Each value is an array of rule tables: { sizeX, sizeY, sizeZ, seed, spawnId = integers, tunnelType = string (optional), maxDist = number (optional) }. |

### sphereVoxelDensityAddition {#spherevoxeldensityaddition}

``` { .lua .api-signature }
world:sphereVoxelDensityAddition( position, radius, material, player? )
```

Modify voxel terrain with a sphere shape

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](World.md) | The world. |
| `position` | [Vec3](Vec3.md) | The world position of the sphere. |
| `radius` | number | The radius of the sphere. |
| `material` | integer | The material to add [0-7]. |
| `player` *(optional)* | [Player](Player.md) | The player who constructed. (Optional) |

### sphereVoxelDensitySubtraction {#spherevoxeldensitysubtraction}

``` { .lua .api-signature }
world:sphereVoxelDensitySubtraction(
    position,
    radius,
    filter?,
    strength?,
    callback?,
    params?
)
```

Modify destructable terrain with a sphere shape

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](World.md) | The world. |
| `position` | [Vec3](Vec3.md) | The world position of the sphere. |
| `radius` | number | The radius of the sphere. |
| `filter` *(optional)* | integer | The materials the shape can modify. (See [sm.world.voxelFilter](../Static-Functions/sm.world.md#voxelfilter)). (Defaults to sm.world.voxelFilter.all) |
| `strength` *(optional)* | number | The strength of the modification. (Defaults to radius) |
| `callback` *(optional)* | string | Lua function to call when cell is loaded. Callback parameters are a table of destruction data { remDensities = {integer, ..}, avgPositions = {[Vec3](Vec3.md), ..} } and (optional) pass-through params passed to this function. |
| `params` *(optional)* | any | Parameter passed to the callback. (Optional) |

### voxelDensityAddition {#voxeldensityaddition}

``` { .lua .api-signature }
world:voxelDensityAddition(
    position,
    surfaceNormal,
    maxDistance,
    targetDensity,
    material,
    filter?,
    player?
)
```

Modify destructable terrain

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](World.md) | The world. |
| `position` | [Vec3](Vec3.md) | The voxel world position. |
| `surfaceNormal` | [Vec3](Vec3.md) | The surface normal. |
| `maxDistance` | number | The maximum distance from position that can be modified. |
| `targetDensity` | integer | The target density to add. |
| `material` | integer | The material to add [0-7]. |
| `filter` *(optional)* | integer | The materials the shape can modify. (See [sm.world.voxelFilter](../Static-Functions/sm.world.md#voxelfilter)). (Defaults to sm.world.voxelFilter.all) |
| `player` *(optional)* | [Player](Player.md) | The player who constructed. (Optional) |

<a id="voxeldensitysubtraction"></a>
### voxelDensitySubtraction(Vec3, Vec3, number, integer, integer?, boolean?, string?, any?) {#voxeldensitysubtraction-vec3-vec3-number-integer-integer-optional-boolean-optional-string-optional-any-optional}

``` { .lua .api-signature }
world:voxelDensitySubtraction(
    position,
    direction,
    radius,
    targetDensity,
    filter?,
    enableDestructionEffect?,
    callback?,
    params?
)
```

Modify destructible terrain around a point or line with a radius.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](World.md) | The world. |
| `position` | [Vec3](Vec3.md) | The world position a of the modification. |
| `direction` | [Vec3](Vec3.md) | The world direction of the modification. Non normalized direction that defines the center line of modification. |
| `radius` | number | The maximum distance from positions in the line defined by position and direction that can be modified. |
| `targetDensity` | integer | The target density to remove. |
| `filter` *(optional)* | integer | The materials the shape can modify. (See [sm.world.voxelFilter](../Static-Functions/sm.world.md#voxelfilter)). (Defaults to sm.world.voxelFilter.all) |
| `enableDestructionEffect` *(optional)* | boolean | Whether to enable destruction effect. (Defaults to true) |
| `callback` *(optional)* | string | Lua function to call when cell is loaded. Callback parameters are a table of destruction data { remDensities = {integer, ..}, avgPositions = {[Vec3](Vec3.md), ..} } and (optional) pass-through params passed to this function. |
| `params` *(optional)* | any | Parameter passed to the callback. (Optional) |

### voxelDensitySubtraction(Vec3, Vec3, number, table, integer?, boolean?, string?, any?) {#voxeldensitysubtraction-vec3-vec3-number-table-integer-optional-boolean-optional-string-optional-any-optional}

``` { .lua .api-signature }
world:voxelDensitySubtraction(
    position,
    direction,
    radius,
    targetDensities,
    filter?,
    enableDestructionEffect?,
    callback?,
    params?
)
```

Modify destructible terrain around a point or line with a radius.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](World.md) | The world. |
| `position` | [Vec3](Vec3.md) | The world position a of the modification. |
| `direction` | [Vec3](Vec3.md) | The world direction of the modification. Non normalized direction that defines the center line of modification. |
| `radius` | number | The maximum distance from positions in the line defined by position and direction that can be modified. |
| `targetDensities` | table | A table of target densities to remove per material type {[1] = integer, .., [8] = integer}. |
| `filter` *(optional)* | integer | The materials the shape can modify. (See [sm.world.voxelFilter](../Static-Functions/sm.world.md#voxelfilter)). (Defaults to sm.world.voxelFilter.all) |
| `enableDestructionEffect` *(optional)* | boolean | Whether to enable destruction effect. (Defaults to true) |
| `callback` *(optional)* | string | Lua function to call when cell is loaded. Callback parameters are a table of destruction data { remDensities = {integer, ..}, avgPositions = {[Vec3](Vec3.md), ..} } and (optional) pass-through params passed to this function. |
| `params` *(optional)* | any | Parameter passed to the callback. (Optional) |

## Client-only

### isCellLoadedClient {#iscellloadedclient}

``` { .lua .api-signature }
world:isCellLoadedClient( cellX, cellY )
```

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](World.md) | The world to look in. |
| `cellX` | integer | The cell X value. |
| `cellY` | integer | The cell Y value. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | If the cell is loaded or not. |

# sm.terrainTile

Reads .tile file data

## Constants

### loadFlags {#loadflags}

Prefab content load flags.

| Value |
| --- |
| creations |
| nodes |
| assets |
| decals |
| harvestables |
| kinematics |
| voxelMeshes |
| all |

**Returns:**

| Type | Description |
| --- | --- |
| table | List of flags for use with getContentFromPrefab. |

## Functions

### getAssetsForCell {#getassetsforcell}

``` { .lua .api-signature }
sm.terrainTile.getAssetsForCell( tileUid, cellOffsetX, cellOffsetY, sizeLevel )
```

Returns a table of all assets in a terrain cell.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tileUid` | [Uuid](../Userdata/Uuid.md) | The tile uuid. |
| `cellOffsetX` | integer | The cell X offset. |
| `cellOffsetY` | integer | The cell Y offset. |
| `sizeLevel` | integer | The size level of asset. [0-3] |

**Returns:**

| Type | Description |
| --- | --- |
| table | A table { { uuid = [Uuid](../Userdata/Uuid.md), pos = [Vec3](../Userdata/Vec3.md), rot = [Quat](../Userdata/Quat.md), colors = { string = [Color](../Userdata/Color.md), ...}, tags = { string, ... } }, ... } of assets in the cell. |

### getClutterIdxAt {#getclutteridxat}

``` { .lua .api-signature }
sm.terrainTile.getClutterIdxAt( tileUid, cellOffsetX, cellOffsetY, x, y )
```

Returns the clutter index at position (x,y) in a tile cell.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tileUid` | [Uuid](../Userdata/Uuid.md) | The tile uuid. |
| `cellOffsetX` | integer | The cell X offset. |
| `cellOffsetY` | integer | The cell Y offset. |
| `x` | integer | The local X value. |
| `y` | integer | The local Y value. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The clutter index. |

### getColorAt {#getcolorat}

``` { .lua .api-signature }
sm.terrainTile.getColorAt( tileUid, cellOffsetX, cellOffsetY, lod, x, y )
```

Returns the terrain color at position (x,y) in a tile cell.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tileUid` | [Uuid](../Userdata/Uuid.md) | The tile uuid. |
| `cellOffsetX` | integer | The cell X offset. |
| `cellOffsetY` | integer | The cell Y offset. |
| `lod` | integer | The level of detail. [0-5] |
| `x` | integer | The local X value. |
| `y` | integer | The local Y value. |

**Returns:**

| Type | Description |
| --- | --- |
| number,number,number | The color R, G, B values. |

### getContentFromPrefab {#getcontentfromprefab}

``` { .lua .api-signature }
sm.terrainTile.getContentFromPrefab( prefabPath, loadFlags? )
```

Returns the content of a prefab.

Return value 1: A table of creations in the prefab. { { name = string, pos = [Vec3](../Userdata/Vec3.md), rot = [Quat](../Userdata/Quat.md), sortingIndex = integer, tags = { string, ... } }, ... }

Return value 2: A table of prefabs in the prefab. { { name = string, pos = [Vec3](../Userdata/Vec3.md), rot = [Vec3](../Userdata/Vec3.md), scale = [Vec3](../Userdata/Vec3.md), tags = { string, ... }, flags = integer }, ... }

Return value 3: A table of nodes in the prefab. { { pos = [Vec3](../Userdata/Vec3.md), rot = [Quat](../Userdata/Quat.md), scale = [Vec3](../Userdata/Vec3.md), tags = { string, ... }, params = table } }

Return value 4: A table of assets in the prefab. { { uuid = [Uuid](../Userdata/Uuid.md), pos = [Vec3](../Userdata/Vec3.md), rot = [Quat](../Userdata/Quat.md), slopeNormal = [Vec3](../Userdata/Vec3.md), colors = { string = [Color](../Userdata/Color.md), ...}, tags = { string, ... } }, ... }

Return value 5: A table of decals in the prefab. { { pos = [Vec3](../Userdata/Vec3.md), rot = [Vec3](../Userdata/Vec3.md), scale = [Vec3](../Userdata/Vec3.md), decalId = integer, color = [Color](../Userdata/Color.md), layer = integer,  tags = { string, ... } }, ... }

Return value 6: A table of harvestables in the prefab. { {uuid = [Uuid](../Userdata/Uuid.md), pos = [Vec3](../Userdata/Vec3.md), rot = [Quat](../Userdata/Quat.md), color = [Color](../Userdata/Color.md), params = table, tags = { string, ... } }, ... }

Return value 7: A table of kinematics in the prefab. { {uuid = [Uuid](../Userdata/Uuid.md), pos = [Vec3](../Userdata/Vec3.md), rot = [Quat](../Userdata/Quat.md), scale = [Vec3](../Userdata/Vec3.md), color = [Color](../Userdata/Color.md), params = table, tags = { string, ... } }, .. }

Return value 8: A table containing the min and max bounds of the prefab. { min = [Vec3](../Userdata/Vec3.md), max = [Vec3](../Userdata/Vec3.md) }

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `prefabPath` | string | The path to the prefab file. |
| `loadFlags` *(optional)* | integer | A mask of content to load. Defaults to all objects (optional) |

**Returns:**

| Type | Description |
| --- | --- |
| table,table,table,table,table,table,table,table | Prefab content tables. |

### getCreationsForCell {#getcreationsforcell}

``` { .lua .api-signature }
sm.terrainTile.getCreationsForCell( tileUid, cellOffsetX, cellOffsetY )
```

Returns a table of all creations in a terrain cell.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tileUid` | [Uuid](../Userdata/Uuid.md) | The tile uuid. |
| `cellOffsetX` | integer | The cell X offset. |
| `cellOffsetY` | integer | The cell Y offset. |

**Returns:**

| Type | Description |
| --- | --- |
| table | A table { { pathOrJson = string, pos = [Vec3](../Userdata/Vec3.md), rot = [Quat](../Userdata/Quat.md) }, ... } of creations in the cell. |

### getCreatorId {#getcreatorid}

``` { .lua .api-signature }
sm.terrainTile.getCreatorId( path )
```

Returns the id of the tiles creator.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `path` | string | The tile's path. |

**Returns:**

| Type | Description |
| --- | --- |
| string | The creator's id. |

### getDecalsForCell {#getdecalsforcell}

``` { .lua .api-signature }
sm.terrainTile.getDecalsForCell( tileUid, cellOffsetX, cellOffsetY )
```

Returns all decals for a cell in a tile.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tileUid` | [Uuid](../Userdata/Uuid.md) | The tile uuid. |
| `cellOffsetX` | integer | The cell X offset. |
| `cellOffsetY` | integer | The cell Y offset. |

**Returns:**

| Type | Description |
| --- | --- |
| table | A table { { pos = [Vec3](../Userdata/Vec3.md), rot = [Vec3](../Userdata/Vec3.md), scale = [Vec3](../Userdata/Vec3.md), decalId = integer, color = [Color](../Userdata/Color.md), layer = integer,  tags = { string, ... } }, ... } of decals in the cell. |

### getHarvestablesForCell {#getharvestablesforcell}

``` { .lua .api-signature }
sm.terrainTile.getHarvestablesForCell(
    tileUid,
    cellOffsetX,
    cellOffsetY,
    sizeLevel
)
```

Returns a table of all harvestables in a terrain cell.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tileUid` | [Uuid](../Userdata/Uuid.md) | The tile uuid. |
| `cellOffsetX` | integer | The cell X offset. |
| `cellOffsetY` | integer | The cell Y offset. |
| `sizeLevel` | integer | The size level of harvestables. [0-3] |

**Returns:**

| Type | Description |
| --- | --- |
| table | A table { {uuid = [Uuid](../Userdata/Uuid.md), pos = [Vec3](../Userdata/Vec3.md), rot = [Quat](../Userdata/Quat.md), color = [Color](../Userdata/Color.md), params = table, tags = { string, ... } }, ... } of harvestables in the cell. |

### getHeightAt {#getheightat}

``` { .lua .api-signature }
sm.terrainTile.getHeightAt( tileUid, cellOffsetX, cellOffsetY, lod, x, y )
```

Returns the terrain height at position (x,y) in a tile cell.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tileUid` | [Uuid](../Userdata/Uuid.md) | The tile uuid. |
| `cellOffsetX` | integer | The cell X offset. |
| `cellOffsetY` | integer | The cell Y offset. |
| `lod` | integer | The level of detail. [0-5] |
| `x` | integer | The local X value. |
| `y` | integer | The local Y value. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The height. |

### getKinematicsForCell {#getkinematicsforcell}

``` { .lua .api-signature }
sm.terrainTile.getKinematicsForCell(
    tileUid,
    cellOffsetX,
    cellOffsetY,
    sizeLevel
)
```

Returns a table of all kinematics in a terrain cell.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tileUid` | [Uuid](../Userdata/Uuid.md) | The tile uuid. |
| `cellOffsetX` | integer | The cell X offset. |
| `cellOffsetY` | integer | The cell Y offset. |
| `sizeLevel` | integer | The size level of kinematics. [0-3] |

**Returns:**

| Type | Description |
| --- | --- |
| table | A table { {uuid = [Uuid](../Userdata/Uuid.md), pos = [Vec3](../Userdata/Vec3.md), rot = [Quat](../Userdata/Quat.md), scale = [Vec3](../Userdata/Vec3.md), color = [Color](../Userdata/Color.md), params = table, tags = { string, ... } }, .. } of kinematics in the cell. |

### getMaterialAt {#getmaterialat}

``` { .lua .api-signature }
sm.terrainTile.getMaterialAt( tileUid, cellOffsetX, cellOffsetY, lod, x, y )
```

Returns the terrain material at position (x,y) in a tile cell.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tileUid` | [Uuid](../Userdata/Uuid.md) | The tile uuid. |
| `cellOffsetX` | integer | The cell X offset. |
| `cellOffsetY` | integer | The cell Y offset. |
| `lod` | integer | The level of detail. [0-5] |
| `x` | integer | The local X value. |
| `y` | integer | The local Y value. |

**Returns:**

| Type | Description |
| --- | --- |
| number,number,number,number,number,number,number,number | Material weights 1-8. |

### getNodesForCell {#getnodesforcell}

``` { .lua .api-signature }
sm.terrainTile.getNodesForCell( tileUid, cellOffsetX, cellOffsetY )
```

Returns all nodes for a cell in a tile.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tileUid` | [Uuid](../Userdata/Uuid.md) | The tile uuid. |
| `cellOffsetX` | integer | The cell X offset. |
| `cellOffsetY` | integer | The cell Y offset. |

**Returns:**

| Type | Description |
| --- | --- |
| table | A table { { pos = [Vec3](../Userdata/Vec3.md), rot = [Quat](../Userdata/Quat.md), scale = [Vec3](../Userdata/Vec3.md), tags = { string, ... }, params = table } } of nodes in the cell. |

### getPrefabsForCell {#getprefabsforcell}

``` { .lua .api-signature }
sm.terrainTile.getPrefabsForCell( tileUid, cellOffsetX, cellOffsetY )
```

Returns all prefabs in a cell.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tileUid` | [Uuid](../Userdata/Uuid.md) | The tile uuid. |
| `cellOffsetX` | integer | The cell X offset. |
| `cellOffsetY` | integer | The cell Y offset. |

**Returns:**

| Type | Description |
| --- | --- |
| table | A table { { name = string, pos = [Vec3](../Userdata/Vec3.md), rot = [Vec3](../Userdata/Vec3.md), scale = [Vec3](../Userdata/Vec3.md), tags = { string, ... }, flags = integer }, ... } of prefabs in the cell. |

### getSize {#getsize}

``` { .lua .api-signature }
sm.terrainTile.getSize( path )
```

Returns the size of a tile as the number of cells along one of the axises.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `path` | string | The tile's path. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The size. |

### getTileUuid {#gettileuuid}

``` { .lua .api-signature }
sm.terrainTile.getTileUuid( path )
```

Returns the uuid for a tile file.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `path` | string | The tile's path. |

**Returns:**

| Type | Description |
| --- | --- |
| [Uuid](../Userdata/Uuid.md) | The tile's uuid. |

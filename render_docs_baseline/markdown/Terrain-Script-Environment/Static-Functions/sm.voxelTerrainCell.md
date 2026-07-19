# sm.voxelTerrainCell

Voxel grid

## Constants

### voxelFilter {#voxelfilter}

Filters are used to specify what materials an action should modify.

| Value | Description |
| --- | --- |
| none | 0 |
| material0 | 1 |
| material1 | 2 |
| material2 | 4 |
| material3 | 8 |
| material4 | 16 |
| material5 | 32 |
| material6 | 64 |
| material7 | 128 |
| all | 255 |

**Returns:**

| Type | Description |
| --- | --- |
| table | The filter type list. |

## Functions

### copyTileCellVoxels {#copytilecellvoxels}

``` { .lua .api-signature }
sm.voxelTerrainCell.copyTileCellVoxels(
    tileUid,
    cellOffsetX,
    cellOffsetY,
    rotationStep,
    srcPos?,
    dstPos?,
    srcSize?
)
```

Copies a custom amount of voxel data from a tile to the voxel grid.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tileUid` | [Uuid](../Userdata/Uuid.md) | The tile uuid. |
| `cellOffsetX` | integer | The tile cell X offset. |
| `cellOffsetY` | integer | The tile cell Y offset. |
| `rotationStep` | integer | The tile rotation (0-3). |
| `srcPos` *(optional)* | [Vec3](../Userdata/Vec3.md) | The source chunk coord in the tile cell to copy. |
| `dstPos` *(optional)* | [Vec3](../Userdata/Vec3.md) | The destination coord in the cell voxel grid. |
| `srcSize` *(optional)* | [Vec3](../Userdata/Vec3.md) | The source size in chunks to copy. |

### copyTileCellVoxelsOnlyAir {#copytilecellvoxelsonlyair}

``` { .lua .api-signature }
sm.voxelTerrainCell.copyTileCellVoxelsOnlyAir(
    tileUid,
    cellOffsetX,
    cellOffsetY,
    rotationStep,
    srcPos,
    dstPos,
    srcSize
)
```

Copies a custom amount of voxel data from a tile to the voxel grid.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tileUid` | [Uuid](../Userdata/Uuid.md) | The tile uuid. |
| `cellOffsetX` | integer | The tile cell X offset. |
| `cellOffsetY` | integer | The tile cell Y offset. |
| `rotationStep` | integer | The tile rotation (0-3). |
| `srcPos` | [Vec3](../Userdata/Vec3.md) | The source chunk coord in the tile to copy. |
| `dstPos` | [Vec3](../Userdata/Vec3.md) | The destination coord in the cell voxel grid. |
| `srcSize` | [Vec3](../Userdata/Vec3.md) | The source size in chunks to copy. |

### copyTileCellVoxelsOnlyAirAndMasked {#copytilecellvoxelsonlyairandmasked}

``` { .lua .api-signature }
sm.voxelTerrainCell.copyTileCellVoxelsOnlyAirAndMasked(
    tileUid,
    cellOffsetX,
    cellOffsetY,
    rotationStep,
    srcPos,
    dstPos,
    srcSize,
    voxelFilter
)
```

Copies a custom amount of voxel data from a tile to the voxel grid.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tileUid` | [Uuid](../Userdata/Uuid.md) | The tile uuid. |
| `cellOffsetX` | integer | The tile cell X offset. |
| `cellOffsetY` | integer | The tile cell Y offset. |
| `rotationStep` | integer | The tile rotation (0-3). |
| `srcPos` | [Vec3](../Userdata/Vec3.md) | The source chunk coord in the tile to copy. |
| `dstPos` | [Vec3](../Userdata/Vec3.md) | The destination coord in the cell voxel grid. |
| `srcSize` | [Vec3](../Userdata/Vec3.md) | The source size in chunks to copy. |
| `voxelFilter` | integer | The voxel material filter to be copied. (See [sm.voxelTerrainCell.voxelFilter](#voxelfilter)) |

### copyTileCellVoxelsOnlyFilled {#copytilecellvoxelsonlyfilled}

``` { .lua .api-signature }
sm.voxelTerrainCell.copyTileCellVoxelsOnlyFilled(
    tileUid,
    cellOffsetX,
    cellOffsetY,
    rotationStep,
    srcPos,
    dstPos,
    srcSize
)
```

Copies a custom amount of voxel data from a tile to the voxel grid.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tileUid` | [Uuid](../Userdata/Uuid.md) | The tile uuid. |
| `cellOffsetX` | integer | The tile cell X offset. |
| `cellOffsetY` | integer | The tile cell Y offset. |
| `rotationStep` | integer | The tile rotation (0-3). |
| `srcPos` | [Vec3](../Userdata/Vec3.md) | The source chunk coord in the tile to copy. |
| `dstPos` | [Vec3](../Userdata/Vec3.md) | The destination coord in the cell voxel grid. |
| `srcSize` | [Vec3](../Userdata/Vec3.md) | The source size in chunks to copy. |

### fillEmptyConvexHull {#fillemptyconvexhull}

``` { .lua .api-signature }
sm.voxelTerrainCell.fillEmptyConvexHull(
    vertices,
    margin,
    densityThreshold,
    material,
    density,
    noiseFrequency?,
    noiseIntensity?
)
```

Sets empty voxel (below threshold) material and density in convex hull shape in the cell's voxel grid.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `vertices` | table | Table of vertices {[Vec3](../Userdata/Vec3.md), ...} that make up the convex hull. |
| `margin` | number | Hull margin added outside the hull. |
| `densityThreshold` | number | Existing normalized density must be below threshold for fill to happen. |
| `material` | integer | New material to set in convex hull. |
| `density` | number | New normalized density to set in convex hull. |
| `noiseFrequency` *(optional)* | number | Noise frequency of applied simplex noise. (Defaults to 1) |
| `noiseIntensity` *(optional)* | number | Noise intensity of applied simplex noise. (Defaults to 0) |

### setDensityConvexHull {#setdensityconvexhull}

``` { .lua .api-signature }
sm.voxelTerrainCell.setDensityConvexHull(
    vertices,
    margin,
    density,
    voxelFilter?,
    noiseFrequency?,
    noiseIntensity?
)
```

Sets density in convex hull shape to the cell's voxel grid.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `vertices` | table | Table of vertices {[Vec3](../Userdata/Vec3.md), ...} that make up the convex hull. |
| `margin` | number | Hull margin added outside the hull. |
| `density` | number | New normalized density. |
| `voxelFilter` *(optional)* | integer | The voxel material filter to overwrite. (Defaults to [sm.voxelTerrainCell.voxelFilter.all](#voxelfilter)) |
| `noiseFrequency` *(optional)* | number | Noise frequency of applied simplex noise. (Defaults to 1) |
| `noiseIntensity` *(optional)* | number | Noise intensity of applied simplex noise. (Defaults to 0) |

### setMaterialAndDensityConvexHull {#setmaterialanddensityconvexhull}

``` { .lua .api-signature }
sm.voxelTerrainCell.setMaterialAndDensityConvexHull(
    vertices,
    margin,
    material,
    density,
    voxelFilter?,
    noiseFrequency?,
    noiseIntensity?
)
```

Sets material in convex hull shape in the cell's voxel grid.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `vertices` | table | Table of vertices {[Vec3](../Userdata/Vec3.md), ...} that make up the convex hull. |
| `margin` | number | Hull margin added outside the hull. |
| `material` | integer | New material in convex hull. |
| `density` | number | New normalized density. |
| `voxelFilter` *(optional)* | integer | The voxel material filter to overwrite. (Defaults to [sm.voxelTerrainCell.voxelFilter.all](#voxelfilter)) |
| `noiseFrequency` *(optional)* | number | Noise frequency of applied simplex noise. (Defaults to 1) |
| `noiseIntensity` *(optional)* | number | Noise intensity of applied simplex noise. (Defaults to 0) |

### setMaterialConvexHull {#setmaterialconvexhull}

``` { .lua .api-signature }
sm.voxelTerrainCell.setMaterialConvexHull(
    vertices,
    margin,
    material,
    voxelFilter?,
    noiseFrequency?,
    noiseIntensity?
)
```

Sets material in convex hull shape in the cell's voxel grid.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `vertices` | table | Table of vertices {[Vec3](../Userdata/Vec3.md), ...} that make up the convex hull. |
| `margin` | number | Hull margin added outside the hull. |
| `material` | integer | New material in convex hull. |
| `voxelFilter` *(optional)* | integer | The voxel material filter to overwrite. (Defaults to [sm.voxelTerrainCell.voxelFilter.all](#voxelfilter)) |
| `noiseFrequency` *(optional)* | number | Noise frequency of applied simplex noise. (Defaults to 1) |
| `noiseIntensity` *(optional)* | number | Noise intensity of applied simplex noise. (Defaults to 0) |

### writeTileCellVoxels {#writetilecellvoxels}

``` { .lua .api-signature }
sm.voxelTerrainCell.writeTileCellVoxels(
    tileUid,
    cellOffsetX,
    cellOffsetY,
    rotationStep
)
```

Writes the voxel data from a tile to the cell's voxel grid.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `tileUid` | [Uuid](../Userdata/Uuid.md) | The tile uuid. |
| `cellOffsetX` | integer | The tile cell X offset. |
| `cellOffsetY` | integer | The tile cell Y offset. |
| `rotationStep` | integer | The tile rotation (0-3). |

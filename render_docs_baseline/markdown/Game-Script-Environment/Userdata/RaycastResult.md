# RaycastResult

**Usage:** Server And Client

**Serializable:** No

A userdata object representing a <strong>raycast result</strong>.

A <strong>raycast result</strong> is a collection of data received from a raycast. The result contains information about where the raycast travelled and what objects it eventually hit.

Raycast results are the result of functions such as [sm.physics.raycast](../Static-Functions/sm.physics.md#raycast), [sm.physics.distanceRaycast](../Static-Functions/sm.physics.md#distanceraycast) and [sm.localPlayer.getRaycast](../Static-Functions/sm.localPlayer.md#getraycast).

**Values:**

- <a id="directionworld"></a>`directionWorld` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the direction vector of the raycast

- <a id="fraction"></a>`fraction` [ **number** ] <br>
    - `Get`: Returns the fraction (0&ndash;1) of the distance reached until collision divided by the ray's length.

- <a id="normallocal"></a>`normalLocal` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the normal vector of the surface that was hit, relative to the target's rotation.

- <a id="normalworld"></a>`normalWorld` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the normal vector of the hit surface

- <a id="originworld"></a>`originWorld` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the starting world position of the raycast.

- <a id="pointlocal"></a>`pointLocal` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the world position of the point that was hit, relative to the target's position.

- <a id="pointworld"></a>`pointWorld` [ **[Vec3](Vec3.md)** ] <br>
    - `Get`: Returns the world position of the point that was hit.

- <a id="type"></a>`type` [ **string** ] <br>
    - `Get`: Returns the physics type of the target that was hit. (See [sm.physics.types](../Static-Functions/sm.physics.md#types))

- <a id="valid"></a>`valid` [ **boolean** ] <br>
    - `Get`: Returns whether the raycast successfully hit a target.

## Functions

### getAreaTrigger {#getareatrigger}

``` { .lua .api-signature }
raycastResult:getAreaTrigger(  )
```

Returns the [AreaTrigger](AreaTrigger.md) hit during the raycast. This is only possible if [RaycastResult.type](#type) is equal to "areaTrigger", otherwise this will return nil.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `raycastResult` | [RaycastResult](RaycastResult.md) | The raycast result. |

**Returns:**

| Type | Description |
| --- | --- |
| [AreaTrigger](AreaTrigger.md) | The areaTrigger target. |

### getBody {#getbody}

``` { .lua .api-signature }
raycastResult:getBody(  )
```

Returns the [Body](Body.md) hit during the raycast. This is only possible if [RaycastResult.type](#type) is equal to "body", otherwise this will return nil.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `raycastResult` | [RaycastResult](RaycastResult.md) | The raycast result. |

**Returns:**

| Type | Description |
| --- | --- |
| [Body](Body.md) | The body target. |

### getCharacter {#getcharacter}

``` { .lua .api-signature }
raycastResult:getCharacter(  )
```

Returns the [Character](Character.md) hit during the raycast. This is only possible if [RaycastResult.type](#type) is equal to "character", otherwise this will return nil.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `raycastResult` | [RaycastResult](RaycastResult.md) | The raycast result. |

**Returns:**

| Type | Description |
| --- | --- |
| [Character](Character.md) | The character target. |

### getHarvestable {#getharvestable}

``` { .lua .api-signature }
raycastResult:getHarvestable(  )
```

Returns the [Harvestable](Harvestable.md) hit during the raycast. This is only possible if [RaycastResult.type](#type) is equal to "harvestable", otherwise this will return nil.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `raycastResult` | [RaycastResult](RaycastResult.md) | The raycast result. |

**Returns:**

| Type | Description |
| --- | --- |
| [Harvestable](Harvestable.md) | The harvestable target. |

### getJoint {#getjoint}

``` { .lua .api-signature }
raycastResult:getJoint(  )
```

Returns the [Joint](Joint.md) hit during the raycast. This is only possible if [RaycastResult.type](#type) is equal to "joint", otherwise this will return nil.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `raycastResult` | [RaycastResult](RaycastResult.md) | The raycast result. |

**Returns:**

| Type | Description |
| --- | --- |
| [Joint](Joint.md) | The joint target. |

### getLiftData {#getliftdata}

``` { .lua .api-signature }
raycastResult:getLiftData(  )
```

Returns the [Lift](Lift.md) hit during the raycast. This is only possible if [RaycastResult.type](#type) is equal to "lift", otherwise this will return nil.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `raycastResult` | [RaycastResult](RaycastResult.md) | The raycast result. |

**Returns:**

| Type | Description |
| --- | --- |
| [Lift](Lift.md), boolean						The lift; True if the lift is top |  |

### getShape {#getshape}

``` { .lua .api-signature }
raycastResult:getShape(  )
```

Returns the [Shape](Shape.md) hit during the raycast. This is only possible if [RaycastResult.type](#type) is equal to "body", otherwise this will return nil.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `raycastResult` | [RaycastResult](RaycastResult.md) | The raycast result. |

**Returns:**

| Type | Description |
| --- | --- |
| [Shape](Shape.md) | The shape target. |

### getTerrainAssetMaterialName {#getterrainassetmaterialname}

``` { .lua .api-signature }
raycastResult:getTerrainAssetMaterialName(  )
```

Returns the material hit during the raycast. This is only possible if [RaycastResult.type](#type) is equal to "terrainAsset", otherwise this will return empty.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `raycastResult` | [RaycastResult](RaycastResult.md) | The raycast result. |

**Returns:**

| Type | Description |
| --- | --- |
| string | The material name. |

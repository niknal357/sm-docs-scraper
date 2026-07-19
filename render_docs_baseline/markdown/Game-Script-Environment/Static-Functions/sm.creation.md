# sm.creation

A <strong>Creation</strong> represent a collection of [bodies](sm.body.md) linked together by [joints](sm.joint.md).

## Server + Client

<a id="getblueprintcost"></a>
### getBlueprintCost(string, integer?) {#getblueprintcost-string-integer-optional}

``` { .lua .api-signature }
sm.creation.getBlueprintCost( filePath, bodyId? )
```

Returns a table with uuid's and quantity. A body can be sent in to remove from blueprint cost.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `filePath` | string | The file path for the blueprint. |
| `bodyId` *(optional)* | integer | The id of a body.(Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| table | The table of { [Uuid](../Userdata/Uuid.md), quantity } |

### getBlueprintCost(table, integer?) {#getblueprintcost-table-integer-optional}

``` { .lua .api-signature }
sm.creation.getBlueprintCost( table, bodyId? )
```

Returns a table with uuid's and quantity. A body can be sent in to remove from blueprint cost.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `table` | table | The lua table for the blueprint. |
| `bodyId` *(optional)* | integer | The id of a body.(Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| table | The table of { [Uuid](../Userdata/Uuid.md), quantity } |

## Server-only

### buildMultiShape {#buildmultishape}

``` { .lua .api-signature }
sm.creation.buildMultiShape(
    shape,
    worldPosition,
    worldRotation,
    localPosition,
    localRotation
)
```

Builds a multi shape

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `shape` | [Uuid](../Userdata/Uuid.md) | The uuid of shape to build. |
| `worldPosition` | [Vec3](../Userdata/Vec3.md) | World position of shape. |
| `worldRotation` | [Quat](../Userdata/Quat.md) | World rotation of shape. |
| `localPosition` | [Vec3](../Userdata/Vec3.md) | Local position of shape. |
| `localRotation` | [Quat](../Userdata/Quat.md) | Local rotation of shape. |

### exportToString {#exporttostring}

``` { .lua .api-signature }
sm.creation.exportToString( body, exportTransforms?, forceDynamic? )
```

Exports creation to blueprint formatted json string.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](../Userdata/Body.md) | Any body in the creation. |
| `exportTransforms` *(optional)* | boolean | Export the current world transform of bodies. Defaults to false. |
| `forceDynamic` *(optional)* | boolean | Force export to dynamic bodies. Defaults to false. |

**Returns:**

| Type | Description |
| --- | --- |
| string | The blueprint json string. |

### exportToTable {#exporttotable}

``` { .lua .api-signature }
sm.creation.exportToTable( body, exportTransforms?, forceDynamic? )
```

Exports creation to blueprint lua table.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `body` | [Body](../Userdata/Body.md) | Any body in the creation. |
| `exportTransforms` *(optional)* | boolean | Export the current world transform of bodies. Defaults to false. |
| `forceDynamic` *(optional)* | boolean | Force export to dynamic bodies. Defaults to false. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The blueprint lua table. |

### importFromFile {#importfromfile}

``` { .lua .api-signature }
sm.creation.importFromFile(
    world,
    pathString,
    worldPosition?,
    worldRotation?,
    importTransforms?,
    indestructible?
)
```

Imports blueprint json file to world.

> **Warning:**
> If the blueprint was not exported with transforms the importer will treat it as if importTransforms was disabled.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](../Userdata/World.md) | The world to import to. |
| `pathString` | string | The blueprint path. |
| `worldPosition` *(optional)* | [Vec3](../Userdata/Vec3.md) | World position of import. If importTransforms is enabled position is applied to the imported transform. (Defaults to vec3.zero().) |
| `worldRotation` *(optional)* | [Quat](../Userdata/Quat.md) | World rotation of import. If importTransforms is enabled rotation is applied to the imported transform. (Defaults to quat.identity().) |
| `importTransforms` *(optional)* | boolean | Import world transforms from bodies. (Defaults to false.) |
| `indestructible` *(optional)* | boolean | (DEPRECATED) Ignored, use setDestructable(false) on each body in creation. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| table | The table {[Body](../Userdata/Body.md), ...} of bodies created from the blueprint. |

### importFromString {#importfromstring}

``` { .lua .api-signature }
sm.creation.importFromString(
    world,
    jsonString,
    worldPosition?,
    worldRotation?,
    importTransforms?,
    forceInactive?
)
```

Imports blueprint json string to world.

> **Warning:**
> If the blueprint was not exported with transforms the importer will treat it as if importTransforms was disabled.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `world` | [World](../Userdata/World.md) | The world to import to. |
| `jsonString` | string | The blueprint json string. |
| `worldPosition` *(optional)* | [Vec3](../Userdata/Vec3.md) | World position of import. If importTransforms is enabled position is applied to the imported transform. (Defaults to vec3.zero().) |
| `worldRotation` *(optional)* | [Quat](../Userdata/Quat.md) | World rotation of import. If importTransforms is enabled rotation is applied to the imported transform. (Defaults to quat.identity().) |
| `importTransforms` *(optional)* | boolean | Import world transforms from bodies. (Defaults to false.) |
| `forceInactive` *(optional)* | boolean | Import interactables in an inactive state. (Defaults to false.) |

**Returns:**

| Type | Description |
| --- | --- |
| table | The table {[Body](../Userdata/Body.md), ...} of bodies created from the blueprint. |

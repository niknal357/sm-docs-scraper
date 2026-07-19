# sm.cell

The <strong>cell</strong> api exposes and expands on parts of the world loading process.

These methods are commonly called from cell loading callbacks in World type scripts.

## Server + Client

### getNodesByTag {#getnodesbytag}

``` { .lua .api-signature }
sm.cell.getNodesByTag( x, y, tag, world? )
```

Returns a table of nodes which contains the given tag for a cell coordinate.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `x` | integer | X-coordinate. |
| `y` | integer | Y-coordinate. |
| `tag` | string | Tag to match with. |
| `world` *(optional)* | world | The world we are searching in. (Optional, defaults to current world) |

**Returns:**

| Type | Description |
| --- | --- |
| table | Table containing { position = [Vec3](../Userdata/Vec3.md), rotation = [Quat](../Userdata/Quat.md), scale = [Vec3](../Userdata/Vec3.md), tags = {string, ...}, params = table } for each node. |

### getNodesByTags {#getnodesbytags}

``` { .lua .api-signature }
sm.cell.getNodesByTags( x, y, tags, world? )
```

Returns a table of nodes which contain all of the given tags for a cell coordinate.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `x` | integer | X-coordinate. |
| `y` | integer | Y-coordinate. |
| `tags` | table | A table {string, ...} of tags to match with. |
| `world` *(optional)* | world | The world we are searching in (Optional, defaults to current world) |

**Returns:**

| Type | Description |
| --- | --- |
| table | Table containing { position = [Vec3](../Userdata/Vec3.md), rotation = [Quat](../Userdata/Quat.md), scale = [Vec3](../Userdata/Vec3.md), tags = {string, ...}, params = table } for each node. |

### getTags {#gettags}

``` { .lua .api-signature }
sm.cell.getTags( x, y, world? )
```

Returns a table of tags for a cell coordinate.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `x` | integer | X-coordinate |
| `y` | integer | Y-coordinate |
| `world` *(optional)* | world | The world we are searching in. (Optional, defaults to current world) |

**Returns:**

| Type | Description |
| --- | --- |
| table | Table {string, ...} of tags. |

## Server-only

### getHarvestables {#getharvestables}

``` { .lua .api-signature }
sm.cell.getHarvestables( x, y, size )
```

Returns a table of [harvestables](sm.harvestable.md) of a given size for a cell coordinate.

Sizes are:

0: Tiny - plants and crops.

1: Small - small trees and rocks.

2: Medium - medium trees, visible at a long distance.

3: Large - large trees, visible at a very long distance.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `x` | integer | The X-coordinate. |
| `y` | integer | The Y-coordinate. |
| `size` | integer | Size of harvestable (defaults to any size). |

**Returns:**

| Type | Description |
| --- | --- |
| table | A table {[harvestable](sm.harvestable.md), ...} of harvestables. |

### getHarvestablesByUuid {#getharvestablesbyuuid}

``` { .lua .api-signature }
sm.cell.getHarvestablesByUuid( x, y, uuid, size )
```

Returns a table of [harvestables](sm.harvestable.md) of a given size for a cell coordinate and Uuid.

Sizes are:

0: Tiny - plants and crops.

1: Small - small trees and rocks.

2: Medium - medium trees, visible at a long distance.

3: Large - large trees, visible at a very long distance.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `x` | integer | The X-coordinate. |
| `y` | integer | The Y-coordinate. |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the harvestable(s) |
| `size` | integer | Size of harvestable (defaults to any size). |

**Returns:**

| Type | Description |
| --- | --- |
| table | A table {[harvestable](sm.harvestable.md), ...} of harvestables. |

### getInteractablesByAnyUuid {#getinteractablesbyanyuuid}

``` { .lua .api-signature }
sm.cell.getInteractablesByAnyUuid( x, y, uuids )
```

Returns a table of [interactables](sm.interactable.md) which matches any of the given [uuids](sm.uuid.md) for a cell coordinate.

> **Note:**
> Can only be used in a server_onCellLoaded callback.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `x` | integer | The X-coordinate. |
| `y` | integer | The Y-coordinate. |
| `uuids` | table | A table {[Uuid](../Userdata/Uuid.md), ...} of uuids to match interactables against. |

**Returns:**

| Type | Description |
| --- | --- |
| table | A table {[interactable](sm.interactable.md)} of found interactables with matching uuid. |

### getInteractablesByTag {#getinteractablesbytag}

``` { .lua .api-signature }
sm.cell.getInteractablesByTag( x, y, tag )
```

Returns a table of [interactables](sm.interactable.md) which contain the given tag for a cell coordinate.

> **Note:**
> Can only be used in a server_onCellLoaded callback.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `x` | integer | The X-coordinate. |
| `y` | integer | The Y-coordinate. |
| `tag` | string | A tag to match with. |

**Returns:**

| Type | Description |
| --- | --- |
| table | A table {[interactable](sm.interactable.md), ...} of found interactables with matching tag. |

### getInteractablesByTags {#getinteractablesbytags}

``` { .lua .api-signature }
sm.cell.getInteractablesByTags( x, y, tags )
```

Returns a table of [interactables](sm.interactable.md) which contain all of the given tags for a cell coordinate.

~ can be used to exclude a specific tag. Example: { "FRUIT", "~BANANA" } finds interactables tagged with FRUIT but excludes interactables that are also tagged with BANANA.

> **Note:**
> Can only be used in a server_onCellLoaded callback

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `x` | integer | The X-coordinate |
| `y` | integer | The Y-coordinate |
| `tags` | table | A table {string, ...} of tags to match with. |

**Returns:**

| Type | Description |
| --- | --- |
| table | A table {[interactable](sm.interactable.md), ...} of found interactables with matching tags |

### getInteractablesByUuid {#getinteractablesbyuuid}

``` { .lua .api-signature }
sm.cell.getInteractablesByUuid( x, y, uuid )
```

Returns a table of [interactables](sm.interactable.md) of a given [uuid](sm.uuid.md) for a cell coordinate.

> **Note:**
> Can only be used in a server_onCellLoaded callback.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `x` | integer | The X-coordinate. |
| `y` | integer | The Y-coordinate. |
| `uuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the interactable(s) |

**Returns:**

| Type | Description |
| --- | --- |
| table | A table {[interactable](sm.interactable.md), ...} of found interactables with matching uuid. |

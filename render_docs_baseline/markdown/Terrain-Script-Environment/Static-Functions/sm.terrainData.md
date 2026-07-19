# sm.terrainData

The data manager helps storing script data, both locally and between server and client in multiplayer games.

## Functions

### exists {#exists}

``` { .lua .api-signature }
sm.terrainData.exists(  )
```

Check if terrain data exists for this world.

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if data exists. False otherwise. |

### legacy_getData {#legacy_getdata}

``` { .lua .api-signature }
sm.terrainData.legacy_getData(  )
```

> **Deprecated:**
> Use [sm.terrainData.load](#load)
>

Legacy function for reading creative terrain. <strong>Do not use.</strong>

**Returns:**

| Type | Description |
| --- | --- |
| string | The serialized bitser data. |

### legacy_loadTerrainData {#legacy_loadterraindata}

``` { .lua .api-signature }
sm.terrainData.legacy_loadTerrainData( id )
```

> **Deprecated:**
> Use [sm.terrainData.load](#load)
>

Legacy function for reading creative custom terrain. <strong>Do not use.</strong>

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `id` | integer | The id. |

**Returns:**

| Type | Description |
| --- | --- |
| any | The data. Any lua object. |

### legacy_saveTerrainData {#legacy_saveterraindata}

``` { .lua .api-signature }
sm.terrainData.legacy_saveTerrainData( id, data )
```

> **Deprecated:**
> Use [sm.terrainData.save](#save)
>

Legacy function for storing creative custom terrain. <strong>Do not use.</strong>

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `id` | integer | The id. |
| `data` | any | The data. Any lua object. |

### legacy_setData {#legacy_setdata}

``` { .lua .api-signature }
sm.terrainData.legacy_setData( data )
```

> **Deprecated:**
> Use [sm.terrainData.save](#save)
>

Legacy function for storing creative terrain. <strong>Do not use.</strong>

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `data` | string | The serialized bitser data. |

### load {#load}

``` { .lua .api-signature }
sm.terrainData.load(  )
```

Load terrain data for this world if available.

**Returns:**

| Type | Description |
| --- | --- |
| any | The data. Any lua object. |

### save {#save}

``` { .lua .api-signature }
sm.terrainData.save( data )
```

Save and share terrain data over network from server to client.

The data is accessible from the same world.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `data` | any | The data. Any lua object. |

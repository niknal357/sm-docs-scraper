# sm.storage

**Associated type:** [Storage](../Userdata/Storage.md)

<strong>Storage</strong> is used for saving and loading any Lua data into the world's database. This allows for data to be retrieved after closing and reloading the world.

Storage can only be used on the server.

> **Warning:**
> Storage allows for data to be saved immediately into the world's database. This is a <strong>very slow</strong> process and should be done as sparsely as possible.
> If you have data that is shared globally and updated often, consider using global variables instead. Ideally, storage should only be used to save data upon closing the world, or when saving a creation on the Lift.

## Functions

### load {#load}

``` { .lua .api-signature }
sm.storage.load( key )
```

Loads Lua data stored with a given key. The <em>key</em> can be any lua object.

If no data is stored with the given key, this returns nil.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `key` | any | The key. |

**Returns:**

| Type | Description |
| --- | --- |
| any | The data stored. |

### loadTerrainData {#loadterraindata}

``` { .lua .api-signature }
sm.storage.loadTerrainData( worldId )
```

Load terrain data for this world if available.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `worldId` | integer | The id of the world to load terrain data for. |

**Returns:**

| Type | Description |
| --- | --- |
| any | The data. Any lua object. |

### save {#save}

``` { .lua .api-signature }
sm.storage.save( key, data )
```

Saves any Lua object with a given key. The <em>key</em> can be any lua object.

The data will remain stored after closing the world, and is retrieved using [load](#load), provided the same key.

> **Note:**
> The data is stored globally <strong>within the current mod</strong>. As of such, keys will not collide with external mods and scripts.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `key` | any | The key that will be used to get the data. |
| `data` | any | The data to be stored. |

### saveAndSync {#saveandsync}

``` { .lua .api-signature }
sm.storage.saveAndSync( key, data )
```

Saves any Lua object with a given key. The <em>key</em> can be any lua object.

The data will remain stored after closing the world and synchronized to other clients, and is retrieved using [load](#load), provided the same key.

> **Note:**
> The data is stored globally <strong>within the current mod</strong>. As of such, keys will not collide with external mods and scripts.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `key` | any | The key that will be used to get the data. |
| `data` | any | The data to be stored. |

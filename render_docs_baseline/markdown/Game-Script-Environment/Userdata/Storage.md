# Storage

**Associated namespace:** [sm.storage](../Static-Functions/sm.storage.md)

**Usage:** Server Only

**Serializable:** No

A userdata object representing a <strong>storage</strong> object.

> **Note:**
> A storage object is accessable via `self.storage` in scripted shapes (see [ShapeClass](../Classes/ShapeClass.md)).
> The storage object also allows for data to be saved in creations saved on the Lift.

## Server-only

### load {#load}

``` { .lua .api-signature }
storage:load(  )
```

Loads Lua data stored in the storage object.

If no data is stored in the object, this returns nil.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `storage` | [Storage](Storage.md) | The storage. |

**Returns:**

| Type | Description |
| --- | --- |
| any | The data stored. |

### save {#save}

``` { .lua .api-signature }
storage:save( data )
```

Saves any Lua data into the storage object.

The data will remain stored after closing the world, and is retrieved using [load](#load).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `storage` | [Storage](Storage.md) | The storage. |
| `data` | any | The data to be stored. |

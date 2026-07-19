# Container

**Associated namespace:** [sm.container](../Static-Functions/sm.container.md)

**Usage:** Server And Client

**Serializable:** Yes

Represents a container

**Values:**

- <a id="allowcollect"></a>`allowCollect` [ **boolean** ] <br>
    - `Get`: (Server-Only) Returns whether the container can collect items.
    - `Set`: (Server-Only) Sets whether the container can collect items.

- <a id="allowspend"></a>`allowSpend` [ **boolean** ] <br>
    - `Get`: (Server-Only) Returns whether the container can spend items.
    - `Set`: (Server-Only) Sets whether the container can spend items.

- <a id="id"></a>`id` [ **integer** ] <br>
    - `Get`: Returns the id of a container.

- <a id="size"></a>`size` [ **integer** ] <br>
    - `Get`: Returns the number of slots in a container.

**Operations:**

| Operation | Returns | Description |
| --- | --- | --- |
| <a id="__eq"></a>`Container == Container` | boolean | Checks if two instances of [Container](Container.md) refer to the same Container. |

## Server + Client

### canCollect {#cancollect}

``` { .lua .api-signature }
container:canCollect( itemUuid, quantity )
```

Checks if `sm.container.collect` is allowed using the same parameters.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](Container.md) | The container. |
| `itemUuid` | [Uuid](Uuid.md) | The uuid of the item. |
| `quantity` | integer | The number of items. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Indicates if the action is possible. |

### canCollectAll {#cancollectall}

``` { .lua .api-signature }
container:canCollectAll( uuids, quantities )
```

Checks if the container can collect a set of items.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](Container.md) | The container. |
| `uuids` | table | The uuids of items to check. |
| `quantities` | table | The number of items of each uuid. Needs to match the number of uuids. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Indicates if the action is possible. |

### canSpend {#canspend}

``` { .lua .api-signature }
container:canSpend( itemUuid, quantity )
```

Checks if [sm.container.spend](../Static-Functions/sm.container.md#spend) is allowed.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](Container.md) | The container. |
| `itemUuid` | [Uuid](Uuid.md) | The uuid of the item. |
| `quantity` | integer | The number of items. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Indicates if the action is possible. |

### getItem {#getitem}

``` { .lua .api-signature }
container:getItem( slot )
```

Returns a table containing item uuid, quantity (and instance id for tools) at given slot.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](Container.md) | The container. |
| `slot` | integer | The slot. |

**Returns:**

| Type | Description |
| --- | --- |
| table | Table containg item {uuid = [Uuid](Uuid.md), instance = integer, quantity = integer}. |

### getMaxStackSize {#getmaxstacksize}

``` { .lua .api-signature }
container:getMaxStackSize(  )
```

Returns the max stack size in the container.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](Container.md) | The container. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The max stack size. |

### getRevision {#getrevision}

``` { .lua .api-signature }
container:getRevision(  )
```

Returns the network revision number of the container.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](Container.md) | The container. |

**Returns:**

| Type | Description |
| --- | --- |
| number | The revision |

### getSize {#getsize}

``` { .lua .api-signature }
container:getSize(  )
```

Returns the number of slots in a container.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](Container.md) | The container. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The size. |

### isEmpty {#isempty}

``` { .lua .api-signature }
container:isEmpty(  )
```

Returns true if the container is empty.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](Container.md) | The container. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the container is empty. |

### isFull {#isfull}

``` { .lua .api-signature }
container:isFull(  )
```

Returns true if all container slots in the container is at max capacity.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](Container.md) | The container. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the container is empty. |

## Server-only

### bindOnTransaction {#bindontransaction}

``` { .lua .api-signature }
container:bindOnTransaction( callback, object? )
```

Binds a container's onTransaction event to a custom callback. The event is triggered when a transaction is completed.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](Container.md) | The container instance. |
| `callback` | string | The name of the Lua function to bind. |
| `object` *(optional)* | table | The object that will receive the callback. (optional) |

### clear {#clear}

``` { .lua .api-signature }
container:clear(  )
```

Clears out the contents of the container.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](Container.md) | The container. |

### collect {#collect}

``` { .lua .api-signature }
container:collect( itemUuid, quantity, mustCollectAll? )
```

Adds a quantity of a given item to a container.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](Container.md) | The container. |
| `itemUuid` | [Uuid](Uuid.md) | The uuid of the item. |
| `quantity` | integer | The number of items. |
| `mustCollectAll` *(optional)* | boolean | Must collect all items for the transaction to be valid. Defaults to true. (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The number of items successfully added. |

### getAllowCollect {#getallowcollect}

``` { .lua .api-signature }
container:getAllowCollect(  )
```

Returns whether the container can collect items.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](Container.md) | The container. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the container can collect. |

### getAllowSpend {#getallowspend}

``` { .lua .api-signature }
container:getAllowSpend(  )
```

Returns whether the container can spend items.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](Container.md) | The container. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the container can spend. |

### hasChanged {#haschanged}

``` { .lua .api-signature }
container:hasChanged( tick )
```

Returns true if the given tick is lower than the tick the container was last changed.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](Container.md) | The container. |
| `tick` | integer | The tick. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Returns true if the container has been changed. |

### resize {#resize}

``` { .lua .api-signature }
container:resize( size, stackSize? )
```

Resize a container.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](Container.md) | The container instance. |
| `size` | integer | The new size of the container. |
| `stackSize` *(optional)* | integer | The stack size. Defaults to maximum possible stack size(65535). |

### setAllowCollect {#setallowcollect}

``` { .lua .api-signature }
container:setAllowCollect( allow )
```

Sets whether the container can collect items.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](Container.md) | The container. |
| `allow` | boolean | True if the container can collect. |

### setAllowSpend {#setallowspend}

``` { .lua .api-signature }
container:setAllowSpend( allow )
```

Sets whether the container can spend items.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](Container.md) | The container. |
| `allow` | boolean | True if the container can spend. |

### setFilters {#setfilters}

``` { .lua .api-signature }
container:setFilters( filter )
```

Set item filter.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](Container.md) | The container. |
| `filter` | table | A table of the item uuid's {[Uuid](Uuid.md), ...} allowed to be stored in the container. |

### setItem {#setitem}

``` { .lua .api-signature }
container:setItem( slot, itemUuid, quantity, instance? )
```

Sets the number of items stacked in a given container slot.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](Container.md) | The container. |
| `slot` | integer | The slot. |
| `itemUuid` | [Uuid](Uuid.md) | The uuid of the item. |
| `quantity` | integer | The number of items. |
| `instance` *(optional)* | integer | The instance id, if the item is a tool. (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Indicates if the action is possible. |

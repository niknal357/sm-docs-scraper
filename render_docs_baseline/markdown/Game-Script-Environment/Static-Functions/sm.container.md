# sm.container

**Associated type:** [Container](../Userdata/Container.md)

## Server + Client

### getFirstItem {#getfirstitem}

``` { .lua .api-signature }
sm.container.getFirstItem( container )
```

Returns a table containing item uuid, quantity (and instance id for tools) at first available slot

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](../Userdata/Container.md) | The container. |

**Returns:**

| Type | Description |
| --- | --- |
| table | Table containg item {uuid  = [Uuid](../Userdata/Uuid.md), instance = integer, quantity = integer}. |

### itemUuid {#itemuuid}

``` { .lua .api-signature }
sm.container.itemUuid( container )
```

Returns a table containing all item uuids in a container.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](../Userdata/Container.md) | The container. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The table of item uuids {[Uuid](../Userdata/Uuid.md), ..}. |

### quantity {#quantity}

``` { .lua .api-signature }
sm.container.quantity( container )
```

Returns a table containing all item quantities in a container.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](../Userdata/Container.md) | The container. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The table of item quantities {integer, ..}. |

### totalQuantity {#totalquantity}

``` { .lua .api-signature }
sm.container.totalQuantity( container, itemUuid )
```

Returns the total number of a given item uuid in a container.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](../Userdata/Container.md) | The container. |
| `itemUuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the item. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The quantity of the given item uuid. |

### uniqueItemUuids {#uniqueitemuuids}

``` { .lua .api-signature }
sm.container.uniqueItemUuids( container )
```

Returns a table containing all item uuids in a container.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](../Userdata/Container.md) | The container. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The table of item uuids {[Uuid](../Userdata/Uuid.md), ..}. |

## Server-only

### abortTransaction {#aborttransaction}

``` { .lua .api-signature }
sm.container.abortTransaction(  )
```

Aborts a transaction.

### beginTransaction {#begintransaction}

``` { .lua .api-signature }
sm.container.beginTransaction(  )
```

Starts a new <em>transaction</em> shared across all containers. A transaction is a collection of all changes of container items will be collected and processed

A transaction must be ended with [sm.container.endTransaction](#endtransaction).

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether starting a transaction was successful. |

### collectToSlot {#collecttoslot}

``` { .lua .api-signature }
sm.container.collectToSlot(
    container,
    slot,
    itemUuid,
    quantity,
    mustCollectAll
)
```

Performs a collect operation to a specific slot.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](../Userdata/Container.md) | The container. |
| `slot` | integer | The container slot. |
| `itemUuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the item to be added. |
| `quantity` | integer | The number of items to be added. |
| `mustCollectAll` | boolean | If true, only add items if there is enough room. If false, add as many items as possible. Defaults to true. (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The number of items successfully added. |

### endTransaction {#endtransaction}

``` { .lua .api-signature }
sm.container.endTransaction(  )
```

Ends a transaction.

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Whether ending a transaction was successful. |

### moveAll {#moveall}

``` { .lua .api-signature }
sm.container.moveAll( container, container, moveAll? )
```

Moves the content from one container to another.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](../Userdata/Container.md) | The source container. |
| `container` | [Container](../Userdata/Container.md) | The destination container. |
| `moveAll` *(optional)* | boolean | If true, requires that all items can be moved. Defaults to true. (Optional) |

### moveAllToCarryContainer {#movealltocarrycontainer}

``` { .lua .api-signature }
sm.container.moveAllToCarryContainer( container, player, color )
```

Moves the content of input container to the player carry container and assigns the carry color.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](../Userdata/Container.md) | The container to assign. |
| `player` | [Player](../Userdata/Player.md) | The player to receive the carry content and color. |
| `color` | [Color](../Userdata/Color.md) | The color to assign. |

### spend {#spend}

``` { .lua .api-signature }
sm.container.spend( container, itemUuid, quantity, mustSpendAll?, avoidSlot? )
```

Removes a quantity of a given item from a container.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](../Userdata/Container.md) | The container. |
| `itemUuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the item. |
| `quantity` | integer | The number of items. |
| `mustSpendAll` *(optional)* | boolean | If true, only remove items if there are enough. If false, remove as many items as possible. Defaults to true. (Optional) |
| `avoidSlot` *(optional)* | integer | If the spending should try and avoid a specific inventory slot if the resource is available in inventory. (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The number of items successfully removed. |

### spendFromSlot {#spendfromslot}

``` { .lua .api-signature }
sm.container.spendFromSlot( container, slot, itemUuid, quantity, mustSpendAll? )
```

Performs a [sm.container.spend](#spend) operation from a specific slot. 

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](../Userdata/Container.md) | The container. |
| `slot` | integer | The container slot. |
| `itemUuid` | [Uuid](../Userdata/Uuid.md) | The uuid of the item to be removed. |
| `quantity` | integer | The number of items to be removed. |
| `mustSpendAll` *(optional)* | boolean | If true, only remove items if there are enough. If false, remove as many items as possible. Defaults to true. (Optional) |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The number of items successfully removed. |

### swap {#swap}

``` { .lua .api-signature }
sm.container.swap( container, container, slotFrom, slotTo )
```

Swaps two item slots.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `container` | [Container](../Userdata/Container.md) | The first container. |
| `container` | [Container](../Userdata/Container.md) | The second container. |
| `slotFrom` | integer | The first slot |
| `slotTo` | integer | The second slot |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Indicates if the action is possible. |

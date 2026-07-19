# ClientScriptableObject

**Associated namespace:** [sm.clientScriptableObject](../Static-Functions/sm.clientScriptableObject.md)

**Usage:** Client Only

**Serializable:** Yes

A userdata object representing a <strong>scriptable object</strong>.

**Values:**

- <a id="clientpublicdata"></a>`clientPublicData` [ **table** ] <br>
    - `Get`: (Client-Only) Returns public data from a client scriptable object.
    - `Set`: (Client-Only) Sets public data on a client scriptable object.

- <a id="id"></a>`id` [ **number** ] <br>
    - `Get`: (Client-Only) Returns the id of a client scriptable object.

- <a id="world"></a>`world` [ **[World](World.md)** ] <br>
    - `Get`: (Client-Only) Returns the worldId of a client scriptable object.

**Operations:**

| Operation | Returns | Description |
| --- | --- | --- |
| <a id="__eq"></a>`ClientScriptableObject == ClientScriptableObject` | boolean | Checks if two instances of [ClientScriptableObject](ClientScriptableObject.md) refer to the same ClientScriptableObject. |

## Client-only

### destroy {#destroy}

``` { .lua .api-signature }
clientScriptableObject:destroy(  )
```

Destroys a client scriptable Object.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `clientScriptableObject` | [ClientScriptableObject](ClientScriptableObject.md) | The scriptable object. |

### getClientPublicData {#getclientpublicdata}

``` { .lua .api-signature }
clientScriptableObject:getClientPublicData( scriptableObject )
```

Returns public data from a client scriptable object.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `scriptableObject` | [ScriptableObject](ScriptableObject.md) | The scriptableObject. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The client public data. |

### getData {#getdata}

``` { .lua .api-signature }
clientScriptableObject:getData( scriptableObject )
```

Returns json data from a client scriptableObject.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `scriptableObject` | [ScriptableObject](ScriptableObject.md) | The scriptableObject. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The json data. |

### getId {#getid}

``` { .lua .api-signature }
clientScriptableObject:getId(  )
```

Returns the id of a client scriptable object.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `clientScriptableObject` | [ClientScriptableObject](ClientScriptableObject.md) | The scriptable object. |

**Returns:**

| Type | Description |
| --- | --- |
| number | id						The clientScriptableObject id. |

### getWorld {#getworld}

``` { .lua .api-signature }
clientScriptableObject:getWorld( scriptableObject )
```

Returns the worldId of a client scriptable object.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `scriptableObject` | [ScriptableObject](ScriptableObject.md) | The scriptable object. |

**Returns:**

| Type | Description |
| --- | --- |
| [World](World.md) | world				The world. |

### setClientPublicData {#setclientpublicdata}

``` { .lua .api-signature }
clientScriptableObject:setClientPublicData( scriptableObject, data )
```

Sets public data on a client scriptable object.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `scriptableObject` | [ScriptableObject](ScriptableObject.md) | The scriptableObject. |
| `data` | table | The client public data. |

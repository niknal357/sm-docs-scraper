# ScriptableObject

**Associated namespace:** [sm.scriptableObject](../Static-Functions/sm.scriptableObject.md)

**Usage:** Server And Client

**Serializable:** Yes

A userdata object representing a <strong>scriptable object</strong>.

**Values:**

- <a id="clientpublicdata"></a>`clientPublicData` [ **table** ] <br>
    - `Get`: (Client-Only) Returns client public data from a scriptableObject.
    - `Set`: (Client-Only) Sets client public data on a scriptableObject.

- <a id="id"></a>`id` [ **number** ] <br>
    - `Get`: Returns the id of a scriptable object.

- <a id="publicdata"></a>`publicData` [ **table** ] <br>
    - `Get`: (Server-Only) Returns (server) public data from a scriptableObject.
    - `Set`: (Server-Only) Sets (server) public data on a scriptableObject.

- <a id="world"></a>`world` [ **[World](World.md)** ] <br>
    - `Get`: Returns the world of a scriptable object.

**Operations:**

| Operation | Returns | Description |
| --- | --- | --- |
| <a id="__eq"></a>`ScriptableObject == ScriptableObject` | boolean | Checks if two instances of [ScriptableObject](ScriptableObject.md) refer to the same ScriptableObject. |

## Server + Client

### getData {#getdata}

``` { .lua .api-signature }
scriptableObject:getData(  )
```

Returns json data from a scriptableObject.

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
scriptableObject:getId(  )
```

Returns the id of a scriptable object.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `scriptableObject` | [ScriptableObject](ScriptableObject.md) | The scriptable object. |

**Returns:**

| Type | Description |
| --- | --- |
| number | id					The scriptableObject id. |

### getWorld {#getworld}

``` { .lua .api-signature }
scriptableObject:getWorld(  )
```

Returns the world of a scriptable object.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `scriptableObject` | [ScriptableObject](ScriptableObject.md) | The scriptable object. |

**Returns:**

| Type | Description |
| --- | --- |
| [World](World.md) | world				The world. |

## Server-only

### destroy {#destroy}

``` { .lua .api-signature }
scriptableObject:destroy(  )
```

Destroys a scriptable Object.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `scriptableObject` | [ScriptableObject](ScriptableObject.md) | The scriptable object. |

### getPublicData {#getpublicdata}

``` { .lua .api-signature }
scriptableObject:getPublicData(  )
```

Returns (server) public data from a scriptableObject.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `scriptableObject` | [ScriptableObject](ScriptableObject.md) | The scriptableObject. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The public data. |

### setPublicData {#setpublicdata}

``` { .lua .api-signature }
scriptableObject:setPublicData( data )
```

Sets (server) public data on a scriptableObject.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `scriptableObject` | [ScriptableObject](ScriptableObject.md) | The scriptableObject. |
| `data` | table | The public data. |

## Client-only

### getClientPublicData {#getclientpublicdata}

``` { .lua .api-signature }
scriptableObject:getClientPublicData(  )
```

Returns client public data from a scriptableObject.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `scriptableObject` | [ScriptableObject](ScriptableObject.md) | The scriptableObject. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The client public data. |

### setClientPublicData {#setclientpublicdata}

``` { .lua .api-signature }
scriptableObject:setClientPublicData( data )
```

Sets client public data on a scriptableObject.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `scriptableObject` | [ScriptableObject](ScriptableObject.md) | The scriptableObject. |
| `data` | table | The client public data. |

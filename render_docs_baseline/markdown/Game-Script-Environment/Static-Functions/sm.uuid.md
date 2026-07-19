# sm.uuid

**Associated type:** [Uuid](../Userdata/Uuid.md)

A universally unique identifier (<strong>UUID</strong>) is a 128-bit number that can guarantee uniqueness across space and time.

To generate one, use [sm.uuid.new](#new).

## Functions

### generateNamed {#generatenamed}

``` { .lua .api-signature }
sm.uuid.generateNamed( namespace, name )
```

Generates a named (version 5) uuid.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `namespace` | [Uuid](../Userdata/Uuid.md) | A uuid namespace for the name. The namespace makes sure any equal name from different namespaces do not collide. |
| `name` | string | A name, to generate a uuid from. Provided the same namespace and name, the uuid will be the same. |

**Returns:**

| Type | Description |
| --- | --- |
| [Uuid](../Userdata/Uuid.md) | The created uuid. |

### generateRandom {#generaterandom}

``` { .lua .api-signature }
sm.uuid.generateRandom(  )
```

Generates a random (version 4) uuid.

**Returns:**

| Type | Description |
| --- | --- |
| [Uuid](../Userdata/Uuid.md) | The generated uuid. |

### getNil {#getnil}

``` { .lua .api-signature }
sm.uuid.getNil(  )
```

Creates a nil uuid {00000000-0000-0000-0000-000000000000}

**Returns:**

| Type | Description |
| --- | --- |
| [Uuid](../Userdata/Uuid.md) | The nil uuid. |

<a id="new"></a>
### new(Uuid?) {#new-uuid-optional}

``` { .lua .api-signature }
sm.uuid.new( uuid? )
```

Creates a uuid from a string or generates a random uuid (version 4).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` *(optional)* | [Uuid](../Userdata/Uuid.md) | The uuid to create a uuid instance from. If none is provided, generate a random uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| [Uuid](../Userdata/Uuid.md) | The created uuid. |

### new(string?) {#new-string-optional}

``` { .lua .api-signature }
sm.uuid.new( uuid? )
```

Creates a uuid from a string or generates a random uuid (version 4).

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `uuid` *(optional)* | string | The uuid string to create a uuid instance from. If none is provided, generate a random uuid. |

**Returns:**

| Type | Description |
| --- | --- |
| [Uuid](../Userdata/Uuid.md) | The created uuid. |

# Global

Globals

## Functions

### class {#class}

``` { .lua .api-signature }
class( base? )
```

Creates a new class object.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `base` *(optional)* | table | An optional base class to inherit from. (Defaults to inheriting from no class) |

**Returns:**

| Type | Description |
| --- | --- |
| table | Class table. |

### dofile {#dofile}

``` { .lua .api-signature }
dofile( filename )
```

Opens the named file and executes its contents as a Lua chunk. In case of errors, dofile propagates the error to its caller.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `filename` | string | The name of the file to be loaded. |

### enumType {#enumtype}

``` { .lua .api-signature }
enumType( object )
```

Returns the type of an object as an enum integer. This includes standard Lua types and userdata types specific to this API.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `object` | any | The object instance. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The object type. |

### print {#print}

``` { .lua .api-signature }
print( ... )
```

Prints data to the console. This is useful for debugging.

> **Note:**
> If the game is running with the `-dev` flag, any output will be added to the game logs.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `...` | any | The arguments to be printed. |

### type {#type}

``` { .lua .api-signature }
type( object )
```

Returns the type of an object as a string. This includes standard Lua types and userdata types specific to this API.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `object` | any | The object instance. |

**Returns:**

| Type | Description |
| --- | --- |
| string | The object type. |

# Uuid

**Associated namespace:** [sm.uuid](../Static-Functions/sm.uuid.md)

**Usage:** Server And Client

**Serializable:** Yes

A userdata object representing a <strong>uuid</strong>.

**Operations:**

| Operation | Returns | Description |
| --- | --- | --- |
| <a id="__eq"></a>`Uuid == Uuid` | boolean | Checks if two uuids are equal. |
| <a id="__tostring"></a>`tostring(Uuid)` | string | Returns the uuid as a string. |

## Functions

### isNil {#isnil}

``` { .lua .api-signature }
uuid:isNil(  )
```

Checks if the uuid is nil {00000000-0000-0000-0000-000000000000}

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if the uuid is nil. |

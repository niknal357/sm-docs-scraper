# BuilderGuide

**Associated namespace:** [sm.builderGuide](../Static-Functions/sm.builderGuide.md)

**Usage:** Server And Client

**Serializable:** No

A userdata object representing a <strong>builder guide</strong>.

**Values:**

- <a id="id"></a>`id` [ **integer** ] <br>
    - `Get`: Returns the id of a guide.

**Operations:**

| Operation | Returns | Description |
| --- | --- | --- |
| <a id="__eq"></a>`BuilderGuide == BuilderGuide` | boolean | Checks if two instances of [BuilderGuide](BuilderGuide.md) refer to the same BuilderGuide. |

## Functions

### destroy {#destroy}

``` { .lua .api-signature }
builderGuide:destroy(  )
```

Destroys a guide.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `guide` | [BuilderGuide](BuilderGuide.md) | The guide to be destroyed. |

### getCurrentStageIndex {#getcurrentstageindex}

``` { .lua .api-signature }
builderGuide:getCurrentStageIndex(  )
```

Returns the stage index of a guide.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `guide` | [BuilderGuide](BuilderGuide.md) | The guide. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The stage index. |

### getErrorInfo {#geterrorinfo}

``` { .lua .api-signature }
builderGuide:getErrorInfo(  )
```

Returns error information of the builder guide.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `guide` | [BuilderGuide](BuilderGuide.md) | The guide. |

**Returns:**

| Type | Description |
| --- | --- |
| table | Table of errors { blocks = number, joints = number, parts = number, connections = number, connectionsReversed = number }, |

### getId {#getid}

``` { .lua .api-signature }
builderGuide:getId(  )
```

Returns the id of a guide.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `guide` | [BuilderGuide](BuilderGuide.md) | The guide. |

**Returns:**

| Type | Description |
| --- | --- |
| integer | The guide's id. |

### getStageInfo {#getstageinfo}

``` { .lua .api-signature }
builderGuide:getStageInfo(  )
```

Returns information about the current stage.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `guide` | [BuilderGuide](BuilderGuide.md) | The guide. |

**Returns:**

| Type | Description |
| --- | --- |
| table | Table of stage info { blocksLeft = number, jointsLeft = number, partsLeft = number, connectionsLeft = number },  |

### isComplete {#iscomplete}

``` { .lua .api-signature }
builderGuide:isComplete(  )
```

Returns the completion status of a guide.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `guide` | [BuilderGuide](BuilderGuide.md) | The guide. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | True if the guide is completed. |

### update {#update}

``` { .lua .api-signature }
builderGuide:update(  )
```

Update the state of a guide. Should be called whenever the root [Shape](Shape.md) of the builder guide has changed.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `guide` | [BuilderGuide](BuilderGuide.md) | The guide |

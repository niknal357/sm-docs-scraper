# sm.json

Parses and writes json files from and to lua values.

## Functions

### fileExists {#fileexists}

``` { .lua .api-signature }
sm.json.fileExists( path )
```

Checks if a json file exists at the input path

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `path` | string | The json file path. |

**Returns:**

| Type | Description |
| --- | --- |
| boolean | Return true if the file exists. |

### open {#open}

``` { .lua .api-signature }
sm.json.open( path )
```

Opens a json file and parses to Lua table.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `path` | string | The json file path. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The table. |

### parseJsonString {#parsejsonstring}

``` { .lua .api-signature }
sm.json.parseJsonString( json )
```

Parses a json string to lua table.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `json` | string | The json string. |

**Returns:**

| Type | Description |
| --- | --- |
| table | The table. |

### save {#save}

``` { .lua .api-signature }
sm.json.save( root, path )
```

Write a lua table to json.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `root` | table | The lua table. |
| `path` | string | The json file path. |

### writeJsonString {#writejsonstring}

``` { .lua .api-signature }
sm.json.writeJsonString( root, stylized? )
```

Writes a json string from a lua table.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `root` | table | The lua table. |
| `stylized` *(optional)* | boolean | Generates stylized json if true, compact if false. (Defaults to false) |

**Returns:**

| Type | Description |
| --- | --- |
| string | The json string. |

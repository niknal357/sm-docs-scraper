# sm.terrainGeneration

Allows reading and writing in game storage from terrain generation scripts.

## Functions

### getTempData {#gettempdata}

``` { .lua .api-signature }
sm.terrainGeneration.getTempData( key )
```

Loads temporary data stored by terrain generation.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `key` | any | Key used to lookup the saved data. |

**Returns:**

| Type | Description |
| --- | --- |
| any | The saved data. |

### loadGameStorage {#loadgamestorage}

``` { .lua .api-signature }
sm.terrainGeneration.loadGameStorage( key )
```

Loads data stored by terrain generation.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `key` | any | Key used to lookup the saved data. |

**Returns:**

| Type | Description |
| --- | --- |
| any | The saved data. |

### saveAndSyncGameStorage {#saveandsyncgamestorage}

``` { .lua .api-signature }
sm.terrainGeneration.saveAndSyncGameStorage( key, data )
```

Saves data produced from terrain generation and synchronizes to clients. Saved data can be retrived in later game sessions and by the game lua environment.  

 

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `key` | any | Key used to lookup the saved data. |
| `data` | any | Data to save.  |

### saveGameStorage {#savegamestorage}

``` { .lua .api-signature }
sm.terrainGeneration.saveGameStorage( key, data )
```

Saves data produced from terrain generation. Saved data can be retrived in later game sessions and by the game lua environment.  

 

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `key` | any | Key used to lookup the saved data. |
| `data` | any | Data to save.  |

### setAndSyncGameStorageNoSave {#setandsyncgamestoragenosave}

``` { .lua .api-signature }
sm.terrainGeneration.setAndSyncGameStorageNoSave( key, data )
```

Sets data produced from terrain generation and synchronizes to clients. This data is only valid during the game session.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `key` | any | Key used to lookup the saved data. |
| `data` | any | Data to save. |

### setGameStorageNoSave {#setgamestoragenosave}

``` { .lua .api-signature }
sm.terrainGeneration.setGameStorageNoSave( key, data )
```

Sets data produced from terrain generation. This data is only valid during the game session. Does not synchronize to clients

 

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `key` | any | Key used to lookup the saved data. |
| `data` | any | Data to save.  |

### setTempData {#settempdata}

``` { .lua .api-signature }
sm.terrainGeneration.setTempData( key, data )
```

Sets temporary data produced from terrain generation.

 

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `key` | any | Key used to lookup the saved data. |
| `data` | any | Data to save.  |

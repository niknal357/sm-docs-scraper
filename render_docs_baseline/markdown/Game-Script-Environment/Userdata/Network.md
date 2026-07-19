# Network

**Usage:** Server And Client

**Serializable:** No

A userdata object representing a <strong>network</strong> object.

<strong>Network</strong> is used for sending data between scripts running on server and client. This allows the server to call a function on the client with optional arguments, and vice versa.

> **Note:**
> A network object is accessable via `self.network` in scripted shapes (see [ShapeClass](../Classes/ShapeClass.md)).

> **Warning:**
> Network allows any Lua data to be sent between the host and other players in real-time. This may result in <strong>high latency</strong> and lag in multiplayer.
> To avoid lag and minimize bandwidth usage, consider only sending data when necessary, when data has changed, and attempt to send as little amount of data as possible.

## Server-only

### sendToClient {#sendtoclient}

``` { .lua .api-signature }
network:sendToClient( player, callbackMethod, args? )
```

Sends a network event from the server to a client. This will run the callback method on the client with optional arguments.

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `network` | [Network](Network.md) | The network. |
| `player` | [Player](Player.md) | The client player (or the host). |
| `callbackMethod` | string | The client function name. |
| `args` *(optional)* | any | Optional arguments to be sent to the client. |

### sendToClients {#sendtoclients}

``` { .lua .api-signature }
network:sendToClients( callbackMethod, args? )
```

Sends a network event from the server to all clients. This will run the callback method on every client with optional arguments.

```lua
-- Example of calling client function over network
function MyHorn.server_onSledgehammer( self, position, player ) 
	self.network:sendToClients( 'client_hit', position )
end
 
function MyHorn.client_hit( self, position ) 
	-- Play sound
	sm.audio.play( 'Horn', position )
end
```

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `network` | [Network](Network.md) | The network. |
| `callbackMethod` | string | The client function name. |
| `args` *(optional)* | any | Optional arguments to be sent to the client. |

### setClientData {#setclientdata}

``` { .lua .api-signature }
network:setClientData( data, channel? )
```

Sets a lua object that will automatically be synchronized to clients.

Scripts which use this feature needs to implement 'client_onClientDataUpdate'.

'client_onClientDataUpdate' will be called on the client whenever the data has changed,

including setting the data for the first time.

Channel 1 will be received before channel 2 if both are updated.

```lua
-- Example:
function MyEngine.server_onCreate( self )
	self.network:setClientData( { "gear" = 1 } )
end
function MyEngine.client_onClientDataUpdate( self, data, channel )
	if channel == 1 then
		self.interactable:setPoseWeight( 0, data.gear / self.maxGears )
	end
end
```

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `network` | [Network](Network.md) | The network. |
| `data` | any | Persistent data to be synchronized with existing and new clients. |
| `channel` *(optional)* | integer | Client data channel, 1 to 4 (Optional) (Defaults to 1) |

## Client-only

### sendToServer {#sendtoserver}

``` { .lua .api-signature }
network:sendToServer( callbackMethod, args? )
```

Sends a network event from the client to the server. This will run the callback method on the server with optional arguments.

```lua
-- Example of calling server function over network, called function receives the optional argument and the sending player
function MySwitch.client_onInteract( self ) 
	self.network:sendToServer( 'server_setSwitch', { active = true } )
end

function MySwitch.server_setSwitch( self, args, player ) 
	-- Set state of switch
	self.interactable.active = args.active
end
```

**Parameters:**

| Name | Type | Description |
| --- | --- | --- |
| `network` | [Network](Network.md) | The network. |
| `callbackMethod` | string | The server function name. |
| `args` *(optional)* | any | Optional arguments to be sent to the server. |

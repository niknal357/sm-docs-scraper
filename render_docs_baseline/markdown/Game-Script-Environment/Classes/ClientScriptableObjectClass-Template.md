# ClientScriptableObjectClass script template

[Back to ClientScriptableObjectClass](ClientScriptableObjectClass.md)

Copy this starter script and remove anything you do not need.

```lua
ClientScriptableObject = class()

-- Server callbacks
-- Docs: ClientScriptableObjectClass.html#server_oncreate
function ClientScriptableObject.server_onCreate( self )
end

-- Docs: ClientScriptableObjectClass.html#server_ondestroy
function ClientScriptableObject.server_onDestroy( self )
end

-- Docs: ClientScriptableObjectClass.html#server_onrefresh
function ClientScriptableObject.server_onRefresh( self )
end

-- Docs: ClientScriptableObjectClass.html#server_onfixedupdate
function ClientScriptableObject.server_onFixedUpdate( self, timeStep )
end

-- Docs: ClientScriptableObjectClass.html#server_onreceiveupdate
function ClientScriptableObject.server_onReceiveUpdate( self )
end

-- Client callbacks
-- Docs: ClientScriptableObjectClass.html#client_oncreate
function ClientScriptableObject.client_onCreate( self )
end

-- Docs: ClientScriptableObjectClass.html#client_ondestroy
function ClientScriptableObject.client_onDestroy( self )
end

-- Docs: ClientScriptableObjectClass.html#client_onrefresh
function ClientScriptableObject.client_onRefresh( self )
end

-- Docs: ClientScriptableObjectClass.html#client_onfixedupdate
function ClientScriptableObject.client_onFixedUpdate( self, timeStep )
end

-- Docs: ClientScriptableObjectClass.html#client_onupdate
function ClientScriptableObject.client_onUpdate( self, deltaTime )
end

-- Docs: ClientScriptableObjectClass.html#client_onclientdataupdate
function ClientScriptableObject.client_onClientDataUpdate( self, data, channel )
end

-- Docs: ClientScriptableObjectClass.html#client_onlocalplayerchangedworld
function ClientScriptableObject.client_onLocalPlayerChangedWorld( self, world )
end
```

# ScriptableObjectClass script template

[Back to ScriptableObjectClass](ScriptableObjectClass.md)

Copy this starter script and remove anything you do not need.

```lua
ScriptableObject = class()

-- Constants
-- Docs: ScriptableObjectClass.html#issaveobject
ScriptableObject.isSaveObject = false

-- Server callbacks
-- Docs: ScriptableObjectClass.html#server_oncreate
function ScriptableObject.server_onCreate( self )
end

-- Docs: ScriptableObjectClass.html#server_ondestroy
function ScriptableObject.server_onDestroy( self )
end

-- Docs: ScriptableObjectClass.html#server_onrefresh
function ScriptableObject.server_onRefresh( self )
end

-- Docs: ScriptableObjectClass.html#server_onfixedupdate
function ScriptableObject.server_onFixedUpdate( self, timeStep )
end

-- Docs: ScriptableObjectClass.html#server_onreceiveupdate
function ScriptableObject.server_onReceiveUpdate( self )
end

-- Docs: ScriptableObjectClass.html#server_onunload
function ScriptableObject.server_onUnload( self )
end

-- Client callbacks
-- Docs: ScriptableObjectClass.html#client_oncreate
function ScriptableObject.client_onCreate( self )
end

-- Docs: ScriptableObjectClass.html#client_ondestroy
function ScriptableObject.client_onDestroy( self )
end

-- Docs: ScriptableObjectClass.html#client_onrefresh
function ScriptableObject.client_onRefresh( self )
end

-- Docs: ScriptableObjectClass.html#client_onfixedupdate
function ScriptableObject.client_onFixedUpdate( self, timeStep )
end

-- Docs: ScriptableObjectClass.html#client_onupdate
function ScriptableObject.client_onUpdate( self, deltaTime )
end

-- Docs: ScriptableObjectClass.html#client_onclientdataupdate
function ScriptableObject.client_onClientDataUpdate( self, data, channel )
end

-- Docs: ScriptableObjectClass.html#client_onlocalplayerchangedworld
function ScriptableObject.client_onLocalPlayerChangedWorld( self, world )
end
```

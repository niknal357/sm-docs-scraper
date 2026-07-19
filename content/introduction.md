# Introduction

Welcome to the Scrap Mechanic Lua API reference. This site presents the [official Scrap Mechanic API documentation](https://scrapmechanic.com/api/index.html) in a searchable, navigable format.

## Start here

- [Game script environment](Game-Script-Environment/index.md) covers scripts used by games, worlds, parts, tools, characters, and other gameplay systems.
- [Terrain script environment](Terrain-Script-Environment/index.md) covers terrain generation and terrain-related APIs.

Most mod scripts use the Game environment. APIs available only in a specific environment are listed within that environment.

## How the API is organized

- **Static Functions** are functions called directly, such as `sm.shape.createPart(...)`.
- **Userdata** represents game objects and utility values, such as `Shape`, `Player`, `Vec3`, and `Uuid`.
- **Classes** define callbacks that the game invokes on scripts, such as `server_onCreate` and `client_onUpdate`.

Function pages show parameters, return values, and whether an API is available on the server, client, or both.

## Lua and multiplayer

Scrap Mechanic uses Lua 5.1. The [Lua 5.1 reference manual](https://www.lua.org/manual/5.1/) covers the language itself, while this site documents the APIs provided by the game.

Scrap Mechanic separates simulation into server and client contexts. Server code controls authoritative game state. Client code handles local input, presentation, and other player-specific behavior. Check each API's availability before using it in a callback.

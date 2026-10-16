# Idle Sryfe Miner — Public CI & Release Status

This **public** repository contains **only safe build metadata, release notes and validation workflows**. The complete Android game source, design documents, balancing parameters and all APK build artifacts live in a separate **private** repository owned by the same developer.

## Status
- Game: Idle Sryfe Miner
- Phase: CP001 native Android prototype
- Monetization: disabled; fairness-first design
- Official APK: not released yet
- Private source: **not mirrored**, checked out or uploaded here.

## GitHub Actions model
The public GitHub-hosted runner checks the published metadata and enforces a source-leak guard. **Native Android builds use the private repository's own GitHub-hosted runners**. GitHub Actions works for private repositories too. We intentionally do not put a private-source checkout token in public workflows or expose source-containing build artifacts.

## Development checkpoints
1. CP001 playable vertical slice
2. CP002 progression and visual polish
3. CP003 economy and balance testing
4. CP004 original Sryfe visuals and cosmetics
5. CP005 device testing and performance
6. CP006 usability and accessibility
7. CP007 optional fair monetization after gameplay is complete

No copyrighted assets or code from any other miner game are included.

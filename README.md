# SanchosCTL
SanchosCTL is a simple CLI tool for managing SanchosOS and the Sanchos ecosystem.

## Commands
| Flag | Full Option | Description |
| :--- | :--- | :--- |
| `-h` | `--help` | Show help message |
| `-i [pkg_name]` | `--install [pkg_name]` | Install applications |
| `-u` | `--update` | Update system and Sanchos ecosystem packages|
| `-id` | `--id` | SanchosID login, register, or exit account |
| `-vpn` | `--sanchosvpn` | Update SanchosVPN subscription |
| `-c` | `--check` | Perform full system check |
| `-t` | `--theme` | Change system theme |
| `-fb` | `--fullbackup` | Create full system backup |
| `-b [dir]` | `--backup [dir]` | Create partial backup |
| `-rb [achive]` | `--restorebackup [achive]` | Restore files from backup |
| `-w` | `--tui` | Run in terminal interface mode |

## Examples
Run terminal user interface mode:
```sh
sanchosctl --tui
```


Made by Sanchos from https://sanchos.su
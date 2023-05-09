# Plexx
#### Watch, request and download media automatically
### Services

- Plex Media Server
- Overseerr
- Jackett
- Radarr
- Sonarr
- qBittorrent

### Install
```
compile .env
with yours download, movies and series path folder
```
```bash
RUN
docker-compose up -d
```

### Linux only
#### for external drivers it may be required
```bash
lsblk #for list external usb devices
mount /dev/{YOUR_DEV_NAME} /media/root/folder 
```

### Configure
### Jackett > hostname:9117
##### Torrent Indexer Manager
```
Configure Torrent Indexer
```
### Radarr > hostname:7878
##### Monitoring and Download Requested Overseerr Movies
```
Add Jackett Indexer
Indexer > Torznab (custom)
```
```
Set root folder to /movies
```
```
Set Movies Profile and preferred lenguages 
```
```
Set qBittorrent as Torrent Client
```
### Sonarr > hostname:8989
##### Monitoring and Download Requested Overseerr Series 
```
Add Jackett Indexer
Indexer > Torznab (custom)
```
```
Set root folder to /tv
```
```
Set Series Profile and preferred lenguages 
```
```
Set qBittorrent as Torrent Client
```
### Overseerr > hostname:5055
##### Search and Request Media to Radarr and Sonarr
```
Configure Radarr and Sonarr 
```
### qBittorent > hostname:8080
##### Torrent Client
```
Set download folder to /downloads
```
### Plex > hostname:32400
##### Media Player
```
Add Movies and Series Libraries
Movies > /movies
Series > /tv
```
### Open Router Ports
- Jackett: 9117
- Radarr: 7878
- Sonarr: 8989
- Overseerr: 5055
- qBittorrent: 8080
- qBittorrent: 6881
- Plex: 32400
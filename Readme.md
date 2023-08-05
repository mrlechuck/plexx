# <span style="color:orange; font-size:40px">Plexx</span>
#### Watch, request and download media automatically
## <span style="color:MediumAquamarine">Services</span>

- Plex Media Server
- Tautulli
- Overseerr
- Jackett
- Flaresolverr
- Radarr
- Sonarr
- qBittorrent

## <span style="color:LightSeaGreen">Install</span>
- rename .env.example to .env
- compile .env with yours folders paths

```bash
RUN
docker-compose up -d
```

### <span style="color:SlateGray">Linux only</span>
#### for external drivers it may be required
```bash
lsblk #for list external usb devices
mount /dev/{YOUR_DEV_NAME} /media/root/folder 
```

## <span style="color:Teal">Configure</span>
### <span style="color:DarkSeaGreen">Jackett</span> > hostname:9117
##### Torrent Indexer Manager
```
Configure Torrent Indexer
```
### <span style="color:Green">Flaresolverr</span> > hostname:8191
##### Proxy server to bypass Cloudflare protection
```
Set FlareSolverr API URL into Jackett Configuration
Example: http://hostname:8191
```
### <span style="color:DarkKhaki">Radarr</span> > hostname:7878
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
### <span style="color:CadetBlue">Sonarr</span> > hostname:8989
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
### <span style="color:SlateBlue">Overseerr</span> > hostname:5055
##### Search and Request Media to Radarr and Sonarr
```
Configure Radarr and Sonarr 
```
### <span style="color:CornflowerBlue">qBittorent</span> > hostname:8080
##### Torrent Client
```
Set incomplete download path to /incomplete
```
```
Optional:
• Set alternative UI:
    - /qbitt-ui/vuetorrent
    - /qbitt-ui/mat-unix

• Set rrs feed
```
### <span style="color:Goldenrod">Plex</span> > hostname:32400
##### Media Player
```
Add Movies and Series Libraries
Movies > /movies
Series > /tv
```
### <span style="color:Cyan">Tautulli</span> > hostname:8181
##### Plex Activity Monitor
```
• Open Tautulli in your Browser (hostname:8181)
• Follow Quickstart Configuration 
• Configure Tautulli in Overseerr (Settings > Plex)
```
<i>You can find Tautulli <b>API Key</b> in Tautulli > Settings > Web Interface</i>

## <span style="color:RoyalBlue">Open Router Ports (Optional)</span>
- Jackett: 9117
- Flaresolverr: 8191
- Radarr: 7878
- Sonarr: 8989
- Overseerr: 5055
- qBittorrent: 8080
- qBittorrent: 6881
- Plex: 32400
- Tautulli: 8181

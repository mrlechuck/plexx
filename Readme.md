# <span style="color:orange; font-size:40px">Plexx</span>
#### Request your media and the ecosystem will find and download it for you

## <span style="color:MediumAquamarine">Services</span>
- Plex Media Server (Media Library)
- Tautulli (Plex Users Activity Monitor)
- Overseerr (Media Catalog to Search and Request Media)
- Jackett (Torrent Indexer Manager)
- Flaresolverr (Proxy Server to Bypass Cloudflare Protection)
- Radarr (Monitoring and Download Requested Overseerr Movies)
- Sonarr (Monitoring and Download Requested Overseerr Series)
- qBittorrent (Torrent Client)

## <span style="color:LightSeaGreen">Install</span>
- rename .env.example to .env
- compile .env with yours folders paths
- run the command below in the root folder

```bash
docker compose up -d
```

### <span style="color:SlateGray">Linux only</span>
#### for external drivers it may be required
```bash
lsblk #list external usb devices
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
##### Media Catalog to Search and Request Media with Radarr and Sonarr
```
Configure Radarr and Sonarr 
```
### <span style="color:CornflowerBlue">qBittorent</span> > hostname:8080
##### Torrent Client
```
[Nerd Only]

• Set network interface and IP binding
  - Settings > Advanced > Network interface (sample: eth0)
  - Settings > Advanced > Optional IP to bind (sample: All IPv4 addresses)
```
```
[Optional]

• Set path for incomplete downloads to /incomplete
  in Settings > Downloads
  
• Set alternative UI:
    - /qbitt-ui/vuetorrent
    - /qbitt-ui/mat-unix

• Set rrs feed
```
### <span style="color:Goldenrod">Plex</span> > hostname:32400
##### Media Library
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

## <span style="color:#ff1269">Service Update Reference</span>
Run the command below in the root folder
```bash
docker compose down
docker compose pull
docker compose up -d
```

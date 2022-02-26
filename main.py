from fastapi import FastAPI
import uvicorn

import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials 


cid ="427c7e94df2b4d1f89ad703f2d83d005" 
secret = "02a04d31f6a64e3ca79f8d16b7dfa51e" 
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret) 
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "Enter an artist name to find related artists!"
    }
    
    
@app.get("/getRelatedArtists/{name}")

async def getRelatedArtists(name: str):
    results = sp.search(q='artist: '+name , type='artist')
    items = results['artists']['items']
    
    if len(items) == 0:
        return {"Error: ": "Oops! Cannot find the artist you are looking for. Please enter a valid artist name."}
    else:
        uri = items[0]['uri']
        related = sp.artist_related_artists(uri)
        
        related_art = ''
        for artists in related['artists']:
            artist = artists['name'] + ", "
            related_art = related_art + artist
            
        return {"Related artists: ": related_art}

    
    
if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")

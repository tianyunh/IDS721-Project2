import asyncio
from main import getRelatedArtists

def test_getRelatedArtists():
    assert asyncio.run(getRelatedArtists("Radiohead")) == {"Related artists: ":"Thom Yorke, Blur, Pixies, Interpol, Portishead, The Flaming Lips, Pulp, Jeff Buckley, my bloody valentine, Sonic Youth, Arcade Fire, Slowdive, Elliott Smith, PJ Harvey, Pavement, Neutral Milk Hotel, The Verve, Joy Division, The Smashing Pumpkins, Yo La Tengo, "}
    assert asyncio.run(getRelatedArtists("somerandomartist")) == {"Error: ": "Oops! Cannot find the artist you are looking for. Please enter a valid artist name."}
# A python interface to the [Volumio](https://volumio.org/)
  [REST API](https://volumio.github.io/docs/API/REST_API.html)

This a simple and not very complete interface using the
*simple_rest_client* package.

Its focus is on querying a Volumio instance for playlists, lists of
albums/artists, and playing selections from those lists.

However, of the documented
[Volumio REST API](https://volumio.github.io/docs/API/REST_API.html)
resources are available via the simple_rest_client object at _volumio.api_.

# Examples

## Get a list of artists.
```
import volumio
volumio = volumio.VolumioClient()  # Defaults to _volumio.local_ API url.
artists = volumio.list_artists()  # Returns a list of 'artist://' uris
```

## Play all tracks by an artist (first artist in the list).
```
# Calling <resource>.list() is how to do GET with simple_rest_client.
resp = volumio.api.browse.list({'uri': artists[0]})
tracks = []
for l in resp.body['navigation']['lists']:
    tracks.extend(i for i in l['items'] if i['type'] == 'song')
volumio.play_tracks(tracks)
```

## Playback control
```
volumio.pause()
volumio.resume()
volumio.prev()
volumio.next()
volumio.volume('+10')
volumio.volume('-10')
```

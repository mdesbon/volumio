#!/usr/bin/env python3

import simple_rest_client.api

class VolumioClientException(Exception):
    pass


class VolumioClient(object):
    def __init__(
            self, api_url='http://volumio.local/api/v1', no_connect=False
    ):
        self.api = simple_rest_client.api.API(
            api_root_url=api_url,
            json_encode_body=True
        )
        for r in [
            'commands', 'getState', 'browse', 'search', 'replaceAndPlay',
            'addToQueue', 'getQueue', 'listplaylists', 'ping',
            'getSystemVersion',
        ]:
            self.api.add_resource(resource_name=r)
        # Test connection
        if not no_connect:
            resp = self.api.getsystemversion.list()
            if resp.body['variant'] != 'volumio':
                raise VolumioClientException(
                    f"Failed to connect to volumio: {resp}"
                )

    def command(self, cmd, **args):
        if args is None:
            args = {}
        args['cmd'] = cmd
        resp = self.api.commands.list(params=args)
        return resp

    def _browse(self, params):
        resp = self.api.browse.list(params=params)
        if 'navigation' not in resp.body:
            raise Exception(f"Search failed: {resp}")
        return resp.body['navigation']['lists'][0]['items']

    def list_playlists(self):
        dictlist = self._browse(params={'uri': 'playlists'})
        return {r['title']: r for r in dictlist}

    def list_albums(self):
        dictlist = self._browse(params={'uri': 'albums://'})
        return {r['title']: r for r in dictlist}

    def list_artists(self):
        dictlist = self._browse(params={'uri': 'artists://'})
        return {r['title']: r for r in dictlist}

    def play_playlist(self, playlist_name):
        self.command('playplaylist', name=playlist_name)

    def pause(self):
        self.command('pause')

    def resume(self):
        self.command('play')

    def get_state(self):
        resp = self.api.getstate.list()
        return resp.body

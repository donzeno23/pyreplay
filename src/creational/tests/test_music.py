import pytest
import music

from config import service_config


def test_pandora_service_connection():

    pandora = music.services.get('PANDORA', **service_config)
    pandora.test_connection()

@pytest.mark.darwin
def test_pandora_service_comparison():

    pandora = music.services.get('PANDORA', **service_config)
    pandora2 = music.services.get('PANDORA', **service_config)
    assert id(pandora) == id(pandora2), f"id(pandora) == id(pandora2): {id(pandora) == id(pandora2)}"

# Note: Running with  "pytest -v -s -E staging" the below test will be skipped
@pytest.mark.env("stage1")
def test_spotify_service_connection():

    spotify = music.services.get('SPOTIFY', **service_config)
    spotify.test_connection()

def test_spotify_comparison():

    spotify = music.services.get('SPOTIFY', **service_config)
    spotify2 = music.services.get('SPOTIFY', **service_config)
    assert id(spotify) == id(spotify2), f"id(spotify) == id(spotify2): {id(spotify) == id(spotify2)}"

def test_local_service():

    local = music.services.get('LOCAL', **service_config)
    local.test_connection()


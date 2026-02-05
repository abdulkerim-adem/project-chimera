import pytest
from skills.download_video import download
from skills.transcribe import transcribe
from skills.post_social import post

def test_download_video_returns_dict():
    # Expectation: returns a dict with 'file_path' key (not implemented yet -> should fail)
    res = download("http://example.com/video.mp4")
    assert isinstance(res, dict)
    assert "file_path" in res

def test_transcribe_returns_text():
    # Expectation: returns a dict with 'text' key (not implemented -> should fail)
    res = transcribe("some/path.mp4")
    assert isinstance(res, dict)
    assert "text" in res

def test_post_social_returns_post_id():
    # Expectation: returns a dict with 'post_id' key (not implemented -> should fail)
    res = post("hello world")
    assert isinstance(res, dict)
    assert "post_id" in res
from flask import url_for


def test_version_returns_200(client):
    assert client.get(url_for('version')).status_code == 200


def test_index_returns_404(client):
    res = client.get(url_for('version'))
    assert res.json['version'] == 1

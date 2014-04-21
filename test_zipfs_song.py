# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division

from zipfs_song import song_counts
from zipfs_song import quality
from zipfs_song import zipf_index
from zipfs_song import to_songs
from zipfs_song import sorted_songs
from zipfs_song import Song

def test_song_counts():
    assert song_counts('4 2') == (4, 2)

def test_song_counts_with_whitespace():
    assert song_counts(' 4 2  ') == (4, 2)

def test_to_songs():
    song = to_songs(['4 foo'])[0]
    assert song.index == 1
    assert song.times_played == 4
    assert song.title == 'foo'

def test_zipf_index():
    song1, song2 = to_songs(['4 foo', '6 bar'])
    assert zipf_index(song1) == 1 / 1
    assert zipf_index(song2) == 1 / 2

def test_quality():
    song1, song2 = to_songs(['4 foo', '6 bar'])
    assert quality(song1) == 4 / (1 / 1)
    assert quality(song2) == 6 / (1 / 2)

def test_quality_for_unplayed_song():
    song = Song(42, 0, 'boring song')
    assert quality(song) == 0

def test_sorted_songs():
    songs = to_songs(['4 foo', '6 bar', '10 baz'])
    expected = [Song(3, 10, 'baz'), Song(2, 6, 'bar'), Song(1, 4, 'foo')]
    assert quality(expected[0]) > quality(expected[1]) > quality(expected[2])
    assert sorted_songs(songs) == expected

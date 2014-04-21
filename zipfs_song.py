#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
import itertools
import fileinput
from collections import namedtuple

Song = namedtuple('Song', ['index', 'times_played', 'title'])

def zipf_index(song):
    return 1 / song.index

def quality(song):
    return song.times_played / zipf_index(song)

def sorted_songs(songs):
    return sorted(songs, key=quality, reverse=True)

def song_counts(line):
    songs_given, songs_to_select = (int(part) for part in line.strip().split(' '))
    return songs_given, songs_to_select

def to_songs(lines):
    def parse_line(line):
        parts = line.strip().split(' ')
        return int(parts[0]), parts[1]
    return [Song(index + 1, *parse_line(line)) for index, line in enumerate(lines)]
    
if __name__ == '__main__':
    input_lines = fileinput.input()
    songs_given, songs_to_select = song_counts(''.join(itertools.islice(input_lines, 1)))
    songs = to_songs(input_lines)
    assert len(songs) == songs_given
    songs_sorted_by_quality = sorted_songs(songs)
    assert len(songs_sorted_by_quality) >= songs_to_select
    selected_songs = itertools.islice(songs_sorted_by_quality, songs_to_select)
    for song in selected_songs:
        print(song.title)

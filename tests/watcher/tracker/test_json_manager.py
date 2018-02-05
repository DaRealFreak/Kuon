#!/usr/bin/python
# -*- coding: utf-8 -*-

from opskins.watcher.tracker import TrackConditions
from opskins.watcher.tracker.json_manager import JsonManager

if __name__ == '__main__':
    example_items = [
        {
            'search_word': "m4 howl min",
            'value': 80000,
            'unit': '#',
            'condition': TrackConditions.BELOW_VALUE
        },
        {
            'search_word': "m4 howl min",
            'value': 10,
            'unit': '%',
            'condition': TrackConditions.BELOW_AVERAGE
        }
    ]
    tracked_items = JsonManager.get_tracked_items()
    print(tracked_items)
    JsonManager.save_tracked_items(example_items)

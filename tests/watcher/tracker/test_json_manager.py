#!/usr/bin/python
# -*- coding: utf-8 -*-

from opskins.watcher.tracker import TrackConditions
from opskins.watcher.tracker.json_manager import JsonManager

if __name__ == '__main__':
    example_items = [
        {
            'search_item': "m4 howl min",
            'value': 80000,
            'unit': '#',
            'condition': TrackConditions.BELOW_VALUE
        },
        {
            'search_item': "\"Desert Eagle | Blaze\"",
            'value': 0.01,
            'unit': '%',
            'condition': TrackConditions.BELOW_AVERAGE_LAST_SOLD
        },
        {
            'search_item': "ak vulcan min",
            'value': 0,
            'unit': '#',
            'condition': TrackConditions.BELOW_CHEAPEST_LAST_SOLD
        },
    ]
    tracked_items = JsonManager.get_tracked_items()
    print(tracked_items)
    JsonManager.save_tracked_items(example_items)

#!/usr/bin/python
# -*- coding: utf-8 -*-
from kuon.watcher.tracker import TrackConditions
from kuon.watcher.tracker.json_manager import JsonManager

if __name__ == '__main__':
    example_items = [
        {
            'search_item': "M4A4 | Howl (Minimal Wear)",
            'conditions': [
                {
                    'key': 'price',
                    'value': 80000,
                    'unit': '#',
                    'condition': TrackConditions.BELOW_VALUE
                }
            ]
        },
        {
            'search_item': "Desert Eagle | Blaze (Factory New)",
            'conditions': [
                {
                    'key': 'wear_value',
                    'value': 0.01,
                    'unit': '#',
                    'condition': TrackConditions.BELOW_VALUE
                },
                {
                    'key': 'price',
                    'value': 0.01,
                    'unit': '%',
                    'condition': TrackConditions.BELOW_AVERAGE_LAST_SOLD
                }
            ]
        },
        {
            'search_item': "AK-47 | Vulcan (Minimal Wear)",
            'conditions': [
                {
                    'key': 'price',
                    'value': 0,
                    'unit': '#',
                    'condition': TrackConditions.BELOW_CHEAPEST_LAST_SOLD
                }
            ]
        },
    ]
    tracked_items = JsonManager.get_tracked_items()
    print(tracked_items)
    JsonManager.save_tracked_items(example_items)

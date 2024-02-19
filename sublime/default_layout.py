import sublime

def plugin_loaded():
    layout = {
    "cols": [0.0, 0.75, 1.0],  # Define three columns
    "rows": [0.0, 0.33, 0.66, 1.0],  # Define four rows
    "cells": [
        [0, 0, 1, 3],  # Group 1: covers 75% of width and entire height
        [1, 0, 2, 1],  # Group 2: covers 25% of width and first row
        [1, 1, 2, 2],  # Group 2: covers 25% of width and second row
        [1, 2, 2, 3]   # Group 2: covers 25% of width and third row
    ]
    }
    sublime.active_window().run_command("set_layout", layout)
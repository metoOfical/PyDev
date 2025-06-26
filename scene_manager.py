import json

def save_scene(scene_objects, filename):
    """
    scene_objects: lista dict, np:
    [{
        "model": "cube",
        "position": [0,1,0],
        "rotation": [0,0,0],
        "scale": [1,1,1],
        "color": [1,0,0]
    }, ...]
    """
    with open(filename, 'w') as f:
        json.dump(scene_objects, f, indent=4)

def load_scene(filename):
    with open(filename, 'r') as f:
        return json.load(f)

from ursina import *
from scene_manager import load_scene

def create_entity(obj):
    color_rgba = tuple(obj.get("color", [1,1,1])) + (1,)
    return Entity(
        model=obj.get("model", "cube"),
        position=tuple(obj.get("position", [0,0,0])),
        rotation=tuple(obj.get("rotation", [0,0,0])),
        scale=tuple(obj.get("scale", [1,1,1])),
        color=color_rgba,
        collider='box'
    )

def main():
    app = Ursina()

    scene_objects = load_scene('scene.json')

    for obj in scene_objects:
        create_entity(obj)

    EditorCamera()  # pozwala obracać i przybliżać kamerę myszką

    app.run()

if __name__ == "__main__":
    main()

script_classes = {
    "Rotator": Rotator,
    # Tu możesz dodać kolejne klasy skryptów
}

active_scripts = []

def create_entity(obj):
    color_rgba = tuple(obj.get("color", [1,1,1])) + (1,)
    ent = Entity(
        model=obj.get("model", "cube"),
        position=tuple(obj.get("position", [0,0,0])),
        rotation=tuple(obj.get("rotation", [0,0,0])),
        scale=tuple(obj.get("scale", [1,1,1])),
        color=color_rgba,
        collider='box'
    )

    # Dodajemy skrypt jeśli jest
    script_name = obj.get("script")
    if script_name and script_name in script_classes:
        script_instance = script_classes[script_name](ent)
        script_instance.start()
        active_scripts.append(script_instance)

    return ent

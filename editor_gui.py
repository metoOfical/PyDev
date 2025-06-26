import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
from scene_manager import save_scene, load_scene

class SceneEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Edytor sceny 2D/3D")

        self.scene_objects = []

        self.listbox = tk.Listbox(self, width=50)
        self.listbox.pack()

        btn_frame = tk.Frame(self)
        btn_frame.pack()

        tk.Button(btn_frame, text="Dodaj Cube", command=self.add_cube).grid(row=0, column=0)
        tk.Button(btn_frame, text="Usuń wybrany", command=self.remove_selected).grid(row=0, column=1)
        tk.Button(btn_frame, text="Zapisz scenę", command=self.save).grid(row=1, column=0)
        tk.Button(btn_frame, text="Wczytaj scenę", command=self.load).grid(row=1, column=1)
        tk.Button(btn_frame, text="Edytuj wybrany", command=self.edit_selected).grid(row=2, column=0, columnspan=2)

    def add_cube(self):
        obj = {
            "model": "cube",
            "position": [0,0,0],
            "rotation": [0,0,0],
            "scale": [1,1,1],
            "color": [1,1,1]
        }
        self.scene_objects.append(obj)
        self.refresh_listbox()

    def remove_selected(self):
        sel = self.listbox.curselection()
        if sel:
            idx = sel[0]
            del self.scene_objects[idx]
            self.refresh_listbox()

    def save(self):
        filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files","*.json")])
        if filename:
            save_scene(self.scene_objects, filename)
            messagebox.showinfo("Zapisano", f"Scena zapisana do {filename}")

    def load(self):
        filename = filedialog.askopenfilename(filetypes=[("JSON files","*.json")])
        if filename:
            self.scene_objects = load_scene(filename)
            self.refresh_listbox()
            messagebox.showinfo("Wczytano", f"Scena wczytana z {filename}")

    def edit_selected(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showwarning("Brak wyboru", "Wybierz obiekt do edycji")
            return
        idx = sel[0]
        obj = self.scene_objects[idx]

        for prop in ['position', 'rotation', 'scale', 'color']:
            val = simpledialog.askstring("Edytuj", f"Wartość {prop} (lista liczb, np. 0,1,0):",
                                         initialvalue=','.join(map(str, obj[prop])))
            if val:
                try:
                    obj[prop] = list(map(float, val.split(',')))
                except:
                    messagebox.showerror("Błąd", f"Niepoprawny format dla {prop}")
                    return
        self.scene_objects[idx] = obj
        self.refresh_listbox()

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for i, obj in enumerate(self.scene_objects):
            pos = ','.join(map(lambda x: f"{x:.1f}", obj['position']))
            self.listbox.insert(tk.END, f"{i}: {obj['model']} at {pos}")

if __name__ == "__main__":
    app = SceneEditor()
    app.mainloop()

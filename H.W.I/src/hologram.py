import open3d as o3d

def load_3d_model(model_path):
    """Ładuje model 3D do wizualizacji."""
    model = o3d.io.read_triangle_mesh(model_path)
    if not model.has_triangles():
        raise ValueError("Nieprawidłowy model 3D. Upewnij się, że plik zawiera dane siatki trójkątów.")
    model.compute_vertex_normals()
    return model

def display_hologram(model):
    """Wyświetla model 3D w interaktywnym oknie."""
    o3d.visualization.draw_geometries([model])

if __name__ == "__main__":
    model_path = "../models/example_model.obj"
    try:
        model = load_3d_model(model_path)
        display_hologram(model)
    except Exception as e:
        print(f"Błąd: {e}")
import numpy as np
import open3d as o3d

# Tworzenie prostego modelu hełmu jako siatki trójkątów
vertices = np.array([
    [0, 1, 0],   # Góra hełmu
    [-1, 0.5, 1], [1, 0.5, 1],   # Przód hełmu
    [-1, 0.5, -1], [1, 0.5, -1], # Tył hełmu
    [-1, -1, 1], [1, -1, 1],     # Dół przodu
    [-1, -1, -1], [1, -1, -1]    # Dół tyłu
], dtype=np.float64)  # Zmiana na float64 dla Open3D

triangles = np.array([
    [0, 1, 2], [0, 2, 4], [0, 4, 3], [0, 3, 1],  # Górna część hełmu
    [1, 2, 5], [2, 5, 6], [1, 5, 6],  # Przód poprawiony
    [3, 4, 7], [4, 7, 8], [3, 7, 8],  # Tył poprawiony
    [5, 6, 7], [6, 7, 8],  # Dół
    [1, 3, 5], [3, 5, 7],  # Boki
    [2, 4, 6], [4, 6, 8]   # Boki
], dtype=np.int32)

# Tworzenie obiektu mesh
helmet_mesh = o3d.geometry.TriangleMesh()
helmet_mesh.vertices = o3d.utility.Vector3dVector(vertices)
helmet_mesh.triangles = o3d.utility.Vector3iVector(triangles)

# Generowanie normalnych powierzchni
helmet_mesh.compute_vertex_normals()
helmet_mesh.compute_triangle_normals()

# Sprawdzanie poprawności modelu
if not helmet_mesh.has_triangles():
    print("Błąd: Model nie zawiera siatki trójkątów!")
else:
    print("Model poprawnie utworzony.")

# Zapis do pliku OBJ
output_path = "helmet.obj"
success = o3d.io.write_triangle_mesh(output_path, helmet_mesh, write_ascii=True)
if success:
    print(f"Model hełmu zapisany jako {output_path}")
else:
    print("Błąd zapisu pliku.")

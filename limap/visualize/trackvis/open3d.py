
# Tariq Abuhashim
# for mission systesm

import numpy as np
import open3d as o3d
from .base import BaseTrackVisualizer
from ..vis_utils import compute_robust_range_lines
from ..vis_lines import open3d_get_line_set, open3d_get_cameras

class Open3DTrackVisualizer(BaseTrackVisualizer):
    def __init__(self, tracks):
        super(Open3DTrackVisualizer, self).__init__(tracks)

    def reset(self):
        app = o3d.visualization.gui.Application.instance
        app.initialize()
        return app

    def vis_all_lines(self, n_visible_views=4, width=2, scale=1.0):
        lines = self.get_lines_n_visible_views(n_visible_views)
        vis = o3d.visualization.Visualizer()
        vis.create_window(height=1080, width=1920)
        line_set = open3d_get_line_set(lines, width=width, ranges=ranges, scale=scale)
        vis.add_geometry(line_set)
        vis.run()
        vis.destroy_window()

    def rotation_matrix_from_vectors(self, vec1, vec2):
        """ Generate a rotation matrix that aligns vec1 to vec2 """
        a, b = vec1 / np.linalg.norm(vec1), vec2 / np.linalg.norm(vec2)
        v = np.cross(a, b)
        c = np.dot(a, b)
        s = np.linalg.norm(v)
        kmat = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
        rotation_matrix = np.eye(3) + kmat + kmat.dot(kmat) * ((1 - c) / (s ** 2))
        return rotation_matrix

    def vis_reconstruction(self, imagecols, normals=None, centers=None, n_visible_views=4, width=2, ranges=None, scale=1.0, cam_scale=1.0):
        lines = self.get_lines_n_visible_views(n_visible_views)
        lranges = compute_robust_range_lines(lines)
        scale_cam_geometry = abs(lranges[1, :] - lranges[0, :]).max()

        vis = o3d.visualization.Visualizer()
        vis.create_window(height=1080, width=1920)
        line_set = open3d_get_line_set(lines, width=width, ranges=ranges, scale=scale)
        vis.add_geometry(line_set)
        camera_set = open3d_get_cameras(imagecols, ranges=ranges, scale_cam_geometry=scale_cam_geometry * cam_scale, scale=scale)
        vis.add_geometry(camera_set)

        if normals is not None and centers is not None:
            color = [1, 0, 0]  # Red color for visualization

            for normal, center in zip(normals, centers):
                print(f"{normal} {center}")
                # Create a new arrow for each normal
                arrow = o3d.geometry.TriangleMesh.create_arrow(cylinder_radius=0.2, cone_radius=0.4, cylinder_height=2, cone_height=1.0)
                # Compute transformation matrix
                R = self.rotation_matrix_from_vectors(np.array([0, 0, 1]), normal)
                T = np.eye(4)
                T[:3, :3] = R
                T[:3, 3] = center
                # Apply the transformation
                arrow.transform(T)
                arrow.paint_uniform_color(color)
                vis.add_geometry(arrow)

        vis.run()
        vis.destroy_window()


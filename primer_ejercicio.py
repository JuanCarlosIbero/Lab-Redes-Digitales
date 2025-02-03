import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Line3DCollection

def rotation_matrix_z(alpha):
    #Creates a rotation matrix for a rotation about the Z-axis
    return np.array([
        [np.cos(alpha), -np.sin(alpha), 0],
        [np.sin(alpha),  np.cos(alpha), 0],
        [0,              0,             1]
    ])

def rotation_matrix_y(beta):
    #Creates a rotation matrix for a rotation about the Y-axis
    return np.array([
        [np.cos(beta),  0, np.sin(beta)],
        [0,            1,             0],
        [-np.sin(beta), 0, np.cos(beta)]
    ])
    
def rotation_matrix_x(gamma):
    #Creates a rotation matrix for a rotation about the X-axis
    return np.array([
        [1, 0,              0],
        [0, np.cos(gamma), -np.sin(gamma)],
        [0, np.sin(gamma),  np.cos(gamma)]
    ])
    
def homogeneous_transform(alpha, beta, gamma, p):
    #Calculates the homogeneous transformation matrix
    # Rotation matrices
    Rz = rotation_matrix_z(alpha)
    Ry = rotation_matrix_y(beta)
    Rx = rotation_matrix_x(gamma)
    
    # Combined rotation matrix
    R = Rz @ Ry @ Rx

    # Homogeneous transformation matrix
    T = np.eye(4)
    T[:3, :3] = R
    T[:3, 3] = p

    return T

def plot_transformation(T):
    #Plots the transformation matrix in 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Origin
    origin = np.array([0, 0, 0])
    x_axis = np.array([1, 0, 0])
    y_axis = np.array([0, 1, 0])
    z_axis = np.array([0, 0, 1])

    # Transform axes
    transformed_origin = T[:3, 3]
    transformed_x = transformed_origin + T[:3, 0]
    transformed_y = transformed_origin + T[:3, 1]
    transformed_z = transformed_origin + T[:3, 2]

    # Plot original axes
    ax.quiver(*origin, *x_axis, color='r', label='X-axis (original)')
    ax.quiver(*origin, *y_axis, color='g', label='Y-axis (original)')
    ax.quiver(*origin, *z_axis, color='b', label='Z-axis (original)')

    # Plot transformed axes
    ax.quiver(*transformed_origin, *(transformed_x - transformed_origin), color='r', label='X-axis (transformada)')
    ax.quiver(*transformed_origin, *(transformed_y - transformed_origin), color='g', label='Y-axis (transformada)')
    ax.quiver(*transformed_origin, *(transformed_z - transformed_origin), color='b', label='Z-axis (transformada)')

    # Set plot limits
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])

    # Labels
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')

    plt.legend()
    plt.show()

def main():
    # Input from the user
    alpha = float(input("Ingrese el angulo de rotación alpha (grados) alrededor del eje Z: "))
    beta = float(input("Ingrese el angulo de rotación beta (grados) alrededor del eje Y: "))
    gamma = float(input("Ingrese el angulo de rotación gamma (grados) alrededor del eje X: "))
    px = float(input("Ingrese la coordenada x del vector de traslación: "))
    py = float(input("Ingrese la coordenada y del vector de traslación: "))
    pz = float(input("Ingrese la coordenada z del vector de traslación: "))

    # Convert angles to radians
    alpha = np.radians(alpha)
    beta = np.radians(beta)
    gamma = np.radians(gamma)

    # Translation vector
    p = np.array([px, py, pz])

    # Calculate the homogeneous transformation matrix
    T = homogeneous_transform(alpha, beta, gamma, p)

    # Display the matrix
    print("Matriz de la Transformada Homogenea:\n", T)

    # Plot the transformation
    plot_transformation(T)
    
if __name__ == "__main__":
    main()

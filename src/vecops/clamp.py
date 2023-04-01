
class Clamp:

    @staticmethod
    def clamp(a : int, min : int, max : int) -> int:
        if a < min:
            a = min
        elif a > max:
            a = max
        return a
    
    @staticmethod
    def clamp2D(vector : list[list[int]], min : list[list[int]], max : list[list[int]]) -> list[list[int]]:
        '''Clamps a given vector between min and max vectors
           Input matrix format: [[x],[y]]'''
        vector2D = vector
        vector2D[0][0] = Clamp.clamp(vector[0][0], min[0][0], max[0][0])
        vector2D[1][0] = Clamp.clamp(vector[1][0], min[1][0], max[1][0])
        return vector2D
    
    @staticmethod
    def clamp3D(vector : list[list[int]], min : list[list[int]], max : list[list[int]]) -> list[list[int]]:
        '''Clamps a given vector between min and max vectors
           Input matrix format: [[x],[y],[z]]'''
        vector3D = vector
        vector3D[0][0] = Clamp.clamp(vector[0][0], min[0][0], max[0][0])
        vector3D[1][0] = Clamp.clamp(vector[1][0], min[1][0], max[1][0])
        vector3D[2][0] = Clamp.clamp(vector[2][0], min[2][0], max[2][0])
        return vector3D

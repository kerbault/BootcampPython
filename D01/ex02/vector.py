class Vector:
    def __init__(self, values):
        self.values = values
        self.size = values.len

    def __add__(self):
        print()

    def __radd__(self):
        print()
        # add : scalars and vectors, can have errors with vectors.

    def __sub__(self):
        print()

    def __rsub__(self):
        print()
        # sub : scalars and vectors, can have errors with vectors.

    def __truediv__(self):
        print()

    def __rtruediv__(self):
        print()
        # div : only scalars.

    def __mul__(self):
        print()

    def __rmul__(self):
        print()
        # mul : scalars and vectors, can have errors with vectors,
        # return a scalar if we perform Vector * Vector (dot product)

    def __str__(self):
        print()

    def __repr__(self):
        print()

class GF:
    def __init__(self, value=None, p=None):
        if p is None:
            if value is None or not self._is_prime(value):
                raise ValueError("You must provide a prime modulus p")
            self.p = value
            self.is_factory = True
        else:
            self.p = p
            self.value = value % p
            self.is_factory = False

    def __call__(self, value):
        if not self.is_factory:
            raise TypeError("Cannot call a field element.")
        return GF(value, self.p)

    @staticmethod
    def _is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Arithmetic Operations
    def __add__(self, other):
        other = self._coerce(other)
        return GF(self.value + other.value, self.p)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        other = self._coerce(other)
        return GF(self.value - other.value, self.p)

    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        other = self._coerce(other)
        return GF(self.value * other.value, self.p)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        other = self._coerce(other)
        inv = pow(other.value, -1, self.p)
        return GF(self.value * inv, self.p)

    def __rtruediv__(self, other):
        return self._coerce(other) / self

    def __floordiv__(self, other):
        return self / other

    def __pow__(self, exponent):
        return GF(pow(self.value, exponent, self.p), self.p)

    def __neg__(self):
        return GF(-self.value, self.p)

    # Bitwise operations (optional, not mathematically meaningful, but handy)
    def __and__(self, other):
        other = self._coerce(other)
        return GF(self.value & other.value, self.p)

    def __or__(self, other):
        other = self._coerce(other)
        return GF(self.value | other.value, self.p)

    def __xor__(self, other):
        other = self._coerce(other)
        return GF(self.value ^ other.value, self.p)

    def __lshift__(self, n):
        return GF((self.value << n) % self.p, self.p)

    def __rshift__(self, n):
        return GF(self.value >> n, self.p)

    # Comparisons
    def __eq__(self, other):
        other = self._coerce(other)
        return self.value == other.value

    def __lt__(self, other):
        other = self._coerce(other)
        return self.value < other.value

    def __le__(self, other):
        other = self._coerce(other)
        return self.value <= other.value

    def __gt__(self, other):
        other = self._coerce(other)
        return self.value > other.value

    def __ge__(self, other):
        other = self._coerce(other)
        return self.value >= other.value

    # Hashing
    def __hash__(self):
        return hash((self.value, self.p))

    # Casting and conversions
    def __int__(self):
        return self.value

    def __index__(self):
        return self.value

    def __abs__(self):
        return abs(self.value)

    def __bool__(self):
        return self.value != 0

    # String representations
    def __repr__(self):
        if self.is_factory:
            return f"GF({self.p})"
        return f"F({self.value} mod {self.p})"

    def __str__(self):
        return str(self.value)

    # Internal coercion logic
    def _coerce(self, other):
        if isinstance(other, GF):
            if self.is_factory or other.is_factory:
                raise ValueError("Cannot operate between factory and element instances.")
            if self.p != other.p:
                raise ValueError("Cannot mix elements from different fields.")
            return other
        return GF(other, self.p)


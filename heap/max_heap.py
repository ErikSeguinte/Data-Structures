class Heap:
    """ Uses a 1 based array to make index math more intuitive."""
    def __init__(self):
        self._storage = [None]
        self.size = 0

    @property
    def storage(self):
        # skips the 0th element to make sure tests work.
        return self._storage[1:]

    def insert(self, value):
        self._storage.append(value)
        self.size += 1
        self._bubble_up(self.size)

    def delete(self):
        pass

    def get_max(self):
        return self._storage[1]

    def get_size(self):
        return self.size

    def _bubble_up(self, index):
        while index // 2 > 0:
            if self._storage[index] > self._storage[index // 2]:
                self._storage[index], self._storage[index // 2] = (
                    self._storage[index  // 2],
                    self._storage[index],
                )

            index = index // 2

    def _sift_down(self, index):
        pass

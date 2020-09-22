class Heap:
    """ Uses a 1 based array to make index math more intuitive."""

    def __init__(self):
        self._storage = [None]
        self.size = 0

    @property
    def storage(self):
        # skips the 0th element to make sure tests work.
        return self._storage[1:self.size+1]

    def insert(self, value):
        self._storage.append(value)
        self.size += 1
        self._bubble_up(self.size)

    def delete(self):
        if self.size > 1:
            root = self._storage[1]
            self._storage[1], self._storage[self.size] = self._storage[self.size], None
            self.size -= 1
            self._sift_down(1)

            return root

    def get_max(self):
        return self._storage[1]

    def get_size(self):
        return self.size

    def _bubble_up(self, index):
        while index // 2 > 0:
            if self._storage[index] > self._storage[index // 2]:
                self._storage[index], self._storage[index // 2] = (
                    self._storage[index // 2],
                    self._storage[index],
                )

            index = index // 2

    def _sift_down(self, i):
        while i * 2 <= self.size:
            root = self._storage[i]
            max_child = self._get_max_child(i)

            if self._storage[max_child] > root:
                self._storage[i], self._storage[max_child] = (
                    self._storage[max_child],
                    self._storage[i],
                )

            i = max_child

    def _get_max_child(self, i):
        if ((i * 2 + 1) > self.size) or self._storage[i * 2] > self._storage[i * 2 + 1]:
            return i * 2
        else:
            return i * 2 + 1

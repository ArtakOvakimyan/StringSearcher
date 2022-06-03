__all__ = ['AhoCorasick']
from decorator import decorator


class AhoCorasick:
    """Алгоритм Ахо-Корасик"""
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self.n = len(text)
        self.m = len(pattern)

    @decorator.measure_memory
    def search(self):
        indexes = []
        t = Trie()
        t.add(self.pattern)

        v = t.root
        for i in range(self.n):
            v = t.go(v, self.text[i])
            if v.is_terminal:
                indexes.append(i - self.m + 1)

        return indexes


def num(c) -> int:
    return ord(c)


class Vertex:
    def __init__(self, parent, prev_char: chr) -> None:
        self.next = dict()
        self.is_terminal = False
        self.parent = parent
        self.prev_char = prev_char
        self.suf_link = None
        self.go = dict()


class Trie:
    def __init__(self) -> None:
        self.vertices: [Vertex] = [Vertex(None, None)]
        self.root: Vertex = self.vertices[0]

    def last(self) -> Vertex:
        return self.vertices[-1]

    def add(self, s: str) -> None:
        v = self.root
        for i in range(len(s)):
            if v.next.get(num(s[i])) is None:
                self.vertices.append(Vertex(v, s[i]))
                v.next[num(s[i])] = self.last()
            v = v.next[num(s[i])]
        v.is_terminal = True

    def get_link(self, v: Vertex) -> Vertex:
        if v.suf_link is None:
            if v == self.root or v.parent == self.root:
                v.suf_link = self.root
            else:
                v.suf_link = self.go(self.get_link(v.parent), v.prev_char)
        return v.suf_link

    def go(self, v: Vertex, c: chr) -> Vertex:
        if v.go.get(num(c)) is None:
            if v.next.get(num(c)) is not None:
                v.go[num(c)] = v.next[num(c)]
            elif v == self.root:
                v.go[num(c)] = self.root
            else:
                v.go[num(c)] = self.go(self.get_link(v), c)
        return v.go[num(c)]

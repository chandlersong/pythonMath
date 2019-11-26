import unittest

from algorithm.princeton.chapter1.uf import UF


class UFTestCase(unittest.TestCase):

    def test_tiny(self):
        uf: UF = None

        def print_n(n):
            print("N is {}".format(n))
            nonlocal uf
            uf = UF(n)

        def print_p_q(p, q):
            if uf.connected(p, q):
                return
            uf.union(p, q)
            print("p:{},q:{}".format(p, q))
            print("id list is {}".format(uf.id))

        self.open_read_file("tinyUF.txt", print_n, print_p_q)
        print(uf.count)
        print("id list is {}".format(uf.id))

    @staticmethod
    def open_read_file(filename, head_action, action):
        f = open(filename, "r")
        line = f.readline()

        n = int(line)
        head_action(n)
        line = f.readline()

        for p, q in loop_file_return_two_int(line, f):
            action(p, q)

        f.close()


def loop_file_return_two_int(line, f):
    while line:
        str_array = line.split(" ")
        p = int(str_array[0])
        q = int(str_array[1])
        yield (p, q)
        line = f.readline()


if __name__ == '__main__':
    unittest.main()

import unittest
import subprocess

class TestSequenceFunctions(unittest.TestCase):

    def testdata_txt(self):
        expected_output = \
("""HERE IS THE BEST
Cost: 1.75179633009

[54.796, 41.361, 51.848, 19.414]
[55.396, 30.413, 54.749, 41.328]
[54.501, 43.445, 55.437, 30.396]
[60.419, 71.281, 54.235, 43.447]
[60.125, 29.214, 60.125, 71.214]
[60.111, 29.007, 60.111, 28.961]
[58.758, 29.074, 60.087, 28.961]
[66.77, 38.056, 58.701, 29.07]
[55.393, 17.975, 66.743, 38.1]
[59.244, 29.006, 55.335, 17.953]

""",None)
        p = subprocess.Popen(["python", "search_project.py", "./Data/testdata.txt"], stdout=subprocess.PIPE)
        out = p.communicate()
        self.assertTrue(out == expected_output)

    def mdata_txt(self):
        expected_output = \
("""HERE IS THE BEST
Cost: 1.75179633009

[54.796, 41.361, 51.848, 19.414]
[55.396, 30.413, 54.749, 41.328]
[54.501, 43.445, 55.437, 30.396]
[60.419, 71.281, 54.235, 43.447]
[60.125, 29.214, 60.125, 71.214]
[60.111, 29.007, 60.111, 28.961]
[58.758, 29.074, 60.087, 28.961]
[66.77, 38.056, 58.701, 29.07]
[55.393, 17.975, 66.743, 38.1]
[59.244, 29.006, 55.335, 17.953]

""",None)
        p = subprocess.Popen(["python", "search_project.py", "./Data/testdata.txt"], stdout=subprocess.PIPE)
        out = p.communicate()
        self.assertTrue(out == expected_output)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)
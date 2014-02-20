import unittest
import subprocess
import re

class TestSequenceFunctions(unittest.TestCase):

    def test_testdata_txt(self):
        expected_output = \
"""[54.796, 41.361, 51.848, 19.414]
[55.396, 30.413, 54.749, 41.328]
[54.501, 43.445, 55.437, 30.396]
[60.419, 71.281, 54.235, 43.447]
[60.125, 29.214, 60.125, 71.214]
[60.111, 29.007, 60.111, 29.007]
[58.758, 29.074, 60.087, 28.961]
[66.77, 38.056, 58.701, 29.07]
[55.393, 17.975, 66.743, 38.1]
[59.244, 29.006, 55.335, 17.953]
"""
        p = subprocess.Popen(["python", "search_project.py", "./Data/testdata.txt"], stdout=subprocess.PIPE)
        out = p.communicate()

        outputList = out[0].split("\n")
        output = "\n".join(outputList[3 : len(outputList) - 3])
        
        self.assertTrue(output == expected_output)

    def test_mdata_txt(self):
        expected_output = \
"""[54.796, 41.361, 51.848, 19.414]
[55.396, 30.413, 54.749, 41.328]
[54.501, 43.445, 55.437, 30.396]
[60.419, 71.281, 54.235, 43.447]
[60.125, 29.214, 60.125, 71.214]
[60.111, 29.007, 60.111, 29.007]
[58.758, 29.074, 60.087, 28.961]
[66.77, 38.056, 58.701, 29.07]
[55.393, 17.975, 66.743, 38.1]
[59.244, 29.006, 55.335, 17.953]
[58.303, 36.926, -1.0, 29.058]
"""
        p = subprocess.Popen(["python", "search_project.py", "./Data/mdata.txt"], stdout=subprocess.PIPE)
        out = p.communicate()

        outputList = out[0].split("\n")
        output = "\n".join(outputList[3 : len(outputList) - 3])

        self.assertTrue(output == expected_output)

    def test_tiny_test_txt(self):
        expected_output = \
"""[54.796, 41.361, 51.848, 19.414]
[55.396, 30.413, 54.749, 41.328]
[54.501, 43.445, 55.437, 30.396]
[-1.0, -1.0, -1.0, -1.0]
[60.125, 29.214, 60.125, 71.214]
[60.111, 29.007, 60.111, 29.007]
[58.758, 29.074, 60.087, 28.961]
"""

        p = subprocess.Popen(["python", "search_project.py", "./Data/tiny_test.txt"], stdout=subprocess.PIPE)
        out = p.communicate()

        outputList = out[0].split("\n")
        output = "\n".join(outputList[3 : len(outputList) - 3])

        self.assertTrue(output == expected_output)

    def test_td2_txt(self):
        expected_output = \
"""[54.796, 41.361, 51.848, 19.414]
[55.396, 30.413, 54.749, 41.328]
[54.501, 43.445, 55.437, 30.396]
[60.419, 71.281, 54.235, 43.447]
[60.125, 29.214, 60.125, 71.214]
[60.111, 29.007, 60.111, 29.007]
[58.758, 29.074, 60.087, 28.961]
[66.77, 38.056, 58.701, 29.07]
[55.393, 17.975, 66.743, 38.1]
[59.244, 29.006, 55.335, 17.953]
"""
        p = subprocess.Popen(["python", "search_project.py", "./Data/td2.txt"], stdout=subprocess.PIPE)
        out = p.communicate()

        outputList = out[0].split("\n")
        output = "\n".join(outputList[3 : len(outputList) - 3])
        
        self.assertTrue(output == expected_output)

    def test_tiny_text_2_txt(self):
        expected_output = \
"""[54.796, 41.361, 51.848, 19.414]
[55.396, 30.413, 54.749, 41.328]
[54.501, 43.445, 55.437, 30.396]
[-1.0, -1.0, -1.0, -1.0]
[60.125, 29.214, 60.125, 71.214]
[60.111, 29.007, 60.111, 29.007]
[58.758, 29.074, 60.087, 28.961]
[-1.0, -1.0, -1.0, -1.0]
"""

        p = subprocess.Popen(["python", "search_project.py", "./Data/tiny_test_2.txt"], stdout=subprocess.PIPE)
        out = p.communicate()

        outputList = out[0].split("\n")
        output = "\n".join(outputList[3 : len(outputList) - 3])

        self.assertTrue(output == expected_output)

    def test_tiny_text_3_txt(self):
        expected_output = \
"""[58.758, 29.074, 60.087, 28.961]
[66.77, 38.056, 58.701, 29.07]
[55.393, 17.975, 66.743, 38.1]
[59.244, 29.006, 55.335, 17.953]
[58.303, 36.926, -1.0, 29.058]
[59.743, 32.044, 58.227, 36.987]
[59.526, 29.241, 59.526, 31.965]
[55.105, 19.238, 59.403, 29.239]
"""

        p = subprocess.Popen(["python", "search_project.py", "./Data/tiny_test_3.txt"], stdout=subprocess.PIPE)
        out = p.communicate()

        outputList = out[0].split("\n")
        output = "\n".join(outputList[3 : len(outputList) - 3])

        self.assertTrue(output == expected_output)

    def test_mdata2_txt(self):
        expected_output = \
"""[54.796, 41.361, 51.848, 19.414]
[55.396, 30.413, 54.749, 41.328]
[54.501, 43.445, 55.437, 30.396]
[-1.0, -1.0, -1.0, -1.0]
[60.125, 29.214, 60.125, 71.214]
[60.111, 29.007, 60.111, 29.007]
[58.758, 29.074, 60.087, 28.961]
[66.77, 38.056, 58.701, 29.07]
[55.393, 17.975, 66.743, 38.1]
[59.244, 29.006, 55.335, 17.953]
[-1.0, -1.0, -1.0, -1.0]
"""

        p = subprocess.Popen(["python", "search_project.py", "./Data/mdata2.txt"], stdout=subprocess.PIPE)
        out = p.communicate()

        outputList = out[0].split("\n")
        output = "\n".join(outputList[3 : len(outputList) - 3])

        self.assertTrue(output == expected_output)

    def test_tiny_test_4_txt(self):
        expected_output = \
"""[54.796, 41.361, 51.848, -1.0]
[55.396, 30.413, -1.0, 41.328]
[54.501, 43.445, 55.437, 30.396]
[-1.0, -1.0, -1.0, -1.0]
[60.125, 29.214, 60.125, 71.214]
[60.111, 29.007, 60.111, 29.007]
[58.758, 29.074, 60.087, 28.961]
"""
        
        p = subprocess.Popen(["python", "search_project.py", "./Data/tiny_test_4.txt"], stdout=subprocess.PIPE)
        out = p.communicate()

        outputList = out[0].split("\n")
        output = "\n".join(outputList[3 : len(outputList) - 3])
        
        self.assertTrue(output == expected_output)

    def test_largedata_txt(self):
        expected_output = \
"""[54.796, 41.361, 51.848, 19.414]
[55.396, 30.413, 54.749, 41.328]
[54.501, 43.445, 55.437, 30.396]
[60.419, 71.281, 54.235, 43.447]
[60.125, 29.214, 60.125, 71.214]
[60.111, 29.007, 60.111, 29.007]
[58.758, 29.074, 60.087, 28.961]
[66.770, 38.056, 58.701, 29.070]
[55.393, 17.975, 66.743, 38.100]
[59.244, 29.006, 55.335, 17.953]
[58.303, 36.926, na, 29.058]
[59.743, 32.044, 58.227, 36.987]
[59.526, 29.241, 59.526, 31.965]
[55.105, 19.238, 59.403, 29.239]
[61.947, 40.83, 55.079, 19.304]
[61.690, 63.222, 61.690, 41.111]
[57.045, 41.720, na, na]
[58.428, 39.852, 57.023, 41.822]
[52.631, 39.919, 58.441, 39.915]
[58.427, 32.550, 52.597, 39.994]
[54.411, 41.198, 58.337, 32.591]
[46.830, na, 54.390, 41.141]
[53.766, 41.319, 46.814, na]
[45.945, na, 53.714, 41.339]
[59.853, 73.245, 46.122, na]
[59.346, 41.360, na, na]
[60.573, 70.772, 59.309, 41.478]
[65.249, 67.535, 60.553, 70.685]
[58.394, 32.309, 65.271, 67.334]
[56.120, 29.678, 58.467, 32.380]
[58.654, 41.811, 56.159, 29.866]
[48.21, na, 58.743, 41.978]
[66.186, 68.222, 48.113, na]
[66.357, 31.368, 66.357, 68.277]
[60.381, 31.804, 66.336, 31.356]
[59.247, 30.223, 60.398, 31.882]
[61.657, 62.651, 59.138, 30.218]
[54.478, 42.917, na, na]
[45.779, na, 54.444, 42.922]
[54.043, 30.133, 45.842, na]
"""
        
        p = subprocess.Popen(["python", "search_project.py", "./Data/largedata.txt"], stdout=subprocess.PIPE)
        out = p.communicate()

        outputList = out[0].split("\n")
        output = "\n".join(outputList[3 : len(outputList) - 3])
        
        self.assertTrue(output == expected_output)


suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)

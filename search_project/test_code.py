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
[60.111, 29.007, 60.111, 28.961]
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

#     def test_mdata_txt(self):
#         expected_output = \
# """[54.796, 41.361, 51.848, 19.414]
# [55.396, 30.413,  54.749,  41.328]
# [54.501, 43.445,  55.437,  30.396]
# [60.419, 71.281,  54.235,  43.447]
# [60.125, 29.214,  60.125,  71.214]
# [60.111, 29.007,  60.111,  29.007]
# [58.758, 29.074,  60.087,  28.961]
# [66.770, 38.056,  58.701,  29.070]
# [55.393, 17.975,  66.743,  38.100]
# [59.244, 29.006,  55.335,  17.953]
# [58.303, 36.926, -1.0, 29.058]
# """
#         p = subprocess.Popen(["python", "search_project.py", "./Data/mdata.txt"], stdout=subprocess.PIPE)
#         out = p.communicate()

#         outputList = out[0].split("\n")
#         output = "\n".join(outputList[3 : len(outputList) - 3])

#         self.assertTrue(out == expected_output)

    def test_tiny_test_txt(self):
        expected_output = \
"""[54.796, 41.361, 51.848, 19.414]
[55.396, 30.413, 54.749, 41.328]
[54.501, 43.445, 55.437, 30.396]
[-1.0, -1.0, -1.0, -1.0]
[60.125, 29.214, 60.125, 71.214]
[60.111, 29.007, 60.111, 28.961]
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
[60.111, 29.007, 60.111, 28.961]
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
"""[54.796, 41.361 51.848 19.414]
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
[66.770, 38.056, 58.701, 29.070]
[55.393, 17.975, 66.743, 38.100]
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

#     def test_mdata2_txt(self):
#         expected_output = \
# """[54.796, 41.361, 51.848, 19.414]
# [55.396, 30.413, 54.749, 41.328]
# [54.501, 43.445, 55.437, 30.396]
# [-1.0, -1.0, -1.0, -1.0]
# [60.125, 29.214, 60.125, 71.214]
# [60.111, 29.007, 60.111, 29.007]
# [58.758, 29.074, 60.087, 28.961]
# [66.770, 38.056, 58.701, 29.070]
# 55.393, 17.975, 66.743, 38.100]
# [59.244, 29.006, 55.335, 17.953]
# [-1.0, -1.0, -1.0, -1.0]
# """

#         p = subprocess.Popen(["python", "search_project.py", "./Data/mdata2.txt"], stdout=subprocess.PIPE)
#         out = p.communicate()

#         outputList = out[0].split("\n")
#         output = "\n".join(outputList[3 : len(outputList) - 3])

#         self.assertTrue(output == expected_output)

    def test_tiny_test_4_txt(self):
        expected_output = \
"""[54.796, 41.361  51.848, -1.0]
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


suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)

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
        output = "\n".join(outputList[3 : len(outputList) - 4])
        
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
        output = "\n".join(outputList[3 : len(outputList) - 4])

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
        output = "\n".join(outputList[3 : len(outputList) - 4])

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
        output = "\n".join(outputList[3 : len(outputList) - 4])
        
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
        output = "\n".join(outputList[3 : len(outputList) - 4])

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
        output = "\n".join(outputList[3 : len(outputList) - 4])

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
        output = "\n".join(outputList[3 : len(outputList) - 4])

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
        output = "\n".join(outputList[3 : len(outputList) - 4])
        
        self.assertTrue(output == expected_output)

    def test_test15_txt(self):
        expected_output = \
"""[59.643, -1.0, -1.0, -1.0]
[61.448, 39.737, 59.126, 28.952]
[57.831, 41.071, 61.524, 39.65]
[66.552, 68.425, 57.804, 41.05]
[58.97, 32.706, 66.336, 68.45]
[55.8, 30.97, 58.89, -1.0]
[54.802, 18.041, 55.899, 30.518]
[58.631, 30.288, 54.814, 18.056]
[56.75, 31.77, 58.637, 30.212]
[56.6, 32.976, 56.6, 31.735]
"""
        p = subprocess.Popen(["python", "search_project.py", "./Data/test15.txt"], stdout=subprocess.PIPE)
        out = p.communicate()

        outputList = out[0].split("\n")
        output = "\n".join(outputList[3 : len(outputList) - 4])
        
        self.assertTrue(output == expected_output)

    def test_test14_txt(self):
        expected_output = \
"""[59.756, 72.599, 45.886, -1.0]
[59.812, 41.749, 59.812, 72.339]
[51.886, 41.992, 59.992, 41.58]
[62.934, 36.493, 51.828, 41.97]
[-1.0, -1.0, -1.0, -1.0]
[59.643, -1.0, -1.0, -1.0]
[61.448, 39.737, 59.126, 28.952]
[57.831, 41.071, 61.524, 39.65]
[66.552, 68.425, 57.804, 41.05]
[58.97, 32.706, 66.336, 68.45]
"""
        p = subprocess.Popen(["python", "search_project.py", "./Data/test14.txt"], stdout=subprocess.PIPE)
        out = p.communicate()

        outputList = out[0].split("\n")
        output = "\n".join(outputList[3 : len(outputList) - 4])
        
        self.assertTrue(output == expected_output)

    def test_test13_txt(self):
        expected_output = \
"""[54.659, 18.984, 53.623, 40.766]
[61.69, 63.222, 54.659, 18.984]
[46.829, -1.0, 54.434, 41.016]
[54.227, 39.336, 46.778, -1.0]
[45.912, -1.0, 54.222, 39.538]
[59.756, 72.599, 45.886, -1.0]
[59.812, 41.749, 59.812, 72.339]
[51.886, 41.992, 59.992, 41.58]
[62.934, 36.493, 51.828, 41.97]
[-1.0, -1.0, -1.0, -1.0]
"""
        p = subprocess.Popen(["python", "search_project.py", "./Data/test13.txt"], stdout=subprocess.PIPE)
        out = p.communicate()

        outputList = out[0].split("\n")
        output = "\n".join(outputList[3 : len(outputList) - 4])
        
        self.assertTrue(output == expected_output)

    def test_test12_txt(self):
        expected_output = \
"""[65.384, 38.118, 59.867, 33.967]
[55.41, 38.172, 65.397, 38.172]
[58.437, 30.036, 55.378, 38.176]
[62.466, 32.802, 58.543, 29.995]
[53.559, 40.677, 62.401, 32.726]
[54.659, 18.984, 53.623, 40.766]
[61.69, 63.222, 54.659, 18.984]
[46.829, -1.0, 54.434, 41.016]
[54.227, 39.336, 46.778, -1.0]
[45.912, -1.0, 54.222, 39.538]
"""
        p = subprocess.Popen(["python", "search_project.py", "./Data/test12.txt"], stdout=subprocess.PIPE)
        out = p.communicate()

        outputList = out[0].split("\n")
        output = "\n".join(outputList[3 : len(outputList) - 4])
        
        self.assertTrue(output == expected_output)

    def test_test11_txt(self):
        expected_output = \
"""[58.902, 29.914, 54.964, 18.427]
[58.026, 41.934, 58.871, 30.02]
[58.706, 28.129, 58.08, 41.908]
[57.457, 40.379, 58.647, 28.143]
[59.731, 34.06, 57.412, 40.47]
[65.384, 38.118, 59.867, 33.967]
[55.41, 38.172, 65.397, 38.172]
[58.437, 30.036, 55.378, 38.176]
[62.466, 32.802, 58.543, 29.995]
[53.559, 40.677, 62.401, 32.726]
"""
        p = subprocess.Popen(["python", "search_project.py", "./Data/test11.txt"], stdout=subprocess.PIPE)
        out = p.communicate()

        outputList = out[0].split("\n")
        output = "\n".join(outputList[3 : len(outputList) - 4])
        
        self.assertTrue(output == expected_output)

    def test_test10_txt(self):
        expected_output = \
"""[51.169, 39.341, 54.045, 30.05]
[65.249, 67.535, 60.553, 70.685]
[60.707, 71.103, 65.249, 67.535]
[66.357, 31.368, 60.707, 71.103]
[55.04, 18.306, 66.357, 31.368]
[58.902, 29.914, 54.964, 18.427]
[58.026, 41.934, 58.871, 30.02]
[58.706, 28.129, 58.08, 41.908]
[57.457, 40.379, 58.647, 28.143]
[59.731, 34.06, 57.412, 40.47]
"""
        p = subprocess.Popen(["python", "search_project.py", "./Data/test10.txt"], stdout=subprocess.PIPE)
        out = p.communicate()

        outputList = out[0].split("\n")
        output = "\n".join(outputList[3 : len(outputList) - 4])
        
        self.assertTrue(output == expected_output)

    def test_test9_txt(self):
        expected_output = \
"""[59.247, 30.223, 60.398, 31.882]
[61.657, 62.651, 59.138, 30.218]
[54.478, 42.917, -1.0, -1.0]
[45.779, -1.0, 54.444, 42.922]
[54.043, 30.133, 45.842, -1.0]
[51.169, 39.341, 54.045, 30.05]
[65.249, 67.535, 60.553, 70.685]
[60.707, 71.103, 65.249, 67.535]
[66.357, 31.368, 60.707, 71.103]
[55.04, 18.306, 66.357, 31.368]
"""
        p = subprocess.Popen(["python", "search_project.py", "./Data/test9.txt"], stdout=subprocess.PIPE)
        out = p.communicate()

        outputList = out[0].split("\n")
        output = "\n".join(outputList[3 : len(outputList) - 4])
        
        self.assertTrue(output == expected_output)

    def test_test8_txt(self):
        expected_output = \
"""[58.654, 41.811, 56.159, 29.866]
[48.21, -1.0, 58.743, 41.978]
[66.186, 68.222, 48.113, -1.0]
[66.357, 31.368, 66.357, 68.277]
[60.381, 31.804, 66.336, 31.356]
[59.247, 30.223, 60.398, 31.882]
[61.657, 62.651, 59.138, 30.218]
[54.478, 42.917, -1.0, -1.0]
[45.779, -1.0, 54.444, 42.922]
[54.043, 30.133, 45.842, -1.0]
"""
        p = subprocess.Popen(["python", "search_project.py", "./Data/test8.txt"], stdout=subprocess.PIPE)
        out = p.communicate()

        outputList = out[0].split("\n")
        output = "\n".join(outputList[3 : len(outputList) - 4])
        
        self.assertTrue(output == expected_output)

    def test_test7_txt(self):
        expected_output = \
"""[59.346, 41.36, -1.0, -1.0]
[60.573, 70.772, 59.309, 41.478]
[65.249, 67.535, 60.553, 70.685]
[58.394, 32.309, 65.271, 67.334]
[56.12, 29.678, 58.467, 32.38]
[58.654, 41.811, 56.159, 29.866]
[48.21, -1.0, 58.743, 41.978]
[66.186, 68.222, 48.113, -1.0]
[66.357, 31.368, 66.357, 68.277]
[60.381, 31.804, 66.336, 31.356]
"""
        p = subprocess.Popen(["python", "search_project.py", "./Data/test7.txt"], stdout=subprocess.PIPE)
        out = p.communicate()

        outputList = out[0].split("\n")
        output = "\n".join(outputList[3 : len(outputList) - 4])
        
        self.assertTrue(output == expected_output)

    def test_test6_txt(self):
        expected_output = \
"""[54.411, 41.198, 58.337, 32.591]
[46.83, -1.0, 54.39, 41.141]
[53.766, 41.319, 46.814, -1.0]
[45.945, -1.0, 53.714, 41.339]
[59.853, 73.245, 46.122, -1.0]
[59.346, 41.36, -1.0, -1.0]
[60.573, 70.772, 59.309, 41.478]
[65.249, 67.535, 60.553, 70.685]
[58.394, 32.309, 65.271, 67.334]
[56.12, 29.678, 58.467, 32.38]
"""
        p = subprocess.Popen(["python", "search_project.py", "./Data/test6.txt"], stdout=subprocess.PIPE)
        out = p.communicate()

        outputList = out[0].split("\n")
        output = "\n".join(outputList[3 : len(outputList) - 4])
        
        self.assertTrue(output == expected_output)

    def test_test5_txt(self):
        expected_output = \
"""[61.69, 63.222, 61.69, 41.111]
[57.045, 41.72, -1.0, -1.0]
[58.428, 39.852, 57.023, 41.822]
[52.631, 39.919, 58.441, 39.915]
[58.427, 32.55, 52.597, 39.994]
[54.411, 41.198, 58.337, 32.591]
[46.83, -1.0, 54.39, 41.141]
[53.766, 41.319, 46.814, -1.0]
[45.945, -1.0, 53.714, 41.339]
[59.853, 73.245, 46.122, -1.0]
"""
        p = subprocess.Popen(["python", "search_project.py", "./Data/test5.txt"], stdout=subprocess.PIPE)
        out = p.communicate()

        outputList = out[0].split("\n")
        output = "\n".join(outputList[3 : len(outputList) - 4])
        
        self.assertTrue(output == expected_output)

    def test_test4_txt(self):
        expected_output = \
"""[58.303, 36.926, -1.0, 29.058]
[59.743, 32.044, 58.227, 36.987]
[59.526, 29.241, 59.526, 31.965]
[55.105, 19.238, 59.403, 29.239]
[61.947, 40.83, 55.079, 19.304]
[61.69, 63.222, 61.69, 41.111]
[57.045, 41.72, -1.0, -1.0]
[58.428, 39.852, 57.023, 41.822]
[52.631, 39.919, 58.441, 39.915]
[58.427, 32.55, 52.597, 39.994]
"""
        p = subprocess.Popen(["python", "search_project.py", "./Data/test4.txt"], stdout=subprocess.PIPE)
        out = p.communicate()

        outputList = out[0].split("\n")
        output = "\n".join(outputList[3 : len(outputList) - 4])
        
        self.assertTrue(output == expected_output)

    def test_test3_txt(self):
        expected_output = \
"""[60.111, 29.007, 60.111, 29.007]
[58.758, 29.074, 60.087, 28.961]
[66.77, 38.056, 58.701, 29.07]
[55.393, 17.975, 66.743, 38.1]
[59.244, 29.006, 55.335, 17.953]
[58.303, 36.926, -1.0, 29.058]
[59.743, 32.044, 58.227, 36.987]
[59.526, 29.241, 59.526, 31.965]
[55.105, 19.238, 59.403, 29.239]
[61.947, 40.83, 55.079, 19.304]
"""
        p = subprocess.Popen(["python", "search_project.py", "./Data/test3.txt"], stdout=subprocess.PIPE)
        out = p.communicate()

        outputList = out[0].split("\n")
        output = "\n".join(outputList[3 : len(outputList) - 4])
        
        self.assertTrue(output == expected_output)

    def test_test2_txt(self):
        expected_output = \
"""[58.303, 36.926, -1.0, 29.058]
[59.743, 32.044, 58.227, 36.987]
[59.526, 29.241, 59.526, 31.965]
[55.105, 19.238, 59.403, 29.239]
[61.947, 40.83, 55.079, 19.304]
[61.69, 63.222, 61.69, 41.111]
[57.045, 41.72, -1.0, -1.0]
[58.428, 39.852, 57.023, 41.822]
[52.631, 39.919, 58.441, 39.915]
[58.427, 32.55, 52.597, 39.994]
"""
        p = subprocess.Popen(["python", "search_project.py", "./Data/test2.txt"], stdout=subprocess.PIPE)
        out = p.communicate()

        outputList = out[0].split("\n")
        output = "\n".join(outputList[3 : len(outputList) - 4])
        
        self.assertTrue(output == expected_output)

    def test_test1_txt(self):
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
        p = subprocess.Popen(["python", "search_project.py", "./Data/test1.txt"], stdout=subprocess.PIPE)
        out = p.communicate()

        outputList = out[0].split("\n")
        output = "\n".join(outputList[3 : len(outputList) - 4])

        self.assertTrue(output == expected_output)

    def test_test16_txt(self):
        expected_output = \
"""[55.8, 30.97, 58.89, -1.0]
[54.802, 18.041, 55.899, 30.518]
[58.631, 30.288, 54.814, 18.056]
[56.75, 31.77, 58.637, 30.212]
[56.6, 32.976, 56.6, 31.735]
[56.925, 32.948, 56.589, 32.883]
[54.802, 40.955, 57.011, 32.933]
[62.673, 69.763, 54.828, 41.008]
[54.827, 41.082, 62.763, 69.758]
[59.953, 63.538, 54.824, 41.145]
"""
        p = subprocess.Popen(["python", "search_project.py", "./Data/test16.txt"], stdout=subprocess.PIPE)
        out = p.communicate()

        outputList = out[0].split("\n")
        output = "\n".join(outputList[3 : len(outputList) - 4])
        
        self.assertTrue(output == expected_output)

    def test_test17_txt(self):
        expected_output = \
"""[56.925, 32.948, 56.589, 32.883]
[54.802, 40.955, 57.011, 32.933]
[62.673, 69.763, 54.828, 41.008]
[54.827, 41.082, 62.763, 69.758]
[59.953, 63.538, 54.824, 41.145]
[59.106, 29.384, 59.991, 63.536]
[58.873, 29.193, 59.005, 29.374]
[58.997, 29.351, 58.997, 29.351]
[64.439, 38.179, 58.929, 29.453]
[-1.0, -1.0, -1.0, -1.0]
"""

# Flips these two:
# [58.873, 29.193, 59.005, 29.374]
# [58.997, 29.351, 58.997, 29.351]
        p = subprocess.Popen(["python", "search_project.py", "./Data/test17.txt"], stdout=subprocess.PIPE)
        out = p.communicate()

        outputList = out[0].split("\n")
        output = "\n".join(outputList[3 : len(outputList) - 4])
        
        self.assertTrue(output == expected_output)

    def test_data30_txt(self):
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
[59.743, 32.044, 58.227, 36.987]
[59.526, 29.241, 59.526, 31.965]
[55.105, 19.238, 59.403, 29.239]
[61.947, 40.83, 55.079, 19.304]
[61.69, 63.222, 61.69, 41.111]
[57.045, 41.72, -1.0, -1.0]
[58.428, 39.852, 57.023, 41.822]
[52.631, 39.919, 58.441, 39.915]
[58.427, 32.55, 52.597, 39.994]
[54.411, 41.198, 58.337, 32.591]
[46.83, -1.0, 54.39, 41.141]
[53.766, 41.319, 46.814, -1.0]
[45.945, -1.0, 53.714, 41.339]
[59.853, 73.245, 46.122, -1.0]
[59.346, 41.36, -1.0, -1.0]
[60.573, 70.772, 59.309, 41.478]
[65.249, 67.535, 60.553, 70.685]
[58.394, 32.309, 65.271, 67.334]
[56.12, 29.678, 58.467, 32.38]
[58.654, 41.811, 56.159, 29.866]
"""
        p = subprocess.Popen(["python", "search_project.py", "./Data/data30.txt"], stdout=subprocess.PIPE)
        out = p.communicate()

        outputList = out[0].split("\n")
        output = "\n".join(outputList[3 : len(outputList) - 4])

        self.assertTrue(output == expected_output)

    def test_test18_txt(self):
        expected_output = \
"""[55.299, 42.945, 54.696, 39.212]
[46.219, -1.0, 55.285, 43.018]
[56.379, 29.68, 46.203, -1.0]
[56.977, 32.3, 56.426, 29.689]
[54.244, 44.481, -1.0, -1.0]
[60.811, 71.02, 54.194, 44.271]
[57.743, 40.067, 60.786, 71.089]
[59.742, 29.421, 57.661, -1.0]
[59.127, 30.173, 59.889, -1.0]
[67.088, 32.0, 59.056, 30.128]
"""
        p = subprocess.Popen(["python", "search_project.py", "./Data/test18.txt"], stdout=subprocess.PIPE)
        out = p.communicate()

        outputList = out[0].split("\n")
        output = "\n".join(outputList[3 : len(outputList) - 4])
        
        self.assertTrue(output == expected_output)

    def test_data20_txt(self):
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
[59.743, 32.044, 58.227, 36.987]
[59.526, 29.241, 59.526, 31.965]
[55.105, 19.238, 59.403, 29.239]
[61.947, 40.83, 55.079, 19.304]
[61.69, 63.222, 61.69, 41.111]
[57.045, 41.72, -1.0, -1.0]
[58.428, 39.852, 57.023, 41.822]
[52.631, 39.919, 58.441, 39.915]
[58.427, 32.55, 52.597, 39.994]
"""
        p = subprocess.Popen(["python", "search_project.py", "./Data/data20.txt"], stdout=subprocess.PIPE)
        out = p.communicate()

        outputList = out[0].split("\n")
        output = "\n".join(outputList[3 : len(outputList) - 3])

        self.assertTrue(output == expected_output)

#     def test_largedata_txt(self):
#         expected_output = \
# """[54.796, 41.361, 51.848, 19.414]
# [55.396, 30.413, 54.749, 41.328]
# [54.501, 43.445, 55.437, 30.396]
# [60.419, 71.281, 54.235, 43.447]
# [60.125, 29.214, 60.125, 71.214]
# [60.111, 29.007, 60.111, 29.007]
# [58.758, 29.074, 60.087, 28.961]
# [66.770, 38.056, 58.701, 29.070]
# [55.393, 17.975, 66.743, 38.100]
# [59.244, 29.006, 55.335, 17.953]
# [58.303, 36.926, na, 29.058]
# [59.743, 32.044, 58.227, 36.987]
# [59.526, 29.241, 59.526, 31.965]
# [55.105, 19.238, 59.403, 29.239]
# [61.947, 40.83, 55.079, 19.304]
# [61.690, 63.222, 61.690, 41.111]
# [57.045, 41.720, na, na]
# [58.428, 39.852, 57.023, 41.822]
# [52.631, 39.919, 58.441, 39.915]
# [58.427, 32.550, 52.597, 39.994]
# [54.411, 41.198, 58.337, 32.591]
# [46.830, na, 54.390, 41.141]
# [53.766, 41.319, 46.814, na]
# [45.945, na, 53.714, 41.339]
# [59.853, 73.245, 46.122, na]
# [59.346, 41.360, na, na]
# [60.573, 70.772, 59.309, 41.478]
# [65.249, 67.535, 60.553, 70.685]
# [58.394, 32.309, 65.271, 67.334]
# [56.120, 29.678, 58.467, 32.380]
# [58.654, 41.811, 56.159, 29.866]
# [48.21, na, 58.743, 41.978]
# [66.186, 68.222, 48.113, na]
# [66.357, 31.368, 66.357, 68.277]
# [60.381, 31.804, 66.336, 31.356]
# [59.247, 30.223, 60.398, 31.882]
# [61.657, 62.651, 59.138, 30.218]
# [54.478, 42.917, na, na]
# [45.779, na, 54.444, 42.922]
# [54.043, 30.133, 45.842, na]
# """
        
#         p = subprocess.Popen(["python", "search_project.py", "./Data/largedata.txt"], stdout=subprocess.PIPE)
#         out = p.communicate()

#         outputList = out[0].split("\n")
#         output = "\n".join(outputList[3 : len(outputList) - 4])
        
#         self.assertTrue(output == expected_output)

#     def test_data40_txt(self):
#         expected_output = \
# """[54.796, 41.361, 51.848, 19.414]
# [55.396, 30.413, 54.749, 41.328]
# [54.501, 43.445, 55.437, 30.396]
# [60.419, 71.281, 54.235, 43.447]
# [60.125, 29.214, 60.125, 71.214]
# [60.111, 29.007, 60.111, 29.007]
# [58.758, 29.074, 60.087, 28.961]
# [66.77, 38.056, 58.701, 29.07]
# [55.393, 17.975, 66.743, 38.1]
# [59.244, 29.006, 55.335, 17.953]
# [58.303, 36.926, -1.0, 29.058]
# [59.743, 32.044, 58.227, 36.987]
# [59.526, 29.241, 59.526, 31.965]
# [55.105, 19.238, 59.403, 29.239]
# [61.947, 40.83, 55.079, 19.304]
# [61.69, 63.222, 61.69, 41.111]
# [57.045, 41.72, -1.0, -1.0]
# [58.428, 39.852, 57.023, 41.822]
# [52.631, 39.919, 58.441, 39.915]
# [58.427, 32.55, 52.597, 39.994]
# [54.411, 41.198, 58.337, 32.591]
# [46.83, -1.0, 54.39, 41.141]
# [53.766, 41.319, 46.814, -1.0]
# [45.945, -1.0, 53.714, 41.339]
# [59.853, 73.245, 46.122, -1.0]
# [59.346, 41.36, -1.0, -1.0]
# [60.573, 70.772, 59.309, 41.478]
# [65.249, 67.535, 60.553, 70.685]
# [58.394, 32.309, 65.271, 67.334]
# [56.12, 29.678, 58.467, 32.38]
# [58.654, 41.811, 56.159, 29.866]
# [48.21, -1.0, 58.743, 41.978]
# [66.186, 68.222, 48.113, -1.0]
# [66.357, 31.368, 66.357, 68.277]
# [60.381, 31.804, 66.336, 31.356]
# [59.247, 30.223, 60.398, 31.882]
# [61.657, 62.651, 59.138, 30.218]
# [54.478, 42.917, -1.0, -1.0]
# [45.779, -1.0, 54.444, 42.922]
# [54.043, 30.133, 45.842, -1.0]
# [51.169, 39.341, 54.045, 30.05]
# """
#         p = subprocess.Popen(["python", "search_project.py", "./Data/data40.txt"], stdout=subprocess.PIPE)
#         out = p.communicate()

#         outputList = out[0].split("\n")
#         output = "\n".join(outputList[3 : len(outputList) - 4])

#         self.assertTrue(output == expected_output)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)

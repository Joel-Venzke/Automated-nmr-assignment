import unittest
import subprocess
import re

def getExpectedOutput(filename):
    p = subprocess.Popen(["perl", "dataformatscript.pl", "./Data/"+filename], stdout=subprocess.PIPE)
    out = p.communicate()
    expected_output = "\n".join(out[0].split("\n"))
    return expected_output

def getOutput(filename):
    p = subprocess.Popen(["python", "search_project.py", "./Data/"+filename], stdout=subprocess.PIPE)
    out = p.communicate()
    outputList = out[0].split("\n")
    output = "\n".join(outputList[3 : len(outputList) - 5])
    return output

class TestSequenceFunctions(unittest.TestCase):

    def test_testdata_txt(self):
        self.assertTrue(getOutput("testdata.txt") == getExpectedOutput("testdata.txt"))

    def test_mdata_txt(self):
        self.assertTrue(getOutput("mdata.txt") == getExpectedOutput("mdata.txt"))

    def test_mdata2_txt(self):
        self.assertTrue(getOutput("mdata2.txt") == getExpectedOutput("mdata2.txt"))

    def test_td2_txt(self):
        self.assertTrue(getOutput("td2.txt") == getExpectedOutput("td2.txt"))

    def test_tiny_test_txt(self):
        self.assertTrue(getOutput("tiny_test.txt") == getExpectedOutput("tiny_test.txt"))

    def test_tiny_text_2_txt(self):
        self.assertTrue(getOutput("tiny_test_2.txt") == getExpectedOutput("tiny_test_2.txt"))
    
    def test_tiny_text_3_txt(self):
        self.assertTrue(getOutput("tiny_test_3.txt") == getExpectedOutput("tiny_test_3.txt"))

    def test_tiny_test_4_txt(self):
        self.assertTrue(getOutput("tiny_test_4.txt") == getExpectedOutput("tiny_test_4.txt"))

    def test_test1_txt(self):
        self.assertTrue(getOutput("test1.txt") == getExpectedOutput("test1.txt"))
    
    def test_test2_txt(self):
        self.assertTrue(getOutput("test2.txt") == getExpectedOutput("test2.txt"))   
    
    def test_test3_txt(self):
        self.assertTrue(getOutput("test3.txt") == getExpectedOutput("test3.txt"))
    
    def test_test4_txt(self):
        self.assertTrue(getOutput("test4.txt") == getExpectedOutput("test4.txt"))
    
    def test_test5_txt(self):
        self.assertTrue(getOutput("test5.txt") == getExpectedOutput("test5.txt"))
    
    def test_test6_txt(self):
        self.assertTrue(getOutput("test6.txt") == getExpectedOutput("test6.txt"))
    
    def test_test7_txt(self):
        self.assertTrue(getOutput("test7.txt") == getExpectedOutput("test7.txt"))
    
    def test_test8_txt(self):
        self.assertTrue(getOutput("test8.txt") == getExpectedOutput("test8.txt"))
    
    def test_test9_txt(self):
        self.assertTrue(getOutput("test9.txt") == getExpectedOutput("test9.txt"))
    
    def test_test10_txt(self):
        self.assertTrue(getOutput("test10.txt") == getExpectedOutput("test10.txt"))
    
    def test_test11_txt(self):
        self.assertTrue(getOutput("test11.txt") == getExpectedOutput("test11.txt"))
    
    def test_test12_txt(self):
        self.assertTrue(getOutput("test12.txt") == getExpectedOutput("test12.txt"))
    
    def test_test13_txt(self):
        self.assertTrue(getOutput("test13.txt") == getExpectedOutput("test13.txt"))

    def test_test14_txt(self):
        self.assertTrue(getOutput("test14.txt") == getExpectedOutput("test14.txt"))

    def test_test15_txt(self):
        self.assertTrue(getOutput("test15.txt") == getExpectedOutput("test15.txt"))

    def test_test16_txt(self):
        self.assertTrue(getOutput("test16.txt") == getExpectedOutput("test16.txt"))

    def test_test17_txt(self):
        self.assertTrue(getOutput("test17.txt") == getExpectedOutput("test17.txt"))

    def test_test18_txt(self):
        self.assertTrue(getOutput("test18.txt") == getExpectedOutput("test18.txt"))

    def test_data11_txt(self):
        self.assertTrue(getOutput("data11.txt") == getExpectedOutput("data11.txt"))

    def test_data12_txt(self):
        self.assertTrue(getOutput("data12.txt") == getExpectedOutput("data12.txt"))

    def test_data13_txt(self):
        self.assertTrue(getOutput("data13.txt") == getExpectedOutput("data13.txt"))

    def test_data14_txt(self):
        self.assertTrue(getOutput("data14.txt") == getExpectedOutput("data14.txt"))

    def test_data15_txt(self):
        self.assertTrue(getOutput("data15.txt") == getExpectedOutput("data15.txt"))

    def test_data16_txt(self):
        self.assertTrue(getOutput("data16.txt") == getExpectedOutput("data16.txt"))

    def test_data17_txt(self):
        self.assertTrue(getOutput("data17.txt") == getExpectedOutput("data17.txt"))

    def test_data18_txt(self):
        self.assertTrue(getOutput("data18.txt") == getExpectedOutput("data18.txt"))

    def test_data19_txt(self):
        self.assertTrue(getOutput("data19.txt") == getExpectedOutput("data19.txt"))

    def test_data20_txt(self):
        self.assertTrue(getOutput("data20.txt") == getExpectedOutput("data20.txt"))

    def test_data21_txt(self):
        self.assertTrue(getOutput("data21.txt") == getExpectedOutput("data21.txt"))

    def test_data22_txt(self):
        self.assertTrue(getOutput("data22.txt") == getExpectedOutput("data22.txt"))

    def test_data23_txt(self):
        self.assertTrue(getOutput("data23.txt") == getExpectedOutput("data23.txt"))

    def test_data24_txt(self):
        self.assertTrue(getOutput("data24.txt") == getExpectedOutput("data24.txt"))

    def test_data25_txt(self):
        self.assertTrue(getOutput("data25.txt") == getExpectedOutput("data25.txt"))

    def test_data26_txt(self):
        self.assertTrue(getOutput("data26.txt") == getExpectedOutput("data26.txt"))

    def test_data27_txt(self):
        self.assertTrue(getOutput("data27.txt") == getExpectedOutput("data27.txt"))

    def test_data28_txt(self):
        self.assertTrue(getOutput("data28.txt") == getExpectedOutput("data28.txt"))

    def test_data29_txt(self):
        self.assertTrue(getOutput("data29.txt") == getExpectedOutput("data29.txt"))

    def test_data30_txt(self):
        self.assertTrue(getOutput("data30.txt") == getExpectedOutput("data30.txt"))

    def test_data31_txt(self):
        self.assertTrue(getOutput("data31.txt") == getExpectedOutput("data31.txt"))

    def test_data32_txt(self):
        self.assertTrue(getOutput("data32.txt") == getExpectedOutput("data32.txt"))

    def test_data33_txt(self):
        self.assertTrue(getOutput("data33.txt") == getExpectedOutput("data33.txt"))

    def test_data34_txt(self):
        self.assertTrue(getOutput("data34.txt") == getExpectedOutput("data34.txt"))

    def test_data35_txt(self):
        self.assertTrue(getOutput("data35.txt") == getExpectedOutput("data35.txt"))

    # def test_data36_txt(self):
    #     self.assertTrue(getOutput("data36.txt") == getExpectedOutput("data36.txt"))

    # def test_data37_txt(self):
    #     self.assertTrue(getOutput("data37.txt") == getExpectedOutput("data37.txt"))

    # def test_data38_txt(self):
    #     self.assertTrue(getOutput("data38.txt") == getExpectedOutput("data38.txt"))

    # def test_data39_txt(self):
    #     self.assertTrue(getOutput("data39.txt") == getExpectedOutput("data39.txt"))

    # def test_data40_txt(self):
    #     self.assertTrue(getOutput("data40.txt") == getExpectedOutput("data40.txt"))

    # def test_data41_txt(self):
    #     self.assertTrue(getOutput("data41.txt") == getExpectedOutput("data41.txt"))

suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)
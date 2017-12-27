
from SVM_test import start_test_SVM


test_result = []
for i in range(1, 15, 2):
    for j in range(20, 90, 20):
        print("start_test_SVM(i=", i,", j=", j,")")
        test_result.append( [i, j, start_test_SVM(i, j)])
        print("------------------------")
print(test_result)


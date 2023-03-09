import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm
from sklearn import metrics
from sklearn.model_selection import train_test_split

total_correct_predictions = 0
total_incorrect_predictions = 0

digits = datasets.load_digits()

n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))
clf = svm.SVC(gamma=0.001, C=100)



#random verdelen
X_train, X_test, Y_train, Y_test = train_test_split(data, digits.target, test_size=0.3333333333, shuffle=True)

# Learn the digits on the train subset
clf.fit(X_train, Y_train)



prediction = clf.predict(X_test)



for i in range(len(Y_test)):
    if prediction[i] == Y_test[i]:
        total_correct_predictions += 1
    else:
        total_incorrect_predictions += 1

accuracy = (total_correct_predictions/(total_correct_predictions+total_incorrect_predictions))*100

print("Accuracy:", accuracy)
print("amount of files in test", len(X_test))
print("amount of files in train", len(X_train))
print("total amount of files", len(X_test) + len(X_train) )


plt.imshow(digits.images[-4], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()

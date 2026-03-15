
from sklearn.tree import DecisionTreeClassifier

X = [[1], [2], [3], [4], [5], [6]]
y = [0, 1, 0, 1, 0, 1]

model = DecisionTreeClassifier()
model.fit(X, y)

num = int(input("Enter a number: "))
prediction = model.predict([[num]])

if prediction == 1:
    print("Even Number")
else:
    print("Odd Number")
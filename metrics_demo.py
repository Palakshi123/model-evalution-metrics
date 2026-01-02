# metrics_demo.py
# Simple demo of ML evaluation metrics using scikit-learn
# Focus: Fraud vs Not-Fraud intuition

# 1. Import libraries
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

# 2. Create a synthetic fraud dataset (fraud is rare)
X, y = make_classification(
    n_samples=2000,
    n_features=10,
    n_informative=5,
    weights=[0.95, 0.05],   # 5% fraud
    random_state=42
)

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# 4. Train a simple model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 5. Make predictions
y_pred = model.predict(X_test)

# 6. Calculate metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

# 7. Print results with simple explanations
print("\nFraud Detection Metrics (Fraud = 1, Not Fraud = 0)\n")

print("Confusion Matrix:")
print(cm)

print("\nMetrics:")
print(f"Accuracy  : {accuracy:.2f}  -> Overall correctness (can be misleading for fraud)")
print(f"Precision : {precision:.2f}  -> When we say 'fraud', how often we are right")
print(f"Recall    : {recall:.2f}  -> Out of all fraud cases, how many we catch")
print(f"F1 Score  : {f1:.2f}  -> Balance between precision and recall")

print("\nSimple takeaway:")
print("- High precision means fewer normal users are flagged as fraud")
print("- High recall means fewer fraud cases are missed")
print("- Accuracy alone is not enough when fraud is rare")

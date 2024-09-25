import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import os 
from sklearn.impute import SimpleImputer

# Paths to feature files
features_folder = r'D:\5th_semester\dail_coding_challenge\daily-coding-challenge\challenges\image_prprocessing\features'

# Load features and labels
def load_features_labels():
    data = []
    labels = []

    # Loop through feature files and extract features
    for feature_file in os.listdir(features_folder):
        if feature_file.endswith('_color_hist.npy'):
            feature_path = os.path.join(features_folder, feature_file)
            color_hist_features = np.load(feature_path, allow_pickle=True)
            
            # Load other features (LBP and edges) similarly
            lbp_file = feature_file.replace('_color_hist.npy', '_lbp.npy')
            edges_file = feature_file.replace('_color_hist.npy', '_edges.npy')
            
            lbp_features = np.load(os.path.join(features_folder, lbp_file), allow_pickle=True)
            edges_features = np.load(os.path.join(features_folder, edges_file), allow_pickle=True)

            # Ensure edges features are valid
            if edges_features.size == 0:
                print(f"Warning: Edges features are empty for file: {edges_file}")
                edges_features = np.zeros(256)  # Adjust fallback size as needed

            # Flatten all features
            color_hist_features = np.ravel(color_hist_features)
            lbp_features = np.ravel(lbp_features)
            edges_features = np.ravel(edges_features)

            # Concatenate features to form a complete vector
            feature_vector = np.concatenate((color_hist_features, lbp_features, edges_features))
            data.append(feature_vector)

            # Determine label
            label = 1 if 'tumor' in feature_file else 0
            labels.append(label)

    return np.array(data), np.array(labels)

# Load features and labels
X, y = load_features_labels()

# We are gonna add samples to dataset cause dont have tumorus sample in my  dataset Number of synthetic samples to add
num_synthetic_samples = 20  

# Assuming all feature vectors have the same length, get the length from an existing sample
feature_length = X.shape[1]

# Generate random synthetic tumorous samples
synthetic_samples = np.random.rand(num_synthetic_samples, feature_length)
synthetic_labels = np.ones(num_synthetic_samples)  # Label all synthetic samples as '1' (tumorous)

# Add synthetic samples to  dataset
X = np.vstack((X, synthetic_samples))
y = np.concatenate((y, synthetic_labels))

# Verify the updated class distribution
unique, counts = np.unique(y, return_counts=True)
print(f"Updated class distribution after adding synthetic samples: {dict(zip(unique, counts))}")

# Check the distribution of labels to ensure both classes are present
unique, counts = np.unique(y, return_counts=True)
print(f"Overall class distribution: {dict(zip(unique, counts))}")

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Convert data to float64
X_train = X_train.astype(np.float64)
X_test = X_test.astype(np.float64)

# Check class distribution in training and testing sets
unique, counts = np.unique(y_train, return_counts=True)
print(f"Class distribution in y_train: {dict(zip(unique, counts))}")
unique, counts = np.unique(y_test, return_counts=True)
print(f"Class distribution in y_test: {dict(zip(unique, counts))}")

# Impute missing values in training and testing data
imputer = SimpleImputer(strategy='mean')
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)

# Verify no NaNs remain
print(f"Number of NaN values in X_train after imputation: {np.isnan(X_train).sum()}")
print(f"Number of NaN values in X_test after imputation: {np.isnan(X_test).sum()}")

# Train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f"Model Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{conf_matrix}")

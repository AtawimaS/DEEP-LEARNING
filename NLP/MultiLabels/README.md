# Multilabel Classification Project

## Description
This project aims to build a multilabel classification model using a dataset obtained from Kaggle. This dataset includes the necessary data to train the model for classifying text into various label categories

## Dataset
The dataset used in this project is:
- **Title**: Multilabel Classification Dataset
- **Source**: [Kaggle](https://www.kaggle.com/datasets/shivanandmn/multilabel-classification-dataset/code)

### Dataset Structure
- `train.csv`: This file contains training data with the corresponding features and labels.
- `test.csv`: This file contains testing data that will be used to evaluate the model after training.

## How to Use the Dataset
1. **Download the Dataset**:
   You can download the dataset from Kaggle using the link above. Make sure to sign up on Kaggle if you haven't done so.

2. **Import the Dataset**:
   After downloading, you can load the dataset into your project using pandas:

   ```python
   import pandas as pd

   train = pd.read_csv('path/to/train.csv')
   test = pd.read_csv('path/to/test.csv')

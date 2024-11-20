This repository contains the implementation of a Fake News Detection model. The model uses deep learning techniques, including FastText supervised word classification and a CNN-LSTM hybrid model. The model achieves an accuracy of 91% and an F1-score of 91%.
Project Overview;-
This project aims to develop a robust model for detecting fake news from a given text. The model uses a hybrid architecture combining FastText for supervised word classification and CNN-LSTM for text classification. The key components of the project include data preprocessing, feature extraction, and model evaluation.

Dataset: WELFake Dataset.
The dataset used for this project is the WELFake dataset, which consists of news articles with labeled information regarding whether the news is fake or real.

Model Description
1. Preprocessing Steps
2. FastText Supervised Word Classification
3. FastText was applied to the dataset for supervised word classification to learn word representations efficiently.
4. The embeddings produced by FastText were used as input to the CNN-LSTM model.


Results
The model achieved the following performance metrics:

Accuracy: 91%
F1-Score: 91%
These results demonstrate the effectiveness of combining FastText word embeddings with CNN-LSTM architecture for fake news detection.

To run the project, follow these steps:

Clone the repository:

Copy code
  https://github.com/anilkrmandal/FakeNewsDetecctor.git
  cd FakeNewsDetecctor
open the .ipynb file in colab/jupyter/vs code 
and run all

Our Experiments:-

We experimented with various models to evaluate their accuracy and identify areas for improvement.

For the unsupervised fasttext model, we integrated LDA with an attention mechanism and incorporated LIME, achieving an accuracy of 93%.

In the machine learning models with LIME:

LDA gave us a coherence score of 0.38 and a perplexity of -8.7078.
Random Forest: Precision 0.9302, Recall 0.9358, F1-score 0.9330.
SVM: Precision 0.9064, Recall 0.8992, F1-score 0.9028.
Decision Tree: Precision 0.8565, Recall 0.8794, F1-score 0.8678.
Logistic Regression: Precision 0.9040, Recall 0.9008, F1-score 0.9024.
Ensemble Model: Accuracy 0.9092, Precision 0.9349, Recall 0.8829, F1-score 0.9082.
AdaBoost: Accuracy 0.8677, Precision 0.8750, Recall 0.8633, F1-score 0.8691.

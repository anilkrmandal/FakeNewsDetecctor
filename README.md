Usage
Load the Dataset: The dataset should be in CSV format. Place your dataset file in the appropriate directory and update the file path in the code.

Preprocess the Data: The data is cleaned and prepared for training, including removing null values, stopwords, and special characters.

Train the FastText Model: The FastText model is trained on the preprocessed text data to create word embeddings.

Create FastText Embeddings: Convert the cleaned text data into embeddings that can be used for training the CNN-LSTM model.

Train the CNN-LSTM Model: The model is defined and trained using the generated embeddings.

Evaluate the Model: The model's performance is evaluated on the test set, and results are visualized.

Data Preprocessing
The data preprocessing steps include:
Loading the dataset using Pandas.
Handling missing values by filling them with empty strings.
Tokenization and removal of stopwords using NLTK.
Text normalization, including lowercasing and removal of non-essential characters.
Lemmatization of tokens.
Splitting the dataset into training and testing sets.

Model Training
The model training process involves the following steps:
Training a FastText model in unsupervised mode on the cleaned training data.
Generating FastText embeddings for both the training and testing sets.
Reshaping the embeddings for input into the CNN-LSTM model.
Defining the CNN-LSTM architecture and training the model with early stopping and learning rate scheduling.

Results
The results include:
Model accuracy and loss curves during training and validation.
A confusion matrix visualizing the model's predictions.
A classification report providing precision, recall, and F1-score for each class.

Example Output
Test Loss: 0.2891
Test Accuracy: 0.8891

Acknowledgments
FastText for word embeddings.
TensorFlow for deep learning framework.
NLTK for natural language processing tools.
The dataset used in this project.

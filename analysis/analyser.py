# -*- coding: utf-8 -*-

import sys
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split


class Analyser(object):

    dataset = None
    x_train = None
    x_test = None
    y_train = None
    y_test = None
    pipeline = None

    def train(self, data_folder):

        # Getting training data
        self.dataset = load_files(data_folder)

        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(
            self.dataset.data, self.dataset.target, test_size=0.5)

        # Tokenizing text
        count_vect = CountVectorizer()
        X_train_counts = count_vect.fit_transform(self.x_train)

        # Getting term frequences
        tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
        X_train_tf = tf_transformer.transform(X_train_counts)

        # Training a classifier
        self.pipeline = Pipeline([
            ('vect', CountVectorizer()),
            ('tfidf', TfidfTransformer()),
            ('clf', SGDClassifier(loss='hinge', penalty='l2',
                                alpha=1e-3, random_state=42,
                                max_iter=5, tol=None)),
        ])

        self.pipeline.fit(self.x_train, self.y_train)     
        return True


    def predict(self, item):
        predicted = self.pipeline.predict([item])
        return self.dataset.target_names[predicted[0]]


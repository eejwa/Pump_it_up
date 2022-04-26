#!/usr/bin/env python

## define a function for testing a classifier and a keras NN
from sklearn.model_selection import cross_val_score, cross_validate
from sklearn import metrics
# going to use a wrapper to allow a keras nn to be used with cross_val_score()
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

def test_classifier(classifier, train, labels, cross_val=True):
    classifier.fit(train, labels)
    predicted_labels = classifier.predict(train)
    label_names = ['functional', 'non functional', 'functional needs repair']
    precision = metrics.precision_score(labels, predicted_labels, average=None, labels = label_names)
    recall = metrics.recall_score(labels, predicted_labels, average=None, labels = label_names)
    print("Accuracy:", metrics.accuracy_score(labels, predicted_labels))
    print("Precision:", precision)
    print("Recall:", recall)

    ## plot the precision and recall for the different classes

    fig = plt.figure(figsize=(8,12))
    pos = np.arange(len(label_names))
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    
    ax1.bar(pos, precision, align='center', tick_label=label_names, linewidth=1)
    ax2.bar(pos, recall, align='center', tick_label=label_names, linewidth=1)

    # ax1.set_xticks(pos, labels = label_names)
    # ax2.set_xticks(pos, labels = label_names)
    ax1.set_ylabel('Precision')
    ax2.set_ylabel('Recall')
    
    plt.show()
    


    if cross_val == True:

        # more challenging than expected to get recall and precision to play nicely with cross_validate()
        # scores = cross_validate(classifier, train, labels,
        #                          scoring=["accuracy", metrics.precision_score(average=None), metrics.recall_score(average=None)], cv=10) 
        scores = cross_val_score(classifier, train, labels,
                                     scoring='accuracy', cv=10) 

        print(f"mean cross validation accuracy: ", np.mean(scores), '+/-', np.std(scores))

        

        # for metric in ['accuracy', 'precision', 'recall']:
        #     scores = cross_val_score(classifier, train, labels,
        #                              scoring=metric, cv=10) 
                                 
        #     # print(f"cross validation {metric}: ", scores)
        #     print(f"mean {metric}: ", np.mean(scores), '+/-', np.std(scores))


    else:
        pass

def test_NN(model, train, labels, cross_val=True, epochs=20, val_split=0.2):

    model.fit(train, labels, epochs=epochs, validation_split=val_split)
    # gives us a probability of each of the labels being true!
    predicted_labels = model.predict(train)
    predicted_labels_bool = np.argmax(predicted_labels, axis=1)
    labels_bool = np.argmax(labels, axis=1)
    print(predicted_labels_bool)
    print(labels_bool)
    print("Accuracy:", metrics.accuracy_score(labels_bool, predicted_labels_bool))
    print("Precision:", metrics.precision_score(labels_bool, predicted_labels_bool, average=None))
    print("Recall:", metrics.recall_score(labels_bool, predicted_labels_bool, average=None))
    
    # if cross_val == True:
    #     nn_classifier = KerasClassifier(model=model, epochs=epochs, validation_split=val_split)
        
    #     scores = cross_val_score(nn_classifier, train, labels,
    #                                 scoring="accuracy", cv=10) 
        
    #     # print('cross validation scores: ', scores)
    #     print(f"mean cross validation accuracy: ", np.mean(scores), '+/-', np.std(scores))
            
    # else:
    #     pass
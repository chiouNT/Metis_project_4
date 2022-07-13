from sklearn import metrics
from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np



def makeROCPlot(inputX, inputY, model_name, plot=True):
    fpr, tpr, thresholds=metrics.roc_curve(inputY, model_name.predict_proba(inputX)[:,1])
    auc_score = metrics.roc_auc_score(inputY, model_name.predict_proba(inputX)[:,1])
    
    if plot == True:
        plt.plot([0,1], [0,1], linestyle='--', label='No Skill')
        plt.plot(fpr, tpr, lw=2, label = '{0} (ROC AUC score : {1:.2f})'.format(model_name, auc_score))
        
        plt.xlim([-0.05,1.05])
        plt.ylim([-0.05,1.05])
        
        plt.xlabel('False positive rate')
        plt.ylabel('True positive rate')
        
        plt.title('ROC curve for ClinVar variant classification')
        plt.legend(loc="upper left")
        
        plt.show()
    
    return (fpr, tpr)
    
def makeCombinedROC(tuples, model_names):
    for i , data in enumerate(tuples):
        plt.plot(data[0], data[1], label ='{}'.format(model_names[i]))
            # axis labels
    plt.plot([0,1], [0,1], linestyle='--', label='No Skill')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curves for Test Data')
    plt.legend(bbox_to_anchor=(1.05, 0), loc='lower left')
    
    plt.show()


def makeScorePlot(inputX, inputY, model_name, plot=True):
    thresh_ps = np.linspace(.10,.50,1000)
    model_val_probs = model_name.predict_proba(inputX)[:,1] 
    
    f1_scores, prec_scores, rec_scores, acc_scores = [], [], [], []
    
    for p in thresh_ps:
        model_val_labels = model_val_probs >= p
        f1_scores.append(f1_score(inputY, model_val_labels))    
        prec_scores.append(precision_score(inputY, model_val_labels))
        rec_scores.append(recall_score(inputY, model_val_labels))
        acc_scores.append(accuracy_score(inputY, model_val_labels))
    
    best_f1_score = np.max(f1_scores) 
    best_thresh_p = thresh_ps[np.argmax(f1_scores)]
    
    if plot == True:
        plt.plot(thresh_ps, f1_scores, label = "F1")
        plt.plot(thresh_ps, prec_scores, label = "Precision")
        plt.plot(thresh_ps, rec_scores, label = "Recall")
        plt.plot(thresh_ps, acc_scores, label = "Accuracy")
        
        plt.title('{}'.format(model_name))
        plt.xlabel('P threshold')
        plt.ylabel('Metric score')
        
        plt.axvline(x=best_thresh_p, linestyle='--', label='best F1 score {:.1f}'.format(best_f1_score))
        plt.legend(loc='upper right')
        
        plt.show()
        
        print('{} best F1 score {:.3f} at prob decision threshold >= {:.3f}'.format(model_name,best_f1_score, best_thresh_p))
    
    return (thresh_ps, f1_scores, prec_scores, rec_scores, acc_scores, best_f1_score, best_thresh_p)
    

def makeCombinedScore(tuples, model_names):
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 12))

    for data , ax, i in zip(tuples, axs.ravel(), range(4)):
        ax.plot(data[0], data[1], label = "F1")
        ax.plot(data[0], data[2], label = "Precision")
        ax.plot(data[0], data[3], label = "Recall")
        ax.plot(data[0], data[4], label = "Accuracy")
        ax.axvline(x=data[6], linestyle='--', label='best F1 score {:.2f}'.format(data[5]))

        ax.set_xlabel('P threshold')
        ax.set_ylabel('Metric score')
        
        ax.set_title('{}'.format(model_names[i]))
        ax.legend(loc='upper right')
        
        fig.show()



    

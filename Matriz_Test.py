from sklearn.metrics import confusion_matrix
import seaborn as sn
import matplotlib.pyplot as plt
import pandas as pd

y_actu = [2, 0, 2, 2, 0, 1, 1, 2, 2, 0, 1, 2]
y_pred = [0, 0, 2, 1, 0, 2, 1, 0, 2, 0, 2, 2]

cm=confusion_matrix(y_actu, y_pred)
print(cm)
resultado = pd.DataFrame(cm, index= ['Fresh Apple','Fresh Banana','Fresh Orange'],columns = ['Fresh Apple','Fresh Banana','Fresh Orange'])
#fig = plt.figure(figsize= (6,6))
#ax = fig.add_subplot(1,1,1)
sn.heatmap(resultado, annot=True, linewidths=1, linecolor= 'white', cmap="Reds")
font= {'family': 'serif',
     'color': 'darkred',
    'weight': 'normal',
    'size':6}
ax.set_title("Matrix de confusion ",fontdict ={'family': 'serif','color': 'black','weight': 'normal','size':7})
ax.set_ylabel("Preditec Label", labelpad=6, fontdict={'family': 'serif','color': 'black','weight': 'normal','size':7})
ax.set_xlabel("True Label", labelpad=6, fontdict={'family': 'serif','color': 'black','weight': 'normal','size':7})
plt.show()

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


matplotlib.rcParams['figure.figsize'] = (16.0, 9.0)
script=open("spec.txt").read()
stopwords=set(STOPWORDS)
bond=np.array(Image.open("images.jpg"))

from matplotlib.colors import LinearSegmentedColormap as lsc
colors=["#000000","#0060A8","#484848","#FFF200"]
cmap=lsc.from_list("mycmap",colors)
wc=WordCloud(background_color="white",stopwords=stopwords,mask=bond,width=1987,height=787,colormap=cmap)
wc.generate(script)
plt.figure()
plt.imshow(wc,interpolation="bilinear")
plt.axis("off")
plt.show()
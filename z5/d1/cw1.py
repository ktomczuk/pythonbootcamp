
Napisz poniżej funkcję, która wyprintuje Twoje imię i nazwisko:





In [7]:


























def printowanie():
    print('Kamil Tomczuk')

printowanie()









Kamil Tomczuk



































Indeksowanie, wycinanie, iterowanie - Indexing, Slicing and Iterating
































Stwórz liste sześcianów liczb od 0 do 9





In [14]:






np.arange(10)


















import numpy as np
a = [0, 1 ,2, 3, 4, 5, 6, 7, 8, 9]
b = np.array(a)
d = np.arange(10)
c = d ** 3
print(b)
print(d)
print(c)

[0 1 2 3 4 5 6 7 8 9]
[0 1 2 3 4 5 6 7 8 9]
[0   1   8  27  64 125 216 343 512 729]

wybierz
z
listy
zaznaczone
elementy

[0, 1, 8 *, *27, 64, 125, 216, 343, 512, 729]

In[16]:

import numpy as np

d = np.arange(10)
c = d ** 3
c[2:5]

Out[16]:

array([8, 27, 64], dtype=int32)

[0 *, 1, *8, 27, 64, 125, 216, 343, 512, 729]

In[22]:

c[0:5:2]

c[0:5:2]

Out[22]:

array([0, 8, 64], dtype=int32)

przekształć
by
otrzymać
wynik

[-1000, 1, -1000, 27, -1000, 125, 216, 343, 512, 729]

In[23]:

c

c[0:5:2] = -1000
c

Out[23]:

array([-1000, 1, -1000, 27, -1000, 125, 216, 343, 512,
       729], dtype=int32)

Odwróć
listę

In[24]:

c[::-1]

Out[24]:

array([729, 512, 343, 216, 125, -1000, 27, -1000, 1,
       -1000], dtype=int32)

Sprawdź
typ

In[32]:

c.shape

type(c)
c.dtype
c.size
c.shape

Out[32]:

(10,)

W
pętli
for wyprintuj dla każdego elementu pierwiastek sześcienny z elementy

In[35]:






)


















for i in c:
    print(i ** (1 / 3))

nan
1.0
nan
3.0
nan
4.999999999999999
5.999999999999999
6.999999999999999
7.999999999999999
8.999999999999998

c:\users\kurs\pycharmprojects\zajecia2\venv\lib\site - packages\ipykernel_launcher.py: 2: RuntimeWarning: invalid
value
encountered in power

Stwórz
macierz
10
x10
z
kwadratami
liczb
od
1
do
100

In[50]:

q = (np.arange(1, 101).reshape((10, 10))) ** 2

q = (np.arange(1, 101).reshape((10, 10))) ** 2
print(q)

[[1     4     9    16    25    36    49    64    81   100]
[121   144   169   196   225   256   289   324   361   400]
[441   484   529   576   625   676   729   784   841   900]
[961  1024  1089  1156  1225  1296  1369  1444  1521  1600]
[1681  1764  1849  1936  2025  2116  2209  2304  2401  2500]
[2601  2704  2809  2916  3025  3136  3249  3364  3481  3600]
[3721  3844  3969  4096  4225  4356  4489  4624  4761  4900]
[5041  5184  5329  5476  5625  5776  5929  6084  6241  6400]
[6561  6724  6889  7056  7225  7396  7569  7744  7921  8100]
[8281  8464  8649  8836  9025  9216  9409  9604  9801 10000]]


-----------------------------------------------------------------------
import numpy as np
red = False
green = False
blue = True
plt.imshow(im2*np.array([red, green, blue]))
lum_img = im2[:,:,0]
plt.imshow(lum_img)
plt.imshow(lum_img, cmap="hot")
plt.colorbar()
------------------------------------------------------------------
df = pd.DataFrame([[1, 2], [4, 5], [7, 8]], index=['cobra', 'viper', 'sidewinder'], columns=['max_speed', 'shield'])
df
bb = pd.DataFrame([[1, 2], [4, 5], [7, 8]], index=['cobra', 'viper', 'sidewinder'], columns=['max_speed', 'shield'])
bb
df+bb
df.loc['sidewinder']
(df+bb).iloc[2,0]

---------------------------------------------------------------------------
data = pd.read_csv("files_pandas_21_01_2017/titanic_train.csv")
#data.head()
#data.loc[0, 'Survived']

data.info(memory_usage='deep')
data.dtypes
data.Sex
df = pd.DataFrame(data)
#df.loc['Name']
#data = pd.read_csv("files_pandas_21_01_2017/titanic_train.csv", dtype['Survived': bool])
data = pd.read_csv("files_pandas_21_01_2017/titanic_train.csv", dtype={'Survived': np.bool, 'Pclass': np.int8, 'PassengerId': np.int16})
data.info(memory_usage='deep')
--------------------------------
import pandas as pd
import numpy as np
#import DataFrame as df
import os

#folder_path = "C:\Users\kurs\PycharmProjects\Zajecia2\z5\szablony_cwiczen\files_pandas_21_01_2017"
data = pd.read_csv("files_pandas_21_01_2017/titanic_train.csv")
data.head()





























Stwórz
macierz
5
x5
gdzie
na
krawędziach
będą
0
a
w
środku
1

In[63]:

5

z = 5
q = np.arange(z ** 2).reshape((z, z))
print(q)
q = np.zeros([z, z])
print(q)
q1 = np.ones([z, z])
print(q1)
print(q1[1, 1])
q[1:-1, 1:-1] = 1
print(q)
​









[[0  1  2  3  4]
[5  6  7  8  9]
[10 11 12 13 14]
[15 16 17 18 19]
[20 21 22 23 24]]
[[0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0.]]
[[1. 1. 1. 1. 1.]
[1. 1. 1. 1. 1.]
[1. 1. 1. 1. 1.]
[1. 1. 1. 1. 1.]
[1. 1. 1. 1. 1.]]
1.0
[[0. 0. 0. 0. 0.]
[0. 1. 1. 1. 0.]
[0. 1. 1. 1. 0.]
[0. 1. 1. 1. 0.]
[0. 0. 0. 0. 0.]]



































Stwórz
tabliczkę
mnożenia
liczb
od
0
do
9
w
postaci
dwuwymiarowej
macierzy

In[75]:

a = np.arange(10)
b = np.arange(10).reshape((10, 1))
print(a)
print(b)
a * b
​









[0 1 2 3 4 5 6 7 8 9]
[[0]
[1]
[2]
[3]
[4]
[5]
[6]
[7]
[8]
[9]]




Out[75]:

array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
       [0, 2, 4, 6, 8, 10, 12, 14, 16, 18],
       [0, 3, 6, 9, 12, 15, 18, 21, 24, 27],
       [0, 4, 8, 12, 16, 20, 24, 28, 32, 36],
       [0, 5, 10, 15, 20, 25, 30, 35, 40, 45],
       [0, 6, 12, 18, 24, 30, 36, 42, 48, 54],
       [0, 7, 14, 21, 28, 35, 42, 49, 56, 63],
       [0, 8, 16, 24, 32, 40, 48, 56, 64, 72],
       [0, 9, 18, 27, 36, 45, 54, 63, 72, 81]])

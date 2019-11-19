import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;

  
    
df=pd.read_excel("D:\pythondata\perceptrondata.xls");#读取原题数据
df=pd.DataFrame(df);
x=df.values[:,:-1];#x代表所有行的第一列到倒数第二列的数据，即分类实例的所有特征向量
y=df.values[:,-1];#y代表df的倒数第一列数据，即分类实例的所有类别
a=x.shape;
n=a[0];#n代表x特征向量的行数
m=a[1];#m代表x特征向量的列数
w=[];#创建空列表，w代表分离超平面中的法向量
for i in range(m):
    w.append(0);#列表的长度与特征向量的特征个数相同
#若直接命令w[0]=0,w[1]=0时，会报错，直接按照索引向列表内添加东西时，因为空的列表不能直接指定其位置。
b=0;#b代表分离超平面的截距
k=1;#用来判别是否找到最优的超平面。假设值为1，即未找到
while (k==1):
    k=0;
    for i in range(n):
        t=np.dot(w,x[i]);#用来计算w*x
        if (y[i]*(t+b)<=0):
            w=w+np.dot(y[i],x[i]);
            b=b+y[i];
            k=1;
print("分离超平面的法向量w={0},截距b={1}".format(w,b));
########可视化结果
#
def plot_and_scatter(df=None,w=0,b=0):
    xmin=df.values[:,:-1].min();
    xmax=df.values[:,:-1].max();
    xdiff=(xmax-xmin)*0.5;
    xx=np.linspace((xmin-xdiff),(xmax+xdiff),100);
    yy=-b-w[1]*xx;
    plt.figure();
    plt.xlabel("X(1)");
    plt.ylabel("X(2)");#设置坐标轴的文字标签
    ax=plt.gca();# get current axis 获得坐标轴对象
    ax.spines["right"].set_color("none");
    ax.spines["top"].set_color("none"); # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
    ax.xaxis.set_ticks_position("bottom");
    ax.yaxis.set_ticks_position("left");
    ax.spines["bottom"].set_position(("data",0));
    ax.spines["left"].set_position(("data",0));#指定 data设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
    plt.plot(xx,yy,"r");
    color_list=["blue","green","black","pink","orange"];
    y=df.values[:,-1];

    a=set(y);
    a=list(a);
    y_num=len(a);
    t=0;
    for j in range(y_num):
        tt=a[j];
        y_index=[i for i,y in enumerate(y) if y==tt];
        x_group1=df.values[y_index,0];
        x_group2=df.values[y_index,1];
        plt.scatter(x_group1,x_group2);
        t=t+1;

plot_and_scatter(df,w,b);
plt.show();




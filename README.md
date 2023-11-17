# My-undergraduate-graduation
### 这是我的本科毕设项目，它帮助我获得了大连工业大学优秀毕业论文。

### 以下是安装运行说明书：

1、首先需要安装Ubuntu18.04.6虚拟机，然后安装Ryu控制器和Mininet模拟器，构建SDN环境。


安装Mininet模拟器具体操作如下：

root模式下安装git：apt-get install git

输入y

git安装成功

安装mininet：git clone https://github.com/mininet/mininet.git

cd util

安装：./install.sh -n3v

输入sudo mn --test pingall，创建最小的网络拓扑，检查mininet是否安装成功

mininet安装成功


安装Ryu控制器具体操作如下：

root模式下安装pip工具：wget https://bootstrap.pypa.io/pip/3.5/get-pip.py多执行几次

回到用户目录下，执行安装文件：python get-pip.py

pip安装完成

安装ryu控制器，git克隆文件：git clone https://github.com/osrg/ryu.git

cd ryu

使用pip安装ryu的依赖：pip3 install -r tools/pip-requires

执行安装文件：python setup.py install

ryu安装完成


2、把”源代码/ryu/“文件夹下的4个脚本文件routing.py、mab.py、enode_select.py和my_shortest_forward.py放在虚拟机的ryu/ryu/app/目录下。


3、把”源代码/mininet/“文件夹下的脚本文件aar.py放在虚拟机的mininet/examples/目录下。


4、分别打开两个终端，进入root模式下。


5、在其中一个终端中执行如下命令：

cd ryu

cd ryu

cd app

进入到ryu/ryu/app/目录下。


6、在另一个终端中执行如下命令：

cd mininet

cd examples

进入到mininet/examples/目录下。


7、运行最短路径路由算法：

在ryu所在终端下，执行如下命令：

ryu-manager my_shortest_forward.py --observe-links

把ryu控制器起来。


在mininet所在终端下，执行如下命令：

python aar.py

创建网络拓扑。


使用hx ping hy命令（如h1 ping h7）发送数据包，测量链路的时延。

使用iperf hx hy命令（如iperf h1 h7），测量节点之间的吞吐量。


8、运行强化学习路由算法：

在ryu所在终端下，执行如下命令：

ryu-manager --observe-links routing.py enode_select.py

在ryu控制器中运行强化学习路由算法。


在mininet所在终端下，执行如下命令：

python aar.py

创建网络拓扑。


使用hx ping hy命令（如h1 ping h7）发送数据包，测量链路的时延。

使用iperf hx hy命令（如iperf h1 h7），测量节点之间的吞吐量。


程序可以自动在ryu/ryu/app/目录下生成强化学习奖励值的文本文件。









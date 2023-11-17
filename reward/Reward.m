x=[1,2,3,4,5,6,7,8,9];
egreedy=[6.04,7.44,7.36,7.34,7.25,6.17,7.36,7.35,7.29];
softmax=[7.23,7.12,7.20,7.14,7.36,7.43,7.20,7.13,7.28];
UCB=[7.17,7.24,7.36,7.17,7.31,7.18,7.08,7.37,7.38];
shortestforward=[5.5,5.5,5.5,5.5,5.5,5.5,5.5,5.5,5.5];
set(gca,'ytick',5:0.5:8)
plot(x,egreedy);
hold on
plot(x,softmax);
hold on
plot(x,UCB);
hold on
plot(x,shortestforward);
grid on
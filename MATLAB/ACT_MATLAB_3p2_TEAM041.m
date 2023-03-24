clear; clc

graph1 = (-5:0.1:15);
f1 = (((1/3)*(graph1.^4)) - (2*(graph1.^2)) - (2.3*(graph1.^2)) + (6*graph1) + 4);

hold on

graph2 = (0:0.1:10);
f2 = 300*(graph2.^(1/2));

grid
axis([-5 15 -100 5000])
legend("f1", "f2");
plot(graph1, f1, 'bo-', graph2, f2, 'ro-');
title("Functions:")
xlabel('Function Input:')
ylabel('Function Output:')

hold off

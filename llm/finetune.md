https://zhuanlan.zhihu.com/p/646831196
https://zhuanlan.zhihu.com/p/622810394

那既然通过数学方法直接做SVD行不通，那就让模型自己去学怎么做SVD吧！
当 越小时，低秩矩阵表示的信息精炼，但不全面。我们通过调大 ，来放大forward过程中新知识对模型的影响。
当 越小时，低秩矩阵表示的信息精炼，噪声/冗余信息少，此时梯度下降的方向也更加确信，所以我们可以通过调大 ，
适当增加梯度下降的步伐，也就相当于调整learning rate了。

https://zhuanlan.zhihu.com/p/422416657
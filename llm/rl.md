https://www.zhihu.com/people/who-u/posts

https://mp.weixin.qq.com/s/_QLnE4TlJ87aSpKJvnihZA

https://mp.weixin.qq.com/s/REJSp1Ue8qM03Y4tSjK1Hg

https://blog.csdn.net/v_JULY_v/article/details/132939877

https://mp.weixin.qq.com/s/Wsuzj_k39GYzyYfwPedN4A

多模型采样：
计算偏好强度
1.低强度的偏好数据的负面影响：研究发现，数据集中偏好强度最低的20%的数据对模型在验证集上的性能有负面影响。
这些数据的偏好强度平均值小于0，表明这些数据可能包含错误的偏好标签。
2.中等强度偏好数据的中立影响：偏好强度在20%到40%之间的数据，在训练后，模型在验证集上的预测准确率大约为0.5。
这些数据的偏好强度平均值接近0，表明这些数据的偏好差异不大，模型在这些数据上的学习效果一般。
3.高强度的偏好数据的积极影响：剩余的数据（偏好强度最高的60%）显著提高了模型的性能。
然而，仅使用偏好强度最高的10%的数据训练模型时，并没有达到最佳性能。这可能是因为这些数据过于强烈，导致模型可能过度拟合这些数据。

deeepspeed stage3 数据结构
batch["prompt"] = batch["prompt"].flip(1)
batch["prompt_att_mask"] = batch["prompt_att_mask"].flip(1)`

question+zanswer
question+fanswer
question+zanswer
question+fanswer
question+zanswer+mask
question+fanswer+mask
question+zanswer+mask
question+fanswer+mask

question
answer
label

prompt  generate_sequence  prompt+answer
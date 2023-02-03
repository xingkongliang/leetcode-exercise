# ---------------------------
# 非极大值抑制（Non-Maximum Suppression，NMS），顾名思义就是抑制不是极大值的元素
# ---------------------------
import numpy as np
import torch
 
# 输入：
#   dets: 边界框tensor,每一个单元为(x1,y1,x2,y2,confidence)，每个框都对应一个分数
#         (x1,y1)表示框的左上角坐标，(x2,y2)表示框的右下角坐标
#   thresh: iou过滤阈值
# 输出：nms处理过的边界框
 
def nms_cpu(dets, thresh):
    dets = dets.numpy()
    x1 = dets[:, 0]  # 取出所有的边界框左上角点的x坐标放入x1
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    scores = dets[:, 4]
 
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)  # 计算所有边界框的面积
    # numpy的argsort()函数：返回数组值从小到大的索引值，
    # 再加上[::-1]返回数组值从大到小的索引值,
    # 也可以order = np.argsort(-score)
    order = scores.argsort()[::-1] #分数从大到小排列的索引值
 
    # 每次选出scores中最大的那个边界框
    keep = []
    while order.size > 0:
        i = order[0]
        keep.append(i)  # 保留该类剩余box中得分最高的索引
        xx1 = np.maximum(x1[i], x1[order[1:]])#获取得分最高的边界框与其他所有框的的重叠区域的左上角x坐标
        yy1 = np.maximum(y1[i], y1[order[1:]])#标量和numpy取最值，结果是一个numpy
        xx2 = np.minimum(x2[i], x2[order[1:]])#此处是minimun，不是maximum。求得分最高的边界框与其他所有框的的重叠区域的右下角x坐标
        yy2 = np.minimum(y2[i], y2[order[1:]])
 
        # 计算重叠的面积,不重叠时面积为0
        w = np.maximum(0.0, xx2 - xx1 + 1)
        h = np.maximum(0.0, yy2 - yy1 + 1)
        inter = w * h#得到最大得分框和其他框的重叠面积
 
        # 计算IOU=重叠面积/(得分最大的框面积+当前的框面积-重叠面积)
        ovr = inter / (areas[i] + areas[order[1:]] - inter)
        # 保留iou小于等于阈值的边界框，其它则被过滤了
        # numpy.where() 有两种用法：
        # 1.np.where(condition, x, y):满足条件(condition)，输出x，不满足输出y。
        # 2.np.where(condition):输出满足条件(即非0)元素的坐标(等价于numpy.nonzero)
        inds = np.where(ovr <= thresh)[0]#重叠面积小表示要保留
        # 因为ovr数组的长度比order数组少一个,所以这里要将所有下标后移一位,
        # 获得下一个目标区域的得分最高的一个的索引
        order = order[inds + 1]
 
    return torch.IntTensor(keep)
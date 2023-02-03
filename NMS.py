import torch
#坐标原点在左上角，横轴x,纵轴y,y向下画
def iou(box,boxes,isMin = False):#一个框与一堆框计算,最小面积
    #先计算box的面积[x1,y1,x2,y2]
    box_area = (box[2] -box[0]) * (box[3] -box[1])
    boxes_area =(boxes[:,2]- boxes[:,0]) * (boxes[:,3] -boxes[:,1])#把张量的某一列全取出来
    #求交集,求左上角x最大，y最小；右下角x
    xx1 = torch.maximum(box[0], boxes[:, 0])  #
    yy1 = torch.maximum(box[1], boxes[:, 1])  #
    xx2 = torch.minimum(box[2], boxes[:, 2])  #
    yy2 = torch.minimum(box[3], boxes[:, 3])  #
    #判断是否有交集,与0比较
    w,h = torch.maximum(torch.Tensor([0]),xx2-xx1),torch.maximum(torch.Tensor([0]),yy2-yy1)
    over_area = w * h#交集
    #有交集/并集 ，与交集 / 最小面积
    if isMin:
        return over_area / torch.min(box_area,boxes_area)
    else:
        return over_area / (box_area +boxes_area-over_area)#并集等于两面积相加-交集
 
#定义nms
def nms(boxes,thresh = 0.3,isMin = False):#阈值0.3
    #根据boxes的置信度排序，假设置信度在第一列
    new_boxes =boxes[boxes[:,0].argsort(descending=True)]#设置默认参数，降序排序,用boxes【】索引
    #取出置信度最大的框
    keep_boxes = []#定义保留最大框数组
    while len(new_boxes) > 0:
        max_box = new_boxes[0]
        keep_boxes.append(max_box)
        if len(new_boxes)>1:
        #存其他框，除第一个
            other_boxes = new_boxes[1:]
            #将这些框进行iou计算
            # 小于我们设定的阈值的框才保留，说明框的不是同一个物体
            #torch.where()返回满足条件的索引
            #用other_boxes接收索引，重新赋给new，循环操作
            new_boxes = other_boxes[torch.where(iou(max_box,other_boxes,isMin)<thresh)]
        else:
            break
    return torch.stack(keep_boxes)
 
if __name__ == '__main__':
    boxes = torch.Tensor([[0.5,1,1,10,10],[0.9,1,2,11,11],[0.4,8,8,12,12]])
    print(nms(boxes))
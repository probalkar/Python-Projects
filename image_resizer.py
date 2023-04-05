import cv2

#Configuration parameters
source = input("Enter your image location here: ")
lst = source.split(".")
op_format = input("Enter your output format: ")
dest = f"{lst[0]}.{op_format}"
resize_percent = int(input("By how much percent do you wish to resize your image? : "))

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

#Calculate custom percent of original dimension
new_w = int(src.shape[1]*resize_percent/ 100) 
new_h = int(src.shape[0]*resize_percent/ 100) 

#Resize image
op = cv2.resize(src, (new_w,new_h))

cv2.imwrite(dest,op)
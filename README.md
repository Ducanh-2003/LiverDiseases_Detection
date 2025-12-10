# **BreastCancer Detection**

## A Flask-based web application for breast cancer prediction from histopathology images.

# **Tuần 1 (17/11/2025 - 21/11/2025)**

> ## ***18/11/2025***
## **Những gì đã học và làm được:**

* ## Học được các cú pháp cơ bản của Markdown.
* ## Học được cách tạo diagram và chart cơ bản bằng Mermaid
* ## Fork dataset từ [liver disease Computer Vision Model](https://universe.roboflow.com/anusha-shetty-eprky/cancer-vvl9r/browse?queryText=like-image%3A7CPVxTMvh2roMPYBgnOZ&pageSize=50&startingIndex=0&browseQuery=true) rồi tiến hành tiền xử lý và thêm các augment để training model YOLOv8
* ## Học được cách train model thu được file trọng số `best_model.pt` để tích hợp vào backend
* ## Sử dụng Flask xây dựng 1 web application python:
    * ## Backend: Xây dựng 1 server Flask, xây dựng logic API (`api/predict`) nhận file ảnh, vẽ bounding box, encoded Base64 và trả về kết quả dự đoán dạng `JSON` 
    * ## Frontend: Xây dựng giao diện (UI) đơn giản bằng **HTML5, CSS3, và JavaScript**, sử dụng **Fetch API** gửi `formData` đến backend, xử lý `JSON` trả về để hiển thị lên giao diện 

## **Hướng giải quyết đã thực hiện:** 
* ## Sau khi train lại với tỉ lệ train/valid/test là 70/20/10 thì model trả về kết quả dự đoán tốt hơn khi test ảnh valid cho ra kết quả dự đoán đúng (>80%)


> ## ***19/11/2025***

## **Những gì đã học và làm được:**
* ## Tìm ra hướng giải quyết cho vấn đề tồn đọng
* ## Tìm hiểu cách cơ bản để deploy lên Render
* ## Tìm hiểu cách bảo mật file `.pt` khi deploy lên môi trường production: lưu file trọng số vào googledrive, server tự động tải model sử dụng file ID được bảo mật trong Environment Variable của Render khi khởi động

# **Tuần 2 (24/11/2025 - 28/11/2025)**

## **Nghỉ do thiệt hại mưa lũ**

# **Tuần 3 (1/12/2025 - 5/12/2025)**

>## ***1/12/2025***

## **Những gì đã học và làm được:**
* ## Tìm hiểu các hàm biến đổi ảnh thực thi như thế nào với thư viện OpenCV 
* ## Tiếp tục tìm hiểu về dataset được sử dụng
* ## Cải thiện lại ở bước prepossesing và augmentation dataset chính xác hơn
* ## Retrain model với dataset mới 

> ## ***4-8/12/2025***

## **Những gì đã học và làm được:**
* ## Đổi lại bộ dataset từ classification mô bệnh tế bào ung thư (tế bào bình thường và tế bào ung thư giai đoạn 1,2,3) sang object detection các bệnh về gan (gan phình to, xơ gan, viêm gan, gan nhiễm mỡ).
* ## Train lại 
* ## Sửa lại demo
* ## Viết báo cáo
---


---

## Dataset: https://universe.roboflow.com/roboflow-100/liver-disease

## Cấu trúc dataset: 3976 ảnh
|  | Train | Valid | Test |
|---|---|---|---|
| Ballooning | 698 | 198 | 100 |
| Fibrosis | 694 | 198 | 100 |
| Inflammation | 688 | 196 | 100 |
| Steatosis | 693 | 198 | 99 |
| null | 8 | 4 | 0 |

## Tài liệu tham khảo: 
## https://docs.roboflow.com/datasets/dataset-versions/image-preprocessing
## https://docs.roboflow.com/datasets/dataset-versions/image-augmentation
## https://docs.roboflow.com/annotate/use-roboflow-annotate#mark-null



## **Link demo:** [![Render](https://img.shields.io/badge/Render-Live_App-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://breastcancer-detection-4o3g.onrender.com/)

## **Flowchart:**
```mermaid
flowchart BT

    subgraph Init [Giai đoạn 1: Khởi động Server]
        Start(Chạy run.py) --> Check{Kiểm tra file .pt}
        
        %% Nhánh Local
        Check -- "Đã có (Local)" --> Load
        
        %% Nhánh Production
        Check -- "Chưa có (Production)" --> Get[Lấy MODEL_ID từ Env Var của Render];
        Get--> Download[Tải model từ Google Drive];
        Download --> Load[Load Model YOLO vào RAM];
        
        Load --> Ready(Server Sẵn sàng);
    end

    subgraph "Frontend" [Giai đoạn 2: Xử lý yêu cầu]
        A(Bắt đầu: User chọn ảnh) --> B[js: tạo formData cho file ảnh];
        B --> C[js: gửi Fetch POST đến /api/predict];
        H[JS: Nhận JSON từ server] --> I[JS: Gán chuỗi Base64 vào img Data URL];
        I --> J[Hiển thị ảnh đã bounding box và text kết quả ];
        J --> K(Kết thúc: User thấy kết quả);
        
    end

    subgraph "Backend"
        C --> D[Flask: /api/predict nhận request];
        D --> E[Đọc ảnh dạng bytes, gọi hàm];
        E --> F[Model nhận img và chạy dự đoán];
        F --> G[Vẽ bounding bõ và mã hóa base64 ảnh];
        G --> H[Trả về JSON gồm ảnh encoded và text dự đoán];
    end

    

# **BreastCancer\_Detection**

## A Flask-based web application for breast cancer prediction from histopathology images.

# **Tuần 1 (17/11/2025 - 21/11/2025)**

> ## ***18/11/2025***
## **Những gì đã học và làm được:**

* ## Học được các cú pháp cơ bản của Markdown.
* ## Học được cách tạo diagram và chart cơ bản bằng Mermaid
* ## Fork dataset từ [Cancer](https://universe.roboflow.com/anusha-shetty-eprky/cancer-vvl9r/browse?queryText=like-image%3A7CPVxTMvh2roMPYBgnOZ&pageSize=50&startingIndex=0&browseQuery=true) rồi tiến hành tiền xử lý và thêm các augment để training model YOLOv8
* ## Học được cách train model thu được file trọng số `best_model.pt` để tích hợp vào backend
* ## Sử dụng Flask xây dựng 1 web application python:
    * ## Backend: Xây dựng 1 server Flask, xây dựng logic API (`api/predict`) nhận file ảnh, vẽ bounding box, encoded Base64 và trả về kết quả dự đoán dạng `JSON` 
    * ## Frontend: Xây dựng giao diện (UI) đơn giản bằng **HTML5, CSS3, và JavaScript**, sử dụng **Fetch API** gửi `formData` đến backend, xử lý `JSON` trả về để hiển thị lên giao diện 

## **Những khó khăn tồn đọng:**
* ## Khi test để model nhận dạng những ảnh trong valid kết quả trả về sai hoặc nếu đúng thì conf khá thấp
![Ảnh valid](frontend/statics/assets/valid1.png) 
### (solved)
* ## Khi đưa những ảnh không phải là ảnh tế bào ung thư để nhận dạng thì trả về kết quả là 1 trong 4 class đã train 
![Ảnh test](frontend/statics/assets/test2.png)

## **Hướng giải quyết đã thực hiện:** 
* ## Sau khi train lại với tỉ lệ train/valid/test là 70/20/10 thì model trả về kết quả dự đoán tốt hơn khi test ảnh valid cho ra kết quả dự đoán đúng (>80%)


> ## ***19/11/2025***

## **Những gì đã học và làm được:**
* ## Tìm ra hướng giải quyết cho vấn đề tồn đọng
* ## Tìm hiểu cách cơ bản để deploy lên Render
* ## Tìm hiểu cách bảo mật file `.pt` khi deploy lên môi trường production: lưu file trọng số vào googledrive, server tự động tải model sử dụng file ID được bảo mật trong Environment Variable của Render khi khởi động

## **Những khó khăn tồn đọng:**
## Khi test với hình ảnh không phải là ảnh mô tế bào vẫn nhận dạng và phân loại vài class Normalcell (conf > 90%) (solved)

## **Hướng giải quyết đã thực hiện:**
* ## Retrain model với bộ dataset cũ được thêm vào 400 hình ảnh car, person, fruit,... được gán nhãn null làm background images để tránh cho mô hình nhận diện nhầm các đối tượng không liên quan
* ## Đặt Threshold 0.25 để loại bỏ các đối tượng không liên quan mà mô hình có thể nhận diện nhầm với conf thấp

## **Kết quả:** 
| Trước | Sau |
| :---: | :---: |
| ![Ảnh Valid](frontend/statics/assets/test2.png) | ![Ảnh Test](frontend/statics/assets/test2afterretrain.png) |

## **Link demo:** [![Render](https://img.shields.io/badge/Render-Live_App-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://breastcancer-detection-4o3g.onrender.com/)

## **Flowchart:**
```mermaid
flowchart TD
    subgraph "Frontend"
        A(Bắt đầu: User chọn ảnh) --> B[js: tạo formData cho file ảnh];
        B --> C[js: gửi Fetch POST đến /api/predict];
        H[JS: Nhận JSON từ server] --> I["JS: Gán chuỗi Base64 vào <img> Data URL"];
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

    

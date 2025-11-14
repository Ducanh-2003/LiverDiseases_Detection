document.addEventListener('DOMContentLoaded', function() {
    const file_input = document.getElementById('fileInput');
    const btn_predict = document.getElementById('btnPredict');
    const img_preview = document.getElementById('imgPreview');
    const img_result = document.getElementById('imgResult');
    const box_result = document.getElementById('boxResult');
    const txt_result = document.getElementById('txtResult');
    const txt_loading = document.getElementById('txtLoading');

    const api_url = 'http://127.0.0.1:5000/predict';

    file_input.addEventListener('change', function() {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                img_preview.src = e.target.result;
                img_preview.style.display = 'block';
                box_result.style.display = 'none';
            }
            reader.readAsDataURL(file);
        }
    });

    btn_predict.addEventListener('click', async function() {
        const file = file_input.files[0];
        if (!file) {
            alert('Please select an image file first.');
            return;
        }   
        const formData = new FormData();
        formData.append('file', file);

        try{
            const response = await fetch(api_url, {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (data.error) {   
                alert('Error: ' + data.error);
            } else {
                img_result.src = "data:image/jpeg;base64," + data.image_base64;
                txt_result.innerHTML = "<h3>Prediction Result:</h3>";

                if (data.detections.length === 0) {
                    txt_result.innerHTML += "<p>No abnormalities detected.</p>";
                } else {
                    const ul = document.createElement('ul');
                    data.detections.forEach(det => {
                        const li = document.createElement('li');
                        const style = det.class.includes('g3') || det.class.includes('g2') ? 'color:red; font-weight: bold' : '';
                        li.innerHTML = `<span style="${style}">${det.class} - Confidence: ${(det.confidence * 100).toFixed(2)}%</span>`;
                        ul.appendChild(li);
                    });     
                    txt_result.appendChild(ul);
                }
                box_result.style.display = 'block';
            }
        } catch (error) {
            alert('An error occurred while processing the request.');
        } finally {
            txt_loading.style.display = 'none';
            btn_predict.disabled = false;
        }
    });
})
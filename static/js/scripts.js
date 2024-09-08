document.getElementById('uploadForm').onsubmit = async function(event) {
    event.preventDefault();
    const formData = new FormData();
    formData.append('image', document.getElementById('image').files[0]);

    const response = await fetch('/compress', {
        method: 'POST',
        body: formData
    });

    const data = await response.json();
    document.getElementById('originalSize').innerText = `Original Size: ${(data.original_size / 1024).toFixed(2)} KB`;
    document.getElementById('compressedSize').innerText = `Compressed Size: ${(data.compressed_size / 1024).toFixed(2)} KB`;
    document.getElementById('compressionPercentage').innerText = `Compression Percentage: ${data.compression_percentage.toFixed(2)}%`;

    const downloadButton = document.getElementById('downloadButton');
    downloadButton.style.display = 'block';
    downloadButton.onclick = async function() {
        const downloadResponse = await fetch('/download', {
            method: 'POST',
            body: formData
        });
        const blob = await downloadResponse.blob();
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'compressed_image.jpg';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    };
};
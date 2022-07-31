class FileUpload {

    constructor(input) {
        this.input = input;
        this.max_length = 1000 * 1000 * 8;
    }

    create_progress_bar() {
        var progress = `<div class="file-icon">
                            <i class="fa fa-file-o" aria-hidden="true"></i>
                        </div>
                        <div class="file-details">
                            <p class="filename center"></p>
                            <small class="textbox center"></small>
                            <div class="progress" style="margin-top: 5px;">
                                <div class="progress-bar bg-success" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%">
                                </div>
                            </div>
                        </div>`
        document.getElementById('uploaded_files').innerHTML = progress
    }

    upload() {
        this.create_progress_bar();
        this.initFileUpload();
    }

    initFileUpload() {
        this.file = this.input.files[0];
        this.upload_file(0, null);
    }

    //upload file
    upload_file(start, model_id) {
        var end;
        var self = this;
        var existingPath = model_id;
        var formData = new FormData();
        var nextChunk = start + this.max_length + 1;
        var currentChunk = this.file.slice(start, nextChunk);
        var uploadedChunk = start + currentChunk.size;
        if (uploadedChunk >= this.file.size) {
            end = 1;
        } else {
            end = 0;
        }
        formData.append('file', currentChunk)
        formData.append('filename', this.file.name)
        $('.filename').text(this.file.name)
        $('.textbox').text("در حال آپلود عکس")
        formData.append('end', end)
        formData.append('existingPath', existingPath);
        formData.append('nextSlice', nextChunk);
        formData.append('title', $("#title").val());
        formData.append('document_pattern_size', $('#document_pattern_size').val());
        formData.append('accepted_types', acceptedTypes);
        console.log(acceptedTypes);
        $.ajaxSetup({
            headers: {
                "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
            }
        });
        $.ajax({
            xhr: function () {
                var xhr = new XMLHttpRequest();
                xhr.upload.addEventListener('progress', function (e) {
                    if (e.lengthComputable) {
                        if (self.file.size < self.max_length) {
                            var percent = Math.round((e.loaded / e.total) * 100);
                        } else {
                            var percent = Math.round((uploadedChunk / self.file.size) * 100);
                        }
                        $('.progress-bar').css('width', percent + '%');
                        $('.progress-bar').text(percent + '%');
                    }
                });
                return xhr;
            },

            url: '/educational/upload-image/',
            type: 'POST',
            dataType: 'json',
            cache: false,
            processData: false,
            contentType: false,
            data: formData,
            error: function (xhr) {
                if (xhr.status === 400){
                    if (xhr.responseJSON['size'] === false) {
                        Swal.fire({
                            icon: 'error',
                            title: '😁😁😁😁😁'
                        });
                    } else {
                        Swal.fire({
                            icon: 'error',
                            title: xhr.responseJSON['data']
                        })
                    }
                }
            },
            success: function (res) {
                if (nextChunk < self.file.size) {
                    // upload file in chunks
                    existingPath = res.existingPath;
                    self.upload_file(nextChunk, existingPath);
                } else {
                    // upload complete
                    let textbox = $('.textbox');
                    textbox.text("لطفا صبر کنید!");
                    textbox.addClass('text-success');
                    $('#submit').hide();
                    $('#send').click();
                }
            }
        });
    };
}

(function ($) {
    $('#submit').on('click', (event) => {
        event.preventDefault();
        var uploader = new FileUpload(document.querySelector('#fileupload'))
        console.log(document.querySelector('#fileupload'));
        uploader.upload();
    });
})(jQuery);

ondragenter = function(evt) {
    evt.preventDefault();
    evt.stopPropagation();
};

ondragover = function(evt) {
    evt.preventDefault();
    evt.stopPropagation();
};

ondragleave = function(evt) {
    evt.preventDefault();
    evt.stopPropagation();
};
  
ondrop = function(evt) {
    evt.preventDefault();
    evt.stopPropagation();
    const files = evt.originalEvent.dataTransfer;
    var uploader = new FileUpload(files);
    uploader.upload();
};

$('#dropBox')
    .on('dragover', ondragover)
    .on('dragenter', ondragenter)
    .on('dragleave', ondragleave)
    .on('drop', ondrop);


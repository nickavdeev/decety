function GetPhotos(request, shop_id, id, color, size, description, height, waist, thighs, chest, biceps) {
    let data = new FormData();
    data.append("shop_id",      shop_id);
    data.append("id",           id);
    data.append("color",        color);
    data.append("size",         size);
    data.append("description",  description);
    data.append("d1",           10 * height);
    data.append("d2",           10 * waist);
    data.append("d3",           10 * thighs);
    data.append("d4",           10 * chest);
    data.append("d5",           10 * biceps);

    $.ajax({
        url: 'https://decety.com/api/get',
        data: data,
        processData: false,
        contentType: false,
        type: 'POST',
        success: function(data){
            data = JSON.parse(data);
            let image_list;
            if (data.error === '') {
                console.log(data.result);
                image_list = data.result.map(function (image_id) {
                    // return 'https://decety.com/api/image-small/' + image_id;
                    return 'https://decety.com/api/image/' + image_id;
                });

                $('#360-view').attr('data-image-list', JSON.stringify(image_list));

                if (request === 360) {
                    return window.CI360.init();
                }
                else if (request === 1) {
                    document.getElementById("photo-preview").src = image_list[0];
                }
            }
            else {
                if (request === 1){
                    alert('Ошибка сервера. Пожалуйста, повторите позднее.')
                }
            }
        }
    });
}

//이미지 미리보기
function showImg(input) {
    if(input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('#preview').attr('src', e.target.result);
        }
        reader.readAsDataURL(input.files[0]);   
    }
}
 
$(".inp-img").on('change', function(){
    showImg(this);
});
 


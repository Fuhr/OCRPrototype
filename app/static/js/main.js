


$(function() {
	FastClick.attach(document.body);

	$('#file').change(function() {
		$('.preview-box').find('span').remove();
		PreviewImage();
	});


});

function PreviewImage() {
	oFReader = new FileReader();
	oFReader.readAsDataURL($('file')[0].files[0]);

	oFReader.onload = function (oFREvent) {
	    $('#uploadPreview')[0].src = oFREvent.target.result;
	};
};
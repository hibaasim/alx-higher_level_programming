$(document).ready(function() {
	$(INPUT#btn_translate).on('click', function() {
		const language = $(INPUT#language_code).val();
		$.get('https://hellosalut.stefanbohacek.dev/?lang=${language}', function(data) {
			$('DIV#hello').text(data.hello);
		});
	});

});

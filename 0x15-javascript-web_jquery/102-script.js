$(document).ready(() => {
    $('#btn_translate').click(() => {
        const code = $('input#language_code').val()
        console.log(code)
        fetch(`https://hellosalut.stefanbohacek.dev/?lang={code}`)
					.then(response => {
						if (response.ok) {
							return response.json();
						}
					})
					.then(data => $("div#hello").text(data.hello));
    });
}
)

$(document).ready(fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(response => {
    if (response.ok) {
      return response.json();
    }
  }).then(
    data => {
      $('div#hello').text(`${data.hello}`);
    }
  ));

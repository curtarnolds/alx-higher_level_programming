$(document).ready(function () {
  fetch('https://swapi-api.alx-tools.com/api/people/5/?format=json')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      $('#character').text(data.name);
    })
    .catch(error => {
      console.error('Fetch error:', error);
    });
});

$(document).ready(
  fetch('https://swapi-api.alx-tools.com/api/films/?format=json')
    .then(response => {
      if (response.ok) {
        return response.json();
      }
    })
    .then(data => {
      data.results.map(result => $('ul#list_movies').append(`<li>${result.title}</li>`));
    })
);

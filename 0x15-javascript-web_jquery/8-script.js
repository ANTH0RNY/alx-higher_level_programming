$(() => {
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data, textStatus) => {
	if (textStatus === 'success' {
	    const films = data.results;
	    films.forEach(film) => {
		$('#list_movies').append('<li>' + '</li>');
	    });
	   }
    });
});

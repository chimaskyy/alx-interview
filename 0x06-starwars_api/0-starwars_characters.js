#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

if (!id) {
  console.error('Usage: node get_characters.js movie_id');
  process.exit(1);
}

function getCharacters (movieId) {
  request.get(url, (error, response, body) => {
    if (error) {
      console.error('Error fetching movie data:', error.message);
      return;
    }

    if (response.statusCode !== 200) {
      console.error(`Error fetching movie data: ${response.statusCode}`);
      return;
    }

    const data = JSON.parse(body);
    const charUrls = data.characters;

    for (const charUrl of charUrls) {
      request.get(charUrl, (error, response, body) => {
        if (error) {
          console.error('Error fetching character data:', error.message);
          return;
        }

        if (response.statusCode !== 200) {
          console.error(
            `Error fetching character data: ${response.statusCode}`
          );
          return;
        }

        const charData = JSON.parse(body);
        console.log(charData.name);
      });
    }
  });
}

getCharacters(id);

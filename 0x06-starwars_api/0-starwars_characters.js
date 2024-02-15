#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

request(URL, (error, response, body) => {
    if (!error) {
        const characters = JSON.parse(body).characters;
        for (const charURL of characters) {
            request(charURL, (error, response, body) => {
                if (!error) {
                    console.log(JSON.parse(body).name);
                }
            });
        }
    }
});

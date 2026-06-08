function showWeather(){

    const city =
        document.getElementById("cityInput").value;

    const result =
        document.getElementById("weatherResult");

    if(city === ""){

        result.innerHTML =
        "<p>Please enter a city name</p>";

        return;
    }

    const formattedCity =
        city.charAt(0).toUpperCase() +
        city.slice(1).toLowerCase();

    const weatherData = {

        Bengaluru:{
            temp:"28°C",
            weather:"Cloudy ☁️",
            humidity:"65%"
        },

        Delhi:{
            temp:"35°C",
            weather:"Sunny ☀️",
            humidity:"40%"
        },

        Mumbai:{
            temp:"30°C",
            weather:"Rainy 🌧️",
            humidity:"80%"
        },

        Chennai:{
            temp:"32°C",
            weather:"Hot 🔥",
            humidity:"70%"
        },

        Hyderabad:{
            temp:"29°C",
            weather:"Partly Cloudy ⛅",
            humidity:"55%"
        },

        Kolkata:{
            temp:"31°C",
            weather:"Humid 🌫️",
            humidity:"78%"
        },

        Pune:{
            temp:"27°C",
            weather:"Pleasant 🌤️",
            humidity:"50%"
        },

        Jaipur:{
            temp:"38°C",
            weather:"Very Hot ☀️",
            humidity:"25%"
        },

        Ahmedabad:{
            temp:"36°C",
            weather:"Sunny 🌞",
            humidity:"35%"
        },

        Kochi:{
            temp:"26°C",
            weather:"Rainy 🌧️",
            humidity:"88%"
        },

        Mysuru:{
            temp:"24°C",
            weather:"Cool 🌥️",
            humidity:"60%"
        },

        Goa:{
            temp:"29°C",
            weather:"Beach Weather 🏖️",
            humidity:"75%"
        }

    };

    if(weatherData[formattedCity]){

        result.innerHTML =

        `
        <h2>${formattedCity}</h2>

        <p>🌡️ Temperature:
        ${weatherData[formattedCity].temp}</p>

        <p>☁️ Weather:
        ${weatherData[formattedCity].weather}</p>

        <p>💧 Humidity:
        ${weatherData[formattedCity].humidity}</p>
        `;

    }

    else{

        result.innerHTML =
        "<p>City data not available</p>";

    }

}
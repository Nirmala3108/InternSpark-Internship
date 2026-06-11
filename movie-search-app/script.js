const searchBtn =
document.getElementById("searchBtn");

const searchInput =
document.getElementById("searchInput");

const movieContainer =
document.getElementById("movieContainer");

const loading =
document.getElementById("loading");

const error =
document.getElementById("error");

searchBtn.addEventListener(
    "click",
    searchMovies
);

searchInput.addEventListener(
    "keypress",
    function(e){

        if(e.key==="Enter"){
            searchMovies();
        }

    }
);

async function searchMovies(){

    const query =
    searchInput.value.trim();

    if(!query){

        showError(
        "Please enter a movie name."
        );

        return;
    }

    movieContainer.innerHTML="";
    error.innerHTML="";

    loading.innerHTML=
    `
    <div class="loader">
        <div class="spinner-border text-danger">
        </div>
    </div>
    `;

    try{

        const response =
        await fetch(
        `https://api.tvmaze.com/search/shows?q=${query}`
        );

        const data =
        await response.json();

        loading.innerHTML="";

        if(data.length===0){

            showError(
            "No results found."
            );

            return;
        }

        displayMovies(data);

    }
    catch(err){

        loading.innerHTML="";

        showError(
        "Network Error. Please try again."
        );

        console.error(err);
    }
}

function displayMovies(data){

    movieContainer.innerHTML="";

    data.forEach(item=>{

        const show = item.show;

        const image =
        show.image
        ? show.image.medium
        : "https://via.placeholder.com/300x450";

        movieContainer.innerHTML +=

        `
        <div class="col-lg-3 col-md-4 col-sm-6">

            <div class="card">

                <img
                src="${image}"
                alt="${show.name}">

                <div class="card-body">

                    <h5 class="movie-title">
                        ${show.name}
                    </h5>

                    <p class="rating">
                        ⭐ ${show.rating.average || "N/A"}
                    </p>

                    <p>
                        ${show.genres.join(", ")}
                    </p>

                    <button
                    class="btn btn-outline-light w-100"
                    onclick="showDetails(${show.id})">

                    View Details

                    </button>

                </div>

            </div>

        </div>
        `;

    });
}

async function showDetails(id){

    const response =
    await fetch(
    `https://api.tvmaze.com/shows/${id}`
    );

    const show =
    await response.json();

    document.getElementById(
    "modalBody"
    ).innerHTML=

    `
    <div class="row">

        <div class="col-md-4">

            <img
            src="${
            show.image
            ? show.image.original
            : 'https://via.placeholder.com/300'
            }"

            class="img-fluid rounded">

        </div>

        <div class="col-md-8">

            <h2>${show.name}</h2>

            <p>
            <strong>Language:</strong>
            ${show.language}
            </p>

            <p>
            <strong>Status:</strong>
            ${show.status}
            </p>

            <p>
            <strong>Genres:</strong>
            ${show.genres.join(", ")}
            </p>

            <p>
            <strong>Rating:</strong>
            ${show.rating.average || "N/A"}
            </p>

            <div class="summary">

            ${show.summary || "No summary available"}

            </div>

        </div>

    </div>
    `;

    new bootstrap.Modal(
    document.getElementById(
    "detailsModal"
    )
    ).show();
}

function showError(message){

    error.innerHTML=

    `
    <div class="alert alert-danger">
        ${message}
    </div>
    `;
}

window.onload = () => {
    searchInput.value = "Batman";
    searchMovies();
};
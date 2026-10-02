const data = {

    au: [
        "College AU",
        "Coffee Shop AU",
        "Fantasy AU",
        "Apocalypse AU",
        "Royalty AU",
        "Neighbors AU"
    ],

    size: [
        "Mini",
        "Midi",
        "Maxi"
    ],

    fandom: [
        "Detroit: Become Human",
        "Fallout: New Vegas",
        "Batman",
        "Marvel",
        "Harry Potter",
        "Star Wars",
        "Original"
    ],

    genre: [
        "Romance",
        "Fluff",
        "Angst",
        "Comedy",
        "Drama",
        "Horror",
        "Mystery"
    ],

    kink: [
        "Praise",
        "Jealousy",
        "Teasing",
        "Possessiveness",
        "Power Play"
    ],

    trope: [
        "Enemies to Lovers",
        "Friends to Lovers",
        "Strangers to Lovers",
        "Fake Dating",
        "Only One Bed",
        "Forced Proximity",
        "Slow Burn",
        "Mutual Pining"
    ]

};


function randomItem(array) {

    return array[
        Math.floor(Math.random() * array.length)
    ];

}


function getValue(id, array) {

    const element = document.getElementById(id);

    if (element.value === "random") {
        return randomItem(array);
    }

    return element.value;

}


function generateIdea() {

    const idea = {

        au: getValue("au", data.au),

        size: getValue("size", data.size),

        fandom: getValue("fandom", data.fandom),

        genre: getValue("genre", data.genre),

        kink: getValue("kink", data.kink),

        trope: getValue("trope", data.trope)

    };


    const result = document.getElementById("result");

    const content = document.getElementById("result-content");


    content.innerHTML = `

        <div class="result-item">
            <span class="result-label">FANDOM</span>
            <span class="result-value">${idea.fandom}</span>
        </div>

        <div class="result-item">
            <span class="result-label">AU</span>
            <span class="result-value">${idea.au}</span>
        </div>

        <div class="result-item">
            <span class="result-label">SIZE</span>
            <span class="result-value">${idea.size}</span>
        </div>

        <div class="result-item">
            <span class="result-label">GENRE</span>
            <span class="result-value">${idea.genre}</span>
        </div>

        <div class="result-item">
            <span class="result-label">KINK</span>
            <span class="result-value">${idea.kink}</span>
        </div>

        <div class="result-item">
            <span class="result-label">TROPE</span>
            <span class="result-value">${idea.trope}</span>
        </div>

    `;


    result.classList.remove("hidden");

    result.scrollIntoView({
        behavior: "smooth"
    });

}


document
    .getElementById("randomize")
    .addEventListener("click", generateIdea);


document
    .getElementById("again")
    .addEventListener("click", generateIdea);
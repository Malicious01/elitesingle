document.addEventListener("DOMContentLoaded", () => {
    const cards = document.querySelectorAll(".card");
    const maxVisible = 2;

    cards.forEach((card, index) => {
        if (index >= maxVisible) card.style.display = "none";
    });

    if (cards.length > maxVisible) {
        const unlock = document.createElement("button");
        unlock.innerText = "View more profiles";
        unlock.className = "unlock-btn";

        unlock.onclick = () => {
            window.open(
                "https://wa.me/254118400440?text=Hi%20I%20want%20to%20view%20more%20profiles%20on%20EliteSingle",
                "_blank"
            );
        };

        document.querySelector("main").appendChild(unlock);
    }
});


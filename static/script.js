// document.querySelector(".bi-linkedin").onclick= () => {alert("working")}

let current = 0;
let step = 12;

function showMore() {
    let cards = document.querySelectorAll(".doctor-card");

    for (let i = current; i < current + step && i < cards.length; i++) {
        cards[i].style.display = "block";
    }

    current += step;


    if (current >= cards.length) {
        document.getElementById("btn").style.display = "none";
    }
}

window.onload = showMore;
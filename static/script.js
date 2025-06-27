let canvas = document.getElementById("canvas");
let ctx = canvas.getContext("2d");
let painting = false;

canvas.addEventListener("mousedown", () => painting = true);
canvas.addEventListener("mouseup", () => painting = false);
canvas.addEventListener("mousemove", draw);

function draw(e) {
    if (!painting) return;
    ctx.fillStyle = "black";
    ctx.fillRect(e.offsetX, e.offsetY, 10, 10);
}

function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function submitCanvas() {
    let image = canvas.toDataURL("image/png");
    fetch("/predict", {
        method: "POST",
        body: JSON.stringify({ image }),
        headers: { "Content-Type": "application/json" }
    }).then(res => res.json()).then(data => {
        document.getElementById("result").innerText = data.prediction;
    });
}

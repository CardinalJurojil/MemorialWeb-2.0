console.log("Javascript here!!")

  document.getElementById("image").addEventListener("mouseover", function() {
    var picPath = document.getElementById("picPath").value;
    this.src = picPath;
});

document.getElementById("image").addEventListener("mouseout", function() {
    var imagePath = document.getElementById("imagePath").value;
    this.src = imagePath;
});

fetch('/Memorial/1/Message/30/Reaction/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCSRFToken()  // Include CSRF token if needed
    },
    body: JSON.stringify({
        reaction_type: "like"
    })
});
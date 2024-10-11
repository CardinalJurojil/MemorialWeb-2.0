console.log("Javascript here!!")

  document.getElementById("image").addEventListener("mouseover", function() {
    var picPath = document.getElementById("picPath").value;
    this.src = picPath;
});

document.getElementById("image").addEventListener("mouseout", function() {
    var imagePath = document.getElementById("imagePath").value;
    this.src = imagePath;
});
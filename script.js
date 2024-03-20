function escalonarMatriz() {
  var matrizInput = document.getElementById("matrizInput").value;
  console.log(matrizInput);

  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
          document.getElementById("resultado").innerHTML = this.responseText;
      }
  };
  xhttp.open("POST", "http://127.0.0.1:5000", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded", "Control-Allow-Origin");
  xhttp.send("matriz=" + encodeURIComponent(matrizInput));
}

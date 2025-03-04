let result = document.getElementById("result");
result.style.display="none";

document.getElementById("predictionForm").addEventListener("submit", function(event) {
        event.preventDefault();

        let age = document.getElementById("age").value;
        let sex = document.getElementById("sex").value;
        let bmi = document.getElementById("bmi").value;
        let children = document.getElementById("children").value;
        let smoker = document.getElementById("smoker").value;
        let region = document.getElementById("region").value;

        let formData = new FormData();
        formData.append("age", age);
        formData.append("sex", sex);
        formData.append("bmi", bmi);
        formData.append("children", children);
        formData.append("smoker", smoker);
        formData.append("region", region); 

        fetch("/predict", {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            result.style.display = "block";
            result.innerHTML += data.prediction.toFixed(2);
        })
        .catch(error => {
            console.error("Error:", error);
        });
});

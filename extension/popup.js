chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
  const url = tabs[0].url;
  document.getElementById("currentUrl").innerText = url;

  fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ url: url })
  })
    .then(response => response.json())
    .then(data => {
      const statusDiv = document.getElementById("status");
      if (data.prediction === "Phishing") {
        statusDiv.innerText = "🚨 Phishing Site";
        statusDiv.className = "status phishing";
      } else {
        statusDiv.innerText = "✅ Legitimate Site";
        statusDiv.className = "status legit";
      }
    })
    .catch(error => {
      document.getElementById("status").innerText = "⚠️ Error contacting server";
    });
});

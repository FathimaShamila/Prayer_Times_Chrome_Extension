document.addEventListener("DOMContentLoaded", () => {
  const ul = document.getElementById("times");
  const errorDiv = document.getElementById("error");

  if (!navigator.geolocation) {
    errorDiv.textContent = "Geolocation not supported";
    return;
  }

  navigator.geolocation.getCurrentPosition(
    ({ coords }) => {
      const lat = 41.8781;
      const lon = -87.6298;
      fetch(`http://localhost:5001/prayer-times?lat=${lat}&lon=${lon}`)
        .then(res => res.json())
        .then(data => {
          if (data.error){
            errorDiv.textContent = data.error;
            return;
          }
          ul.innerHTML = "";
          const header = document.createElement("li");
          header.className = "list-group-item active text-center";
          header.textContent = `${data.date} (${data.timezone})`;
          ul.appendChild(header);
          const displayOrder = ["fajr","sunrise","dhuhr","asr","maghrib","sunset","isha","midnight"];
          displayOrder.forEach(prayer => {
            if (data.times[prayer]) {
              const li = document.createElement("li");
              li.className = "list-group-item d-flex justify-content-between align-items-center";
              li.innerHTML = `
                <span class ="prayer-name">${prayer}</span>
                <span class="badge bg-primary rounded-pill">${data.times[prayer]}</span>`;
              ul.appendChild(li);
            }
          });
        })
        .catch(() => errorDiv.textContent = "Error fetching prayer times.");
    },
    () => errorDiv.textContent = "Location access denied."
  );
});


// 🔗 Highlight Active Sidebar Link
const sidebarLinks = document.querySelectorAll('.sidebar a');
sidebarLinks.forEach(link => {
  link.addEventListener('click', (e) => {
    e.preventDefault();
    sidebarLinks.forEach(l => l.classList.remove('active'));
    link.classList.add('active');
  });
});

// 🌀 Simulate Dynamic Stats Update
document.addEventListener('DOMContentLoaded', () => {
  // Replace this with actual fetch if you connect to a backend API
  const stats = {
    violations: Math.floor(Math.random() * 200),
    alerts: Math.floor(Math.random() * 10)
  };

  const detectionCard = document.querySelector('.card:nth-of-type(1) p');
  const alertsCard = document.querySelector('.card:nth-of-type(2) p');

  detectionCard.textContent = `${stats.violations} violations today`;
  alertsCard.textContent = `${stats.alerts} zones need attention`;
});

// 🎥 (Optional) Simulate Video Stream Source
// You can replace this section with real MJPEG/WebSocket logic
const videoContainer = document.querySelector('.video-player');

if (videoContainer) {
  const video = document.createElement('video');
  video.src = "your-stream-url.mjpeg"; // Replace with actual stream URL
  video.autoplay = true;
  video.muted = true;
  video.playsInline = true;
  video.style.width = "100%";
  video.style.height = "100%";
  video.style.objectFit = "cover";

  // Remove placeholder text and add video element
  videoContainer.innerHTML = "";
  videoContainer.appendChild(video);
}


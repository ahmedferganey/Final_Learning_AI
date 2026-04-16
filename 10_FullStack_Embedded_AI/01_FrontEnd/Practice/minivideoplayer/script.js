// script.js

const video = document.getElementById("myVideo");

// ▶ Play video
function playVideo() {
  video.play();
}

// ⏸ Pause video
function pauseVideo() {
  video.pause();
}

// 🔇 Toggle mute
function toggleMute() {
  video.muted = !video.muted;
}

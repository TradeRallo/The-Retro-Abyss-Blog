// ===== Арт-вьювер =====

let artIndex = 0;

const artImg = document.getElementById('currentArt');
document.getElementById('nextArt').addEventListener('click', () => {
    artIndex = (artIndex + 1) % arts.length;
    artImg.src = arts[artIndex];
});
document.getElementById('prevArt').addEventListener('click', () => {
    artIndex = (artIndex - 1 + arts.length) % arts.length;
    artImg.src = arts[artIndex];
});

// ===== Музыкальный плеер =====

let songIndex = 0;
const player = document.getElementById('musicPlayer');

document.getElementById('playBtn').addEventListener('click', () => player.play());
document.getElementById('pauseBtn').addEventListener('click', () => player.pause());
document.getElementById('nextSong').addEventListener('click', () => {
    songIndex = (songIndex + 1) % songs.length;
    player.src = songs[songIndex];
    player.play();
});
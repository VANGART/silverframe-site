// Pages intérieures SilverFrame : le lecteur Vimeo ne se charge qu'au clic (option dnt=1, aucun cookie avant).
document.querySelectorAll('.lance').forEach(b => b.addEventListener('click', () => {
  const f = document.createElement('iframe');
  f.src = 'https://player.vimeo.com/video/' + b.dataset.vimeo + '?autoplay=1&title=0&byline=0&portrait=0&dnt=1';
  f.allow = 'autoplay; fullscreen; picture-in-picture';
  f.allowFullscreen = true;
  f.title = b.dataset.titre || 'Film';
  b.replaceWith(f);
  f.focus();
}));
